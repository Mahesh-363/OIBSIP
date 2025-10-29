# 🚗 Car Price Prediction using Machine Learning
# Author: Vommi Uma Mahesh
# Internship: Oasis Infobyte | Data Science
# Dataset: car data.csv

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error
from tabulate import tabulate  # ✅ For neat table display

# Step 1: Load dataset
car_dataset = pd.read_csv("car data.csv")
print("✅ Dataset Loaded Successfully!\n")

# Step 2: Explore the dataset (in clean tabular format)
print("🔍 Sample Data (First 5 Rows):\n")
print(tabulate(car_dataset.head(), headers='keys', tablefmt='fancy_grid'))
print("\n📏 Dataset Shape:", car_dataset.shape)
print("🧩 Columns:", list(car_dataset.columns), "\n")

# Step 3: Handle missing values if any
car_dataset = car_dataset.dropna()

# Step 4: Encode categorical columns
text_columns = car_dataset.select_dtypes(include=['object']).columns
for column in text_columns:
    car_dataset[column] = car_dataset[column].astype('category').cat.codes

# Step 5: Split features and target
feature_data = car_dataset.drop(["Selling_Price"], axis=1)
target_price = car_dataset["Selling_Price"]

# Step 6: Split into train and test sets
train_features, test_features, train_labels, test_labels = train_test_split(
    feature_data, target_price, test_size=0.2, random_state=42
)
print(f"🧠 Training Samples: {train_features.shape}, Testing Samples: {test_features.shape}\n")

# Step 7: Train Random Forest model
price_predictor = RandomForestRegressor(n_estimators=100, random_state=42)
price_predictor.fit(train_features, train_labels)
print("🎯 Model Training Completed!\n")

# Step 8: Make predictions
predicted_prices = price_predictor.predict(test_features)

# Step 9: Evaluate model performance
r2 = r2_score(test_labels, predicted_prices)
mae = mean_absolute_error(test_labels, predicted_prices)
print("📊 Model Evaluation Results:")
print(f"🔹 R² Score: {r2:.3f}")
print(f"🔹 Mean Absolute Error: {mae:.3f}\n")

# Step 10: Plot Actual vs Predicted Prices
plt.figure(figsize=(7, 5))
sns.scatterplot(x=test_labels, y=predicted_prices)
plt.xlabel("Actual Selling Price (₹ Lakh)")
plt.ylabel("Predicted Selling Price (₹ Lakh)")
plt.title("Actual vs Predicted Car Prices")
plt.tight_layout()
plt.savefig("car_price_comparison.png")
plt.close()

# Step 11: Plot Feature Importance
importance_values = pd.Series(price_predictor.feature_importances_, index=feature_data.columns)
importance_values.nlargest(8).plot(kind='barh', color='teal')
plt.title("Top 8 Factors Influencing Car Prices")
plt.tight_layout()
plt.savefig("feature_importance_chart.png")
plt.close()

print("📈 Visualizations saved: car_price_comparison.png, feature_importance_chart.png")
