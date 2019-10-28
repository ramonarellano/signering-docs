.. _archive-client:

Archive Client
****************************

If you have documents in the archive, you can retrieve them by their Ids.
Read :ref:`client-configuration` to set up the archive client.



..  tabs::

    .. group-tab:: C#

        ..  code-block:: c#

            ClientConfiguration clientConfiguration = null; //As initialized earlier

            ...

            var archiveClient = new ArchiveClient(clientConfiguration);

            var owner = new DocumentOwner("123456789");
            var archivedDocumentId = new ArchivedDocumentId("abcde12345");

            var padesByteStream = await archiveClient.GetPades(owner, archivedDocumentId);

    ..  group-tab:: Java

        ..  code-block:: java

            ClientConfiguration clientConfiguration = null; //As initialized earlier

            ...

            ArchiveClient archiveClient = new ArchiveClient(clientConfiguration);

            DocumentOwner owner = DocumentOwner.ofOrganizationNumber("123456789");
            String archivedDocumentId = "abcde12345";

            InputStream pAdESStream = archiveClient.GetPades(owner, archivedDocumentId);

    .. group-tab:: Http

            To download a document do a ``HTTP GET`` to: ``api.<environment>.signering.posten.no/api/<org-num>/archive/documents/<id>/pades`` , where <environment> is difiqa, difitest or just remove the environment part for the production environment.

            For more information on the format of the signed document, see :ref:`signerte-dokumenter`.


