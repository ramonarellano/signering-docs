.. _archive_client

Archive Client
****************************


If you have created a job  as explained in the documentation, you can also retrieve the signed documents by the generated job Ids.


From Direct Flow
===============================

If you have created a direct client already, you can use the same configuration to create an Archive client.
Instead of using a global sender, you need to create as well a document owner, corresponding the organization that owns the archived documents.

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


From Portal Flow
===============================

If you have created a Portal client, You can use the same configuration and make a new Archive client in the same way as in the Direct flow.

..  tabs::

    .. group-tab:: C#

        ..  code-block:: c#

            ClientConfiguration clientConfiguration = null; //As initialized earlier

            ...

            var portalJobResponse = await portalClient.Create(portalJob);

            var jobid = directJobResponse.JobId;

            var archiveClient = new ArchiveClient(clientConfiguration);
            var owner = new DocumentOwner(clientConfiguration.GlobalSender.OrganizationNumber);

            var padesByteStream = await archiveClient.GetPades(owner, jobid);

    ..  group-tab:: Java

        ..  code-block:: java

            ClientConfiguration clientConfiguration = null; // As initialized earlier

            ...

            PortalJobResponse portalJobResponse = client.create(portalJob);

            long jobid = directJobResponse.getSignatureJobId();

            ArchiveClient archiveClient = new ArchiveClient(clientConfiguration);
            DocumentOwner owner = new DocumentOwner(clientConfiguration.getGlobalSender.getOrganizationNumber());

            InputStream PAdESStream = await archiveClient.GetPades(owner, jobid);

