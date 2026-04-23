import sys
from reader import read_data
from processor import DataProcessor
from writer import write_data
import config
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Default values
input_file = config.INPUT_FILE
output_file = config.OUTPUT_FILE

# Override using CLI if provided
if len(sys.argv) >= 3:
    input_file = sys.argv[1]
    output_file = sys.argv[2]


# Read
logging.info("Pipeline Started")

data = read_data(input_file)

if not data:
    logging.warning("No Data to Process")
else:
    # Process
    logging.info("Data Read Successfully")

    processor = DataProcessor(data)
    result = processor.count_frequency()

    logging.info("Processing Completed")

    # Write
    write_data(output_file, result)

    logging.info("Data Written Successfully")

logging.info("Pipeline Completed")

