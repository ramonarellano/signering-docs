Dokumentpakke
***************

Integriteten til dokumenter og metadata i signeringstjenesten skal kunne valideres mange år etter mottak. Det er ivaretatt ved at informasjonen pakkes i en dokumentpakke som beskyttes med digitale signaturer som beskrevet nedenfor. I praksis er dette en zip-fil med en gitt struktur som inneholder en digital signatur over innholdet.

Standarder
============

===================== ======================================================================================================= ==============
Standard              Dokument                                                                                                 Versjon
===================== ======================================================================================================= ==============
ETSI, ETSI TS 102 918 Electronic Signatures and Infrastructures (ESI); Associated Signature [#etsi1]_                          ETSI, 2013-06.
ETSI, ETSI TS 103 174 Electronic Signatures and Infrastructures (ESI); ASiC Baseline Profile [#etsi2]_                         ETSI, 2013-06.
ETSI, ETSI TS 101 903 Electronic Signatures and Infrastructures (ESI); XML Advanced Electronic Signatures (XAdES) [#etsi3]_    ETSI, 2010-12.
ETSI, ETSI TS 103 171 Electronic Signatures and Infrastructures (ESI); XAdES Baseline Profile [#etsi4]_                        ETSI, 2012-03.
===================== ======================================================================================================= ==============

ASiC-profil for dokumentpakken
-------------------------------

Dokumentet pakkes i en dokumentpakke sammen med noe metadata i henhold til ASiC (ETSI TS 102 918) [#etsi1]_, og videre begrenset i henhold til profilen definert i Baseline Profile (ETSI TS 103 174) [#etsi2]_. Ytterlige begrensninger følger nedenfor:

========================= ================================================================================================================================ =========================================================================================================================================================================================================
Krav                      Felt                                                                                                                             Kommentar
========================= ================================================================================================================================ =========================================================================================================================================================================================================
krav 6.1  [#etsi29]_       ASiC conformance                                                                                                                Skal være “ASiC-E XAdES”
krav 8.1 [#etsi211]_       ASiC-E Media type identification                                                                                                Skal være “ASiC file extension is”.asice
krav 8.2 [#etsi211]_       ASiC-E Signed data object                                                                                                       Alle filer utenfor META-INF katalogen skal være signert.
krav 8.3.1 [#etsi212]_     ASiC-E XAdES signature                                                                                                          Det skal kun være en signatur i META-INF katalogen, med navn signatures.xml. Denne signaturen skal dekke alle andre filer i beholderen, og avsenderens virksomhetssertifikat skal benyttes for signering.
krav 8.3.2 [#etsi212]_     Requirements for the contents of Container” refererer til “6.2.2 punkt 4b) "META-INF/manifest.xml" if present […] i”ASiC":etsi1 Denne filen skal ikke være tilstede.
========================= ================================================================================================================================ =========================================================================================================================================================================================================

Signatur i dokumentpakken
--------------------------

Dokumentpakken bør være signert av “Behandlingsansvarlig”, men kan signeres av “Databehandler”.

Signaturen skal være i henhold til XAdES (ETSI TS 101 903) [#etsi3]_ med basisprofilen definert i XAdES Baseline Profile (ETSI TS 103 171) [#etsi4]_ (B-Level Conformance). Ytterlige begrensninger følger nedenfor:

========================= ============================================= ===================================================================================================================================================================================================================================================================
Krav                      Felt                                          Kommentar
========================= ============================================= ===================================================================================================================================================================================================================================================================
krav 5.1 [#etsi48]_        Algorithm requirements                       Signeringsalgoritmen skal være `rsa-sha256 <http://www.w3.org/2001/04/xmldsig-more#rsa-sha256>`_. Fingeravtrykksalgoritmen i referansene skal være `sha256 <http://www.w3.org/2001/04/xmlenc#sha256>`_. Fingeravtrykksalgoritmen i CertDigest skal være `sha1 <http://www.w3.org/2000/09/xmldsig#sha1>`_.
krav 6.2.1 [#etsi410]_     Placement of the signing certificate         Alle sertifikater fra virkomhetsertifikatet og opp til og inkludert en tiltrodd rot skal være inkludert.
krav 6.2.2 [#etsi411]_     Canonicalization of ds:SignedInfo element    Bør være `xml-c14n11 <http://www.w3.org/2006/12/xml-c14n11>`_. Kan være `REC-xml-c14n-20010315 <http://www.w3.org/TR/2001/REC-xml-c14n-20010315>`_
krav 6.2.3 [#etsi411]_     Profile of ds:Reference element              Alle dokumenter skal være med, og det er ikke lov med referanser utenfor dokumentpakken.
krav 6.2.4 [#etsi412]_     Transforms within ds:Reference element       Alle fil-referansene skal være uten transform, og referansen til SignedProperties skal være `REC-xml-c14n-20010315 <http://www.w3.org/TR/2001/REC-xml-c14n-20010315>`_
krav 6.3.1 [#etsi412]_     Profile of xades:SigningCertificate element  Ingen ytterlige begrensninger.
krav 6.3.2 [#etsi413]_     Profile of xades:SigningTime element         Tidsangivelsen skal være korrekt innenfor +/- 5 sekunder.
krav 6.3.3 [#etsi413]_     Profile of xades:DataObjectFormat element    Kun MimeType og ObjectReference skal være med.
========================= ============================================= ===================================================================================================================================================================================================================================================================

..  rubric:: Footnotes

.. [#etsi1] http://www.etsi.org/deliver/etsi_ts/102900_102999/102918/01.03.01_60/ts_102918v010301p.pdf
.. [#etsi2] http://www.etsi.org/deliver/etsi_ts/103100_103199/103174/02.02.01_60/ts_103174v020201p.pdf
.. [#etsi29] http://www.etsi.org/deliver/etsi_ts/103100_103199/103174/02.02.01_60/ts_103174v020201p.pdf#page=9
.. [#etsi211] http://www.etsi.org/deliver/etsi_ts/103100_103199/103174/02.02.01_60/ts_103174v020201p.pdf#page=11
.. [#etsi212] http://www.etsi.org/deliver/etsi_ts/103100_103199/103174/02.02.01_60/ts_103174v020201p.pdf#page=12
.. [#etsi3] http://www.etsi.org/deliver/etsi_ts%5C101900_101999%5C101903%5C01.04.02_60%5Cts_101903v010402p.pdf
.. [#etsi4] http://www.etsi.org/deliver/etsi_ts/103100_103199/103171/02.01.01_60/ts_103171v020101p.pdf
.. [#etsi48] http://www.etsi.org/deliver/etsi_ts/103100_103199/103171/02.01.01_60/ts_103171v020101p.pdf#page=8
.. [#etsi410] http://www.etsi.org/deliver/etsi_ts/103100_103199/103171/02.01.01_60/ts_103171v020101p.pdf#page=10
.. [#etsi411] http://www.etsi.org/deliver/etsi_ts/103100_103199/103171/02.01.01_60/ts_103171v020101p.pdf#page=11
.. [#etsi412] http://www.etsi.org/deliver/etsi_ts/103100_103199/103171/02.01.01_60/ts_103171v020101p.pdf#page=12
.. [#etsi413] http://www.etsi.org/deliver/etsi_ts/103100_103199/103171/02.01.01_60/ts_103171v020101p.pdf#page=13
