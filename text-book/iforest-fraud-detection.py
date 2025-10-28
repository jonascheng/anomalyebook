# Import necessary modules
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
import shap

# Load the dataset
data = pd.read_csv('InsFraudDataset6.csv')

# Train Isolation Forest
model = IsolationForest(contamination=0.25, random_state=42)
model.fit(data)

# Predict anomaly scores
anomaly_scores = model.decision_function(data)
predictions = model.predict(data)

# Add predictions to DataFrame
# df = pd.DataFrame(data, columns=[f"Feature_{i}" for i in range(data.shape[1])])
df = data.copy()
df['Anomaly_Score'] = anomaly_scores
df['Prediction'] = predictions

# Display the DataFrame with anomaly scores
print(df)

# Explain the anomalies using SHAP library
explainer = shap.Explainer(model.predict, data)
shap_values = explainer(data)
# Visualizing SHAP Values for the First Data Point
shap.plots.waterfall(shap_values[0])
# Printing Anomalies and Their SHAP Values
for i in range(len(data)):
    if predictions[i] == -1:
        print(f"Anomaly detected in data point {i}: {data.iloc[i]}")
        shap.plots.waterfall(shap_values[i])
