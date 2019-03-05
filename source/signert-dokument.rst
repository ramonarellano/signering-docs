Signerte dokumenter
====================
Med en digital signatur kan man signere dokumenter papirløst ved å bruke autentisering av en person og koble det sammen med et dokument. For signerte PDF-dokumenter er signaturdata i selve filen, og mange PDF-lesere har mulighet til å vise den digitale signaturen.

Etter at signering av et dokument er fullført så har vi en *teknisk signatur* og en *signert PDF*. En teknisk signatur kalles *XML Advanced Electronic Signature (XAdES)*, og er beviset på at du har signert digitalt. En signert PDF kalles *PDF Advanced Electronic Signature (PAdES)*, og består av originaldokumentet og den tekniske signaturen. 

En teknisk signatur er en XML-fil som inneholder data som gjør at vi kan verifisere hvem som signerte, og sjekke om dokumentet er endret fra signeringstidspunktet. En signert PDF, PAdES, inneholder tekniske signaturer, XAdES, for alle undertegnere. XAdES inneholder de bevis som gjør at det er en gydlig signatur. Dette inkluderer blant annet hvilken signeringsmetode som ble brukt, hvem som signerte når og hvilken IP-adresse undertegner hadde.

Alle dokumenter kan lastes ned i en periode etter at signeringsoppdraget er fullført. Levetiden er avhengig av om `langtidslagring`_ er aktivert for avsenderen.

Hvordan identifiseres undertegnere i et ferdig signert dokument?
------------------------------------------------------------------

Under opprettelse av signeringsoppdrag kan avsender velge hvordan undertegnerne skal identifiseres i de signerte dokumentene. 
Avsender velger å inkludere én av følgende identifikatorer i signerte dokumenter:

Når avsender er en bedrift: 
- Navn + fødselsnummer
- Navn + fødselsdato 

Når avsender er en offentlig virksomhet: 
- Navn + fødselsnummer
- Navn

..  NOTE::
    Dersom du vil at undertegners fødselsnummer skal fremkomme på det signerte dokumentet er du av personvermessige hensyn nødt til å adressere undertegner på fødselsnummer i signeringsoppdraget. 

Hvis du utelater fødselsnummer i de signerte dokumentene kan vi ikke påvise identiteten med 100 % sikkerhet.\ `1`_\  Vi kan likevel i de aller fleste tilfeller oppnå tilstrekkelig beviskraft, på bakgrunn av konteksten signeringen skjer i.

Sannsynligheten er for eksempel svært liten for at 2 personer med navn Kari Olsen signerer en lærekontrakt med Lærlingebedrift AS på eksakt samme tidspunkt. I tillegg vil tekniske spor (audit trail), og andre eksterne forhold som kunderelasjon eller opplysninger i dokumentet også støtte opp under identiteten til den som har signert.
