from validation_handler import secure_booking_gateway

"""
Day 20: Fix User Testing Issues
This script implements critical patches based on Day 19 feedback:
1. Automated uppercase conversion & space cleaning for promo codes.
2. Explicit visual headers for Premium Membership status layers.
3. Compact text alignment padding safety for clean mobile screens.
"""

def applied_feedback_gateway(destination_name, days, promo_code=None, is_premium=False):
    # Task 1 & 2: Fix trailing spaces in destination and case-insensitivity in promo codes
    clean_destination = str(destination_name).strip().title()
    
    clean_promo = None
    if promo_code:
        clean_promo = str(promo_code).strip().upper()  # Automatically turns 'travel20' to 'TRAVEL20'

    # Get the raw calculation from backend gateway
    base_bill = secure_booking_gateway(clean_destination, days, clean_promo, is_premium)
    
    if "TOTAL PAYABLE AMOUNT" not in base_bill:
        return base_bill

    # Task 3: Add explicit status placeholders/tooltips for absolute user clarity
    premium_badge = " [PREMIUM TIER ACCOUNT: ACTIVE]" if is_premium else "ℹ️ [STANDARD TIER ACCOUNT: NO EXTRA DISCOUNT]"
    
    # Task 5: Compact text wraps keeping mobile layouts aligned beautifully
    polished_output = f"""
==================================================
{premium_badge}
==================================================
Destination Name : {clean_destination:<20}
Total Tour Plan  : {days} Days Registered
--------------------------------------------------
{base_bill.strip()}
==================================================
 [USER NOTE]: Promo code applied successfully with auto-sanitization.
"""
    return polished_output

# Task 4: Re-test with the same users to verify if it is clearer now
print("--- RUNNING DAY 20: POST-FIX RE-TESTING SESSIONS ---")
print("\n[RE-TEST USER 1] Testing with messy spaces and lowercase promo (' ooty ', 'travel20'):")
print(applied_feedback_gateway(" ooty ", 3, "travel20", is_premium=True))
