#####################################
# Import Modules at the Top
#####################################

# Import from Python Standard Library
import pathlib

# Import from external packages
import requests

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name = "fintel_solar.csv"

#####################################
# Define Functions
#####################################

def fetch_csv_file(folder_name: str, filename: str, url: str) -> None:
    """
    Fetch CSV data from the given URL and write it to a file.

    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        url (str): URL of the CSV file to fetch.

    Returns:
        None

    Example:
        fetch_csv_file("data", "data.csv", "https://example.com/data.csv")
    """
    if not url:
        logger.error("The URL provided is empty. Please provide a valid URL.")
        return

    try:
        logger.info(f"Fetching CSV data from {url}...")
        response = requests.get(url)
        response.raise_for_status()
        write_csv_file(folder_name, filename, response.text)
        logger.info(f"SUCCESS: CSV file fetched and saved as {filename}")
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Request error occurred: {req_err}")

def write_csv_file(folder_name: str, filename: str, string_data: str) -> None:
    """
    Write CSV data to a file.

    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        string_data (str): CSV content as a string.

    Returns:
        None
    """
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        logger.info(f"Writing CSV data to {file_path}...")
        file_path.parent.mkdir(parents=True, exist_ok=True)
        #with file_path.open('w') as file:
        with open(f"{folder_name}/{filename}", "w", encoding="utf-8-sig") as file:
            file.write(string_data)
        logger.info(f"SUCCESS: CSV data written to {file_path}")
    except IOError as io_err:
        logger.error(f"Error writing CSV data to {file_path}: {io_err}")

#####################################
# Define main() function
#####################################

def main():
    """
    Main function to demonstrate fetching CSV data.
    """
    csv_url = 'https://github.com/dfintel25/Sample-Data/raw/refs/heads/main/Solar_Footprints_V2_7811899327930675815.csv'
    logger.info("Starting CSV fetch demonstration...")
    fetch_csv_file(fetched_folder_name, "fintel_solar.csv", csv_url)

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()

# TODO: Run this script to ensure all functions work as intended.
