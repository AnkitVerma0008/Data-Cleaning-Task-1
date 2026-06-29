# Data Cleaning and Preprocessing - Task 1

## Objective

The objective of this task is to clean and preprocess the raw marketing campaign dataset by identifying and fixing common data quality issues such as missing values, duplicate records, inconsistent column names, and incorrect data types.

## Dataset

* **Dataset Name:** Marketing Campaign
* **File:** `marketing_campaign.csv`

## Tools Used

* Python 3.14
* Pandas
* Visual Studio Code

## Steps Performed

### 1. Loaded the Dataset

The dataset was loaded using the Pandas library.

### 2. Checked Dataset Information

Used `df.info()` and `df.shape` to understand the structure of the dataset.

### 3. Identified Missing Values

Checked all columns for missing values using `isnull().sum()`.

### 4. Handled Missing Values

Filled missing values in the **Income** column using the mean of the column.

### 5. Checked Duplicate Records

Identified duplicate rows using `duplicated()`.

### 6. Removed Duplicate Records

Removed duplicate rows using `drop_duplicates()`.

### 7. Standardized Column Names

Converted all column names to lowercase for better consistency.

### 8. Converted Date Column

Converted the `dt_customer` column from text format to datetime format.

### 9. Verified Data Types

Checked all column data types after cleaning.

### 10. Exported the Cleaned Dataset

Saved the cleaned dataset as:

`cleaned_marketing_campaign.csv`

## Output Files

* `marketing_campaign.csv`
* `cleaned_marketing_campaign.csv`
* `data_cleaning.py`

## Conclusion

The dataset was successfully cleaned and prepared for further analysis. Missing values were handled, duplicate records were checked and removed, column names were standardized, and the date column was converted into the correct format. The cleaned dataset is now ready for data analysis and visualization.
