# Travel Booking Application

## 1. Problem Statement
Building a smart travel booking application that helps users explore top holiday destinations, compare real-time prices, and check accommodation availability smoothly.

## 2. Dataset Source
* **Source:** Custom curated travel dataset.
* **Primary Data Path:** `Data/destinations.csv`
* **Cleaned Data Path:** `Data/processed/cleaned_destinations.csv`

## 3. Project Approach & Preprocessing (Week 1)
* **Data Exploration:** Analyzed dataset shapes, types, and verified zero missing values using Python (`explore.py`).
* **Data Cleaning:** Properly formatted structure and moved it to the processed folder.
* **Feature Engineering:** Created derived features like budget metrics, mapping categorical availability, and splitting the data into an 80/20 train/test ratio (`features.py`).

## 4. Core Implementation & Features (Week 2 Updates)
* **Core Feature 1 (Cost Calculator):** Implemented a destination finder and dynamic trip cost calculator with type verification (`booking_feature.py`).
* **Core Feature 2 (Promo Engine):** Connected a coupon/discount tier system to the base calculator function (`discount_feature.py`).
* **Core Feature 3 (Receipt Generator):** Created an end-to-end receipt generator that calculates 12% GST tax and tier-specific service fees (`receipt_feature.py`).
* **Validation Gateway:** Wrapped core execution flows inside automated try-except exception blocks (`validation_handler.py`).
* **Test Suite:** Designed an automated 10-flow testing matrix covering standard paths and adversarial edge cases (`test_suite.py`).

## 5. Visualizations & System Charts
Below are the initial structural charts for our dataset flow:

![Data Flow Chart](https://placehold.co/600x300/2c3e50/ffffff?text=Data+Flow+and+Exploration+Chart)

![Feature Engineering Split](https://placehold.co/600x300/27ae60/ffffff?text=Train+Test+80-20+Split+Visualization)

