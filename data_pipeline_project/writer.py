import json
import logging

def write_data(file_path, data):
    try:
        logging.info(f"Writting data to {file_path}")

        with open(file_path, "w") as file:
            json.dump(data, file, indent=2)
    except Exception as e:
        logging.error(f"Error writting file: {e}")

