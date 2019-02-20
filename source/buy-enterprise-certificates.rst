
Buy Enterprise Certificates
***************************

As a sending organization, you must authenticate with an enterprise certificate issued by Buypass or Commfides.

You only need to buy the enterprise certificate (Virksomhetssertifikat) from Buypass or Commfides, but you need a test certificate and a production certificate. The test certificate will be used in the testing phase, and as soon as you are ready to go into production, you will have to replace it with the production certificate.


.. _`buypass home page`: https://www.buypass.no/produkter/virksomhetssertifikat-esegl

.. tabs::

   .. tab:: Buypass

    Both production and test certificate can be bought from the Buypass home page. Please `click here <https://www.buypass.no/produkter/virksomhetssertifikat-esegl>`_ for the Norwegian version, or `here <https://www.buypass.com/products/eseal--and-enterprise-certificate>`_ for the English version. Please select *Test-sertifikat/Test certificate* for testing and *Standard sertifikat/Standard Certificate* for use in a production environment.

    When buying an enterprise certificate from Buypass, you will receive an email containing two *.p12* files. The two files have different serial numbers, and these refer to certficates used for authentication and encryption (*autentisering og kryptering*) and signature (*signering*). You shall only use the one marked for authentication and encryption.

   .. tab:: Commfides

    Both production and test certificates can be bought from the Commfides home page. Please `click here <https://www.commfides.com/en/commfides-virksomhetssertifikat/>`_ for the Norwegian version, or `here <https://www.commfides.com/en/commfides-virksomhetssertifikat/>`_ for the English version. Please see *Bestill Testsertifikat/Order Test Certificate* for testing and *Bestill Virksomhetssertifikat/Order Enterprise Certificate* for use in a production environment.

    When buying an enterprise certificate from Commfides, you will receive an email containing three *.p12* files: *auth*, *enc* and *sign*. You shall use the one named *auth* with :code:`Key Usage = Digital Signature`.