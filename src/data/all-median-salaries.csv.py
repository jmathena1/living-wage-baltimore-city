import os
import polars as pl
import sys

EXCLUDED_AGENCY_IDS = [
        "A35",
        "N/A",
        "SCS"
        ]

EXCLUDED_AGENCY_NAMES = [
        "O01_ELJ",
        "Environmental Control Board",
        "Municipal Zoning & Appeals",
        "N/A",
        "Mayor's Office of Employment Development",
        "Recreation & Parks - Administration",
        "Recreation & Parks - Recreation"
        "SCS - Special City Services",
        "Transportation - Crossing Guards"
        ]
raw_salaries = pl.read_csv("src/data/salaries-fy24.csv")
grouped_median_salaries = raw_salaries.filter(
                ~pl.col("AgencyID").is_in(EXCLUDED_AGENCY_IDS),
                pl.col("AnnualSalary") >= 200).group_by("AgencyName").agg(
                        pl.col("AnnualSalary").median().round(2)
                ).sort("AnnualSalary")
grouped_median_salaries.write_csv(sys.stdout)
