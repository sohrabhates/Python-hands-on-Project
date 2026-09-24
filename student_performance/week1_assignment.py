import pandas as pd
import numpy as np

# Load the student performance dataset
df = pd.read_csv("StudentsPerformance.csv")

# Display the first five rows
print("----- First 5 Rows of the Dataset -----")
print(df.head())

# Check for missing values
print("\n----- Missing Values -----")
missing_values = df.isnull().sum()
print(missing_values)

# Since there are no missing values, no cleaning is required
if missing_values.sum() == 0:
    print("\nNo missing values found. The dataset is already clean.")
else:
    print("\nMissing values detected and need to be handled.")

# Display statistics for student scores
subjects = ["math score", "reading score", "writing score"]

for subject in subjects:
    print(f"\n----- {subject.title()} -----")
    print(f"Average Score : {df[subject].mean():.2f}")
    print(f"Highest Score : {df[subject].max()}")
    print(f"Lowest Score  : {df[subject].min()}")

print("\nAssignment completed successfully.")