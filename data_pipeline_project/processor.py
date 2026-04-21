class DataProcessor:

    def __init__(self, data):
        self.data = data   # store input data

    def count_frequency(self):
        freq = {}

        for item in self.data:
            freq[item] = freq.get(item, 0) + 1

        return freq