.. _egenDirekteIntegrasjon:

API-integrasjon for signering i direkteflyt
*********************************************

Dette integrasjonsmønsteret vil passe for avsendere som har egne portaler og nettløsninger, og som ønsker å tilby signering sømløst som en del av en prosess der brukeren allerede er innlogget i en sesjon på avsenders nettsider. Signeringsprosessen vil oppleves som en integrert del av brukerflyten, og brukeren blir derfor sendt tilbake til avsenders nettsider etter at signeringen er gjennomført. Se :ref:`signering-i-direkteflyt` for mer informasjon om flyten.

Meldingsformatet i APIet er XML, og reelevante typer finnes i filen `direct.xsd <https://github.com/digipost/signature-api-specification/blob/master/schema/xsd/direct.xsd>`_.

|direkteflytskjema|
**Flytskjema signeringsoppdrag i direkteflyt:** *skjemaet viser at en undertegner sendes til signeringsportalen fra avsenders nettside og gjennomfører en signering. Avsender henter status, henter signert dokument og bekrefter prosessering. Heltrukne linjer viser brukerflyt, mens stiplede linjer viser API-kall.*

.. _egenDirekteIntegrasjonSteg1:

Steg 1: Opprette signeringsoppdraget
=====================================

Flyten begynner ved at tjenesteeier gjør et API-kall for å opprette signeringsoppdraget. Dette kallet gjøres som en multipart-request, der den ene delen er dokumentpakken og den andre delen er metadata.

-  Kallet gjøres som en ``HTTP POST`` mot ressursen ``<rot-URL>/direct/signature-jobs``
-  Dokumentpakken legges med multipart-kallet med mediatypen ``application/octet-stream``. Se :ref:`informasjonOmDokumentpakken` for mer informasjon om dokumentpakken.
-  Metadataene som skal sendes med i dette kallet er definert av elementet ``direct-signature-job-request``. Disse legges med multipart-kallet med mediatypen ``application/xml``.


Følgende er et eksempel på metadata for et signeringsoppdrag:

.. code-block:: xml

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

En del av metadataene er et sett med URLer definert i elementet ``exit-urls``. Disse URLene vil bli benyttet av signeringstjenesten til å redirecte undertegneren tilbake avsenders portal ved fullført signering. Følgende tre URLer skal oppgis:

-  **completion-url:** Undertegner sendes hit hvis signeringen er vellykket.
-  **rejection-url:** Undertegner sendes hit hvis vedkommende *selv velger* å avbryte signeringen.
-  **error-url:** Undertegner sendes hit hvis det skjer noe galt under signeringen. Dette er noe undertegner *ikke* velger å gjøre selv.

Følgende er et eksempel på ``manifest.xml`` fra dokumentpakken:

.. code-block:: xml

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

Undertegner
------------
Du bør se :ref:`varsler` og :ref:`adressering-av-undertegner` før du starter med dette kapitlet.

Undertegnere kan adresseres og varsles på ulike måter:

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

Andre innstillinger
--------------------

Identifikator i signert dokument
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Elementet ``identifier-in-signed-documents`` brukes for å angi hvordan undertegneren(e) skal identifiseres i de signerte dokumentene. Tillatte verdier er ``PERSONAL_IDENTIFICATION_NUMBER_AND_NAME``, ``DATE_OF_BIRTH_AND_NAME`` og ``NAME``, men ikke alle er gyldige for alle typer signeringsoppdrag og avsendere. For mer informasjon, se :ref:`identifisereUndertegnere`.

Metode for å hente status
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Elementet ``status-retrieval-method`` brukes for å angi hvordan avsender ønsker å hente status for oppdraget. Standardverdien for dette er ``WAIT_FOR_CALLBACK``, som innebærer at avsender ikke foretar seg noe før undertegner sendes til en av URLene angitt i ``exit-urls``. Alternativt kan man bruke verdien ``POLLING`` for å angi at man ønsker å jevnlig spørre etter status. Vi anbefaler å bruke ``WAIT_FOR_CALLBACK``.



Respons
--------

På dette kallet vil man få en respons definert av elementet ``direct-signature-job-response``. Et eksempel på en slik respons for én undertegner kan du se i `API-spesifikasjonen <https://github.com/digipost/signature-api-specification/blob/master/schema/examples/direct/response.xml>`_. Denne responsen inneholder en URL (``redirect-url``) som man redirecter brukerens nettleser til for å starte signeringen. I tillegg inneholder den en URL du benytter for å spørre om status på oppdraget. Her skal man vente til brukeren returneres til en av URLene definert i requesten, for deretter å gjøre et kall for å sjekke status. For å kunne hente status kreves det et token som du får tilbake ved redirecten. Mer informasjon kommer i  :ref:`egenDirekteIntegrasjonSteg3`.

.. code-block:: xml

   <direct-signature-job-response xmlns="http://signering.posten.no/schema/v1">
       <signature-job-id>1</signature-job-id>
       <redirect-url>
           https://signering.posten.no#/redirect/421e7ac38da1f81150cfae8a053cef62f9e7433ffd9395e5805e820980653657
       </redirect-url>
       <status-url>https://api.signering.posten.no/api/{sender-identifier}/direct/signature-jobs/1/status</status-url>
   </direct-signature-job-response>

.. _egenDirekteIntegrasjonSteg2:

Steg 2: Signering av oppdraget
================================

Hele dette steget gjennomføres i signeringsportalen. Du videresender brukeren til portalen ved å benytte URLen du får som svar på opprettelsen av oppdraget. Denne URLen inneholder et engangstoken generert av signeringstjenesten, og det er dette tokenet som gjør at brukeren får tilgang til å lese dokumentet og gjennomføre signeringen.

..  IMPORTANT::
    **Sikkerhet i forbindelse med engangstoken:** For å håndtere sikkerheten i dette kallet vil tokenet kun fungere én gang. Brukeren vil få en cookie av signeringstjenesten ved første kall, slik at en eventuell refresh ikke stopper flyten, men du kan ikke bruke denne URLen på et senere tidspunkt. Årsaken til at vi kun tillater at den brukes kun én gang er at URLer kan fremkomme i eventuelle logger, og de vil dermed ikke være sikre etter å ha blitt benyttet.

Brukeren gjennomfører signeringen og blir deretter sendt tilbake til avsenders portal via URLen spesifisert av ``completion-url``. På slutten av denne URLen vil det legges på et query-parameter (``status_query_token``), som du senere skal benytte når du spør om status. Hvis undertegner avbryter signeringen, eller det skjer en feil, sendes undertegner til henholdsvis ``rejection-url`` eller ``error-url``.

.. _egenDirekteIntegrasjonSteg3:

Steg 3: Hent status
====================

Når undertegner blir sendt tilbake til avsenders portal, kan du gjøre et API-kall (``HTTP GET``) for å hente ned status på oppdraget. Dette gjøres ved å benytte ``status-url`` du fikk i :ref:`Steg 1 <egenDirekteIntegrasjonSteg1>` hvor du legger på query-parameteret (``status_query_token``) du fikk i :ref:`Steg 2 <egenDirekteIntegrasjonSteg2>`.

Dersom du har angitt ``status-retrieval-method=POLLING`` kan du se bort fra ``status_query_token``. Hvis signeringsoppdraget er lagt på en spesifikk kø, så må query-parameteret ``polling_queue`` settes til navnet på køen.


Responsen fra dette kallet er definert gjennom elementet ``direct-signature-job-status-response``. Et eksempel på denne responsen ved et suksessfullt signeringsoppdrag vises under:

.. code:: xml

   <direct-signature-job-status-response xmlns="http://signering.posten.no/schema/v1">
       <signature-job-id>1</signature-job-id>
       <signature-job-status>COMPLETED_SUCCESSFULLY</signature-job-status>
       <status since="2017-01-23T12:51:43+01:00">SIGNED</status>
       <confirmation-url>https://api.signering.posten.no/api/{sender-identifier}/direct/signature-jobs/1/complete</confirmation-url>
       <xades-url>https://api.signering.posten.no/api/{sender-identifier}/direct/signature-jobs/1/xades/1</xades-url>
       <pades-url>https://api.signering.posten.no/api/{sender-identifier}/direct/signature-jobs/1/pades</pades-url>
   </direct-signature-job-status-response>



Steg 4: Laste ned PAdES eller XAdES
-----------------------------------

I forrige steg fikk du to lenker: ``xades-url`` og ``pades-url``. Disse kan du gjøre en ``HTTP GET`` på for å laste ned det signerte dokumentet i de to formatene. For mer informasjon om format på det signerte dokumentet, se :ref:`signerte-dokumenter`.

Steg 5: Bekrefte ferdig prosessering
------------------------------------

Til slutt gjør du et ``HTTP POST``-kall mot ``confirmation-url`` for å bekrefte at du har prosessert jobben ferdig. Hvis :ref:`langtidslagring` benyttes vil dette markere oppdraget som ferdig og lagret. I motsatt fall vil oppdraget slettes fra signeringsportalen.

..  |direkteflytskjema| image:: https://raw.githubusercontent.com/digipost/signature-api-specification/master/integrasjon/flytskjemaer/synkron-maskin-til-maskin.png
    :alt: Flytskjema for direkteintegrasjon