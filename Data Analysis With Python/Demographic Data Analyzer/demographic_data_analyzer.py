# population_stats.py
import pandas as pd

def analyze(df):
    # --- Race distribution ---
    races = df["race"].value_counts()

    # --- Average age of males ---
    male_group = df[df["sex"] == "Male"]
    avg_age_male = round(male_group["age"].mean(), 1)

    # --- Bachelor's degree percentage ---
    total = df.shape[0]
    bachelors_only = df.loc[df["education"] == "Bachelors"]
    pct_bachelors = round((len(bachelors_only) / total) * 100, 1)

    # --- Income comparisons based on education level ---
    higher_ed_levels = ["Bachelors", "Masters", "Doctorate"]
    high_ed_mask = df["education"].isin(higher_ed_levels)
    low_ed_mask = ~high_ed_mask

    high_ed_rich = df.loc[high_ed_mask & (df["salary"] == ">50K")]
    low_ed_rich = df.loc[low_ed_mask & (df["salary"] == ">50K")]

    pct_high_ed_rich = round(len(high_ed_rich) / high_ed_mask.sum() * 100, 1)
    pct_low_ed_rich = round(len(low_ed_rich) / low_ed_mask.sum() * 100, 1)

    # --- Minimum working hours ---
    min_hours = df["hours-per-week"].min()

    # --- Rich percentage among minimum-hour workers ---
    min_workers = df[df["hours-per-week"] == min_hours]
    rich_min_workers = min_workers[min_workers["salary"] == ">50K"]
    pct_rich_min = round((len(rich_min_workers) / len(min_workers)) * 100, 1)

    # --- Countries by income rate ---
    country_total = df["native-country"].value_counts()
    country_rich = df[df["salary"] == ">50K"]["native-country"].value_counts()

    income_ratio = (country_rich / country_total) * 100
    top_country = income_ratio.idxmax()
    top_country_rate = round(income_ratio.max(), 1)

    # --- Most common job for wealthy people in India ---
    india_rich = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]
    popular_job_india = india_rich["occupation"].value_counts().idxmax()

    return {
        "race_count": races,
        "average_age_men": avg_age_male,
        "percentage_bachelors": pct_bachelors,
        "percentage_higher_education_rich": pct_high_ed_rich,
        "percentage_lower_education_rich": pct_low_ed_rich,
        "min_work_hours": min_hours,
        "rich_percentage": pct_rich_min,
        "highest_earning_country": top_country,
        "highest_earning_country_percentage": top_country_rate,
        "top_IN_occupation": popular_job_india,
    }
