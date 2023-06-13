import os
from ftplib import FTP

ftp = FTP('ftp.wwpdb.org')
ftp.login()
ftp.cwd('/pub/pdb/data/structures/all/pdb/')
files = []
ftp.retrlines('NLST', files.append)
os.makedirs('all_pdb_data', exist_ok=True)
for file in files:
    if file.endswith('.gz'):
        local_file = f'all_pdb_data/{file}'
        with open(local_file, 'wb') as f:
            ftp.retrbinary(f'RETR {file}', f.write)
        print(f'Downloaded {file}')
ftp.quit()
print('Download completed.')