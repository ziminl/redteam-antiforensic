


import os

def delete_files_with_extensions(directory, extensions):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_ext = os.path.splitext(file)[1].lower()
            if file_ext in extensions:
                print(f"Deleting file: {file_path}")
                os.remove(file_path)



directory_to_search = "C:/"



extensions_to_delete = [".log", ".txt", ".xml", ".yml", ".json", ".csv", ".trace", ".syslog"]




delete_files_with_extensions(directory_to_search, extensions_to_delete)


