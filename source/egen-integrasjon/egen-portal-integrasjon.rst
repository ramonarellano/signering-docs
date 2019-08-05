.. _egenPortalIntegrasjonSteg1:

Steg 1: Opprette signeringsoppdraget
======================================


Respons
--------

Som respons på dette kallet vil man få elementet ``portal-signature-job-response``. Denne responsen inneholder en ID generert av signeringstjenesten. Du må lagre denne IDen i dine systemer slik at du senere kan koble resultatene du får fra polling-mekanismen til riktig oppdrag.

.. code-block:: xml

   <portal-signature-job-response xmlns="http://signering.posten.no/schema/v1">
       <signature-job-id>1</signature-job-id>
       <cancellation-url>https://api.signering.posten.no/api/{sender-identifier}/portal/signature-jobs/1/cancel</cancellation-url>
   </portal-signature-job-response>

Steg 2: Polling på status
==========================

For å finne ut hva statusen er for de signeringsoppdragene du har opprettet, må du jevnlig sende forespørsler til signeringstjenesten (polling). Som avsender må du sjekke hvilket oppdrag statusoppdateringen gjelder for å oppdatere i ditt system og så bekrefte den.

Responsen på dette kallet vil være én av to ting:

- **statusoppdatering:** en ``200 OK``-respons som inneholder informasjon om ny status for ett oppdrag. Denne er definert av elementet ``portal-signature-job-status-change-response``.
- **ingen oppdatering tilgjengelig:** Dersom det ikke er noen oppdateringer for dine signeringsoppdrag, vil du få en ``204 No Content``-respons.

Hyppighet
----------

Responsene vil alltid inneholde HTTP-headeren ``X-Next-permitted-poll-time`` som forteller deg når du kan gjøre neste forespørsel, og det er viktig at dette tidspunktet overholdes. Dersom man sender en forespørsel før dette tidspunktet har passert, vil man få en ``429 Too Many Requests``-respons tilbake. Denne vil også inneholde headeren ``X-Next-permitted-poll-time`` med et nytt tidspunkt.

..  NOTE::
    I produksjonsmiljøet vil neste tillatte polling-tidspunkt være om 10 minutter om køen er tom, mens for testmiljøer vil det være mellom 5 og 30 sekunder.

I praksis vil tidspunktet for neste tillatte polling-forespørsel være umiddelbart så lenge man får en respons som inneholder en statusoppdatering.


Integrasjon
------------


For å polle, så gjør du en ``HTTP GET`` mot ``<rot-URL>/portal/signature-jobs``. Oppdrag som ikke er lagt på en spesifikk kø vil havne på en standard-kø. Hvis signeringsoppdraget er lagt på en spesifikk kø, så må også query-parameteret ``polling_queue`` settes til navnet på køen, f.eks. ``<rot-URL>/portal/signature-jobs?polling_queue=custom-queue``. Du skal ikke ha med noen request-body på dette kallet.

Følgende er et eksempel på en respons der en del av signeringsoppdraget har blitt fullført:

.. code-block:: xml

   <portal-signature-job-status-change-response xmlns="http://signering.posten.no/schema/v1">
       <signature-job-id>1</signature-job-id>
       <status>IN_PROGRESS</status>
       <confirmation-url>https://api.signering.posten.no/api/{sender-identifier}/portal/signature-jobs/1/complete</confirmation-url>
       <signatures>
           <signature>
               <status since="2017-01-23T12:51:43+01:00">SIGNED</status>
               <personal-identification-number>12345678910</personal-identification-number>
               <xades-url>https://api.signering.posten.no/api/{sender-identifier}/portal/signature-jobs/1/xades/1</xades-url>
           </signature>
           <signature>
               <status since="2017-01-23T12:00:00+01:00">WAITING</status>
               <personal-identification-number>98765432100</personal-identification-number>
           </signature>
           <pades-url>https://api.signering.posten.no/api/{sender-identifier}/portal/signature-jobs/1/pades</pades-url>
       </signatures>
   </portal-signature-job-status-change-response>


Statusoppdateringer du henter vil forsvinne fra køen. Dette gjør det mulig å spørre om statusoppdateringer i parallell, og du vil ikke få samme statusoppdatering to ganger. Det er derfor viktig at du bekrefter mottak av hver statusoppdatering så raskt som mulig, for dersom det likevel skulle skje en feil under overføring eller prosessering, så vil kvitteringen legges på køen igjen etter 10 minutter. Mer informasjon om hvordan du bekrefter en kvittering er beskrevet i :ref:`egen-integrasjon-steg-4`.

Steg 3: Laste ned PAdES eller XAdES
=====================================

Responsen i forrige steg inneholder lenkene ``xades-url`` og ``pades-url``. Disse kan du gjøre en ``HTTP GET`` på for å laste ned det signerte dokumentet i de to formatene. For mer informasjon om format på det signerte dokumentet, se :ref:`signerte-dokumenter`.

XAdES-filen laster du ned per undertegner, mens PAdES-filen lastes ned på tvers av alle undertegnere. Denne vil inneholde signeringsinformasjon for alle undertegnere som frem til nå har signert oppdraget. I de aller fleste tilfeller er det ikke aktuelt å laste ned denne før alle undertegnerne har statusen ``SIGNED``.

..  _egen-integrasjon-steg-4:

Steg 4: Bekrefte ferdig prosessering
======================================

Til slutt gjør du et ``HTTP POST``-kall mot ``confirmation-url`` for å bekrefte at du har mottatt/persistert statusoppdateringen. Dersom statusen indikerer at oppdraget er helt ferdig, så vil dette kallet også bekrefte at du er ferdig med å prosessere hele oppdraget.
Hvis :ref:`langtidslagring` benyttes vil dette markere oppdraget som ferdig og lagret, ellers vil oppdraget slettes fra signeringstjenesten.


