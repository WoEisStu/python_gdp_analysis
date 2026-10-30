"""Generate the example sales dataset in data/example/sales.csv."""

from pathlib import Path

import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
n = 500

dates = pd.date_range("2025-01-01", "2025-12-31", freq="D")
regions = ["North", "South", "East", "West"]
products = ["Widget", "Gadget", "Doohickey"]
prices = {"Widget": 12.5, "Gadget": 30.0, "Doohickey": 7.25}

df = pd.DataFrame(
    {
        "date": rng.choice(dates, n),
        "region": rng.choice(regions, n),
        "product": rng.choice(products, n),
        "units": rng.integers(1, 50, n),
    }
)
df["unit_price"] = df["product"].map(prices)
df["revenue"] = (df["units"] * df["unit_price"]).round(2)
df = df.sort_values("date").reset_index(drop=True)

out = Path("data/example/sales.csv")
out.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(out, index=False, date_format="%Y-%m-%d", encoding="utf-8")
print(f"Wrote {len(df)} rows to {out}")
