Signeringsoppdrag
*******************

..  DANGER::
    Lenker i denne filen er under oppbygging og fungerer ikke nå.

Et signeringsoppdrag inneholder et dokument som skal signeres, og kan adresseres til en eller flere undertegnere som skal signere. Tjenesten tilbyr to ulike typer signeringsoppdrag hvor flyten for å signere er det vesentlige.

Signering i direkteflyt
========================

Signering i direkteflyt skjer når undertegner allerede er pålogget i avsenders system. En slik flyt er ideell hvis avsender ønsker at sluttbrukerne skal oppleve signeringsprosessen som en integrert del av deres nettsted.

Flyten ser typisk slik ut:

#. Undertegner er innlogget i avsenders tjeneste, og utfører en prosess der, f.eks. utfylling av et skjema.
#. Avsender oppretter et signeringsoppdrag i signeringstjenesten maskinelt
#. Undertegner blir sendt til signeringstjenesten og gjennomfører signeringssermonien
#. Undertegner blir sendt tilbake til avsenders tjeneste
#. Avsender laster ned [signatur](#signerte_dokumenter) og tilbyr en kopi av det signerte dokumentet til undertegner

Signering i portalflyt
========================

Signering i portalflyt skjer når undertegner logger inn i signeringsportalen til Posten signering.

Flyten ser typisk slik ut:

#. Avsender oppretter et oppdrag gjennom API eller fra web i avsenderportalen.
#. Posten signering varsler undertegner på e-post (og ev. SMS om spesifiert ved [opprettelse](#opprette-signeringsoppdrag)
#. Undertegner logger inn på signeringsportalen og gjennomfører signeringssermonien
#. Undertegner laster ned [signert kopi](#signerte_dokumenter) av dokumentet
#. Undertegner logger ut av signeringsportalen
#. Avsender laster ned [signatur](#signerte_dokumenter)

Opprette signeringsoppdrag
===========================
Ved opprettelse av signeringsoppdrag kan følgende felter angis:

..  DANGER::
    Lenker under *Ekstra informasjon* er alle lenker som ikke er koblet opp.


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
| E-postadresse             | Ikke relevant           | **Obligatorisk**  | se varsling                                                   |
+---------------------------+-------------------------+-------------------+---------------------------------------------------------------+
| Mobilnummer               | Ikke relevant           | Valgfritt         | se varsling                                                   |
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

I [PAdES](#signerte_dokumenter) vil dokumentet alltid presenteres i A4- og portrett-format. For best resultat anbefales det at det innsendte dokumentet også har dette formatet.

..  DANGER::
    Passordbeskyttede dokumenter (begrenset lese- og/eller skrive-tilgang) er ikke støttet av tjenesten og vil gi feilmelding først ved nedlasting av dokumentet.

Aktiveringstidspunkt
^^^^^^^^^^^^^^^^^^^^^^

Angir tidspunkt for når signeringsoppdraget skal tilgjengeliggjøres for undertegner(e). Dersom aktiveringstidspunktet er i fortiden, blir oppdraget tilgjengelig øyeblikkelig etter opprettelse.

For [kjedete signeringsoppdrag](#kjedet-signatur) gjelder aktiveringstidspunktet for *første gruppe*.

Oppdragets levetid
^^^^^^^^^^^^^^^^^^^^

Angir hvor lenge *etter aktivering* et signeringsoppdrag er tilgjengelig for undertegner før det utløper. Kan maksimalt være 90 dager etter aktivering.

For [kjedete signeringsoppdrag](#kjedet-signatur) gjelder levetiden for *hver gruppe*, slik at alle undertegnere får like mye tid på seg til å signere.

Kansellere signeringsoppdrag
==============================

Kansellering av signeringsoppdrag er bare relevant for signeringsoppdrag som signeres i signeringsportalen, dvs. signering i portalflyt.

Et signeringsoppdrag kan på et hvilket som helst tidspunkt kanselleres av avsender, så lenge ikke oppdraget allerede er fullført. Kansellerte oppdrag blir utilgjengeliggjort for undertegnere som enda ikke har signert.

