# run_analysis.py
import pandas as pd
from demographic_data_analyzer import calculate_demographic_data as analyze_data

# Load dataset
dataset = pd.read_csv("adult.data.csv")

# Perform analysis
analysis_output = analyze_data(dataset)

# Display results
print(analysis_output)
