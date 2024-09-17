# src/utils.py
from datetime import datetime

import csv
import os


import csv
import os

def save_data(data, filepath):
    """Save data to a CSV file, ensuring no duplicate rows."""
    if not data:
        return  # Return if there's no data to write

    # Extract the keys from the first dictionary for the CSV headers
    headers = data[0].keys()

    # Ensure the directory exists
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    # Read existing data from the file, if it exists
    existing_data = []
    if os.path.isfile(filepath):
        with open(filepath, 'r', newline='') as f:
            reader = csv.DictReader(f)
            existing_data = list(reader)
    
    # Create a set of existing rows to check for duplicates
    existing_rows_set = set((tuple(row.items()) for row in existing_data))

    # Convert new data to a set of tuples for comparison
    new_rows_set = set((tuple(row.items()) for row in data))

    # Filter out duplicate rows
    unique_rows_set = new_rows_set - existing_rows_set
    unique_rows = [dict(row) for row in unique_rows_set]

    if not unique_rows:
        return  # No new unique rows to add

    # Write the updated data back to the CSV
    with open(filepath, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)

        # Write header if file is new
        if not existing_data:
            writer.writeheader()

        # Write unique rows
        writer.writerows(unique_rows)

    log_message(f"Data saved to {filepath}")




def log_message(message):
    """Simple logger to print messages with timestamps."""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] {message}")
