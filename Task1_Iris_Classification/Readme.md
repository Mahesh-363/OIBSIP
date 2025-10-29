🌼 Iris Flower Classification using Machine Learning
👨‍💻 Project by: Vommi Uma Mahesh

Internship: AICTE Oasis Infobyte (OIBSIP) — Data Science Internship
Task: Iris Flower Classification

📖 Project Overview

The Iris Flower Classification project is a classic beginner-level machine learning problem.
The goal is to build a model that can predict the species of an Iris flower based on its physical measurements:

Sepal Length

Sepal Width

Petal Length

Petal Width

The dataset used for this task contains details of three flower species:
🌸 Iris Setosa 🌼 Iris Versicolor 🌺 Iris Virginica

This project demonstrates how to go from data understanding → visualization → model training → prediction, in one complete pipeline.

🎯 Objective

To train a machine learning classifier that learns from flower measurements and predicts the species accurately.

⚙️ Tools & Libraries Used

Python

Pandas → Data analysis and manipulation

Matplotlib & Seaborn → Data visualization

Scikit-learn → Machine learning algorithms

Install them easily with:

pip install pandas matplotlib seaborn scikit-learn

🧠 Steps Followed
🪴 Step 1: Import Libraries

Imported Python libraries for handling data, visualizations, and training models.

🪴 Step 2: Load Dataset

Loaded the Iris.csv dataset and viewed its structure using Pandas.

🪴 Step 3: Visualize the Dataset

Created three different plots to understand data patterns:

Count of each Iris species

Pairplot showing feature relationships

Correlation heatmap showing numeric relationships

🪴 Step 4: Data Preparation

Separated input columns (measurements) and output column (species):

flower_features = iris_data.drop(columns="Species")
flower_labels = iris_data["Species"]

🪴 Step 5: Train-Test Split

Divided the dataset into training and testing data:

train_features, test_features, train_labels, test_labels = train_test_split(
    flower_features, flower_labels, test_size=0.2, random_state=12
)

🪴 Step 6: Model Training

Used the Random Forest Classifier to train the model:

iris_classifier = RandomForestClassifier(n_estimators=120, random_state=12)
iris_classifier.fit(train_features, train_labels)

🪴 Step 7: Evaluation

Measured model accuracy and performance using:

accuracy_score(test_labels, predicted_labels)
classification_report(test_labels, predicted_labels)

🪴 Step 8: Make a Prediction

Tested with a new flower’s measurements:

sample_flower = pd.DataFrame([[5.8, 2.8, 5.1, 2.4]], columns=flower_features.columns)
predicted_species = iris_classifier.predict(sample_flower)


Output Example:

🌺 Predicted Species for the sample flower: Iris-virginica

📊 Visualizations
1️⃣ Species Count

Shows the number of samples per species.


2️⃣ Feature Relationships

Pairplot displaying how petal and sepal dimensions differ across species.


3️⃣ Correlation Heatmap

Shows the relationship between numeric features.


📈 Results
Metric	Score
Accuracy	100%
Precision	1.00
Recall	1.00

✅ The model accurately predicts the species of flowers based on their measurements.

🧩 Folder Structure
OIBSIP/
│
├── iris_flower_predictor.py
├── Iris.csv
├── species_count.png
├── pairplot.png
├── heatmap.png
└── README.md

💡 Key Learnings

Through this project, I learned how to:

Load and explore datasets using Pandas

Visualize data relationships using Seaborn

Split data into training and testing sets

Train and evaluate a classification model

Make predictions using a trained machine learning model

🚀 Future Improvements

Experiment with other algorithms like SVM, KNN, or Logistic Regression

Create a simple web app using Streamlit for real-time predictions

Deploy the model using AWS, Flask, or Render

🧾 Acknowledgment

This project is part of the AICTE Oasis Infobyte Data Science Internship Program (OIBSIP).
A big thanks to the Oasis Infobyte team for giving me this practical learning opportunity and helping me gain hands-on experience in Machine Learning.

⭐ If you liked this project, please give it a star on GitHub!
