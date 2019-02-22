Portal flow
****************************

Create job
###########

..  tabs::

    ..  code-tab:: c#

        ClientConfiguration clientConfiguration = null; //As initialized earlier
        var portalClient = new PortalClient(clientConfiguration);

        var documentToSign = new Document(
            "Subject of Message",
            "This is the content",
            FileType.Pdf,
            @"C:\Path\ToDocument\File.pdf"
        );

        var signers = new List<Signer>
        {
            new Signer(new PersonalIdentificationNumber("00000000000"), new NotificationsUsingLookup()),
            new Signer(new PersonalIdentificationNumber("11111111111"), new Notifications(
                new Email("email1@example.com"),
                new Sms("999999999"))),
            new Signer(new ContactInformation {Email = new Email("email2@example.com")}),
            new Signer(new ContactInformation {Sms = new Sms("88888888")}),
            new Signer(new ContactInformation
            {
                Email = new Email("email3@example.com"),
                Sms = new Sms("77777777")
            })
        };

        var portalJob = new Job(documentToSign, signers, "myReferenceToJob");

        var portalJobResponse = await portalClient.Create(portalJob);

    ..  code-tab:: java

        ClientConfiguration clientConfiguration = null; // As initialized earlier
        PortalClient client = new PortalClient(clientConfiguration);

        byte[] documentBytes = null; // Loaded document bytes
        PortalDocument document = PortalDocument.builder("Subject", "document.pdf", documentBytes).build();

        PortalJob portalJob = PortalJob.builder(
                document,
                PortalSigner.identifiedByPersonalIdentificationNumber("12345678910",
                        NotificationsUsingLookup.EMAIL_ONLY).build(),
                PortalSigner.identifiedByPersonalIdentificationNumber("12345678911",
                        Notifications.builder().withEmailTo("email@example.com").build()).build(),
                PortalSigner.identifiedByEmail("email@example.com").build()
        ).build();

        PortalJobResponse portalJobResponse = client.create(portalJob);

..  NOTE::
    You may identify the signature job’s signers by personal identification number :code:`IdentifiedByPersonalIdentificationNumber` or contact information. When identifying by contact information, you may choose between instantiating a :code:`PortalSigner` using :code:`IdentifiedByEmail, :code:`IdentifiedByMobileNumber` or :code:`IdentifiedByEmailAndMobileNumber`.


You can specify a  signature type and required authentication level. If signature type or required authentication level is omitted, default values as specified by the `functional documentation <http://digipost.github.io/signature-api-specification/v1.0/#signaturtype>`_ will apply:

..  tabs::

    ..  code-tab:: c#

        Document documentToSign = null; //As initialized earlier
        var signers = new List<Signer>
        {
            new Signer(new PersonalIdentificationNumber("00000000000"), new NotificationsUsingLookup())
            {
                SignatureType = SignatureType.AdvancedSignature
            }
        };

        var job = new Job(documentToSign, signers, "myReferenceToJob")
        {
            AuthenticationLevel = AuthenticationLevel.Four
        };

..  NOTE::
    Note that only public organizations can do :code:`NotificationsUsingLookup`.


Get status changes
####################

All changes to signature jobs will be added to a queue. You can poll for these changes. All changes must be confirmed after saving or handling them in your system. The following example shows how this can be handled and examples of data to extract from a change response.

..  NOTE::
    If you retrieve a status change, it will be temporarily removed from the queue. If not confirmed it will reappear after some time.

..  tabs::

    ..  code-tab:: c#

        PortalClient portalClient = null; //As initialized earlier

        var jobStatusChanged = await portalClient.GetStatusChange();

        if (jobStatusChanged.Status == JobStatus.NoChanges)
        {
            //Queue is empty. The status change includes next earliest permitted poll time.
        }
        else
        {
            var signatureJobStatus = jobStatusChanged.Status;
            var signatures = jobStatusChanged.Signatures;
            var signatureOne = signatures.ElementAt(0);
            var signatureOneStatus = signatureOne.SignatureStatus;

            //TODO: Persist job status change in your system, to ensure you have the latest status if anything crashes beyond this point.

            // Confirm that you have received and persisted the status change
            await portalClient.Confirm(jobStatusChangeResponse.ConfirmationReference);

        }

        //Polling again:
        try
        {
            var changeResponse2 = await portalClient.GetStatusChange();
        }
        catch (TooEagerPollingException eagerPollingException)
        {
            var nextAvailablePollingTime = eagerPollingException.NextPermittedPollTime;
        }

    ..  code-tab:: java

        PortalClient client = null; // As initialized earlier

        PortalJobStatusChanged statusChange = client.getStatusChange();

        if (statusChange.is(PortalJobStatus.NO_CHANGES)) {
            // Queue is empty. Must wait before polling again
            Instant nextPermittedPollTime = statusChange.getNextPermittedPollTime();
        } else {
            // Recieved status update, act according to status
            PortalJobStatus signatureJobStatus = statusChange.getStatus();
            Instant nextPermittedPollTime = statusChange.getNextPermittedPollTime();
        }



Get signed documents
#####################

When getting XAdES and PAdES for a PortalJob, remember that the XAdES is per signer, while there is only one PAdES.

..  tabs::

    ..  code-tab:: c#

        PortalClient portalClient = null; //As initialized earlier
        var jobStatusChanged = await portalClient.GetStatusChange();

        //Get XAdES:
        var xades = await portalClient.GetXades(jobStatusChanged.Signatures.ElementAt(0).XadesReference);

        //Get PAdES:
        var pades = await portalClient.GetPades(jobStatusChanged.PadesReference);


    ..  code-tab:: java

        PortalClient client = null; // As initialized earlier
        PortalJobStatusChanged statusChange = null; // As returned when polling for status changes

        // Retrieve PAdES:
        if (statusChange.isPAdESAvailable()) {
            InputStream pAdESStream = client.getPAdES(statusChange.getpAdESUrl());
        }

        // Retrieve XAdES for all signers:
        for (Signature signature : statusChange.getSignatures()) {
            if (signature.is(SignatureStatus.SIGNED)) {
                InputStream xAdESStream = client.getXAdES(signature.getxAdESUrl());
            }
        }

        // … or for one specific signer:
        Signature signature = statusChange.getSignatureFrom(
                SignerIdentifier.identifiedByPersonalIdentificationNumber("12345678910"));
        if (signature.is(SignatureStatus.SIGNED)) {
            InputStream xAdESStream = client.getXAdES(signature.getxAdESUrl());
        }


Specifying queues
##################

Specifies the queue that jobs and status changes for a signature job will occur in for signature jobs where :code:`StatusRetrievalMethod == POLLING`. This is a feature aimed at organizations where it makes sense to retrieve status changes from several queues. This may be if the organization has more than one division, and each division has an application that create signature jobs through the API and want to retrieve status changes independent of the other division’s actions.

To specify a queue, set :code:`Sender` :code:`pollingQueue` through when constructing a sender. Please note that the same sender must be specified when polling to retrieve status changes. The :code:`Sender` can be set globally in :code:`ClientConfiguration` or on every job.

..  tabs::

    ..  code-tab:: c#


        PortalClient portalClient = null; //As initialized earlier

        var organizationNumber = "123456789";
        var sender = new Sender(organizationNumber, new PollingQueue("CustomPollingQueue"));

        var documentToSign = new Document(
            "Subject of Message",
            "This is the content",
            FileType.Pdf,
            @"C:\Path\ToDocument\File.pdf"
        );

        var signers = new List<Signer>
        {
            new Signer(new PersonalIdentificationNumber("00000000000"), new NotificationsUsingLookup())
        };

        var portalJob = new Job(documentToSign, signers, "myReferenceToJob", sender);

        var portalJobResponse = await portalClient.Create(portalJob);

        var changedJob = await portalClient.GetStatusChange(sender);

    ..  code-tab:: java

        ClientConfiguration clientConfiguration = null; // As initialized earlier
        PortalClient client = new PortalClient(clientConfiguration);

        Sender sender = new Sender("000000000", PollingQueue.of("CustomPollingQueue"));

        byte[] documentBytes = null; // Loaded document bytes
        PortalDocument document = PortalDocument.builder("Subject", "document.pdf", documentBytes).build();

        PortalJob portalJob = PortalJob.builder(
                document,
                PortalSigner.identifiedByPersonalIdentificationNumber("12345678910",
                        NotificationsUsingLookup.EMAIL_ONLY).build(),
                PortalSigner.identifiedByPersonalIdentificationNumber("12345678911",
                        Notifications.builder().withEmailTo("email@example.com").build()).build(),
                PortalSigner.identifiedByEmail("email@example.com").build()
        ).withSender(sender).build();

        PortalJobResponse portalJobResponse = client.create(portalJob);

        PortalJobStatusChanged statusChange = client.getStatusChange(sender);

Delete documents
#################

After receiving a status change, the documents can be deleted as follows:

..  tabs::

    ..  code-tab:: java

        PortalClient client = null; // As initialized earlier
        PortalJobStatusChanged statusChange = null; // As returned when polling for status changes

        client.deleteDocuments(statusChange.getDeleteDocumentsUrl());

