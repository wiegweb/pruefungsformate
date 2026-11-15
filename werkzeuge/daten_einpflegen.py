#!/usr/bin/env python3
"""Neue Prüfungsbeispiele prüfen und in data/pruefungen.json einpflegen.

Aufruf (im Repo-Ordner):
    python3 werkzeuge/daten_einpflegen.py neue_funde.json            # nur prüfen, nichts schreiben
    python3 werkzeuge/daten_einpflegen.py neue_funde.json --schreiben

neue_funde.json ist ein JSON-Array im selben Format wie data/pruefungen.json.

Das Skript
- prüft jeden neuen Eintrag (Pflichtfelder, Wertebereiche, Link-Form),
- erkennt Dubletten (gleicher Link oder gleicher Titel, auch leicht abweichend geschrieben),
- vergibt fehlende IDs,
- hängt nur gültige, neue Einträge an und schreibt einen Bericht.
Bestehende Einträge werden nie verändert oder gelöscht.
"""
import json, re, sys, unicodedata, datetime, pathlib

DATEI = pathlib.Path(__file__).resolve().parent.parent / "data" / "pruefungen.json"
ACHSEN = [f"achse{i}" for i in range(1, 10)]
PFLICHT = ["titel", "kurzbeschreibung", "link_primaer"]
MEDIEN = {"nicht nötig", "optional", "erforderlich"}


def norm(t):
    t = unicodedata.normalize("NFKD", str(t or "").lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", " ", t).strip()


def link_norm(u):
    u = str(u or "").strip().lower()
    u = re.sub(r"^https?://(www\.)?", "", u)
    return u.rstrip("/")


def pruefe(e):
    """Gibt (fehler, warnungen) für einen Eintrag zurück."""
    fehler, warn = [], []
    if not isinstance(e, dict):
        return ["kein JSON-Objekt"], []
    for f in PFLICHT:
        if not str(e.get(f) or "").strip():
            fehler.append(f"Pflichtfeld '{f}' fehlt")
    link = str(e.get("link_primaer") or "")
    if link and not re.match(r"^https?://\S+$", link):
        fehler.append("link_primaer ist kein http(s)-Link")
    for a in ACHSEN:
        v = e.get(a)
        if v is not None and not (isinstance(v, (int, float)) and 1 <= v <= 5):
            fehler.append(f"{a} muss 1–5 oder null sein (ist {v!r})")
    ki = e.get("ki_rolle")
    if ki is not None and ki not in (0, 1, 2, 3, 4):
        fehler.append(f"ki_rolle muss 0–4 sein (ist {ki!r})")
    dm = e.get("digitale_medien")
    if dm not in (None, "") and dm not in MEDIEN:
        warn.append(f"digitale_medien unbekannt: {dm!r}")
    for f in ("jg_von", "jg_bis"):
        v = e.get(f)
        if v is not None and not (isinstance(v, int) and 1 <= v <= 13):
            warn.append(f"{f} ungewöhnlich: {v!r}")
    bekannt = sum(1 for a in ACHSEN if e.get(a) is not None)
    if bekannt < 3:
        warn.append(f"nur {bekannt} von 9 Achsen eingeordnet")
    if str(e.get("link_status") or "") != "geprüft":
        warn.append(f"Link nicht als geprüft markiert ({e.get('link_status')!r})")
    return fehler, warn


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    schreiben = "--schreiben" in sys.argv
    if len(args) != 1:
        print(__doc__)
        sys.exit(2)
    alt = json.loads(DATEI.read_text(encoding="utf-8"))
    neu = json.loads(pathlib.Path(args[0]).read_text(encoding="utf-8"))
    if not isinstance(neu, list):
        sys.exit("Die neue Datei muss ein JSON-Array sein.")

    links = {link_norm(e.get("link_primaer")) for e in alt if e.get("link_primaer")}
    titel = {norm(e.get("titel")) for e in alt}
    ids = {str(e.get("id")) for e in alt}
    heute = datetime.date.today().strftime("%Y%m%d")

    aufgenommen, abgelehnt, dubletten = [], [], []
    for k, e in enumerate(neu, 1):
        fehler, warn = pruefe(e)
        name = (e.get("titel") if isinstance(e, dict) else None) or f"Eintrag {k}"
        if fehler:
            abgelehnt.append((name, fehler))
            continue
        if link_norm(e["link_primaer"]) in links or norm(e["titel"]) in titel:
            dubletten.append(name)
            continue
        if not str(e.get("id") or "").strip() or str(e["id"]) in ids:
            n = 1
            while f"NEU-{heute}-{n:03d}" in ids:
                n += 1
            e["id"] = f"NEU-{heute}-{n:03d}"
        ids.add(str(e["id"])); links.add(link_norm(e["link_primaer"])); titel.add(norm(e["titel"]))
        aufgenommen.append((e, warn))

    print(f"Bestand: {len(alt)} · geprüft: {len(neu)} · neu aufgenommen: {len(aufgenommen)} · "
          f"Dubletten: {len(dubletten)} · abgelehnt: {len(abgelehnt)}\n")
    for e, warn in aufgenommen:
        print(f"+ {e['id']}: {e['titel']}" + (f"\n    Hinweise: {'; '.join(warn)}" if warn else ""))
    for n in dubletten:
        print(f"= schon vorhanden: {n}")
    for n, f in abgelehnt:
        print(f"- abgelehnt: {n}\n    {'; '.join(f)}")

    if schreiben and aufgenommen:
        alt.extend(e for e, _ in aufgenommen)
        DATEI.write_text(json.dumps(alt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"\n{DATEI.name} geschrieben: jetzt {len(alt)} Einträge.")
    elif aufgenommen:
        print("\nNur geprüft. Mit --schreiben werden die neuen Einträge angehängt.")


if __name__ == "__main__":
    main()
