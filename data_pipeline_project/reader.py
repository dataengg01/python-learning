def read_data(file_path):
    with open(file_path, "r") as file:
        data = file.read().split()
    return data
    

