
Buy Enterprise Certificates
***************************

As a sending organization, you must authenticate with an enterprise certificate issued by Buypass or Commfides. You will need a test certificate and a production certificate.

Test environment
###########################

A test certificate must be used against our test environment. The test certificate will be used in the testing phase, and as soon as you are ready to go into production, you will have to replace it with a production certificate.

.. NOTE::
   It is not possible to use a test certificate in production or the other way around.

.. tabs::

   .. tab:: Buypass

    A test certificate can be bought from the Buypass home page. Please `click here <https://www.buypass.no/produkter/virksomhetssertifikat-esegl>`_ for the Norwegian version, or `here <https://www.buypass.com/products/eseal--and-enterprise-certificate>`_ for the English version. Please select *Test-sertifikat/Test certificate*.

    When buying an enterprise certificate from Buypass, you will receive an email containing two *.p12* files. The two files have different serial numbers, and these refer to certficates used for authentication and encryption (*autentisering og kryptering*) and signature (*signering*). You shall only use the one marked for authentication and encryption.

   .. tab:: Commfides

    A test certificates can be bought from the Commfides home page. Please `click here <https://www.commfides.com/en/commfides-virksomhetssertifikat/>`_ for the Norwegian version, or `here <https://www.commfides.com/en/commfides-virksomhetssertifikat/>`_ for the English version. Please see *Bestill Testsertifikat/Order Test Certificate*.

    When buying an enterprise certificate from Commfides, you will receive an email containing three *.p12* files: *auth*, *enc* and *sign*. You shall use the one named *auth* with :code:`Key Usage = Digital Signature`.


Production environment
###########################

.. DANGER::
   Both the production enterprise certificate and the password must be stored securely. Do not under any circumstances send the file or the password to anyone.

.. tabs::

   .. tab:: Buypass

    A production certificate can be bought from the Buypass home page. Please `click here <https://www.buypass.no/produkter/virksomhetssertifikat-esegl>`_ for the Norwegian version, or `here <https://www.buypass.com/products/eseal--and-enterprise-certificate>`_ for the English version. Please select *Standard sertifikat/Standard Certificate*.

    When buying an enterprise certificate from Buypass, you will receive an email containing two *.p12* files. The two files have different serial numbers, and these refer to certficates used for authentication and encryption (*autentisering og kryptering*) and signature (*signering*). You shall only use the one marked for authentication and encryption.

   .. tab:: Commfides

    A production can be bought from the Commfides home page. Please `click here <https://www.commfides.com/en/commfides-virksomhetssertifikat/>`_ for the Norwegian version, or `here <https://www.commfides.com/en/commfides-virksomhetssertifikat/>`_ for the English version. Please see *Bestill Virksomhetssertifikat/Order Enterprise Certificate* for use in a production environment.

    When buying an enterprise certificate from Commfides, you will receive an email containing three *.p12* files: *auth*, *enc* and *sign*. You shall use the one named *auth* with :code:`Key Usage = Digital Signature`.
