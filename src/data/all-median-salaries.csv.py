import json
import os
import polars as pl
import sys

EXCLUDED_AGENCY_IDS = [
        "A35",
        "N/A",
        "SCS"
        ]

with open("src/data/agency_map.json", "r") as json_file:
    agency_map = json.load(json_file)
raw_salaries = (
        pl.read_csv("src/data/salaries-fy24.csv")
        .with_columns(pl.col("AgencyName").str.strip_chars()
        .replace_strict(agency_map, default=pl.col("AgencyName")).alias("MappedAgencyName"))
        )

grouped_median_salaries = (
        raw_salaries
        .filter(
            ~pl.col("AgencyID").is_in(EXCLUDED_AGENCY_IDS),
            pl.col("AnnualSalary") >= 200)
        .group_by("MappedAgencyName")
        .agg(pl.col("AnnualSalary").median().round(2))
        .sort("AnnualSalary")
        )
grouped_median_salaries.write_csv(sys.stdout)
