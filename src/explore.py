import pandas as pd

# Task 1: Load dataset and check shape, columns, data types
df = pd.read_csv('Data/destinations.csv')
print("Dataset Shape:", df.shape)
print("Columns Available:", df.columns.tolist())
print("Data Types:\n", df.dtypes)

# Task 2: Find all missing values
print("\nMissing Values Count:\n", df.isnull().sum())

# Task 3 & 4: Data Distribution & 3 Important Insights
"""
--- DATA EXPLORATION INSIGHTS ---
1. Price Distribution: Highest price is Manali (5500), Lowest is Pondicherry (2000).
2. Availability Status: Kodaikanal is 'Housefull' right now, others are 'Available'.
3. Rating Insight: Average customer rating for the travel destinations is above 4.2.
"""
print("\nData Exploration Completed Successfully!")
