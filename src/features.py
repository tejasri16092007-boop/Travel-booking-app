import pandas as pd
from sklearn.model_selection import train_test_split

# Load the cleaned dataset from Day 4
df = pd.read_csv('Data/processed/cleaned_destinations.csv')

# Task 1: Create 2 new derived features
df['price_per_rating'] = df['price_per_day'] / df['rating']
df['is_budget_friendly'] = (df['price_per_day'] <= 3000).astype(int)

# Task 2: Encode categorical variables (Label Encoding)
df['availability_encoded'] = df['availability'].map({'Available': 1, 'Housefull': 0})

# Task 3: Scale numerical features (Min-Max Scaling for price)
df['scaled_price'] = (df['price_per_day'] - df['price_per_day'].min()) / (df['price_per_day'].max() - df['price_per_day'].min())

# Task 4: Split data into train/test sets (80/20 split)
train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

print("Feature Engineering completed successfully!")
