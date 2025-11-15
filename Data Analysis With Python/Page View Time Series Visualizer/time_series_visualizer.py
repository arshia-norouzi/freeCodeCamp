# views_visualizer.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and filter data
data = pd.read_csv(
    "fcc-forum-pageviews.csv",
    parse_dates=["date"],
    index_col="date"
)

# Remove extreme outliers
lower, upper = data["value"].quantile([0.025, 0.975])
data = data[(data["value"] >= lower) & (data["value"] <= upper)]


# ----------------------------------------------------------
# Line Plot
# ----------------------------------------------------------
def draw_line_plot():
    frame = data.copy()

    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(frame.index, frame["value"], linewidth=1, color="red")

    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016–12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    fig.savefig("line_plot.png")
    return fig


# ----------------------------------------------------------
# Bar Plot
# ----------------------------------------------------------
def draw_bar_plot():
    frame = data.copy()

    frame["Year"] = frame.index.year
    frame["Month"] = frame.index.month_name()

    table = (
        frame.groupby(["Year", "Month"])["value"]
        .mean()
        .unstack()
    )

    fig = table.plot(kind="bar", figsize=(12, 8)).figure

    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months")

    fig.savefig("bar_plot.png")
    return fig


# ----------------------------------------------------------
# Box Plots
# ----------------------------------------------------------
def draw_box_plot():
    frame = data.reset_index()

    frame["Year"] = frame["date"].dt.year
    frame["Month"] = frame["date"].dt.strftime("%b")
    frame["MonthNum"] = frame["date"].dt.month

    frame = frame.sort_values("MonthNum")

    fig, axes = plt.subplots(1, 2, figsize=(18, 6))

    # Year-wise Trend
    sns.boxplot(
        x="Year",
        y="value",
        data=frame,
        ax=axes[0]
    )
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Month-wise Seasonality
    sns.boxplot(
        x="Month",
        y="value",
        data=frame,
        ax=axes[1]
    )
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    fig.savefig("box_plot.png")
    return fig
