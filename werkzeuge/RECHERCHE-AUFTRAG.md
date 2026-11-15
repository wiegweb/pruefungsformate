# Regelmäßiger Rechercheauftrag (Entwurf)

Dieser Text ist als Auftrag für eine geplante, regelmäßige Claude-Aufgabe gedacht (z. B. monatlich). Er läuft jedes Mal in einer frischen Sitzung und braucht deshalb alle Angaben selbst.

---

**Auftrag**

Du pflegst die Sammlung zukunftsorientierter Prüfungsformate im GitHub-Repository `wiegweb/pruefungsformate` (Datei `data/pruefungen.json`, Web-App unter https://wiegweb.github.io/pruefungsformate/).

1. **Repository holen:** `wiegweb/pruefungsformate` klonen. Lies `data/pruefungen.json`, damit du weißt, was schon enthalten ist.
2. **Recherchieren:** Suche nach konkreten, dokumentierten alternativen Prüfungen und Leistungsnachweisen aus Schulen (DE, AT, CH und international). Bevorzuge Funde, die **seit dem letzten Lauf** veröffentlicht wurden. Quellen: Landesinstitute (QUA-LiS NRW, ISB Bayern, ZSL, LISUM, NLQ …), IQES, Institut für zeitgemäße Prüfungskultur, Lehrkräfte-Blogs, öffentlich sichtbare LinkedIn-Beiträge, öffentliche TaskCards- und Padlet-Pinnwände, internationale Quellen (AI Assessment Scale, Jisc, NZQA …). Achte auf Fächer, die in der Sammlung noch selten sind (Sport, Musik, Naturwissenschaften, Informatik), und auf Beispiele mit KI-Bezug.
3. **Nur Konkretes aufnehmen:** Es muss eine tatsächlich durchgeführte oder ausgearbeitete Prüfung mit Aufgabe oder Ablauf beschrieben sein. Keine allgemeinen Plädoyers, keine Methodenlisten. Jeder Link muss von dir aufgerufen worden sein. Erfinde nichts. Fehlt eine Angabe, trage `null` ein.
4. **Einordnen:** Gleiches Feldschema wie in `data/pruefungen.json`. Achsen 1–9 jeweils 1–5 nach den Stufen in `index.html` (`CONFIG.achsen`), mit Belegstatus „explizit“ oder „eingeschätzt“. `ki_rolle` 0–4. Schreibe die Funde in `neue_funde.json` (JSON-Array).
5. **Einpflegen:** `python3 werkzeuge/daten_einpflegen.py neue_funde.json` ausführen, Bericht lesen, offensichtliche Fehler in `neue_funde.json` korrigieren, dann mit `--schreiben` einpflegen.
6. **Zur Freigabe vorlegen, nicht direkt veröffentlichen:** Neuen Branch `recherche-JJJJ-MM` anlegen, nur `data/pruefungen.json` committen und einen Pull Request öffnen. In die Beschreibung: Zahl der neuen Einträge, je Eintrag Titel + Link + eine Zeile Begründung, Dubletten und abgelehnte Funde, Fächer/Bereiche, die weiter fehlen. Nicht auf `main` pushen.
7. Findest du nichts Neues, das die Kriterien erfüllt, öffne keinen Pull Request und melde das kurz.
