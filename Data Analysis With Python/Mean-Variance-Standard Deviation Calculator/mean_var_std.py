# analysis_tools.py
import numpy as np

def calculate(nums):
    if len(nums) != 9:
        raise ValueError("List must contain nine numbers.")

    m = np.asarray(nums).reshape(3, 3)

    # Compute column-wise and row-wise stats manually
    col_stats = {
        "mean": m.mean(0).tolist(),
        "variance": m.var(0).tolist(),
        "standard deviation": m.std(0).tolist(),
        "max": m.max(0).tolist(),
        "min": m.min(0).tolist(),
        "sum": m.sum(0).tolist(),
    }

    row_stats = {
        "mean": m.mean(1).tolist(),
        "variance": m.var(1).tolist(),
        "standard deviation": m.std(1).tolist(),
        "max": m.max(1).tolist(),
        "min": m.min(1).tolist(),
        "sum": m.sum(1).tolist(),
    }

    total_stats = {
        "mean": float(m.mean()),
        "variance": float(m.var()),
        "standard deviation": float(m.std()),
        "max": float(m.max()),
        "min": float(m.min()),
        "sum": float(m.sum()),
    }

    # Combine manually instead of building in one dict
    output = {}
    for key in ["mean", "variance", "standard deviation", "max", "min", "sum"]:
        output[key] = [
            col_stats[key],
            row_stats[key],
            total_stats[key]
        ]

    return output
