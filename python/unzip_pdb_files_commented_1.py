import os
import gzip
import shutil

# Specify the input and output directories
data_dir = 'C:/Users/thiag/Downloads/all_pdb_data'  # Replace with your path
output_dir = 'C:/Users/thiag/Downloads/all_pdb_data/unzipped'  # Output directory

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Get a list of PDB files in the input directory
pdb_files = [f for f in os.listdir(data_dir) if f.endswith('.ent.gz')]

# Iterate over each PDB file
for pdb_file in pdb_files:
    # Open the gzip file for reading
    with gzip.open(os.path.join(data_dir, pdb_file), 'rb') as f_in:
        # Open a new file in the output directory for writing (remove .gz extension)
        with open(os.path.join(output_dir, pdb_file[:-3]), 'wb') as f_out:
            # Copy the contents from the input file to the output file
            shutil.copyfileobj(f_in, f_out)
