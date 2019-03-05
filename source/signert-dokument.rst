Signerte dokumenter
====================´

Tjenesten tilgjengeliggjør signaturer i to formater når et dokument har
blitt signert – `PAdES`_ og `XAdES`_. Det vil maksimalt finnes én PAdES
for et signeringsoppdrag, mens det vil finnes én XAdES *per
undertegner*.

.. _PAdES: #pades
.. _XAdES: #xades

Alle dokumenter kan lastes ned i en periode etter at signeringsoppdraget
er fullført. Levetiden er avhengig av om `langtidslagring`_ er aktivert
for avsenderen.

Hvordan identifiseres undertegnere i et ferdig signert dokument?
------------------------------------------------------------------

Under opprettelse av signeringsoppdrag kan avsender velge hvordan
undertegnerne skal identifiseres i de signerte dokumentene. 
Avsender velger å inkludere én av følgende identifikatorer i signerte
dokumenter:

Når avsender er en bedrift: 
- Navn + fødselsnummer
- Navn + fødselsdato 

Når avsender er en offentlig virksomhet: 
- Navn + fødselsnummer
- Navn

Merk: Dersom du vil at undertegners fødselsnummer skal fremkomme på det signerte dokumentet er du av personvermessige hensyn nødt til å adressere undertegner på fødselsnummer i signeringsoppdraget. 

Følgende tabell viser hvilke valg som er gyldige for hhv. offentlige og
private avsendervirksomheter når det innhentes `avanserte eller
autentiserte signaturer`_:

=========== ====== =========
\           Privat Offentlig
=========== ====== =========
Avansert    1, 2   1
Autentisert N/A    1, 3
=========== ====== =========

*Merk*: Alternativ 1 kan kun benyttes om fødselsnummer er brukt for å
identifiseres undertegner ved opprettelse av oppdraget. Se for øvrig
avsnittet om `undertegners identifikator og kontaktinfo`_

Hvis du utelater fødselsnummer i de signerte dokumentene kan vi ikke
påvise identiteten med 100 % sikkerhet.\ `1`_\  Vi kan likevel i de
aller fleste tilfeller oppnå tilstrekkelig beviskraft, på bakgrunn av
konteksten signeringen skjer i.

Sannsynligheten er for eksempel svært liten for at 2 personer med navn
Kari Olsen signerer en lærekontrakt med Lærlingebedrift AS på eksakt
samme tidspunkt. I tillegg vil tekniske spor (audit trail), og andre
eksterne forhold som kunderelasjon eller opplysninger i dokumentet også
støtte opp under identiteten til den som har signert.

1 Det signerte dokumentet inneholder en anonymisert identifikator som
identifiserer undertegneren med 100 % sikkerhet hos leverandøren av
e-ID, for eksempel hos BankID. Dette krever oppslag hos leverandøren av
e-ID og støttes kun ved avansert e-signatur.

.. _langtidslagring: #langtidslagring
.. _avanserte eller autentiserte signaturer: #autentisert-og-avansert-e-signatur
.. _undertegners identifikator og kontaktinfo: #identifikator-kontaktinfo
.. _1: #fotnote-e-id-identifikator
