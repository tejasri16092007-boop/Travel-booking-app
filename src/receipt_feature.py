from discount_feature import apply_promo_discount

"""
Day 10: Core Feature 3 - Tax, Service Fee & Final Receipt Generator
This feature integrates Feature 1 and Feature 2 to calculate final government taxes,
handling premium memberships and rendering a clean end-to-end receipt.
"""

def generate_final_receipt(destination_name, days, promo_code=None, is_premium_member=False):
    # Task 4: Add print statements/logs for debugging
    print(f"[DEBUG LOG] Initiating booking pipeline for: {destination_name}")
    
    # Task 2: Test all features together by calling integrated Feature 2 function
    discounted_result = apply_promo_discount(destination_name, days, promo_code)
    
    if "Success!" not in discounted_result:
        print("[DEBUG LOG] Booking failed in preliminary verification stage.")
        return discounted_result
        
    # Extract the cost after discount safely
    try:
        cost_after_discount = float(discounted_result.split("Cost: ")[1].split(" INR")[0])
    except Exception:
        print("[DEBUG LOG] Error parsing previous feature price tokens.")
        return f"Error in processing receipt. {discounted_result}"
        
    # Core Feature 3 logic: Calculate GST/Tax (12%) and Service Fee (500 INR base, 200 INR for Premium)
    tax = cost_after_discount * 0.12
    service_fee = 200 if is_premium_member else 500
    final_bill = cost_after_discount + tax + service_fee
    
    # Task 3: Create a clean sample output format for the working system
    receipt = f"""
    ========================================
             TRAVEL BOOKING RECEIPT         
    ========================================
    Destination    : {destination_name.strip().title()}
    Duration       : {days} Days
    Promo Applied  : {promo_code if promo_code else 'None'}
    Premium Member : {'Yes' if is_premium_member else 'No'}
    ----------------------------------------
    Base & Discounted Cost : {cost_after_discount:.2f} INR
    GST / Tax (12%)        : {tax:.2f} INR
    Service Fee            : {service_fee:.2f} INR
    ----------------------------------------
    TOTAL PAYABLE AMOUNT   : {final_bill:.2f} INR
    ========================================
    Status: Confirmed & Ready to Fly! 
    """
    return receipt

# Run end-to-end tests to show the system working properly
print("\n--- RUNNING DAY 10 END-TO-END SYSTEM TESTS ---")
print(generate_final_receipt("Ooty", 3, "TRAVEL20"))
print(generate_final_receipt("Goa", 4, None, is_premium_member=True))
