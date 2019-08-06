Steg 3: Laste ned PAdES eller XAdES
=====================================

Responsen i forrige steg inneholder lenkene ``xades-url`` og ``pades-url``. Disse kan du gjøre en ``HTTP GET`` på for å laste ned det signerte dokumentet i de to formatene. For mer informasjon om format på det signerte dokumentet, se :ref:`signerte-dokumenter`.

XAdES-filen laster du ned per undertegner, mens PAdES-filen lastes ned på tvers av alle undertegnere. Denne vil inneholde signeringsinformasjon for alle undertegnere som frem til nå har signert oppdraget. I de aller fleste tilfeller er det ikke aktuelt å laste ned denne før alle undertegnerne har statusen ``SIGNED``.

..  _egen-integrasjon-steg-4:

Steg 4: Bekrefte ferdig prosessering
======================================

Til slutt gjør du et ``HTTP POST``-kall mot ``confirmation-url`` for å bekrefte at du har mottatt/persistert statusoppdateringen. Dersom statusen indikerer at oppdraget er helt ferdig, så vil dette kallet også bekrefte at du er ferdig med å prosessere hele oppdraget.
Hvis :ref:`langtidslagring` benyttes vil dette markere oppdraget som ferdig og lagret, ellers vil oppdraget slettes fra signeringstjenesten.


