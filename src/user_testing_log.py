"""
Day 19: User Testing Logs & Session Notes
This script documents the testing sessions conducted with two users,
tracking their confusion points, identified bugs, and planned fixes (Tasks 1-5).
"""

# Task 1, 2, 3 & 4: Detailed documentation of 2 independent user testing sessions
user_test_sessions = {
    "User_1_Review (Classmate)": {
        "duration_minutes": 10,
        "confusion_points": [
            "User tried to enter lowercase promo codes and thought the discount failed due to case mismatch.",
            "Unsure if the 15% activity discount was automatically applied or required an extra click."
        ],
        "bugs_found": [
            "Entering a trailing space inside the destination text string caused an initial parsing mismatch before validation layer caught it."
        ]
    },
    "User_2_Review (Friend)": {
        "duration_minutes": 11,
        "confusion_points": [
            "When maximum budget was set extremely low, user was confused by empty state console blocks formatting layout.",
            "Needed an explicit text confirmation showing whether Premium status is Active or Inactive on screen."
        ],
        "bugs_found": [
            "No terminal crashes occurred, but text alignment wraps slightly tight on small mobile console outputs."
        ]
    }
}

print("=== CODEZONER DAY 19: USER TESTING REPORT ANALYSIS ===")

for user, data in user_test_sessions.items():
    print(f"\n [SESSION LOG] {user}")
    print(f" Observation Duration: {data['duration_minutes']} Minutes (Strict No-Help Mode)")
    
    print(" Points of Confusion:")
    for pt in data['confusion_points']:
        print(f"   - {pt}")
        
    print(" Bugs/Issues Identified:")
    for bug in data['bugs_found']:
        print(f"   - {bug}")

# Task 5: Documenting all planned fixes from this session
print("\n=======================================================")
print(" SYSTEM PLANNED FIXES ROADMAP:")
print("1. Implement strict automated string sanitization (.strip().upper()) for promo codes.")
print("2. Add explicit status headers ('[PREMIUM STATUS: ACTIVE]') on final receipt view.")
print("3. Refine terminal padding layout constraints to look flawless on smaller display widths.")
print("=======================================================")
