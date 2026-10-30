"""A small end-to-end analysis you can run from the terminal.

Run it with:
    uv run python scripts/example_analysis.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import polars as pl

DATA = Path("data/example/sales.csv")
OUTPUTS = Path("outputs")


def main() -> None:
    sales = pl.read_csv(DATA, try_parse_dates=True)

    monthly = (
        sales.group_by(pl.col("date").dt.truncate("1mo").alias("month"), "region")
        .agg(pl.col("revenue").sum())
        .sort("month")
    )
    print(monthly.head(8))

    fig, ax = plt.subplots(figsize=(9, 5))
    for region in sorted(monthly["region"].unique()):
        subset = monthly.filter(pl.col("region") == region)
        ax.plot(subset["month"], subset["revenue"], marker="o", label=region)
    ax.set_title("Monthly revenue by region")
    ax.set_ylabel("Revenue (£)")
    ax.legend()
    fig.tight_layout()

    OUTPUTS.mkdir(exist_ok=True)
    out = OUTPUTS / "monthly_revenue.png"
    fig.savefig(out, dpi=150)
    print(f"Chart saved to {out}")


if __name__ == "__main__":
    main()
