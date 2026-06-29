# ============================================================
# DATA ANALYST INTERNSHIP - TASK 1
# Data Cleaning and Preprocessing
# Dataset: marketing_campaign.csv
# ============================================================

# Step 1: Import Pandas Library
import pandas as pd

# ------------------------------------------------------------
# Step 2: Load Dataset
# sep="\t" is used because the dataset is tab-separated
# ------------------------------------------------------------
df = pd.read_csv("marketing_campaign.csv", sep="\t")

print("=" * 60)
print("ORIGINAL DATASET")
print("=" * 60)

# Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Shape of dataset
print("\nDataset Shape (Rows, Columns):")
print(df.shape)

# Column names
print("\nColumn Names:")
print(df.columns)

# ------------------------------------------------------------
# Step 3: Check Missing Values
# ------------------------------------------------------------
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# ------------------------------------------------------------
# Step 4: Fill Missing Values
# Income column contains missing values.
# Fill them with Mean.
# ------------------------------------------------------------
df["Income"] = df["Income"].fillna(df["Income"].mean())

print("\nMissing Values After Filling:")
print(df.isnull().sum())

# ------------------------------------------------------------
# Step 5: Check Duplicate Records
# ------------------------------------------------------------
duplicate_count = df.duplicated().sum()

print("\nDuplicate Records Found:", duplicate_count)

# ------------------------------------------------------------
# Step 6: Remove Duplicate Records
# ------------------------------------------------------------
df = df.drop_duplicates()

print("Duplicate Records After Removal:", df.duplicated().sum())

# ------------------------------------------------------------
# Step 7: Rename Column Names
# Convert all column names to lowercase
# ------------------------------------------------------------
df.columns = df.columns.str.lower()

print("\nUpdated Column Names:")
print(df.columns)

# ------------------------------------------------------------
# Step 8: Convert Date Column
# dt_customer -> datetime
# ------------------------------------------------------------
df["dt_customer"] = pd.to_datetime(
    df["dt_customer"],
    dayfirst=True,
    errors="coerce"
)

print("\nDate Column Converted Successfully")

# ------------------------------------------------------------
# Step 9: Check Data Types
# ------------------------------------------------------------
print("\nData Types:")
print(df.dtypes)

# ------------------------------------------------------------
# Step 10: Basic Statistical Summary
# ------------------------------------------------------------
print("\nStatistical Summary:")
print(df.describe())

# ------------------------------------------------------------
# Step 11: Final Dataset Information
# ------------------------------------------------------------
print("\nFinal Dataset Information:")
print(df.info())

# ------------------------------------------------------------
# Step 12: Save Cleaned Dataset
# ------------------------------------------------------------
df.to_csv("cleaned_marketing_campaign.csv", index=False)

print("\nCleaned Dataset Saved Successfully!")

# ------------------------------------------------------------
# Step 13: Cleaning Summary
# ------------------------------------------------------------
print("\n" + "=" * 60)
print("DATA CLEANING SUMMARY")
print("=" * 60)

print(f"Total Rows : {df.shape[0]}")
print(f"Total Columns : {df.shape[1]}")

print("\nTasks Performed:")
print("1. Loaded Dataset")
print("2. Displayed First 5 Rows")
print("3. Checked Dataset Information")
print("4. Checked Missing Values")
print("5. Filled Missing Income Values using Mean")
print("6. Checked Duplicate Records")
print("7. Removed Duplicate Records")
print("8. Converted Column Names to Lowercase")
print("9. Converted Date Column to Datetime")
print("10. Verified Data Types")
print("11. Generated Statistical Summary")
print("12. Saved Cleaned Dataset")

print("\nTask Completed Successfully!")
print("=" * 60)