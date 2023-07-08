


import os

def delete_log_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".log"):
                file_path = os.path.join(root, file)
                print(f"Deleting file: {file_path}")
                os.remove(file_path)



directory_to_search = "C:/"



delete_log_files(directory_to_search)


