import pandas as pd
from validation_handler import secure_booking_gateway

"""
Day 16: Advanced Feature 2 - Travel Itinerary & Activity Customizer
This advanced feature connects with previous validation gateways and billing 
systems to dynamically inject premium activity add-ons into the final bill.
"""

def customize_trip_itinerary(destination_name, days, activities=None, promo_code=None, is_premium=False):
    # Task 2: Connect it to the rest of your project (Calling Day 11 Gateway)
    base_bill = secure_booking_gateway(destination_name, days, promo_code, is_premium)
    
    if "TOTAL PAYABLE AMOUNT" not in base_bill:
        return f"Customization Stopped: {base_bill.strip()}"
        
    # Advanced Feature 2 Logic: Activity Add-on Catalog
    activity_catalog = {
        "trekking": 1200.0,
        "scuba": 3500.0,
        "sightseeing": 800.0,
        "food_tour": 1500.0
    }
    
    additional_cost = 0.0
    selected_activities = []
    
    # Task 4: Fast linear processing loops to ensure no performance slowdowns
    if activities:
        for act in activities:
            act_clean = str(act).strip().lower()
            if act_clean in activity_catalog:
                cost = activity_catalog[act_clean]
                # Premium layers get 15% discount on custom activities too
                if is_premium:
                    cost = cost * 0.85
                additional_cost += cost
                selected_activities.append(act_clean.title())
            else:
                print(f"[PERFORMANCE NOTE] Skipped un-cataloged add-on: {act}")

    # Extract base calculated bill total safely using split handlers
    try:
        base_total = float(base_bill.split("TOTAL PAYABLE AMOUNT   : ")[1].split(" INR")[0])
    except Exception:
        base_total = 0.0

    final_integrated_total = base_total + additional_cost

    # Task 3: Render integrated complex output tracking both features active
    customized_summary = f"""{base_bill.strip()}
    ========================================
              CUSTOMIZED ITINERARY          
    ========================================
    Selected Add-ons : {', '.join(selected_activities) if selected_activities else 'None'}
    Activity Cost    : {additional_cost:.2f} INR
    ----------------------------------------
    FINAL INTEGRATED BILL  : {final_integrated_total:.2f} INR
    ========================================
    """
    return customized_summary

# Task 3: Test the full project with both advanced features active
print("--- RUNNING DAY 16 FULL INTEGRATED ADVANCED TESTS ---")
print(customize_trip_itinerary("Ooty", 3, ["trekking", "sightseeing"], "TRAVEL20", is_premium=True))
