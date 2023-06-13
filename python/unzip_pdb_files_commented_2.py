for pdb_file in pdb_files:
    with gzip.open(os.path.join(data_dir, pdb_file), 'rb') as f_in:
        with open(os.path.join(output_dir, pdb_file[:-3]), 'wb') as f_out:  # Remove .gz from the filename
            sh