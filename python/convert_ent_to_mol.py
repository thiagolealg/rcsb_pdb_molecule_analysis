import os
import subprocess

# Define the folder with PDB files
pdb_folder = "C:\\Users\\thiag\\Downloads\\all_pdb_data\\unzipped"

# Define the folder to save the converted files
converted_folder = "C:\\Users\\thiag\\Downloads\\all_pdb_data\\converted"

if not os.path.exists(converted_folder):
    os.makedirs(converted_folder)

# Convert all .ent files in the specified folder using Open Babel
for filename in os.listdir(pdb_folder):
    if filename.endswith(".ent"):
        pdb_file = os.path.join(pdb_folder, filename)
        mol_file = os.path.join(converted_folder, filename.rsplit(".", 1)[0] + ".mol")
        subprocess.run(["obabel", pdb_file, "-O", mol_file])
