# 1) Identifying outliers using Z-score method programmatically
import numpy as np
import pandas as pd

# Create the DataFrame
data = {
    'Invoice ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'Amount': [85, 88, 92, 91, 87, 90, 94, 95, 60, 89, 120, 450]
}
df = pd.DataFrame(data)

# Calculate the mean and standard deviation
mean = np.mean(df['Amount'])
std_dev = np.std(df['Amount'])

# Calculate the Z-score for each data point
df['Z-Score'] = (df['Amount'] - mean) / std_dev

# Define a threshold for identifying outliers
threshold = 3

# Identify outliers
df['Outlier'] = np.abs(df['Z-Score']) > threshold

# Display the results
print(df)

## 2) Identifying outliers using IQR method programmatically
import pandas as pd
# Create the DataFrame
data = {
    'Invoice ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'Amount': [85, 88, 92, 91, 87, 90, 94, 95, 60, 89, 120, 450]
}
df = pd.DataFrame(data)

# Calculate Q1 (25th percentile) and Q3 (75th percentile)
Q1 = df['Amount'].quantile(0.25)
Q3 = df['Amount'].quantile(0.75)

# Calculate the IQR
IQR = Q3 - Q1

# Define the lower and upper bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify outliers
df['Outlier'] = (df['Amount'] < lower_bound) | (df['Amount'] > upper_bound)

# Display the results
print(df)

## 3) Displaying outliers using the Box Plot
import pandas as pd
import matplotlib.pyplot as plt

# Create the DataFrame
data = {
    'Invoice ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'Amount': [85, 88, 92, 91, 87, 90, 94, 95, 60, 89, 120, 450]
}
df = pd.DataFrame(data)

# Calculate Q1 (25th percentile) and Q3 (75th percentile)
Q1 = df['Amount'].quantile(0.25)
Q3 = df['Amount'].quantile(0.75)

# Calculate the IQR
IQR = Q3 - Q1

# Define the lower and upper bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify outliers
df['Outlier'] = (df['Amount'] < lower_bound) | (df['Amount'] > upper_bound)

# Display the results
print(df)

# Plot the box plot
plt.figure(figsize=(10, 6))
plt.boxplot(df['Amount'], vert=False)
plt.xlabel('Amount')
plt.title('Box Plot of Invoice Amounts')
plt.show()

## 4) Identifying outliers using DBSCAN programmatically
import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN

# Create the DataFrame
data = {
    'Invoice ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'Amount': [85, 88, 92, 91, 87, 90, 94, 95, 60, 89, 120, 450, 89, 90, 93, 91, 87, 88, 86, 89]
}
df = pd.DataFrame(data)

# Reshape the 'Amount' column to be a 2D array
X = df['Amount'].values.reshape(-1, 1)

# Apply DBSCAN
dbscan = DBSCAN(eps=10, min_samples=3)
dbscan.fit(X)

# Add the DBSCAN labels to the DataFrame
df['DBSCAN_Label'] = dbscan.labels_

# Identify outliers (DBSCAN labels outliers as -1)
df['Outlier'] = df['DBSCAN_Label'] == -1

# Display the results
print(df)





