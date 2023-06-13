import pandas as pd

# Load the CSV file
data = pd.read_csv("C:\\Users\\thiag\\Downloads\\pdb_data.csv", delimiter=';')

# Remove all rows where the column at index 11 is empty
data = data.dropna(subset=[data.columns[10]])

# Remove all rows where values in the second column are duplicated
data = data.drop_duplicates(subset=data.columns[1])

# Save the resulting DataFrame back to the CSV file
data.to_csv("C:\\Users\\thiag\\Downloads\\pdb_data.csv", sep=';', index=False)
