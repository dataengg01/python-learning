from utils import add
from reader import read_data
from processor import DataProcessor
from writer import write_data

# Read
data = read_data("data.txt")
print(data)

# Process
processor = DataProcessor(data)
result = processor.count_frequency()
print(result)

# Write
write_data("output.txt", result)
print("Data written to output.txt")