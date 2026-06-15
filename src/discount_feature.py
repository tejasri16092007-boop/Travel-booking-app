from booking_feature import calculate_trip_cost

"""
Day 9: Core Feature 2 - Promo Code & Discount Application
This feature successfully connects with Day 8's trip cost calculator 
to apply promotional discounts based on code validity.
"""

def apply_promo_discount(destination_name, days, promo_code=None):
    # Task 2: Connect it to the first feature built yesterday
    base_result = calculate_trip_cost(destination_name, days)
    
    # If Feature 1 returned an error or booking full, pass it directly
    if "Success!" not in base_result:
        return base_result
        
    # Extract total cost value from Feature 1 output string
    try:
        base_cost = float(base_result.split("is ")[1].split(" INR")[0])
    except Exception:
        return f"Error connecting to feature 1 summary. {base_result}"

    # Core Feature 2 logic: Apply Discount
    discount_percentage = 0
    if promo_code:
        code = promo_code.strip().upper()
        if code == "TRAVEL20":
            discount_percentage = 0.20  # 20% Discount
        elif code == "BUDGET10":
            discount_percentage = 0.10  # 10% Discount
        else:
            return f"Result: Invalid Promo Code. Base price remains. {base_result}"
    
    final_cost = base_cost * (1 - discount_percentage)
    discount_amount = base_cost * discount_percentage
    
    return f"Result: Success! Code {promo_code} applied. Saved {discount_amount} INR. Final Integrated Cost: {final_cost} INR."

# Task 3: Test the combination - do they work together correctly?
print("--- RUNNING DAY 9 INTEGRATION TESTS ---")
print("Test 1 (Valid Trip + Valid Promo):", apply_promo_discount("Ooty", 3, "TRAVEL20"))
print("Test 2 (Valid Trip + Another Promo):", apply_promo_discount("Goa", 2, "BUDGET10"))
print("Test 3 (Valid Trip + Invalid Promo):", apply_promo_discount("Manali", 2, "DISCOUNTFREE"))
print("Test 4 (Invalid Trip Integration Test):", apply_promo_discount("Mumbai", 4, "TRAVEL20"))
