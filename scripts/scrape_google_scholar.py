# Prof scholar id lBWMbC8AAAAJ
from scholarly import scholarly, ProxyGenerator
import json
import os
import sys
import time
import random
from datetime import date

def enable_proxies():
    pg = ProxyGenerator()
    ok = pg.FreeProxies()
    if ok:
        scholarly.use_proxy(pg)
    else:
        print("[warn] Could not enable FreeProxies(); continuing without proxies.")

def pub_to_record(pub):
    bib = pub.get("bib", {}) or {}
    return {
        "title": bib.get("title"),
        "authors": bib.get("author") or bib.get("authors"),
        "venue": bib.get("venue") or bib.get("journal"),
        "year": bib.get("pub_year") or bib.get("year"),
        "cited_by": pub.get("num_citations", 0),
        "url": pub.get("pub_url"),
    }

def scrape(user_id, limit=50, delay=2.0, jitter=1.5):
    enable_proxies()

    author = scholarly.search_author_id(user_id)
    author = scholarly.fill(author, sections=["basics", "publications"])

    pubs_out = []
    pubs = author.get("publications", [])[:limit]

    for i, pub in enumerate(pubs, start=1):
        # polite pacing to reduce blocks
        time.sleep(delay + random.random() * jitter)

        # start with what we already have (works even if fill fails)
        record = pub_to_record(pub)

        try:
            filled = scholarly.fill(pub)
            record = pub_to_record(filled)
        except Exception as e:
            print(f"[warn] pub {i}/{len(pubs)} fill failed; using basic data. ({type(e).__name__}: {e})")

        # remove empty keys for cleaner JSON
        record = {k: v for k, v in record.items() if v not in (None, "", [])}
        pubs_out.append(record)

    return {
        "name": author.get("name"),
        "profile_url": f"https://scholar.google.com/citations?user={user_id}&hl=en",
        "updated": str(date.today()),
        "publications": pubs_out
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: python scrape_google_scholar.py USER_ID [LIMIT]")
        sys.exit(1)

    user_id = sys.argv[1]
    limit = int(sys.argv[2]) if len(sys.argv) >= 3 else 50

    data = scrape(user_id, limit=limit)

    os.makedirs("static/scholar", exist_ok=True)
    out_path = f"static/scholar/{user_id}.json"

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Saved {len(data['publications'])} publications → {out_path}")

if __name__ == "__main__":
    main()