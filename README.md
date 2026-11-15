# Ideensammlung für zukunftsorientierte Prüfungsformate

Statische Web-App für GitHub Pages: Schieberegler einstellen, passende Prüfungsbeispiele mit Link zur Originalquelle finden. Kein Build-Schritt, keine externen Ressourcen, kein Tracking, keine Cookies.

## Dateien

```
index.html             die komplette App (HTML, CSS, JavaScript)
data/pruefungen.json   die Sammlung der Prüfungsbeispiele
README.md              diese Anleitung
```

Die JSON-Datei muss im Unterordner `data` liegen und `pruefungen.json` heißen.

## Auf GitHub Pages veröffentlichen

1. Neues öffentliches Repository anlegen, z. B. `wiegweb/pruefungsformate`.
2. `index.html`, `README.md` und den Ordner `data` hochladen (im Browser: „Add file → Upload files“, den Ordner `data` als Ganzes hineinziehen).
3. Im Repository: **Settings → Pages → Build and deployment → Source: „Deploy from a branch“**, Branch `main`, Ordner `/ (root)`, speichern.
4. Nach etwa einer Minute ist die Seite unter `https://wiegweb.github.io/pruefungsformate/` erreichbar.

## Sammlung erweitern

Die Datei `data/pruefungen.json` durch eine neue Fassung ersetzen (gleicher Name, gleicher Ordner). Am Code muss nichts geändert werden: Filteroptionen, Fächerlisten und Zähler entstehen aus den Daten.

Die Datei ist ein JSON-Array. Jeder Eintrag kann diese Felder haben:

`id, titel, kurzbeschreibung, fach, faechergruppe, jg_von, jg_bis, schulform, land, sprache, pruefungsart, ki_rolle (0–4), ki_rolle_begruendung, aias_stufe, digitale_medien, tools, achse1 … achse9 (1–5 oder null), achsen_belegstatus, material_vorhanden, link_primaer, linktyp, fundpfad, weitere_links, urheber, datum, lizenz, link_status, qualitaet, konfidenz`

Regeln der App:

- **Fehlende Angaben blenden nie aus.** Hat ein Beispiel bei einer Achse, beim Jahrgang oder bei den digitalen Medien keine Angabe (`null`, leer, „nicht belegt“), bleibt es bei jeder Regler- und Filterstellung sichtbar und wird mit „keine Angabe“ gekennzeichnet. Im Ranking rutschen Beispiele mit vielen Lücken etwas nach unten.
- Kein Feld ist Pflicht. Einträge, die kein JSON-Objekt sind, werden übersprungen und oben auf der Seite gemeldet.
- Links werden nur angezeigt, wenn sie mit `http://` oder `https://` beginnen.
- Beginnt ein Titel mit `[TEST]`, zeigt die Seite einen Testdaten-Hinweis.

## Texte und Einstellungen ändern

Alles Anpassbare steht am Anfang des Skripts in `index.html` im Objekt `CONFIG`:

- `achsen`: Name, Kurzname, Pole und die fünf Stufenbeschreibungen jedes Reglers. `start` ist die Stufe im Ausgangsprofil (traditionelle Klassenarbeit).
- `ausgangsprofil`: Bezeichnung des Ausgangsprofils.
- `kiStufen`, `fachbereiche`, `laender`: Bezeichnungen in den Filtern.
- `pruefungsartGruppen`: Die Prüfungsarten in den Daten sind sehr kleinteilig. Für den Filter werden sie über Stichworte zu wenigen Gruppen gebündelt. Auf den Karten steht weiterhin die Originalbezeichnung.
- `bewertungsStichworte`: Wörter, an denen die Checkbox „nur mit Erwartungshorizont / Bewertungsraster“ Bewertungsmaterial erkennt (gesucht in `material_vorhanden` und `qualitaet`).
- `proSeite`: Zahl der Karten, die zunächst erscheinen.

## Trefferlogik

- Die Regler sind stufenlos (1,0 bis 5,0). Unter jedem Regler steht die Beschreibung der nächstgelegenen Stufe.
- **Ranking** (Standard): Passung = 1 − mittlere Abweichung über alle aktiven Regler mit bekanntem Wert ÷ 4. Zuerst kommen Beispiele, die auf mindestens der Hälfte der aktiven Regler vergleichbar sind, streng nach Passung sortiert; danach in einem eigenen Abschnitt die mit wenigen Angaben.
- Farben: ab 90 % grün, 80–89 hellgrün, 70–79 gelb, 60–69 orange, 50–59 rot. Beispiele unter 50 % werden ausgeblendet (`SCHWELLE` im Skript); Beispiele ohne vergleichbare Angaben bleiben sichtbar.
- **Filter**: Es erscheinen nur Beispiele, die auf jedem aktiven Regler höchstens um die gewählte Toleranz abweichen. Fehlende Werte gelten als passend.
- Ein Regler auf „egal“ zählt nicht mit.

## Neue Funde einpflegen

`werkzeuge/daten_einpflegen.py` prüft neue Einträge (Pflichtfelder, Wertebereiche, Links), erkennt Dubletten und hängt nur gültige, neue Einträge an. Bestehende Einträge bleiben unverändert.

```
python3 werkzeuge/daten_einpflegen.py neue_funde.json              # nur prüfen
python3 werkzeuge/daten_einpflegen.py neue_funde.json --schreiben  # einpflegen
```

`werkzeuge/RECHERCHE-AUFTRAG.md` enthält den Entwurf für einen regelmäßigen Rechercheauftrag, der neue Funde als Pull Request zur Freigabe vorlegt.

## Lokal testen

Ein Doppelklick auf `index.html` reicht nicht, weil Browser das Nachladen der JSON-Datei von der Festplatte blockieren. Zwei Wege:

- Im Ordner ein Terminal öffnen, `python3 -m http.server 8000` starten und `http://localhost:8000` aufrufen.
- Oder `index.html` direkt öffnen und in der Fehlermeldung über „JSON-Datei von diesem Gerät laden“ die Datei auswählen.
