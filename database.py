import json
import os

def save_booking(details):
    # Data folder irukka-nu paakum, illa na create pannum
    if not os.path.exists("Data"):
        os.makedirs("Data")
        
    file_path = "Data/bookings.json"
    
    # Palaya data irundha read pannum
    data = []
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
            
    # Pudhu data-vai add pannum
    data.append(details)
    
    # File-la save pannum
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
