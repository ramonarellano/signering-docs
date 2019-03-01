Signeringsoppdrag
*******************

..  DANGER::
    Lenker i denne filen er under oppbygging og fungerer ikke nå.

Et signeringsoppdrag inneholder et dokument som skal signeres, og kan adresseres til en eller flere undertegnere som skal signere. Tjenesten tilbyr to ulike typer signeringsoppdrag hvor flyten for å signere er det vesentlige.

Signering i direkteflyt
========================

Signering i direkteflyt skjer når undertegner allerede er pålogget i avsenders system. En slik flyt er ideell hvis avsender ønsker at sluttbrukerne skal oppleve signeringsprosessen som en integrert del av deres nettsted.

Flyten ser typisk slik ut:

1. Undertegner er innlogget i avsenders tjeneste, og utfører en prosess der, f.eks. utfylling av et skjema.
1. Avsender oppretter et signeringsoppdrag i signeringstjenesten maskinelt
1. Undertegner blir sendt til signeringstjenesten og gjennomfører signeringssermonien
1. Undertegner blir sendt tilbake til avsenders tjeneste
1. Avsender laster ned [signatur](#signerte_dokumenter) og tilbyr en kopi av det signerte dokumentet til undertegner

Signering i portalflyt
========================

Signering i portalflyt skjer når undertegner logger inn i signeringsportalen til Posten signering.

Flyten ser typisk slik ut:

1. Avsender oppretter et oppdrag gjennom API eller fra web i avsenderportalen.
1. Posten signering varsler undertegner på e-post (og ev. SMS om spesifiert ved [opprettelse](#opprette-signeringsoppdrag)
1. Undertegner logger inn på signeringsportalen og gjennomfører signeringssermonien
1. Undertegner laster ned [signert kopi](#signerte_dokumenter) av dokumentet
1. Undertegner logger ut av signeringsportalen
1. Avsender laster ned [signatur](#signerte_dokumenter)

Opprette signeringsoppdrag
===========================
Ved opprettelse av signeringsoppdrag kan følgende felter angis:

..  DANGER::
    Lenker under *Ekstra informasjon* er alle lenker som ikke er koblet opp.


+---------------------------+-------------------------+-------------------+---------------------------------------------------------------+
| Felt                      | synkrone oppdrag        | asynkrone oppdrag | Ekstra informasjon                                            |
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

.. [#f1] Synkrone signeringsoppdrag blir alltid aktivert øyeblikkelig etter opprettelse. *Standardverdi* er *øyeblikkelig etter opprettelse*.
.. [#f2] Synkrone signeringsoppdrag har alltid 30 dagers levetid for å unngå at et dokument blir signert uhensiktsmessig lenge etter opprettelsen av oppdraget. Eventuell frist fra avsenders perspektiv må kommuniseres og håndteres i avsenders tjenester.

