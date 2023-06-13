import os
import csv
import shutil
from rdkit import Chem
from rdkit.Chem import Descriptors, rdMolDescriptors
from rdkit import RDLogger

# Suppress RDKit error messages
RDLogger.DisableLog('rdApp.*')

# Define the folder with MOL and PDB files
mol_folder = "C:\\Users\\thiag\\Downloads\\all_pdb_data\\converted"
pdb_folder = "C:\\Users\\thiag\\Downloads\\all_pdb_data\\unzipped"
error_folder = "C:\\Users\\thiag\\Downloads\\all_pdb_data\\error_files"

# Create the error_folder if it doesn't exist
os.makedirs(error_folder, exist_ok=True)

# The CSV file to store data
csv_file = "C:\\Users\\thiag\\Downloads\\pdb_data.csv"

# Check if the CSV file exists
csv_exists = os.path.isfile(csv_file)

# Function to check if a string can be converted to an integer
def is_integer(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

# Initialize CSV writer
with open(csv_file, "a", newline='') as file:
    writer = csv.writer(file, delimiter=';')

    # Read the last processed ID and molecule ID from the CSV file
    last_processed_id = 0
    last_molecule_id = ""

    if csv_exists:
        with open(csv_file, "r") as read_file:
            csv_reader = csv.DictReader(read_file, delimiter=';')
            for row in csv_reader:
                if is_integer(row["Seq ID"]):
                    last_processed_id = max(last_processed_id, int(row["Seq ID"]))

    # Process all .mol files in the converted folder
    file_count = 0
    rejected_files = 0  # Counter for rejected files
    for filename in os.listdir(mol_folder):
        if filename.endswith(".mol"):
            mol_file = os.path.join(mol_folder, filename)
            molecule_id = os.path.splitext(filename)[0]  # Get molecule ID from file name

            # Copy the file to the error folder before processing
            shutil.copy(mol_file, os.path.join(error_folder, filename))

            # Print the name of the file being processed
            print("Processing file:", filename)

            try:
                mol = Chem.MolFromMolFile(mol_file, sanitize=False)
                if mol is not None:
                    try:
                        # Try to sanitize the molecule
                        Chem.SanitizeMol(mol)
                        print("Sanitized molecule:", molecule_id)
                    except ValueError as e:
                        # Handle explicit valence error
                        if 'explicit valence' in str(e):
                            for atom in mol.GetAtoms():
                                atom.SetNumExplicitHs(min(max(0, atom.GetAtomicNum() - atom.GetExplicitValence()), atom.GetAtomicNum()))
                            Chem.SanitizeMol(mol)
                            print("Resolved explicit valence error for molecule:", molecule_id)
                        else:
                            raise e
                else:
                    raise Exception("Could not create molecule from file:", filename)
            except Exception as e:
                # Skip to the next file if an error occurs
                print("Error processing file:", filename)
                print("Error message:", str(e))
                rejected_files += 1  # Increment rejected files counter

                # No need to move the problematic file to the error folder, it was already copied there before processing
                continue

            try:
                # Compute the properties
                smiles = Chem.MolToSmiles(mol)
                formula = rdMolDescriptors.CalcMolFormula(mol)
                exact_mol_wt = Descriptors.ExactMolWt(mol)
                mol_log_p = Descriptors.MolLogP(mol)
                num_h_acceptors = rdMolDescriptors.CalcNumLipinskiHBA(mol)
                num_h_donors = rdMolDescriptors.CalcNumLipinskiHBD(mol)
                num_rotatable_bonds = rdMolDescriptors.CalcNumRotatableBonds(mol)
                ring_count = Descriptors.RingCount(mol)
                tpsa = rdMolDescriptors.CalcTPSA(mol)

                # Write the data to the CSV file
                writer.writerow([last_processed_id + 1, molecule_id, smiles, formula, exact_mol_wt, mol_log_p,
                                 num_h_acceptors, num_h_donors, num_rotatable_bonds, ring_count, tpsa])

                # Update the last processed ID and molecule ID
                last_processed_id += 1
                last_molecule_id = molecule_id

                print("Processed and written to CSV file:", molecule_id)
            except Exception as e:
                # If an error occurs, print the details
                print("Error processing molecule:", molecule_id)
                print("Error message:", str(e))

            # Increment the file count
            file_count += 1

    print("Total files processed:", file_count)
    print("Total files rejected due to errors:", rejected_files)
