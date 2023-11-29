# Webpagina Downloader

Deze tool is ontwikkeld om webpagina's te downloaden van een opgegeven URL. Het volgt recursief alle links op de pagina en downloadt de inhoud ervan, inclusief HTML, afbeeldingen, CSS en JavaScript-bestanden.

## Installatie

1. **Vereisten:**
   - Zorg ervoor dat Python (versie 3.x) is geïnstalleerd.
   - Installeer de benodigde bibliotheken met behulp van `pip`:
     ```bash
     pip install requests beautifulsoup4
     ```

## Gebruik

1. **Clonen van de repository:**
   - Kopieer de repository naar een lokaal pad op je computer:
     ```bash
     git clone https://git.fhict.nl/I507824/website-scrapper.git
     ```

2. **Uitvoering:**
   - Open een terminal en navigeer naar de map van de gekloonde repository.
   - Voer het script uit door het volgende commando in te voeren:
     ```bash
     python scrapper.py
     ```
   
3. **Instructies tijdens uitvoering:**
   - Het programma zal om de volgende informatie vragen:
     - Voer de basis-URL in (bijvoorbeeld: https://example.com/).
     - Geef het maximale aantal redirects op dat het programma moet volgen.

4. **Resultaat:**
   - Het gedownloade materiaal wordt opgeslagen in de 'downloaded_files'-map in de hoofdmap van het project.

## Opmerkingen over eerdere versie

Eerder was er een beperktere versie die specifiek ontworpen was voor het downloaden van webpagina's van Zalando. Dit was vanwege de manier waarop Zalando hun bronnen (afbeeldingen, CSS) linkt in hun HTML.

De beperkingen van de vorige versie waren:
- **Andere websites:** Het kon geen afbeeldingen, CSS of JavaScript van andere websites downloaden vanwege verschillen in bronlinking.
- **Functionele beperking:** Het originele script was ontworpen met specifieke aannames over de bronnen van een webpagina.

Dit nieuwe script is ontwikkeld om breder inzetbaar te zijn en verschillende bronnen van verschillende websites te kunnen downloaden.
