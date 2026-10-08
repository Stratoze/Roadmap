"""Read-only check of real Japanese stats: Anki (via AnkiConnect) and Jellyfin watch time.

Usage: python tools/check_progress.py [days]   (default 7)
Needs Anki desktop open with AnkiConnect. Never writes anything.
"""
import json
import sqlite3
import sys
import urllib.request
from pathlib import Path

DAYS = int(sys.argv[1]) if len(sys.argv) > 1 else 7
JELLYFIN_DB = Path(r"C:\ProgramData\Jellyfin\Server\data\playback_reporting.db")


def anki(action, **params):
    req = json.dumps({"action": action, "version": 6, "params": params}).encode()
    with urllib.request.urlopen("http://localhost:8765", req, timeout=10) as r:
        return json.load(r)["result"]


print("== Anki ==")
try:
    by_day = dict(anki("getNumCardsReviewedByDay"))
    print(f"due now: {len(anki('findCards', query='is:due'))}   "
          f"new today: {len(anki('findCards', query='introduced:1'))}")
    for day in sorted(by_day, reverse=True)[:DAYS]:
        print(f"  {day}  {by_day[day]:>4} reviews")
except OSError:
    print("  Anki not reachable (open Anki desktop and sync first)")

print("\n== Jellyfin watch time ==")
if not JELLYFIN_DB.exists():
    print("  no playback_reporting.db yet (restart Jellyfin, then watch something)")
else:
    db = sqlite3.connect(f"file:{JELLYFIN_DB}?mode=ro", uri=True)
    rows = db.execute(
        "SELECT date(DateCreated), SUM(PlayDuration) / 60, COUNT(*) FROM PlaybackActivity "
        "WHERE date(DateCreated) >= date('now', 'localtime', ?) "
        "GROUP BY 1 ORDER BY 1 DESC", (f"-{DAYS - 1} days",)).fetchall()
    for day, minutes, plays in rows:
        print(f"  {day}  {minutes:>4} min  ({plays} plays)")
    if not rows:
        print(f"  nothing logged in the last {DAYS} days")
