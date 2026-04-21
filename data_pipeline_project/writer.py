def write_data(file_path, data):
    with open(file_path, "w") as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")