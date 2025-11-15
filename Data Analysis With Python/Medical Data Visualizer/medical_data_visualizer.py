# health_charts.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
data = pd.read_csv("medical_examination.csv")

# Calculate BMI and define overweight
data["overweight"] = ((data["weight"] / ((data["height"]/100) ** 2)) > 25).astype(int)

# Re-code cholesterol and glucose: 1 → good, >1 → bad
data["cholesterol"] = (data["cholesterol"] > 1).astype(int)
data["gluc"] = (data["gluc"] > 1).astype(int)


def make_categorical_plot():
    # Reshape relevant variables for counting
    melted = pd.melt(
        data,
        id_vars="cardio",
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"]
    )

    # Count occurrences
    summary = (
        melted.groupby(["cardio", "variable", "value"])
              .size()
              .reset_index(name="count")
    )

    # Build the seaborn bar chart
    chart = sns.catplot(
        data=summary,
        x="variable",
        y="count",
        hue="value",
        col="cardio",
        kind="bar"
    ).fig

    return chart


def make_heatmap():
    # Apply cleaning rules
    cleaned = data[
        (data["ap_lo"] <= data["ap_hi"]) &
        (data["height"].between(data["height"].quantile(0.025),
                                data["height"].quantile(0.975))) &
        (data["weight"].between(data["weight"].quantile(0.025),
                                data["weight"].quantile(0.975)))
    ]

    # Correlation matrix
    matrix = cleaned.corr()

    # Mask top triangle
    upper_mask = np.triu(np.ones_like(matrix, dtype=bool))

    # Create figure
    fig, ax = plt.subplots(figsize=(12, 10))

    sns.heatmap(
        matrix,
        mask=upper_mask,
        annot=True,
        fmt=".1f",
        square=True,
        linewidths=0.5,
        center=0,
        cbar_kws={"shrink": 0.5}
    )

    return fig
