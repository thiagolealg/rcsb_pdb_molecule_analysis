
# RCSB PDB Molecule Analysis

This repository contains code for analyzing molecular data from the RCSB Protein Data Bank (PDB) using Python and R. The analysis includes data extraction, cleaning, and visualization.

## Getting Started

To get started, follow these steps:

1. Clone the repository: `git clone https://github.com/thiagolealg/rcsb_pdb_molecule_analysis.git`
2. Navigate to the repository: `cd rcsb_pdb_molecule_analysis`

## Data Extraction

The first step is to extract the data from the PDB using the `download_pdb_files.py` script. This script connects to the RCSB PDB API and downloads the PDB files for further analysis. The downloaded files are stored in a local directory.

## Data Cleaning

Next, we need to clean the downloaded PDB data using the `clean_pdb_data.py` script. This script reads the downloaded PDB files, removes any error files, and performs necessary transformations to prepare the data for analysis. The cleaned data is then ready for conversion.

## Data Conversion

The `convert_pdb_to_csv.py` script is used to convert the cleaned PDB data into a CSV format, which is more suitable for analysis in Python. The script reads the cleaned data, extracts relevant information such as Seq ID, Molecule ID, SMILES, Molecular Formula, and various molecular properties. It then writes the extracted data into a CSV file named `pdb_data.csv`. The CSV file can be easily loaded and manipulated in Python for further analysis.

## Data Visualization

The `visualize_molecular_data.R` script uses R and several libraries to visualize the molecular data stored in the `pdb_data.csv` file. The script begins by loading the necessary libraries, including `ggplot2`, `dplyr`, `corrplot`, `cluster`, `factoextra`, `stringr`, and `GGally`. These libraries provide powerful tools for data visualization and analysis.

### Histogram of Exact Molecular Weight

The first visualization is a histogram of the exact molecular weight. This plot provides insights into the distribution of molecular weights in the dataset. The script uses the `ggplot2` library to create the histogram and sets appropriate labels for the x-axis, y-axis, and title.

### Boxplot of LogP

The next visualization is a boxplot of the LogP values. LogP is a measure of the partition coefficient between a compound and an organic solvent, which indicates the compound's hydrophobicity. The boxplot helps identify the range, median, and potential outliers in the LogP values.

### Scatterplot of LogP vs. Exact Molecular Weight

The script then creates a scatterplot to compare LogP with the exact molecular weight. This plot visualizes the relationship between these two variables and helps identify any potential correlations or patterns.
<img width="385" alt="Scatterplot of Ring Count and TPSA" src="https://github.com/thiagolealg/rcsb_pdb_molecule_analysis/assets/113521516/27539289-fbd5-42ad-84e9-8ebb37a04350">

### Density Plot of LogP

The density plot provides a smooth representation of the distribution of LogP values. It helps visualize the density of LogP values across the range and provides insights into the overall distribution shape.

### Boxplot of Number of Hydrogen Donors and Acceptors

The next visualization is a boxplot of the number of hydrogen donors and acceptors. This plot provides a comparison of these two variables and helps identify any relationships or differences between them.
<img width="406" alt="Boxplot of Number of Hydrogen Donors and Acceptors" src="https://github.com/thiagolealg/rcsb_pdb_molecule_analysis/assets/113521516/b08aafa3-50aa-4463-a0e5-e614b383ec34">

### Histogram of LogP

The script creates another histogram, this time specifically for LogP values. It provides a more detailed view of the LogP distribution, with a customizable number of bins.
<img width="405" alt="count logp" src="https://github.com/thiagolealg/rcsb_pdb_molecule_analysis/assets/113521516/a0f1231a-8dfb-498b-99d9-56524a0ec1e4">

### Scatterplot of Ring Count and TPSA

The scatterplot compares the ring count and TPSA (Topological Polar Surface Area). It helps visualize any relationship or clustering patterns between these two variables.
<img width="397" alt="Scatterplot of LogP vs exact molecular weight" src="https://github.com/thiagolealg/rcsb_pdb_molecule_analysis/assets/113521516/96fa9eb1-0a62-4a89-8a5e-60cf562b7dc3">

### Boxplot of Exact Molecular Weight

The boxplot of exact molecular weight provides insights into the distribution of molecular weights. It helps identify the range, median, and potential outliers in the dataset.

### Violin Plot of Exact Molecular Weight by Number of Hydrogen Acceptors

The final visualization is a violin plot that showcases the distribution of exact molecular weight based on the number of hydrogen acceptors. This plot helps compare the molecular weights across different numbers of hydrogen acceptors and identifies any potential patterns or differences.
<img width="403" alt="Violin Plot of Exact Molecular Weight by Number of Hydrogen Acceptors" src="https://github.com/thiagolealg/rcsb_pdb_molecule_analysis/assets/113521516/bbd88539-cdd6-40e5-bdbf-2437708fc481">

## Conclusion

This documentation provides an overview of the RCSB PDB Molecule Analysis repository. By following the steps outlined in the "Getting Started" section, you can replicate the analysis and visualize the molecular data. For more detailed information, please refer to the individual scripts and the comments within them.

For any questions or further assistance, please feel free to reach out.
