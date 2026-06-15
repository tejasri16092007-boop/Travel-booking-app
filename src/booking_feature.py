import pandas as pd

"""
Day 8: Core Feature 1 - Destination Search & Total Cost Calculator
This feature checks destination details, filters by real-time availability,
and estimates total booking price while handling wrong inputs robustly.
"""

def calculate_trip_cost(destination_name, days):
    # Task 3: Handle Edge Cases (Empty input or wrong type)
    if not destination_name or str(destination_name).strip() == "":
        return "Error: Destination name cannot be empty."
    
    if not isinstance(destination_name, str):
        return "Error: Destination name must be a valid text string."
        
    try:
        days = int(days)
    except (ValueError, TypeError):
        return "Error: Number of days must be a valid number/integer."
        
    if days <= 0:
        return "Error: Number of days must be greater than 0."

    # Load cleaned dataset
    try:
        df = pd.read_csv('Data/processed/cleaned_destinations.csv')
    except FileNotFoundError:
        return "Error: Cleaned dataset not found."

    # Search for matching destination
    match = df[df['destination'].str.lower() == destination_name.strip().lower()]
    
    if match.empty:
        return f"Result: '{destination_name}' is not found in our catalog."
        
    price = match['price_per_day'].values[0]
    status = match['availability'].values[0]
    
    if status.lower() == 'housefull':
        return f"Result: Sorry, booking full for '{destination_name}'!"
        
    # Calculate final price
    total_cost = price * days
    return f"Result: Success! Total cost for {days} days in {destination_name} is {total_cost} INR."

# Task 2: Test manually with 5 different inputs
print("--- RUNNING DAY 8 MANUAL TESTS ---")
print("Test 1 (Valid Input):", calculate_trip_cost("Ooty", 3))
print("Test 2 (Housefull Edge Case):", calculate_trip_cost("Kodaikanal", 2))
print("Test 3 (Not Found Case):", calculate_trip_cost("Mumbai", 4))
print("Test 4 (Empty Name Edge Case):", calculate_trip_cost("", 5))
print("Test 5 (Wrong Type Edge Case):", calculate_trip_cost("Goa", "abc"))
