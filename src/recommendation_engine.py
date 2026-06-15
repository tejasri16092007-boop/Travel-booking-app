import pandas as pd

"""
Day 15: Advanced Feature 1 - Smart Destination Recommendation Engine
This advanced feature analyzes the cleaned dataset to recommend optimal travel 
destinations based on the user's maximum budget constraints and trip duration.
"""

def recommend_destinations(max_budget, days):
    # Task 3: Start simple - get the basic version working first with validation
    try:
        max_budget = float(max_budget)
        days = int(days)
    except (ValueError, TypeError):
        return "Error: Budget and Days must be valid numbers."

    if max_budget <= 0 or days <= 0:
        return "Error: Budget and Days must be greater than zero."

    # Load dataset safely
    try:
        df = pd.read_csv('Data/processed/cleaned_destinations.csv')
    except FileNotFoundError:
        return "Error: Preprocessed dataset file not found."

    # Advanced Logic: Calculate estimated total cost for each destination dynamically
    df['estimated_total_cost'] = df['price_per_day'] * days
    
    # Filter destinations within budget and that are available (not housefull)
    available_options = df[
        (df['estimated_total_cost'] <= max_budget) & 
        (df['availability'].str.lower() != 'housefull')
    ].copy()

    if available_options.empty:
        return f"Result: Sorry, no destinations found matching your budget of {max_budget} INR for {days} days."

    # Task 4: Sort by a smart Value Score (lower cost options get optimized priority)
    available_options['value_score'] = 10000 / available_options['estimated_total_cost']
    recommendations = available_options.sort_values(by='value_score', ascending=False)

    # Format output layout
    output = f"=== TOP RECOMMENDED DESTINATIONS FOR YOU (Budget: {max_budget} INR) ===\n"
    for idx, row in recommendations.iterrows():
        output += f"- {row['destination'].title()}: Total Cost = {row['estimated_total_cost']:.2f} INR (Price/Day: {row['price_per_day']} INR, Status: {row['availability']})\n"
    
    return output

# Task 4: Test it thoroughly before adding complexity
print("--- RUNNING DAY 15 ADVANCED FEATURE TESTS ---")
print(recommend_destinations(15000, 3))
print("\nTesting Edge Case (Low Budget):")
print(recommend_destinations(1000, 5))
