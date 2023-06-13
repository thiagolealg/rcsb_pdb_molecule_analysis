# Import the necessary libraries
import os
from ftplib import FTP

# Connect to the FTP server
ftp = FTP('ftp.wwpdb.org')
ftp.login()

# Navigate to the desired directory
ftp.cwd('/pub/pdb/data/structures/all/pdb/')

# List all the files in the directory
files = []
ftp.retrlines('NLST', files.append)

# Create the local directory where the files will be saved
os.makedirs('all_pdb_data', exist_ok=True)

# Download PDB files
for file in files:
    if file.endswith('.gz'):
        local_file = f'all_pdb_data/{file}'
        with open(local_file, 'wb') as f:
            ftp.retrbinary(f'RETR {file}', f.write)
        print(f'Downloaded {file}')

ftp.quit()
print('Download completed.')
