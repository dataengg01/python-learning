import logging

def read_data(file_path):
    try:
        logging.info("Reading data from file")
        
        with open(file_path, "r") as file:
            data = file.read().split()
        return data
    except FileNotFoundError:
        logging.error("File Not Found")
        return []
    except Exception as e:
        logging.error(f"Error: Unexpected Error: {e}")
        return []
    

