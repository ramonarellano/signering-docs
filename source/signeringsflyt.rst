Signeringsflyt
*******************

..  DANGER::
    Lenker i denne filen er under oppbygging og fungerer ikke nå.

Et signeringsoppdrag inneholder et dokument som skal signeres, og kan adresseres til en eller flere undertegnere som skal signere. Tjenesten tilbyr i hovedsak to ulike typer signeringsflyter.

.. _signering-i-direkteflyt:

Signering i direkteflyt
========================

Signering i direkteflyt skjer når undertegner allerede er pålogget i avsenders system. En slik flyt er ideell hvis avsender ønsker at sluttbrukerne skal oppleve signeringsprosessen som en integrert del av deres nettsted.

Flyten ser typisk slik ut:

#. Undertegner er innlogget i avsenders tjeneste, og utfører en prosess der, f.eks. utfylling av et skjema er sluttresultatet
#. Avsender oppretter et signeringsoppdrag i signeringstjenesten gjennom API
#. Undertegner blir sendt til signeringstjenesten og gjennomfører signeringen
#. Undertegner blir sendt tilbake til avsenders tjeneste
#. Avsender laster ned signatur og tilbyr en kopi av det signerte dokumentet til undertegner

Se gjerne `denne bildeguiden i Google Presentation for signering i direkteflyt <https://docs.google.com/presentation/d/14Q_-YzaxcGsZOgUR6rJl7rWSwLZwujnuqgkKCrxksoA/edit#slide=id.g3922592cb8_0_0>`_.

.. _signering-i-portalflyt:

Signering i portalflyt
========================

Adressering med fødselsnummer
______________________________

Hvis man adresserer med fødselsnummer så vil undertegner måtte logge inn i signeringsportalen for å kunne se signeringsoppdraget.

Flyten ser typisk slik ut:

#. Avsender oppretter et oppdrag gjennom API eller fra web i avsenderportalen
#. Posten signering varsler undertegner på e-post (og ev. SMS om spesifiert ved opprettelse)
#. Undertegner logger inn på signeringsportalen og gjennomfører signeringssermonien
#. Undertegner laster ned signert dokument
#. Undertegner logger ut av signeringsportalen
#. Avsender laster ned det signerte dokumentet

Se gjerne `denne bildeguiden i Google Presentation for signering i portalflyt, adressering med fødselsnummer <https://docs.google.com/presentation/d/14Q_-YzaxcGsZOgUR6rJl7rWSwLZwujnuqgkKCrxksoA/edit#slide=id.g36b93b9965_0_57>`_.

Adressering uten fødselsnummer
_______________________________

 En signeringsflyt hvor man får tilgang til portalen vha en lenke og et engangspassord. Se bildeguide her.

#. Avsender oppretter et oppdrag gjennom API eller fra web i avsenderportalen
#. Undertegner mottar en unik lenke og engangskode til oppdrag på e-post eller SMS
#. Undertegner trykker på lenken, og fyller inn engangskode til oppdrag
#. Undertegner gjennomfører signeringsseremonien
#. Sluttside som gir mulighet til å laste ned signert dokument

Når man adresserer undertegner uten fødselsnummer, er det avsenders ansvar å sjekke at det er rett eller ønsket person som har signert.

Se gjerne `denne bildeguiden i Google Presentation for signering i portalflyt, adressering uten fødselsnummer <https://docs.google.com/presentation/d/14Q_-YzaxcGsZOgUR6rJl7rWSwLZwujnuqgkKCrxksoA/edit#slide=id.g2e3b4edaeb_0_1>`_.

Opprette signeringsoppdrag
===========================

..  DANGER::
    Lenker under *Ekstra informasjon* er ikke alle koblet opp og vil bli fikset på sikt etterhvert som dokumentasjonen her bygges opp.

Ved opprettelse av signeringsoppdrag kan følgende felter angis:

+---------------------------+-------------------------+-------------------+---------------------------------------------------------------+
| Felt                      | Direkteflyt             | Portalflyt        | Ekstra informasjon                                            |
+===========================+=========================+===================+===============================================================+
| Dokument                  | **Obligatorisk**        | **Obligatorisk**  |                                                               |
+---------------------------+-------------------------+-------------------+---------------------------------------------------------------+
| Undertegner(e)            | **Obligatorisk**        | **Obligatorisk**  | se undertegners kontaktinfo                                   |
+---------------------------+-------------------------+-------------------+---------------------------------------------------------------+
| Tittel                    | **Obligatorisk**        | **Obligatorisk**  |                                                               |
+---------------------------+-------------------------+-------------------+---------------------------------------------------------------+
| Signaturtype              | Valgfritt               | Valgfritt         | se signaturtype                                               |
+---------------------------+-------------------------+-------------------+---------------------------------------------------------------+
| Sikkerhetsnivå            | Valgfritt               | Valgfritt         | se sikkerhetsnivå                                             |
+---------------------------+-------------------------+-------------------+---------------------------------------------------------------+
| Melding til mottaker(e)   | Valgfritt               | Valgfritt         |                                                               |
+---------------------------+-------------------------+-------------------+---------------------------------------------------------------+
| Undertegners identifikator| Valgfritt               | Valgfritt         | se undertegners identifikator                                 |
+---------------------------+-------------------------+-------------------+---------------------------------------------------------------+
| Aktiveringstidspunkt      | Ikke overstyrbar [#f1]_ | Valgfritt         |                                                               |
+---------------------------+-------------------------+-------------------+---------------------------------------------------------------+
| Levetid                   | Ikke overstyrbar [#f2]_ | Valgfritt         |                                                               |
+---------------------------+-------------------------+-------------------+---------------------------------------------------------------+
| E-postadresse             | Ikke relevant           | **Obligatorisk**  | se :ref:`varsler`                                             |
+---------------------------+-------------------------+-------------------+---------------------------------------------------------------+
| Mobilnummer               | Ikke relevant           | Valgfritt         | se :ref:`varsler`                                             |
+---------------------------+-------------------------+-------------------+---------------------------------------------------------------+
| Rekkefølge                | Ikke relevant           | Valgfritt         | se kjedet signatur                                            |
+---------------------------+-------------------------+-------------------+---------------------------------------------------------------+

.. rubric:: Footnotes

.. [#f1] Signeringsoppdrag i direkteflyt blir alltid aktivert øyeblikkelig etter opprettelse. *Standardverdi* er *øyeblikkelig etter opprettelse*.
.. [#f2] Signeringsoppdrag i direkteflyt har alltid 30 dagers levetid for å unngå at et dokument blir signert uhensiktsmessig lenge etter opprettelsen av oppdraget. Eventuell frist fra avsenders perspektiv må kommuniseres og håndteres i avsenders tjenester.

For implementasjon for signeringsoppdrag i portalflyt, se  :ref:`portal-flow`, og for signeringsoppdrag i direkteflyt, se :ref:`direct-flow`.

Begrensninger
______________

Antall undertegnere
^^^^^^^^^^^^^^^^^^^^^

Tjenesten tillater maksimalt 10 undertegnere pr. oppdrag.

Hastighet
^^^^^^^^^^^

Tjenesten tillater maksimalt 10 API-kall i sekundet per organisasjonsnummer. Hvis en avsender overskrider denne grensen vil API-et returnere :code:`HTTP 429 Too Many Requests`, og avsenderen vil bli blokkert i 30 sekunder.

Dokumentformat
^^^^^^^^^^^^^^^^^

Tjenesten støtter dokumenter av typen ren tekst (:code:`.txt`) og PDF (:code:`.pdf`). Både PDF og PDF/A aksepteres av tjenesten. Det signerte dokumentet vil være av samme type som originaldokumentet.
Et originaldokument som er PDF/A gir et signert PAdES-dokument som er PDF/A, og et originaldokument som er PDF versjon 1.1 – 1.7 gir et signert PAdES-dokument som er PDF versjon 1.7.
For PDF/A vil tjenesten alltid produsere signerte PAdES-dokumenter av typen PDF/A-3b, uavhengig av PDF/A-versjon og -konformitetsnivå på originaldokumentet.

For arkivering av signerte dokumenter anbefaler vi å bruke originaldokumenter av typen PDF/A. Dette er et krav hvis det signerte dokumentet skal avleveres til Riksarkivet.

..  NOTE::
    Filen kan maksimalt være 3 MB (:code:`3 145 728 bytes`) stor. PDF-versjoner som støttes er PDF 1.1-1.7.

I PAdES vil dokumentet alltid presenteres i A4- og portrett-format. For best resultat anbefales det at det innsendte dokumentet også har dette formatet.

..  DANGER::
    Passordbeskyttede dokumenter (begrenset lese- og/eller skrive-tilgang) er ikke støttet av tjenesten og vil gi feilmelding først ved nedlasting av dokumentet.

Aktiveringstidspunkt
^^^^^^^^^^^^^^^^^^^^^^

Angir tidspunkt for når signeringsoppdraget skal tilgjengeliggjøres for undertegner(e). Dersom aktiveringstidspunktet er i fortiden, blir oppdraget tilgjengelig øyeblikkelig etter opprettelse.

Signeringsoppdrag i direkteflyt blir alltid aktivert øyeblikkelig etter opprettelse.

Oppdragets levetid
^^^^^^^^^^^^^^^^^^^^

Angir hvor lenge *etter aktivering* et signeringsoppdrag er tilgjengelig for undertegner før det utløper. Kan maksimalt være 90 dager etter aktivering.

Signeringsoppdrag i direkteflyt har alltid 30 dagers levetid for å unngå at et dokument blir signert uhensiktsmessig lenge etter opprettelsen av oppdraget. Eventuell frist fra avsenders perspektiv må kommuniseres og håndteres i avsenders tjenester.

Kansellere signeringsoppdrag
==============================

Kansellering av signeringsoppdrag er bare relevant for signeringsoppdrag som signeres i signeringsportalen, dvs. signering i portalflyt.

Et signeringsoppdrag kan på et hvilket som helst tidspunkt kanselleres av avsender, så lenge ikke oppdraget allerede er fullført. Kansellerte oppdrag blir utilgjengeliggjort for undertegnere som enda ikke har signert.

