# Intelligence Product Factory

The product factory renders multiple analyst views from the same source objects.

Supported initial products:
- Campaign Brief;
- Watch & Warning Note;
- Detection Coverage Assessment;
- Collection Gap Report.

Run:

```bash
python tools/build_products.py --out products/generated
```

Every generated product contains:
- TLP marking;
- as-of date;
- linked PIR;
- source/evidence references where available;
- key judgments;
- explicit uncertainty.

The goal is one knowledge graph, many products — not separate Word documents slowly disagreeing with each other.
