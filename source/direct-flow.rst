Direct flow
****************************

Create job
###########


..  tabs::

    ..  code-tab:: c#

        ClientConfiguration clientConfiguration = null; //As initialized earlier
        var directClient = new DirectClient(clientConfiguration);

        var documentToSign = new Document(
            "Subject of Message",
            "This is the content",
            FileType.Pdf,
            @"C:\Path\ToDocument\File.pdf");

        var exitUrls = new ExitUrls(
            new Uri("http://redirectUrl.no/onCompletion"),
            new Uri("http://redirectUrl.no/onCancellation"),
            new Uri("http://redirectUrl.no/onError")
            );

        var signers = new List<Signer>
        {
            new Signer(new PersonalIdentificationNumber("12345678910")),
            new Signer(new PersonalIdentificationNumber("10987654321"))
        };

        var job = new Job(documentToSign, signers, "SendersReferenceToSignatureJob", exitUrls);

        var directJobResponse = await directClient.Create(job);

    ..  code-tab:: java

        ClientConfiguration clientConfiguration = null; // As initialized earlier
        DirectClient client = new DirectClient(clientConfiguration);

        byte[] documentBytes = null; // Loaded document bytes
        DirectDocument document = DirectDocument.builder("Subject", "document.pdf", documentBytes).build();

        ExitUrls exitUrls = ExitUrls.of(
            "http://sender.org/onCompletion",
            "http://sender.org/onRejection",
            "http://sender.org/onError"
        );

        DirectSigner signer = DirectSigner.withPersonalIdentificationNumber("12345678910").build();
        DirectJob directJob = DirectJob.builder(document, exitUrls, signer).build();

        DirectJobResponse directJobResponse = client.create(directJob);


Get status by token
####################

The signing process is a synchrounous operation in the direct use case. There is no need to poll for changes to a signature job, as the status is well known to the sender of the job. As soon as the signer completes, rejects or an error occurs, the user is redirected to the respective URLs set in ExitUrls. A status_query_token parameter has been added to the url, use this when requesting a status change.

..  tabs::

    ..  code-tab:: c#

        hei

    ..  code-tab:: java

        DirectClient client = null; // As initialized earlier
        DirectJobResponse directJobResponse = null; // As returned when creating signature job

        String statusQueryToken = "0A3BQ54C…";

        DirectJobStatusResponse directJobStatusResponse = client
            .getStatus(StatusReference.of(directJobResponse)
            .withStatusQueryToken(statusQueryToken)
        );

Get status by polling
######################

If you, for any reason, are unable to retrieve status by using the status query token specified above, you may poll the service for any changes done to your organization’s jobs. If the queue is empty, additional polling will give an exception.

..  NOTE::
    For the job to be available in the polling queue, make sure to specify the job's StatusRetrievalMethod as illustrated below.

..  tabs::

    ..  code-tab:: c#

        hei

    ..  code-tab:: java

        DirectClient client = null; // As initialized earlier

        DirectJob directJob = DirectJob.builder(document, exitUrls, signer)
                .retrieveStatusBy(StatusRetrievalMethod.POLLING)
                .build();

        client.create(directJob);

        DirectJobStatusResponse statusChange = client.getStatusChange();

        if (statusChange.is(DirectJobStatus.NO_CHANGES)) {
            // Queue is empty. Must wait before polling again
            Instant nextPermittedPollTime = statusChange.getNextPermittedPollTime();
        } else {
            // Received status update, act according to status
            DirectJobStatus status = statusChange.getStatus();
            Instant nextPermittedPollTime = statusChange.getNextPermittedPollTime();
        }

        client.confirm(statusChange);

..  TIP::
    As illustrated above, you should always query the :code:`statusChange` to find out when you are allowed to poll for statuses next time.

Get signed documents
#####################

..  tabs::

    ..  code-tab:: c#

        hei

    ..  code-tab:: java

        DirectClient client = null; // As initialized earlier
        DirectJobStatusResponse directJobStatusResponse = null; // As returned when getting job status

        if (directJobStatusResponse.isPAdESAvailable()) {
            InputStream pAdESStream = client.getPAdES(directJobStatusResponse.getpAdESUrl());
        }

        for (Signature signature : directJobStatusResponse.getSignatures()) {
            if (signature.is(SignerStatus.SIGNED)) {
                InputStream xAdESStream = client.getXAdES(signature.getxAdESUrl());
            }
        }

Confirm processed job
######################

..  tabs::

    ..  code-tab:: c#

        hei

    ..  code-tab:: java

        DirectClient client = null; // As initialized earlier
        DirectJobStatusResponse directJobStatusResponse = null; // As returned when getting job status

        client.confirm(directJobStatusResponse);

Specifying queues
##################

Specifies the queue that jobs and status changes for a signature job will occur in for signature jobs where :code:`StatusRetrievalMethod == POLLING`. This is a feature aimed at organizations where it makes sense to retrieve status changes from several queues. This may be if the organization has more than one division, and each division has an application that create signature jobs through the API and want to retrieve status changes independent of the other division’s actions.

To specify a queue, set :code:`Sender.pollingQueue` through the constructor :code:`Sender(String, PollingQueue)`. Please note that the same sender must be specified when polling to retrieve status changes. The :code:`Sender` can be set globally in :code:`ClientConfiguration` or on every job.

..  tabs::

    ..  code-tab:: c#

        hei

    ..  code-tab:: java

        DirectClient client = null; // As initialized earlier
        Sender sender = new Sender("000000000", PollingQueue.of("CustomPollingQueue"));

        DirectJob directJob = DirectJob.builder(document, exitUrls, signer)
              .retrieveStatusBy(StatusRetrievalMethod.POLLING).withSender(sender)
              .build();

        client.create(directJob);

        DirectJobStatusResponse statusChange = client.getStatusChange(sender);

        if (statusChange.is(DirectJobStatus.NO_CHANGES)) {
          // Queue is empty. Must wait before polling again
        } else {
          // Recieved status update, act according to status
          DirectJobStatus status = statusChange.getStatus();
        }

        client.confirm(statusChange);

Delete documents
#################

After receiving a status change, the documents can be deleted as follows:

..  tabs::

    ..  code-tab:: c#

        hei

    ..  code-tab:: java

        DirectClient client = null; // As initialized earlier
        DirectJobStatusResponse directJobStatusResponse = null; // As returned when getting job status

        client.deleteDocuments(directJobStatusResponse.getDeleteDocumentsUrl());
