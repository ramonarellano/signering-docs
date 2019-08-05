.. _portal-flow:

Portal flow
****************************

This integration pattern is suitable for senders who want to create :ref:`a signature job in portal flow <signering-i-portalflyt>`. The signing ceremony is performed by the signer in the signing portal, and the sender will then be able to poll for a status and retrieve the signed document. This scenario is designed to support a flow where it is necessary to obtain signatures from more than one signer.

To ease the integration, we provide C# and Java libraries. If you are creating your own client, you will have to interact directly with the API. The message format of the API is XML, and relevant types can be found in `portal.xsd <https://github.com/digipost/signature-api-specification/blob/master/schema/xsd/portal.xsd>`_.

|portalflytskjema|
 **Flow chart for signing in portal flow:** *The chart shows that a sender creates a signature job, starts polling, signers signing the job, a status update is fetched by polling by the sender, followed by downloading the signed document. If you send only one job to one signer, please disregard the first "steg 4"-section. Solid lines show user flow and dashed lines shows requests to and responses from the API.*

Having problems integrating?
===============================

..  TIP::
    Remember that if you are having problems creating a job in a portal signature flow, you can always get in touch with a human on Github:

    ..  tabs::

        ..  group-tab:: C#

            Get help for your `C# integration here <https://github.com/digipost/signature-api-client-dotnet/issues>`_.

        ..  group-tab:: Java

            Get help for your `Java integration here <https://github.com/digipost/signature-api-client-java/issues>`_.

Step 1: Create signature job
==============================

..  tabs::

    ..  group-tab:: C#

        ..  code-block:: c#

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

    ..  group-tab:: Java

        ..  code-block:: java

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

    ..  group-tab:: HTTP

        The flow starts when the sender sends a request to create the signature job to the API. This request is a `multipart message <https://en.wikipedia.org/wiki/MIME#Multipart_messages>`_ comprised of a document bundle part and a metadata part.

        - The request is a ``HTTP POST`` mot ressursen ``<rot-URL>/portal/signature-jobs``.
        - The document bundle is added to the multipart message with ``application/octet-stream`` as media type. See :ref:`informasjonOmDokumentpakken` for more information on the document bundle.
        - The metadata in the multipart request is defined by the ``portal-signature-job-request`` element. These are added with media type ``application/xml``.

        The following example shows metadata for a signature job in a portal flow:

        ..  code-block:: xml

            <portal-signature-job-request xmlns="http://signering.posten.no/schema/v1">
                <reference>123-ABC</reference>
                <polling-queue>custom-queue</polling-queue>
            </portal-signature-job-request>

        An example of the ``manifest.xml`` from the document bundle for a singature job that is to be signed by four signers:

        ..  code-block:: xml

            <portal-signature-job-manifest xmlns="http://signering.posten.no/schema/v1">
               <signers>
                   <signer order="1">
                       <personal-identification-number>12345678910</personal-identification-number>
                       <signature-type>ADVANCED_ELECTRONIC_SIGNATURE</signature-type>
                       <notifications>
                           <!-- Override contact information to be used for notifications -->
                           <email address="signer1@example.com" />
                           <sms number="00000000" />
                       </notifications>
                   </signer>
                   <signer order="2">
                       <personal-identification-number>10987654321</personal-identification-number>
                       <signature-type>AUTHENTICATED_ELECTRONIC_SIGNATURE</signature-type>
                       <notifications>
                           <email address="signer2@example.com" />
                       </notifications>
                   </signer>
                   <signer order="2">
                       <personal-identification-number>01013300001</personal-identification-number>
                       <signature-type>AUTHENTICATED_ELECTRONIC_SIGNATURE</signature-type>
                       <notifications-using-lookup>
                           <!-- Try to send notifications in both e-mail and SMS using lookup -->
                           <email/>
                           <sms/>
                       </notifications-using-lookup>
                   </signer>
                   <signer order="3">
                       <personal-identification-number>02038412546</personal-identification-number>
                       <signature-type>AUTHENTICATED_ELECTRONIC_SIGNATURE</signature-type>
                       <notifications-using-lookup>
                           <email/>
                       </notifications-using-lookup>
                   </signer>
               </signers>
               <sender>
                   <organization-number>123456789</organization-number>
               </sender>
               <document href="document.pdf" mime="application/pdf">
                   <title>Tittel</title>
                   <nonsensitive-title>Sensitiv tittel</nonsensitive-title>
                   <description>Melding til undertegner</description>
               </document>
               <required-authentication>4</required-authentication>
               <availability>
                   <activation-time>2016-02-10T12:00:00+01:00</activation-time>
                   <available-seconds>864000</available-seconds>
               </availability>
               <identifier-in-signed-documents>PERSONAL_IDENTIFICATION_NUMBER_AND_NAME</identifier-in-signed-documents>
            </portal-signature-job-manifest>


..  NOTE::
    You may identify the signature job’s signers by personal identification number :code:`IdentifiedByPersonalIdentificationNumber` or contact information. When identifying by contact information, you may choose between instantiating a :code:`PortalSigner` using :code:`IdentifiedByEmail, :code:`IdentifiedByMobileNumber` or :code:`IdentifiedByEmailAndMobileNumber`.

The signer
-----------------

Before starting this chapter, please reed up on :ref:`varsler` :ref:`adressering-av-undertegner`. Signers can be adressed and notified in different ways.

Adressing the signer
^^^^^^^^^^^^^^^^^^^^^^

..  tabs::

    ..  group-tab:: C#

        ..  code-block:: c#

            //This functionality exists in C#, but the example has not been generated yet.

    ..  group-tab:: Java

        ..  code-block:: java

            //This functionality exists in Java, but the example has not been generated yet.

    ..  group-tab:: HTTP

        ..  tabs::

            ..  tab:: E-mail

                ..  code-block:: xml

                    <signer>
                        <identified-by-contact-information/>
                        <notifications>
                            <email address="email@example.com"/>
                        </notifications>
                        <on-behalf-of>SELF</on-behalf-of>
                    </signer>

            ..  tab:: Mobile

                ..  code-block:: xml

                    <signer>
                        <identified-by-contact-information/>
                        <notifications>
                            <sms number="00000000" />
                        </notifications>
                        <on-behalf-of>SELF</on-behalf-of>
                    </signer>

            ..  tab:: E-mail and mobile

                ..  code-block:: xml

                    <signer>
                        <identified-by-contact-information/>
                        <notifications>
                            <email address="email@example.com"/>
                            <sms number="00000000" />
                        </notifications>
                        <on-behalf-of>SELF</on-behalf-of>
                    </signer>

            ..  tab:: SSN

                Social Security number, with notification by e-mail:

                ..  code-block:: xml

                    <signer>
                        <personal-identification-number>12345678910</personal-identification-number>
                        <notifications>
                            <email address="email@example.com"/>
                        </notifications>
                        <on-behalf-of>SELF</on-behalf-of>
                    </signer>


                With notification as public organization:

                ..  NOTE::
                    Public organizations must use Kontakt- og Reservasjonsregisteret as lookup method.

                ..  code-block:: xml

                    <signer>
                        <personal-identification-number>12345678910</personal-identification-number>
                        <notifications>
                            <notifications-using-lookup/>
                        </notifications>
                        <on-behalf-of>SELF</on-behalf-of>
                    </signer>

            ..  tab:: On behalf of

                A sender can choose if the signer is signing on behalf of himself or by virtue of a role. This is done by setting the attribute ``on-behalf-of`` to ``SELF`` or ``OTHER``.

                The signed document will not be sent to the signers digital mailbox if signing on behalf of someone else. For public organizations, you must address the signer by a chosen phone number and e-mail, as Kontakt- og Reservasjonsregisteret will not be used.

                ..  code-block:: xml

                    <signer>
                        <personal-identification-number>12345678910</personal-identification-number>
                        <notifications>
                            <email address="email@example.com"/>
                            <sms number="00000000" />
                        </notifications>
                        <on-behalf-of>OTHER</on-behalf-of>
                    </signer>

                ..  NOTE::

                    The element ``notifications-using-lookup`` is only available for public organizations. As this will look up the signers *private* contact information, it is not possible at the same time to indicate that the person signing on behalf of someone else. Thus, you cannot set ``on-behalf-of`` to ``OTHER`` if you want to use the Kontakt- og Reservasjonsregisteret to address signers.

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

        // Repeat the polling until signer signs the document, but ensure to do this at a
        // reasonable interval. If you are processing the result a few times a day in your
        // system, only poll a few times a day.
        var change = await portalClient.GetStatusChange();

        switch (change.Status)
        {
            case JobStatus.NoChanges:
                //Queue is empty. Additional polling will result in blocking for a defined period.
                break;
            case JobStatus.Failed:
            case JobStatus.InProgress:
            case JobStatus.CompletedSuccessfully:
            {
                var signatureJobStatus = change.Status;
                var signatures = change.Signatures;
                var signatureOne = signatures.ElementAt(0);
                var signatureOneStatus = signatureOne.SignatureStatus;
                break;
            }
        }

        var pollingWillResultInBlock = change.NextPermittedPollTime > DateTime.Now;
        if (pollingWillResultInBlock)
        {
            //Wait until next permitted poll time has passed before polling again.
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

..  |portalflytskjema| image:: https://raw.githubusercontent.com/digipost/signature-api-specification/master/integrasjon/flytskjemaer/asynkron-maskin-til-maskin.png
    :alt: Flytskjema for portalintegrasjon
