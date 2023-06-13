import os
import gzip
import shutil

data_dir = 'C:/Users/thiag/Downloads/all_pdb_data'  # Replace with your path
output_dir = 'C:/Users/thiag/Downloads/all_pdb_data/unzipped'  # Output directory
os.makedirs(output_dir, exist_ok=True)  # Create the output directory if it doesn't exist

pdb_files = [f for f in os.listdir(data_dir) if f.endswith('.ent.gz')]
