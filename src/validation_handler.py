import pandas as pd
from receipt_feature import generate_final_receipt

"""
Day 11: Error Handling & Validation
This script implements comprehensive validation gateways and try/except layers 
to gracefully catch bad inputs, empty lines, and type issues without breaking the app.
"""

def secure_booking_gateway(destination_name, days, promo_code=None, is_premium_member=False):
    # Task 1 & 4: Input validation with clear, helpful user messages
    if destination_name is None or not isinstance(destination_name, str) or destination_name.strip() == "":
        return "Validation Error: Destination must be a valid, non-empty text string (e.g., 'Ooty')."
        
    if days is None:
        return "Validation Error: Number of days cannot be empty or None."
        
    # Task 2: Try/catch handling around risky type conversions
    try:
        days_checked = int(days)
    except (ValueError, TypeError):
        return f"Type Error: Expected a numerical number for days, but received '{days}' of type {type(days).__name__}."
        
    if days_checked <= 0:
        return f"Value Error: Number of days must be 1 or more. You provided: {days_checked}."

    if promo_code is not None and not isinstance(promo_code, str):
        return "Validation Error: Promo code must be a valid text layout."

    if not isinstance(is_premium_member, bool):
        return "Validation Error: Premium membership status must be either True or False."

    # Task 2: Try/except block wrapping execution pipeline
    try:
        receipt_output = generate_final_receipt(destination_name, days_checked, promo_code, is_premium_member)
        return receipt_output
    except FileNotFoundError:
        return "System Error: The core destinations CSV file could not be found. Please check paths."
    except Exception as e:
        return f"Unexpected Error: Processing failed due to: {str(e)}"

# Task 3: Comprehensive testing with invalid inputs, empty strings, and edge cases
print("--- RUNNING DAY 11 ERROR HANDLING & VALIDATION TESTS ---")

print("\n[TEST 1] Testing with Invalid Type for Days:")
print(secure_booking_gateway("Ooty", "three_days"))

print("\n[TEST 2] Testing with Empty Space Strings:")
print(secure_booking_gateway("   ", 5))

print("\n[TEST 3] Testing with Negative Days Value:")
print(secure_booking_gateway("Goa", -4))

print("\n[TEST 4] Testing with Wrong Destination Datatype:")
print(secure_booking_gateway(98765, 3))
