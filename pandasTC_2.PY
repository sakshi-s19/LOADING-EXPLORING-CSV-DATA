import pandas as pd

# Load CSV file
data = pd.read_csv("covid_data.csv")

# Display dataset information
print("Dataset Information:")
data.info()

# Display statistical summary
print("\nStatistical Summary:")
print(data.describe())