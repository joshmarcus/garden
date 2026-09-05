#!/usr/bin/env python3
"""Append one record of the operator session's spend to context-garden/docs/operator-spend.jsonl.

Reads the Claude Code transcript(s) under ~/.claude/projects/<project>/ and sums usage per
session; prices are list prices per million tokens (input, output, cache read, cache write).
Usage: operator_spend.py [--session <id>] [--project <dir>] [--since ISO] [--until ISO] [--dry-run]
(defaults: newest session, whole session, append a record)."""
import argparse, glob, json, os, time
PRICES = {  # $/MTok: input, output, cache_read, cache_write (list prices, 2026-06)
    "claude-fable-5-1": (10.0, 50.0, 0.25, 12.5), "claude-fable-5": (10.0, 50.0, 0.25, 12.5),
    "claude-opus-5": (5.0, 25.0, 0.5, 6.25), "claude-opus-4-8": (5.0, 25.0, 0.5, 6.25),
    "claude-sonnet-5": (2.0, 10.0, 0.2, 2.5), "claude-haiku-4-5": (1.0, 5.0, 0.1, 1.25),
}
ap = argparse.ArgumentParser(); ap.add_argument("--session"); ap.add_argument("--project", default=os.path.expanduser("~/.claude/projects/-home-joshua-context-garden"))
ap.add_argument("--since"); ap.add_argument("--until"); ap.add_argument("--dry-run", action="store_true", help="print, do not append")
ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "context-garden/docs/operator-spend.jsonl"))
a = ap.parse_args()
files = sorted(glob.glob(os.path.join(a.project, "*.jsonl")), key=os.path.getmtime)
if a.session: files = [f for f in files if a.session in f]
if not files: raise SystemExit("no transcript found")
path = files[-1]; sid = os.path.basename(path).split(".")[0]
tot = {"input": 0, "output": 0, "cache_read": 0, "cache_write": 0}; turns = 0; cost = 0.0; models = {}; first = last = None
with open(path) as fh:
    for line in fh:
        try: e = json.loads(line)
        except Exception: continue
        m = e.get("message") if isinstance(e.get("message"), dict) else None
        if not m or m.get("role") != "assistant" or not m.get("usage"): continue
        ts0 = e.get("timestamp") or ""
        if (a.since and ts0 < a.since) or (a.until and ts0 > a.until): continue
        u = m["usage"]; model = m.get("model", "?"); turns += 1; models[model] = models.get(model, 0) + 1
        i, o, cr, cw = u.get("input_tokens", 0) or 0, u.get("output_tokens", 0) or 0, u.get("cache_read_input_tokens", 0) or 0, u.get("cache_creation_input_tokens", 0) or 0
        tot["input"] += i; tot["output"] += o; tot["cache_read"] += cr; tot["cache_write"] += cw
        pi, po, pr, pw = PRICES.get(model, PRICES["claude-fable-5-1"])
        cost += (i * pi + o * po + cr * pr + cw * pw) / 1e6
        ts = e.get("timestamp"); first = first or ts; last = ts or last
rec = {"since": a.since, "until": a.until, "at": time.strftime("%Y-%m-%dT%H:%M:%S+00:00", time.gmtime()), "session": sid, "first_turn": first, "last_turn": last, "turns": turns, "models": models, "tokens": tot, "list_price_usd": round(cost, 2), "avg_context": int(tot["cache_read"] / max(1, turns))}
if not a.dry_run:
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    with open(a.out, "a") as fh: fh.write(json.dumps(rec) + "\n")
print(f"{rec['at']} session {sid[:8]} turns {turns} avg context {rec['avg_context']:,} list ${cost:,.2f}")
