# Bewertungsregeln für die Reglerwerte

Stand: 20.11.2026. Grundlage ist der Anker-Check mit Timm Wiegmann.
Die Stufenbeschreibungen stehen in `index.html` unter `CONFIG.achsen`.

## Grundsätze

1. **Keine Lücken lassen.** Sagt die Quelle zu einer Achse nichts, wird plausibel geschätzt und der Wert als „eingeschätzt“ markiert. Grundlage für die Schätzung ist der Arbeitsauftrag, nicht nur die Kurzbeschreibung. Wenn möglich, wird die Quelle gelesen. `null` bleibt nur, wenn auch eine begründete Schätzung unmöglich ist.
2. **Die offenste Phase zählt.** Bei mehrphasigen Formaten zählt die offenste Phase, in der wesentliche Teile der bewerteten Leistung entstehen. Diese Regel ist aus R13, ISB15-DEBATTE und ZUM-03 abgeleitet. Beispiele:
   - Ein Produkt entsteht zu Hause und wird in der Schule präsentiert: Ort = 5.
   - Bei einer Debatte wird zu Hause vorbereitet, Hilfsmittel sind dabei frei: Hilfsmittel = 5.
3. **Nur echte Prüfungen.** Aufgenommen wird nur, was eine echte Prüfungsfunktion hat, also benotet wird oder eine Klassenarbeit ersetzt. Kreative Arbeitsblatt-Aufgaben ohne diese Funktion gehören nicht in die Sammlung (R14).

## Regeln pro Achse

| Nr. | Situation | Wert |
|---|---|---|
| R7 | Projekt über Wochen, aber nur in festen Unterrichtsstunden | Zeit 3 |
| – | Gemeinsame Vorarbeit, Schreibkonferenz, Überarbeitung in getrennten Phasen (PK-001) | Zeit 3 |
| R13 | Produkt entsteht zu Hause, Präsentation in der Schule | Ort 5 |
| – | Versuch oder Modellarbeit im Fachraum (QCAA-S9-QUAKE) | Ort 2 |
| – | Vorbereitung teils zu Hause, Vortrag vor der Klasse (QCAA-E7-SPEECH) | Ort 4 |
| R8 | Open Book ohne Angabe zu Internet oder KI | Hilfsmittel 3 |
| – | Open Media mit Vorbereitung zu Hause (ZUM-03); Debatte mit freier Vorbereitung (ISB15-DEBATTE) | Hilfsmittel 5 |
| R3 | Gruppenarbeit, Note rein individuell | Kooperation 3 |
| R4 | Gruppenprodukt plus individuelle Anteile | Kooperation 4 |
| R5 | Präsentation mit Folien | Produkt 2 |
| R6 | Plakat oder Lapbook, auch ohne Audio oder Video | Produkt 3 |
| – | Bild-Text-Beitrag mit gleichwertigen Ebenen (NZQA-91103) | Produkt 3 |
| R2 | Arbeit im Unterricht, Lehrkraft im Raum, keine Prüfungsaufsicht | Aufsicht 3 |
| R12 | Reine mündliche Prüfung, Prüfende anwesend | Aufsicht 1 |
| R11 | Reflexion verlangt, aber nicht in der Note gewichtet | zählt nicht für Bewertung (höchstens 3) |
| R9 | Rückmeldebogen nach der Prüfung, ohne Überarbeitung | Feedback 1 |
| R10 | Selbstreflexion ohne Rückmeldung anderer | zählt nicht für Feedback, nur für Bewertung |

R12 gilt nicht, wenn eine mündliche Verteidigung nur den Abschluss eines längeren Projekts bildet. Dann gelten die Werte der Projektphase.

## Ankerbeispiele (bestätigt)

Die Ankerbeispiele sind nach Achse sortiert. Jeder Wert ist in Timm Wiegmanns Anker-Check vom 20.11.2026 bestätigt oder korrigiert worden.

- **Zeit:** PK-008 = 1 · PK-001 = 3 · TCMA-RENOV = 3
- **Ort:** QCAA-S9-QUAKE = 2 · KMS-03 = 3 · QCAA-E7-SPEECH = 4
- **Hilfsmittel:** TCMA-QUADR = 1 · REK-17-23 = 5 · ZUM-03 = 5 · ISB15-DEBATTE = 5
- **Kooperation:** CH-WAH-KONSUM = 1 · ZUM-04 = 2 · TC-MAERCHEN = 5
- **Produkt:** ISB-13-48 = 1 · PK-021 = 2 · NZQA-91103 = 3 · C3-PROGRESS = 3 · BP25-BUCH = 4 · TC-10 = 4 · REK-15-14 = 5
- **Aufsicht:** CH-DE-DURCHSAGE = 2 · REK-17-4 = 3 · PK-014 = 4 · PK-021 = 5 · PK-SIEGERT-TRIGO = 5
- **Bewertung:** TC-ESP-BARRIO = 1 · ISB14-FOTO = 2 · TC-05 = 4 · BC-M6-INTERVIEW = 5
- **Feedback:** NSW-RUST = 1 · TCMA-QUADR = 1 (nach R9) · ISB14-HOERSPIEL = 3 · REK-EXT1-6 = 5

## Aus der Beschreibung nicht entscheidbar

Bei diesen Einträgen hat Timm „?“ gewählt. Sie müssen anhand der Quelle neu bewertet werden:

- BP25-WINKEL (Zeit)
- BP25-ROUTINE (Ort)
- BP25-RADIO (Ort)
- CH-DE-COMIC (Hilfsmittel)
- TC-TAGESSCHAU (Kooperation)
- KMS-07 (Kooperation)
- OSE-TAJ (Aufsicht)
- ISB15-TOURISMUS (Bewertung)
- REK-BOOKTOK (Feedback; nach R10 voraussichtlich niedriger)

Zu IB-EE (Zeit) gibt es keine Antwort.

## Rolle der KI (Feld `ki_setzung`)

Kategorien nach Joscha Falck („KI-Didaktik: Wie wird KI zur Lernressource statt zur Abkürzung?“, Deutsches Schulportal, 2026). Mehrfachnennung ist möglich.

| Wert | Bedeutung |
|---|---|
| `begrenzt` | begründet begrenzt: KI bewusst ausgeschlossen oder eingeschränkt, damit eine Kompetenz sichtbar wird |
| `integriert` | KI als Tutor oder Sparringspartner, an Lernziele gebunden. Nicht: KI als „Taschenrechner“, der die Antwort liefert |
| `reflektiert` | reflektiert / thematisiert: KI-Einsatz und -Ergebnisse werden geprüft, oder KI ist selbst Thema |
| `offen` | KI erlaubt, die Quelle legt keine Rolle fest |
| leere Liste | ohne Angabe: Die Quelle regelt KI nicht. Das ist kein Verbot |

Regeln:
- `integriert` nur, wenn die Quelle eine lernförderliche Rolle beschreibt; bloße Erlaubnis = `offen`.
- Hilfsmittel-Stufe 1 (keine Hilfsmittel) → `begrenzt`, Status „eingeschätzt“.
- „KI nicht geregelt“ bleibt ohne Angabe, auch bei offenen Hilfsmitteln.
- `ki_setzung_status`: explizit oder eingeschätzt; bei leerer Liste „nicht gesetzt“.

## Felder für spätere automatische Ergänzung

- `erfasst_am` (JJJJ-MM-TT): wann der Eintrag in die Sammlung kam. Für den Bestand aus der Git-Historie nachgetragen (frühestes Datum = Start des Repos).
- `pruefstatus`: „geprüft“ oder „automatisch ergänzt, Sichtung offen“. Die Oberfläche markiert ungeprüfte Einträge mit „neu, Sichtung offen“.
- `data/aenderungslog.json`: ein Eintrag pro Lauf (Datum, manuell/agent, Anzahl neu, Fächer). Das Importskript schreibt ihn bei `--schreiben` mit; `--agent` setzt den Prüfstatus auf „Sichtung offen“.
