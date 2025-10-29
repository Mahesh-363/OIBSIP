# 🌸 Iris Flower Prediction with Visualization
# Author: Vommi Uma Mahesh

# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Step 2: Load dataset
iris_data = pd.read_csv("Iris.csv")
print("✅ Dataset Loaded Successfully!\n")

# Step 3: Data overview
if "Id" in iris_data.columns:
    iris_data.drop(columns="Id", inplace=True)
print("🔍 Data Preview:\n", iris_data.head())

# Step 4: Visualization 1 - Species count
plt.figure(figsize=(6, 4))
sns.countplot(data=iris_data, x="Species", hue="Species", legend=False, palette="cool")
plt.title("Count of Each Iris Species 🌸")
plt.xlabel("Flower Species")
plt.ylabel("Count")
plt.savefig("species_count.png")
plt.close()

# Step 5: Visualization 2 - Pairplot
sns.pairplot(iris_data, hue="Species", palette="husl")
plt.suptitle("Feature Relationships Between Iris Species", y=1.02)
plt.savefig("pairplot.png")
plt.close()

# Step 6: Visualization 3 - Correlation heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(iris_data.drop(columns="Species").corr(), annot=True, cmap="YlGnBu", fmt=".2f")
plt.title("Feature Correlation Heatmap 🌼")
plt.savefig("heatmap.png")
plt.close()

# Step 7: Split data into features and labels
flower_features = iris_data.drop(columns="Species")
flower_labels = iris_data["Species"]

train_features, test_features, train_labels, test_labels = train_test_split(
    flower_features, flower_labels, test_size=0.2, random_state=12
)

# Step 8: Train the model
iris_classifier = RandomForestClassifier(n_estimators=120, random_state=12)
iris_classifier.fit(train_features, train_labels)

# Step 9: Evaluate model
predicted_labels = iris_classifier.predict(test_features)
model_accuracy = accuracy_score(test_labels, predicted_labels) * 100

print("\n🎯 Model Performance:")
print(f"Accuracy: {model_accuracy:.2f}%")
print("\n📊 Classification Report:\n", classification_report(test_labels, predicted_labels))

# Step 10: Test with a new sample flower
sample_flower = pd.DataFrame([[5.8, 2.8, 5.1, 2.4]], columns=flower_features.columns)
predicted_species = iris_classifier.predict(sample_flower)
print("\n🌺 Predicted Species for the sample flower:", predicted_species[0])

print("\n📁 All visualizations have been saved as images in your current folder.")
