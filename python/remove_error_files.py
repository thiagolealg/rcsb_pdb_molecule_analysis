import os

# Directories
error_dir = 'C:\\Users\\thiag\\Downloads\\all_pdb_data\\error_files\\'
converted_dir = 'C:\\Users\\thiag\\Downloads\\all_pdb_data\\converted\\'

# List of files in the error directory
error_files = os.listdir(error_dir)

# Iterate over the error files
for file in error_files:
    # Full path to the file in the converted directory
    converted_file_path = os.path.join(converted_dir, file)

    # If the file exists in the converted directory, remove it
    if os.path.exists(converted_file_path):
        os.remove(converted_file_path)
        print(f'File {file} removed from the converted directory.')
    else:
        print(f'File {file} not found in the converted directory.')
