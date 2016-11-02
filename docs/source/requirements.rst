**Requirements**
****************

Funktionale Requirements
========================
- Der SiteMapCrawler soll aus einer Webseite eine SiteMap erstellen können.
- Der PageDownloader wird eine Url aussuchen und mit Hilfe von PageComposer und PageAnalyser eine Kopie dieser Webseite bilden.
- Der Inhalt der Webseitenkopie besteht aus Medienfiles und Texten, die in Directories strukturiert werden.
- Der PageComposer wird diesen Inhalt für eine Nachbildung der Quellenwebseite vorbereiten.
- Die Nachbildung wird dann der PageSaver erarbeiten können und es wird die Möglichkeit bestehen, diese lokal speichern zu können.

Non-funktionale Requirements
============================
- Performance:
    - Hohe Reaktionszeit (Die Applikation muss möglicht schnell auf die User Interaktion reagieren.)
    - Hohe Transaktionsrate (Einige Componente werden simultan arbeiten können.)
- Genauigkeit der Webseitekopie
- Verfügbarkeit, Zuverlässigkeit & Stabilität
- Effizienz (Die Applikation wird sparsam Systemressourcen verbrauchen.)
- Bedienbarkeit / Usability
