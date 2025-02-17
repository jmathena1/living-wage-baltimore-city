import polars as pl
import sys

from pathlib import Path

def main():
    raw_salaries = pl.read_csv(Path(__file__).parent.parent.parent / "external_data/salaries-fy24.csv")
    grouped_median_salaries = raw_salaries.group_by(
            (pl.col("AgencyName"))
    ).agg(
        pl.col("AnnualSalary").median().round(2)
    )
    grouped_median_salaries.write_csv(sys.stdout)

if __name__ == "__main__":
    main()
