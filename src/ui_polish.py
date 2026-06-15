import time
from itinerary_customizer import customize_trip_itinerary

"""
Day 17: UI & Design Polish
This script implements mock layout views for system processing, 
handling elegant empty data windows, custom loaders, and warning boxes.
"""

def render_loading_state():
    # Task 2: Add proper loading states so users know when things are processing
    print("\n [LOADING] Connecting to Travel Database Matrix...")
    time.sleep(0.3)
    print("🔄 [PROCESSING] Applying personalized interest tags and coupon layouts...")
    time.sleep(0.3)

def render_empty_state():
    # Task 3: Add empty states — what shows when there is no data yet?
    border = "═" * 50
    print(f"\n╔{border}╗")
    print("║                 NO DATA FOUND                 ║")
    print(f"╠{border}╣")
    print("║  It looks like your search query or budget is   ║")
    print("║  currently empty. Select parameters to start.  ║")
    print(f"╚{border}╝")

def render_error_state(error_message):
    # Task 4: Add error states — what shows when something goes wrong?
    border = "═" * 50
    print(f"\n [UI INTERFACE CRITICAL ERROR ALERT]")
    print(f" {error_message}")
    print("Please check your configuration rules and retry.")

def display_polished_app(destination=None, days=0, activities=None, promo=None, is_premium=False):
    # Task 1 & 5: Professional rendering structured perfectly for compact mobile text boxes
    if not destination or destination.strip() == "":
        render_empty_state()
        return

    render_loading_state()
    
    # Process backend payload
    output = customize_trip_itinerary(destination, days, activities, promo, is_premium)
    
    if "Error" in output or "Validation Error" in output:
        render_error_state(output)
    else:
        print("\n [SUCCESS] GENERATING CLEAN RENDERED VIEW:")
        print(output)

# Run complete UI simulation tests
print("--- RUNNING DAY 17 INTERFACE POLISH TESTS ---")
# 1. Success Route
display_polished_app("Goa", 4, ["scuba"], "BUDGET10", is_premium=True)
# 2. Empty State Trigger
display_polished_app(" ", 0)
# 3. Validation Error State Trigger
display_polished_app("Ooty", -5)
