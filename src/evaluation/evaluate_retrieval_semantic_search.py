import json
import sys
import os
import io
from pathlib import Path
from collections import defaultdict
from pinecone import Pinecone
from dotenv import load_dotenv
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from src.retrieval import  retrieve

load_dotenv()

BASE_DIR = Path(__file__).parent.parent

TOP_K     = 5

def evaluate(eval_path: Path, top_k: int = TOP_K):
    eval_set = json.loads(eval_path.read_text(encoding="utf-8"))

    total        = len(eval_set)
    hits         = 0
    rr_list      = []
    failures     = []

    cat_hits     = defaultdict(int)
    cat_total    = defaultdict(int)
    cat_rr       = defaultdict(list)

    print(f"Evaluating {total} queries with top_k={top_k}...\n")

    for item in eval_set:
        qid      = item["id"]
        query    = item["query"]
        exp_file = item["expected_source_file"]
        exp_type = item["expected_chunk_type"]
        category = item["category"]

        matches = retrieve(query, top_k)
        cat_total[category] += 1

        rank = None
        for i, match in enumerate(matches, 1):
            meta = match.get("metadata", {})
            if (meta.get("source_file") == exp_file and
                meta.get("chunk_type")  == exp_type):
                rank = i
                break

        if rank:
            hits += 1
            rr_list.append(1 / rank)
            cat_hits[category] += 1
            cat_rr[category].append(1 / rank)
        else:
            rr_list.append(0)
            cat_rr[category].append(0)
            failures.append({
                "id"      : qid,
                "query"   : query,
                "expected": f"{exp_file} [{exp_type}]",
                "got"     : [
                    f"{m['metadata'].get('source_file','?')} [{m['metadata'].get('chunk_type','?')}] score={m['score']:.3f}"
                    for m in matches[:3]
                ]
            })

        status = f"HIT rank {rank}" if rank else "MISS"
        print(f"  [{qid:3}] {status:10} | {query[:60]}")

    hit_rate = hits / total
    mrr      = sum(rr_list) / total

    print(f"\n{'='*60}")
    print(f"HASIL EVALUASI RETRIEVAL")
    print(f"{'='*60}")
    print(f"Total queries : {total}")
    print(f"Hit Rate @{top_k}  : {hit_rate:.2%}")
    print(f"MRR           : {mrr:.3f}")


    print(f"\n{'-'*60}")
    print(f"{'Kategori':<35} {'Hit Rate':>10} {'MRR':>8} {'N':>5}")
    print(f"{'-'*60}")
    for cat in sorted(cat_total.keys()):
        n        = cat_total[cat]
        h        = cat_hits[cat]
        cat_mrr  = sum(cat_rr[cat]) / n if n else 0
        print(f"  {cat:<33} {h/n:>9.1%} {cat_mrr:>8.3f} {n:>5}")

    if failures:
        print(f"\n{'-'*60}")
        print(f"MISS ({len(failures)} queries):")
        print(f"{'-'*60}")
        for f in failures:
            print(f"\n  [{f['id']}] {f['query']}")
            print(f"       Expected : {f['expected']}")
            print(f"       Top-3 got:")
            for g in f["got"]:
                print(f"         - {g}")

    result = {
        "top_k"    : top_k,
        "total"    : total,
        "hits"     : hits,
        "hit_rate" : round(hit_rate, 4),
        "mrr"      : round(mrr, 4),
        "per_category": {
            cat: {
                "hit_rate": round(cat_hits[cat] / cat_total[cat], 4),
                "mrr"     : round(sum(cat_rr[cat]) / cat_total[cat], 4),
                "n"       : cat_total[cat]
            }
            for cat in sorted(cat_total.keys())
        },
        "failures" : failures
    }

    out_path = BASE_DIR / "data" / "evaluation_result.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(f"\nHasil disimpan ke: {out_path}")

    return result

if __name__ == "__main__":
    eval_path = Path(sys.argv[1]) if len(sys.argv) > 1 else BASE_DIR / "data" / "evaluation_set.json"
    top_k     = int(sys.argv[2]) if len(sys.argv) > 2 else TOP_K
    evaluate(eval_path, top_k=top_k)