import pandas as pd
import time

"""
Day 18: Performance & Optimization
This script implements memory footprint optimization using specific pandas datatypes
and introduces caching mechanics to instantly handle repetitive queries without lagging.
"""

# Task 3: In-memory dictionary cache store to prevent redundant database loops
_booking_cache = {}

def optimized_destination_lookup(destination_name):
    dest_clean = str(destination_name).strip().lower()
    
    # Task 3: High-speed recovery check from Cache Memory if requested before
    if dest_clean in _booking_cache:
        print(f" [CACHE HIT] Instantly fetched from cache memory layer for: '{destination_name}'")
        return _booking_cache[dest_clean]
        
    # Task 1, 2 & 4: Optimize slowest disk operations and memory usage
    try:
        start_time = time.perf_counter()
        
        # Task 4: Forcing minimal datatypes (category, float32) drastically drops memory overhead
        optimized_dtypes = {
            'destination': 'category',
            'availability': 'category',
            'price_per_day': 'float32'
        }
        
        # Vectorized safe reading layer to prevent app crashes on large datasets
        df = pd.read_csv('Data/processed/cleaned_destinations.csv', dtype=optimized_dtypes)
        
        # Fast query scanning loop
        match = df[df['destination'].str.lower() == dest_clean]
        
        if not match.empty:
            result_dict = match.to_dict(orient='records')[0]
            
            # Save into cache layer for future repetitive calls
            _booking_cache[dest_clean] = result_dict
            
            end_time = time.perf_counter()
            print(f" [DISK SCAN] First time scan completed in {end_time - start_time:.6f} seconds.")
            return result_dict
        else:
            return None
            
    except FileNotFoundError:
        return "Error: Processed core database file missing."

# Run benchmarking execution loops to verify optimizations
print("--- RUNNING DAY 18 PERFORMANCE AND MEMORY OPTIMIZATION CHECKS ---")

# 1. First Run: Slow disk reading with minimal datatype optimization logs
print("\n[RUN 1] Parsing Query 'Ooty' (First Time Database Scan):")
print(optimized_destination_lookup("Ooty"))

# 2. Second Run: Blazing fast cache recovery check
print("\n[RUN 2] Repeating Query 'Ooty' (Cache Buffer Trigger Check):")
print(optimized_destination_lookup("Ooty"))
