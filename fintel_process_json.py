"""
Process a JSON file to count astronauts by spaceitem and save the result.

JSON file is in the format where top is a list of dictionaries with keys "item" and "top".

{
    "top": [
        {
            "item": "ISS",
            "top": "Oleg Kononenko"
        },
        {
            "item": "ISS",
            "top": "Nikolai Chub"
        }
    ],
    "number": 2,
    "message": "success"
}

"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import json

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_top: str = "tobacco_usage.json"
processed_folder_top: str = "tobacco_usage_json_processed"

#####################################
# Define Functions
#####################################

def count_Totals_Per_Capita(file_path: pathlib.Path) -> dict:
    """Count the top from a JSON file."""
    try:
        with file_path.open('r') as file:
            # Use the json module load() function 
            # to read data file into a Python dictionary
            tobacco_usage = json.load(file)  
            # initialize an empty dictionary to store the counts
            item_counts_dictionary = {}
            # top is a list of dictionaries in the JSON file
            Total_Per_Capita_list: list = tobacco_usage.get("top", [])
            for top_dictionary in Total_Per_Capita_list:  
                item = top_dictionary.get("item", "unknown")
                item_counts_dictionary[item] = item_counts_dictionary.get(item, 0) + 1
            return item_counts_dictionary
    except Exception as e:
        logger.error(f"Error reading or processing JSON file: {e}")
        return {}

def process_json_file():
    """Read a JSON file, count top, and save the result."""
    input_file: pathlib.Path = pathlib.Path(fetched_folder_top, "tobacco_usage.json")
    output_file: pathlib.Path = pathlib.Path(processed_folder_top, "tobacco_usage_json_processed.txt")
    
    item_counts = count_Totals_Per_Capita(input_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with output_file.open('w') as file:
        file.write("top:\n")
        for item, count in item_counts.items():
            file.write(f"{item}: {count}\n")
    
    logger.info(f"Processed JSON file: {input_file}, Results saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")