# sea_level_visualizer.py

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Load dataset
    data = pd.read_csv("epa-sea-level.csv")

    # Base scatter
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(data["Year"], data["CSIRO Adjusted Sea Level"], s=15, alpha=0.8)

    # Fit line for entire history
    full_fit = linregress(data["Year"], data["CSIRO Adjusted Sea Level"])
    years_full = list(range(1880, 2051))
    sea_full = [full_fit.intercept + full_fit.slope * yr for yr in years_full]
    ax.plot(years_full, sea_full, color="red", label="Full Trend (1880–present)")

    # Fit line only from year 2000 forward
    recent = data[data["Year"] >= 2000]
    rec_fit = linregress(recent["Year"], recent["CSIRO Adjusted Sea Level"])
    years_recent = list(range(2000, 2051))
    sea_recent = [rec_fit.intercept + rec_fit.slope * yr for yr in years_recent]
    ax.plot(years_recent, sea_recent, color="green", label="Recent Trend (2000–present)")

    # Titles and labels
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.legend()

    # Save & return
    fig.savefig("sea_level_plot.png")
    return ax
