.. _direct-flow:

Direct flow
****************************

This is an integration pattern suited for senders with their own portals and web solutions, wishing to offer a seamless signing experience as a part of a process where the user is logged in through a senders web portal. The signature prosess will be perceived as an integrated part of the user flow. The user will be redirected to the senders website after the signing is completed. For more information of the flow, please see :ref:`signering-i-direkteflyt`.

To ease the integration, we provide C# and Java libraries. If you are creating your own client, you will have to interact directly with the API. The message format of the API is XML, and relevant types can be found in `direct.xsd <https://github.com/digipost/signature-api-specification/blob/master/schema/xsd/direct.xsd>`_.

|direkteflytskjema|

**Flow chart for signing in direct flow:** *The chart shows that a signer is sent to the signature portal from the senders website and completes the signing process. The sender gets the status, gets the signed document and confirms processing of the job. Full lines show user flow and broken lines shows API-calls*.

Having problems integrating?
==============================

..  TIP::
    Remember that if you are having problems creating a job in a direct signature flow, you can always get in touch with a human on Github:

    ..  tabs::

        ..  group-tab:: C#

            Get help for your `C# integration here <https://github.com/digipost/signature-api-client-dotnet/issues>`_.

        ..  group-tab:: Java

            Get help for your `Java integration here <https://github.com/digipost/signature-api-client-java/issues>`_.

        ..  group-tab:: HTTP

            Get help for your `HTTP integration here <https://github.com/digipost/signature-api-specification/issues>`_.

.. _directIntegrationStep1:

Step 1: Create signature job
===============================

..  tabs::

    .. group-tab:: C#

        ..  code-block:: c#

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

    ..  group-tab:: Java

        ..  code-block:: java

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

    ..  group-tab:: HTTP

        The flow starts when the sender does an API-call to create the signature job. This call is a multipart request comprised of a document bundle part and a metadata part.

        - The call is a ``HTTP POST`` to the resource ``<rot-URL>/direct/signature-jobs``.
        - The document bundle is added to the multipart call with ``application/octet-stream`` as media type. See :ref:`informasjonOmDokumentpakken` for more information on the document bundle.
        - The metadata in this call is defined by the ``direct-signature-job-request`` element. These are added with media type ``application/xml``.

        The following example shows the metadata for a signature job:

        ..  code-block:: xml

            <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
            <direct-signature-job-request xmlns="http://signering.posten.no/schema/v1">
               <reference>123-ABC</reference>
               <exit-urls>
                   <completion-url>https://www.sender.org/completed</completion-url>
                   <rejection-url>https://www.sender.org/rejected</rejection-url>
                   <error-url>https://www.sender.org/failed</error-url>
               </exit-urls>
               <polling-queue>custom-queue</polling-queue>
            </direct-signature-job-request>

        A part of the metadata is a set of URLs defined by the element ``exit-urls``. These URLs will be used by the signature service to redirect the signer back to the senders portal after completing the signing. The following three URLs must be defined:

        -  **completion-url:** The signer is sent here after a successful signing process.
        -  **rejection-url:** The signer is sent here if Undertegner sendes hit hvis *he or she chooses* to cancel the signing process.
        -  **error-url:** The signer is sent here if something fails during the signing process. This *is not* a result of a user action.

        The following is an example of the ``manifext.xml`` from the document bundle:

        ..  code-block:: xml

            <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
            <direct-signature-job-manifest xmlns="http://signering.posten.no/schema/v1">
               <signer>
                   <personal-identification-number>12345678910</personal-identification-number>
                   <signature-type>ADVANCED_ELECTRONIC_SIGNATURE</signature-type>
                   <on-behalf-of>SELF</on-behalf-of>
               </signer>
               <sender>
                   <organization-number>123456789</organization-number>
               </sender>
               <document href="document.pdf" mime="application/pdf">
                   <title>Tittel</title>
                   <description>Melding til undertegner</description>
               </document>
               <required-authentication>3</required-authentication>
               <identifier-in-signed-documents>PERSONAL_IDENTIFICATION_NUMBER_AND_NAME</identifier-in-signed-documents>
            </direct-signature-job-manifest>


You can specify a  signature type and required authentication level. If signature type or required authentication level is omitted, default values as specified by the `functional documentation <http://digipost.github.io/signature-api-specification/v1.0/#signaturtype>`_ will apply:

..  tabs::

    ..  group-tab:: C#

        ..  code-block:: c#

            Document documentToSign = null; //As initialized earlier
            ExitUrls exitUrls = null; //As initialized earlier
            var signers = new List<Signer>
            {
                new Signer(new PersonalIdentificationNumber("12345678910"))
                {
                    SignatureType = SignatureType.AdvancedSignature
                }
            };

            var job = new Job(documentToSign, signers, "SendersReferenceToSignatureJob", exitUrls)
            {
                AuthenticationLevel = AuthenticationLevel.Four
            };

    ..  group-tab:: Java

        ..  code-block:: java

            //This functionality exists in Java, but the example has not been generated yet.

    ..  group-tab:: HTTP

        This functionality exists with integration via HTTP, but the example has not been generated yet.


Other settings
----------------

Identifier in the signed document
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
..  tabs::

    ..  group-tab:: C#

        ..  code-block:: c#

            //This functionality exists in C#, but the example has not been generated yet.

    ..  group-tab:: Java

        ..  code-block:: java

            //This functionality exists in Java, but the example has not been generated yet.

    ..  group-tab:: HTTP

        The element ``identifier-in-signed-documents`` is used to specify how the signer(s) are to be identified in the signed documents. Allowed values are ``PERSONAL_IDENTIFICATION_NUMBER_AND_NAME``, ``DATE_OF_BIRTH_AND_NAME`` and ``NAME``. Please note that applicable values may be restricted by the type of signature job and sender. For more information, see :ref:`identifisereUndertegnere`.

Status retrieval method
^^^^^^^^^^^^^^^^^^^^^^^^^

..  tabs::

    ..  group-tab:: C#

        ..  code-block:: c#

            //This functionality exists in C#, but the example has not been generated yet.

    ..  group-tab:: Java

        ..  code-block:: java

            //This functionality exists in Java, but the example has not been generated yet.

    ..  group-tab:: HTTP

        The element ``status-retrieval-method`` is used to set how the sender wishes to get status updates for the signature job. ``WAIT_FOR_CALLBACK`` is the standard value, and means that the sender waits until a signer is sent to one of the URLs given by the element ``exit-urls`` before acting accordingly. The alternative is to use ``POLLING`` to specify regular polling to fetch status updates. We recommend using ``WAIT_FOR_CALLBACK``.



Response
--------

..  tabs::

    ..  group-tab:: C#

        ..  code-block:: c#

            //This functionality exists in C#, but the example has not been generated yet.

    ..  group-tab:: Java

        ..  code-block:: java

            //This functionality exists in Java, but the example has not been generated yet.

    ..  group-tab:: HTTP

        The call will result in a response defined by the element ``direct-signature-job-response``. An example of such response for one signer can be seen in the `API-specification <https://github.com/digipost/signature-api-specification/blob/master/schema/examples/direct/response.xml>`_. This response contains a URL (``redirect-url``), which redirects the signers browser to initiate the signing process. In addition, the response contains the URL used to retrieve statuses for the job. The sender must wait until the user is redirected to one of the URLs defined in the request, and then do a call to retrieve the latest status update. The status retrieval requires a token that is aquired when the signer is redirected. Please see :ref:`directIntegrationStep3` for more information.

        ..  code-block:: xml

            <direct-signature-job-response xmlns="http://signering.posten.no/schema/v1">
               <signature-job-id>1</signature-job-id>
               <redirect-url>
                   https://signering.posten.no#/redirect/421e7ac38da1f81150cfae8a053cef62f9e7433ffd9395e5805e820980653657
               </redirect-url>
               <status-url>https://api.signering.posten.no/api/{sender-identifier}/direct/signature-jobs/1/status</status-url>
            </direct-signature-job-response>

The signer
------------

Before starting this chapter, please reed up on :ref:`varsler` :ref:`adressering-av-undertegner`. Signers can be adressed and notified in different ways.

Adressing the signer
^^^^^^^^^^^^^^^^^^^^^^

..  tabs::

    ..  group-tab:: Java

        ..  code-block:: c#

            //This functionality exists in C#, but the example has not been generated yet.

    ..  group-tab:: Java

        ..  code-block:: java

            //This functionality exists in Java, but the example has not been generated yet.

    ..  group-tab:: HTTP

        ..  tabs::

            ..  tab:: Fødselsnummer

                ..  code-block:: xml

                    <signer>
                       <personal-identification-number>12345678910</personal-identification-number>
                       <on-behalf-of>SELF</on-behalf-of>
                    </signer>

                For et utfyllende eksempel, se gjerne `eksempelmanifest for signeringstype og autentisering i API-spesifikasjonen <https://github.com/digipost/signature-api-specification/blob/master/schema/examples/direct/manifest-specify-signtype-and-auth.xml>`_.

            ..  tab:: Selvvalgt identifikator

                Det er mulig å bruke en selvvalgt identifikator for å gjøre koblingen mellom en person i avsenders system og et signeringsoppdrag. En slik identifikator kan være hva som helst som gir mening for avsender, for eksempel kundenummer.

                ..  code-block:: xml

                    <signer>
                        <signer-identifier>kundenummer-134AB47</signer-identifier>
                        <on-behalf-of>SELF</on-behalf-of>
                    </signer>

                For et utfyllende eksempel, se gjerne `eksempelmanifest for selvvalgt identifikator i API-spesifikasjonen <https://github.com/digipost/signature-api-specification/blob/master/schema/examples/direct/manifest-signer-without-pin.xml>`_.

            ..  tab:: På vegne av

                En avsender kan velge om undertegner signerer på vegne av seg selv eller i kraft av en rolle. Dette gjøres ved å sette attributtet ``on-behalf-of`` til enten ``SELF`` eller ``OTHER``.

                 Dersom man signerer på vegne av noen andre, vil det i praksis bety at signert dokument ikke sendes videre til undertegners postkasse.

                ..  code-block:: xml

                    <signer>
                       <personal-identification-number>12345678910</personal-identification-number>
                       <on-behalf-of>OTHER</on-behalf-of>
                    </signer>



.. _directIntegrationStep2:

Steg 2: Signering av oppdraget
================================

Hele dette steget gjennomføres i signeringsportalen. Du videresender brukeren til portalen ved å benytte URLen du får som svar på opprettelsen av oppdraget. Denne URLen inneholder et engangstoken generert av signeringstjenesten, og det er dette tokenet som gjør at brukeren får tilgang til å lese dokumentet og gjennomføre signeringen.

..  IMPORTANT::
    **Sikkerhet i forbindelse med engangstoken:** For å håndtere sikkerheten i dette kallet vil tokenet kun fungere én gang. Brukeren vil få en cookie av signeringstjenesten ved første kall, slik at en eventuell refresh ikke stopper flyten, men du kan ikke bruke denne URLen på et senere tidspunkt. Årsaken til at vi kun tillater at den brukes kun én gang er at URLer kan fremkomme i eventuelle logger, og de vil dermed ikke være sikre etter å ha blitt benyttet.

Brukeren gjennomfører signeringen og blir deretter sendt tilbake til avsenders portal via URLen spesifisert av ``completion-url``. På slutten av denne URLen vil det legges på et query-parameter (``status_query_token``), som du senere skal benytte når du spør om status. Hvis undertegner avbryter signeringen, eller det skjer en feil, sendes undertegner til henholdsvis ``rejection-url`` eller ``error-url``.

.. _directIntegrationStep3:

Step 3: Get status
===================

Status by token
-----------------

The signing process is a synchrounous operation in the direct use case. There is no need to poll for changes to a signature job, as the status is well known to the sender of the job. As soon as the signer completes, rejects or an error occurs, the user is redirected to the respective URLs set in ExitUrls. A :code:`status_query_token` parameter has been added to the url, use this when requesting a status change.

..  tabs::

    ..  group-tab:: C#

        ..  code-block:: c#

            ClientConfiguration clientConfiguration = null; //As initialized earlier
            var directClient = new DirectClient(clientConfiguration);
            JobResponse jobResponse = null; //As initialized when creating signature job
            var statusQueryToken = "0A3BQ54C...";

            var jobStatusResponse =
                await directClient.GetStatus(jobResponse.ResponseUrls.Status(statusQueryToken));

            var jobStatus = jobStatusResponse.Status;


    ..  group-tab:: Java

        ..  code-block:: java

            DirectClient client = null; // As initialized earlier
            DirectJobResponse directJobResponse = null; // As returned when creating signature job

            String statusQueryToken = "0A3BQ54C…";

            DirectJobStatusResponse directJobStatusResponse = client
                .getStatus(StatusReference.of(directJobResponse)
                .withStatusQueryToken(statusQueryToken)
            );

    ..  group-tab:: HTTP


        Når undertegner blir sendt tilbake til avsenders portal, kan du gjøre et API-kall (``HTTP GET``) for å hente ned status på oppdraget. Dette gjøres ved å benytte ``status-url`` du fikk i :ref:`Steg 1 <directIntegrationStep1>` hvor du legger på query-parameteret (``status_query_token``) du fikk i :ref:`Steg 2 <directIntegrationStep2>`.

        Hvis signeringsoppdraget er lagt på en spesifikk kø, så må query-parameteret ``polling_queue`` settes til navnet på køen.


        Responsen fra dette kallet er definert gjennom elementet ``direct-signature-job-status-response``. Et eksempel på denne responsen ved et suksessfullt signeringsoppdrag vises under:

        ..  code:: xml

            <direct-signature-job-status-response xmlns="http://signering.posten.no/schema/v1">
               <signature-job-id>1</signature-job-id>
               <signature-job-status>COMPLETED_SUCCESSFULLY</signature-job-status>
               <status since="2017-01-23T12:51:43+01:00">SIGNED</status>
               <confirmation-url>https://api.signering.posten.no/api/{sender-identifier}/direct/signature-jobs/1/complete</confirmation-url>
               <xades-url>https://api.signering.posten.no/api/{sender-identifier}/direct/signature-jobs/1/xades/1</xades-url>
               <pades-url>https://api.signering.posten.no/api/{sender-identifier}/direct/signature-jobs/1/pades</pades-url>
            </direct-signature-job-status-response>


Status by polling
-------------------

If you, for any reason, are unable to retrieve status by using the status query token specified above, you may poll the service for any changes done to your organization’s jobs. If the queue is empty, additional polling will give an exception.

..  NOTE::
    For the job to be available in the polling queue, make sure to specify the job's :code:`StatusRetrievalMethod` as illustrated below.

..  tabs::

    ..  group-tab:: C#

        ..  code-block:: c#

            ClientConfiguration clientConfiguration = null; // As initialized earlier
            var directClient = new DirectClient(clientConfiguration);

            // Repeat the polling until signer signs the document, but ensure to do this at a
            // reasonable interval. If you are processing the result a few times a day in your
            // system, only poll a few times a day.
            var change = await directClient.GetStatusChange();

            switch (change.Status)
            {
                case JobStatus.NoChanges:
                    // Queue is empty. Additional polling will result in blocking for a defined period.
                    break;
                case JobStatus.CompletedSuccessfully:
                    // Get PAdES
                    // Get XAdES
                    break;
                case JobStatus.Failed:
                    break;
                case JobStatus.InProgress:
                    break;
                default:
                    throw new ArgumentOutOfRangeException();
            }

            // Confirm status change to avoid receiving it again
            await directClient.Confirm(change.References.Confirmation);

            var pollingWillResultInBlock = change.NextPermittedPollTime > DateTime.Now;
            if (pollingWillResultInBlock)
            {
                //Wait until next permitted poll time has passed before polling again.
            }


    ..  group-tab:: Java

        ..  code-block:: Java

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

    ..  group-tab:: HTTP

        Når undertegner blir sendt tilbake til avsenders portal, kan du gjøre et API-kall (``HTTP GET``) for å hente ned status på oppdraget. Dette gjøres ved å benytte ``status-url`` du fikk i :ref:`Steg 1 <directIntegrationStep1>`.

        Hvis signeringsoppdraget er lagt på en spesifikk kø, så må query-parameteret ``polling_queue`` settes til navnet på køen.


        Responsen fra dette kallet er definert gjennom elementet ``direct-signature-job-status-response``. Et eksempel på denne responsen ved et suksessfullt signeringsoppdrag vises under:

        ..  code:: xml

            <direct-signature-job-status-response xmlns="http://signering.posten.no/schema/v1">
               <signature-job-id>1</signature-job-id>
               <signature-job-status>COMPLETED_SUCCESSFULLY</signature-job-status>
               <status since="2017-01-23T12:51:43+01:00">SIGNED</status>
               <confirmation-url>https://api.signering.posten.no/api/{sender-identifier}/direct/signature-jobs/1/complete</confirmation-url>
               <xades-url>https://api.signering.posten.no/api/{sender-identifier}/direct/signature-jobs/1/xades/1</xades-url>
               <pades-url>https://api.signering.posten.no/api/{sender-identifier}/direct/signature-jobs/1/pades</pades-url>
            </direct-signature-job-status-response>

..  TIP::
    As illustrated above, you should always query the :code:`statusChange` to find out when you are allowed to poll for statuses next time.

Step 4: Get signed documents
==============================

..  tabs::

    ..  group-tab:: C#

        ..  code-block:: c#

            ClientConfiguration clientConfiguration = null; //As initialized earlier
            var directClient = new DirectClient(clientConfiguration);
            JobStatusResponse jobStatusResponse = null; // Result of requesting job status

            if (jobStatusResponse.Status == JobStatus.CompletedSuccessfully)
            {
                var padesByteStream = await directClient.GetPades(jobStatusResponse.References.Pades);
            }

            var signature = jobStatusResponse.GetSignatureFor(new PersonalIdentificationNumber("00000000000"));

            if (signature.Equals(SignatureStatus.Signed))
            {
                var xadesByteStream = await directClient.GetXades(signature.XadesReference);
            }

    ..  group-tab:: Java

        ..  code-block:: java

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

    ..  group-tab:: HTTP

        I forrige steg fikk du to lenker: ``xades-url`` og ``pades-url``. Disse kan du gjøre en ``HTTP GET`` på for å laste ned det signerte dokumentet i de to formatene. For mer informasjon om format på det signerte dokumentet, se :ref:`signerte-dokumenter`.

Steg 5: Bekrefte ferdig prosessering
=======================================

..  tabs::

    ..  group-tab:: C#

        ..  code-block:: c#

            //This functionality exists in C#, but the example has not been generated yet.

    ..  group-tab:: Java

        ..  code-block:: java

            //This functionality exists in Java, but the example has not been generated yet.

    ..  group-tab:: HTTP

        Til slutt gjør du et ``HTTP POST``-kall mot ``confirmation-url`` for å bekrefte at du har prosessert jobben ferdig. Hvis :ref:`langtidslagring` benyttes vil dette markere oppdraget som ferdig og lagret. I motsatt fall vil oppdraget slettes fra signeringsportalen.


Specifying queues
===================

Specifies the queue that jobs and status changes for a signature job will occur in for signature jobs where :code:`StatusRetrievalMethod == POLLING`. This is a feature aimed at organizations where it makes sense to retrieve status changes from several queues. This may be if the organization has more than one division, and each division has an application that create signature jobs through the API and want to retrieve status changes independent of the other division’s actions.

To specify a queue, set :code:`Sender` :code:`pollingQueue` through when constructing a sender. Please note that the same sender must be specified when polling to retrieve status changes. The :code:`Sender` can be set globally in :code:`ClientConfiguration` or on every job.

..  tabs::

    ..  group-tab:: C#

        ..  code-block:: c#

            ClientConfiguration clientConfiguration = null; // As initialized earlier
            var directClient = new DirectClient(clientConfiguration);

            String organizationNumber = "123456789";
            var sender = new Sender(organizationNumber, new PollingQueue("CustomPollingQueue"));

            Document documentToSign = null; // As initialized earlier
            ExitUrls exitUrls = null; // As initialized earlier

            var signer = new PersonalIdentificationNumber("00000000000");

            var job = new Job(
                documentToSign,
                new List<Signer> { new Signer(signer) },
                "SendersReferenceToSignatureJob",
                exitUrls,
                sender,
                StatusRetrievalMethod.Polling
            );

            await directClient.Create(job);

            var changedJob = await directClient.GetStatusChange(sender);

    ..  group-tab:: Java

        ..  code-block:: java

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

    ..  group-tab:: HTTP

        This functionality exists with integration via HTTP, but the example has not been generated yet.


Delete documents
==================

After receiving a status change, the documents can be deleted as follows:

..  tabs::

    ..  group-tab:: C#

        ..  code-block:: c#

            //This functionality exists in C#, but the example has not been generated yet.

    ..  group-tab:: Java

        ..  code-block:: java

            DirectClient client = null; // As initialized earlier
            DirectJobStatusResponse directJobStatusResponse = null; // As returned when getting job status

            client.deleteDocuments(directJobStatusResponse.getDeleteDocumentsUrl());

    ..  group-tab:: HTTP

        This functionality exists with integration via HTTP, but the example has not been generated yet.


..  |direkteflytskjema| image:: https://raw.githubusercontent.com/digipost/signature-api-specification/master/integrasjon/flytskjemaer/synkron-maskin-til-maskin.png
    :alt: Flytskjema for direkteintegrasjon