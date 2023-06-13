library(ggplot2)
library(dplyr)
library(corrplot)
library(cluster)
library(factoextra)
library(stringr)
library(GGally)

# Load the data
data <- read.csv("pdb_data.csv", sep = ";")

# Adjust column names
colnames(data) <- c("Seq ID", "Molecule ID", "SMILES", "Molecular Formula", "Exact Mol Wt",
                    "Mol LogP", "Num H Acceptors", "Num H Donors", "Num Rotatable Bonds",
                    "Ring Count", "TPSA")

# Take a look at the first few rows of data
print("First few rows of the data:")
head(data)

# Get a statistical summary
print("Statistical summary:")
summary(data)

# Perform data transformations
data$Exact.Mol.Wt <- as.numeric(gsub("\\.", "", as.character(data$Exact.Mol.Wt)))
data$Mol.LogP <- as.numeric(gsub("\\.", "", as.character(data$Mol.LogP)))
data$TPSA <- as.numeric(gsub("\\.", "", as.character(data$TPSA)))
data$TPSA <- data$TPSA / 1e15
data$TPSA <- round(data$TPSA, 3)
data$Exact.Mol.Wt <- data$Exact.Mol.Wt / 1e15
data$Exact.Mol.Wt <- round(data$Exact.Mol.Wt, 3)
data$Mol.LogP <- data$Mol.LogP / 1e15
data$Mol.LogP <- round(data$Mol.LogP, 3)

# Make a histogram of the exact molecular weight
ggplot(data, aes(x=Exact.Mol.Wt)) +
  geom_histogram(binwidth=10, fill="blue", color="black") +
  theme_minimal() +
  labs(x="Exact Molecular Weight", y="Count", title="Histogram of Exact Molecular Weight") +
  theme(plot.title = element_text(hjust = 0.5))

# Boxplot of LogP
ggplot(data, aes(x=Mol.LogP)) +
  geom_boxplot(fill="lightblue", color="black") +
  theme_minimal() +
  labs(x="LogP", y="Count", title="Boxplot of LogP") +
  theme(plot.title = element_text(hjust = 0.5))

# Scatterplot of LogP vs exact molecular weight
ggplot(data, aes(x=Exact.Mol.Wt, y=Mol.LogP)) +
  geom_point(color="blue") +
  theme_minimal() +
  labs(x="Exact Molecular Weight", y="LogP", title="Scatterplot of LogP vs Exact Molecular Weight") +
  theme(plot.title = element_text(hjust = 0.5))

# Density plot of LogP
ggplot(data, aes(x=Mol.LogP)) +
  geom_density(fill="lightblue", alpha=0.5) +
  labs(title="Density Plot of LogP", x="LogP", y="Density")

# Boxplot of Number of Hydrogen Donors and Acceptors
ggplot(data, aes(x=Num.H.Donors, y=Num.H.Acceptors)) +
  geom_boxplot() +
  labs(title="Boxplot of Number of Hydrogen Donors and Acceptors", x="Number of Hydrogen Donors", y="Number of Hydrogen Acceptors")

# Histogram of LogP
ggplot(data, aes(x=Mol.LogP)) +
  geom_histogram(bins=30, fill="skyblue") +
  theme_minimal() +
  xlab("LogP")

# Scatterplot of Ring Count and TPSA
ggplot(data, aes(x=Ring.Count, y=TPSA)) +
  geom_point() +
  labs(title="Scatterplot of Ring Count and TPSA", x="Ring Count", y="TPSA")

# Boxplot of Exact Molecular Weight
ggplot(data, aes(y=Exact.Mol.Wt)) +
  geom_boxplot(fill="skyblue", color="black") +
  labs(title="Boxplot of Exact Molecular Weight", y="Exact Molecular Weight") +
  theme_minimal()

# Violin Plot of Exact Molecular Weight by Number of Hydrogen Acceptors
ggplot(data, aes(x=Num.H.Acceptors, y=Exact.Mol.Wt)) +
  geom_violin(fill="lightblue", color="black") +
  labs(title="Violin Plot of Exact Molecular Weight by Number of Hydrogen Acceptors", x="Number of Hydrogen Acceptors", y="Exact Molecular Weight") +
  theme_minimal()
