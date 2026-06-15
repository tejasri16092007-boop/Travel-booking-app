from validation_handler import secure_booking_gateway

"""
Day 12: Automated Testing Suite
This script executes 10 distinct end-to-end test cases covering valid paths,
discounts, premium memberships, and bad inputs to ensure full app reliability.
"""

# Task 1 & 3: Define 10 different complete flow testing scenarios
test_scenarios = [
    {"dest": "Ooty", "days": 3, "promo": "TRAVEL20", "premium": False},
    {"dest": "Goa", "days": 5, "promo": "BUDGET10", "premium": True},
    {"dest": "Kodaikanal", "days": 2, "promo": None, "premium": False},
    {"dest": "Manali", "days": 4, "promo": "TRAVEL20", "premium": True},
    {"dest": "Pondicherry", "days": 1, "promo": "BUDGET10", "premium": False},
    {"dest": "Ooty", "days": 7, "promo": None, "premium": True},
    {"dest": "Goa", "days": "invalid_day_string", "promo": "TRAVEL20", "premium": False},
    {"dest": "   ", "days": 3, "promo": None, "premium": False},
    {"dest": "Mumbai", "days": 2, "promo": "TRAVEL20", "premium": False},
    {"dest": "Kodaikanal", "days": -5, "promo": "BUDGET10", "premium": True}
]

print("=== STARTING DAY 12: AUTOMATED 10-FLOW TESTING SUITE ===")

for idx, test in enumerate(test_scenarios, 1):
    print(f"\n--- Running Test Flow {idx}/10 ---")
    print(f"Inputs: Destination={test['dest']}, Days={test['days']}, Promo={test['promo']}, Premium={test['premium']}")
    
    # Executing the complete pipeline flow
    result = secure_booking_gateway(test['dest'], test['days'], test['promo'], test['premium'])
    print(result)

print("\n=======================================================")
print("All 10 complete testing flows executed successfully!")
print("=======================================================")

# Task 5: Peer Testing Feedback & Confusion Points Documented
print("\n--- Classmate Peer Review & Feedback Notes ---")
print("1. Confusion: Case sensitivity issues when entering destination names.")
print("   Fix: Already resolved using .strip().lower() syntax in query handling.")
print("2. Bug Found: App crashed earlier when string alphabets were entered for days count.")
print("   Fix: Resolved by adding robust try/except validation inside validation_handler.")
