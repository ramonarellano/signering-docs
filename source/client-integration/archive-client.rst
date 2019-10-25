.. _archive_client

Archive Client
****************************


If you have created a job  as explained in the documentation, you can also retrieve the signed documents by the generated Id.

From Direct Flow
===============================

..  tabs::

    .. group-tab:: C#

        ..  code-block:: c#

            ClientConfiguration clientConfiguration = null; //As initialized earlier

            ...

            var directJobResponse = await directClient.Create(job);

            var jobid = directJobResponse.JobId;

            var archiveClient = new ArchiveClient(clientConfiguration);
            var owner = new DocumentOwner(clientConfiguration.GlobalSender.OrganizationNumber);

            var padesByteStream = await archiveClient.GetPades(owner, jobid);

    ..  group-tab:: Java

        ..  code-block:: java

            ClientConfiguration clientConfiguration = null; //As initialized earlier

            ...

            DirectJobResponse directJobResponse = client.create(directJob);

            long jobid = directJobResponse.getSignatureJobId();

            ArchiveClient archiveClient = new ArchiveClient(clientConfiguration);
            DocumentOwner owner = new DocumentOwner(clientConfiguration.getGlobalSender.getOrganizationNumber());

            InputStream PAdESStream = await archiveClient.GetPades(owner, jobid);

    ..  group-tab:: HTTP

        //This functionality exists, but the example has not been generated yet.

From Portal Flow
===============================

..  tabs::

    .. group-tab:: C#

        ..  code-block:: c#

            //This functionality exists in C#, but the example has not been generated yet.

    ..  group-tab:: Java

        ..  code-block:: java

            //This functionality exists in Java, but the example has not been generated yet.

    ..  group-tab:: HTTP

        //This functionality exists, but the example has not been generated yet.
