.. _archive-client:

Archive Client
****************************

If you have documents in the archive, you can retrieve them by their IDs.

See :ref:`client-configuration` for instructions on how to set up the configuration for the archive client. Note that the concept of "global sender" is not used by the archive client, and may be omitted in the configuration.



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

            try (InputStream pAdESStream = archiveClient.getPades(owner, archivedDocumentId)) {
                // consume the downloaded PAdES document
            }

    .. group-tab:: Http

            To download a document, send an ``HTTP GET`` request to ``api.<env>.signering.posten.no/api/<organization-num>/archive/documents/<id>/pades``.


            - ``<env>`` is difiqa, difitest, or just remove the environment part for the production environment.
            - ``<organization-num>`` is the organization number whose archive you want to access
            - ``<id>`` is the ID of the document you want to download.
            - The ending ``/pades`` indicates the variant of the document you want to download, and at this point only signed documents (PAdES) is supported. For more information on the format of the signed document, see :ref:`signerte-dokumenter`.
