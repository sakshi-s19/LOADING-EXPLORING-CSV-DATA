import pandas as pd

# Load CSV file
data = pd.read_csv("covid_data.csv")

# Display first 5 records
print("First 5 Records:")
print(data.head())