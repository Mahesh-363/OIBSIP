📘 README.md — Car Price Prediction
# 🚗 Car Price Prediction — Oasis Infobyte Internship (Task 3)

## 📄 Overview
The **Car Price Prediction** project uses **machine learning** to estimate the selling price of a car based on its key features such as brand, year, mileage, fuel type, and ownership details.  
This helps sellers and buyers determine a car’s fair market value accurately.

---

### 📊 About the Dataset
**Source:** Provided by Oasis Infobyte  
**File:** `car data.csv`  

The dataset contains historical data of used cars and includes the following columns:

| Column Name | Description |
|--------------|-------------|
| Car_Name | Model of the car |
| Year | Year of manufacture |
| Selling_Price | Price at which the car is being sold (target) |
| Present_Price | Current ex-showroom price (in lakhs) |
| Driven_kms | Distance driven by the car |
| Fuel_Type | Type of fuel used (Petrol/Diesel/CNG) |
| Selling_type | Type of seller (Dealer/Individual) |
| Transmission | Type of gearbox (Manual/Automatic) |
| Owner | Number of previous owners |

---

### 🧠 Workflow
1. **Import Libraries:** pandas, seaborn, matplotlib, scikit-learn, tabulate  
2. **Load Dataset:** Reads `car data.csv` and displays the first few rows in a clean table format  
3. **Data Preprocessing:**
   - Handle missing values  
   - Convert categorical variables into numeric form  
4. **Feature & Target Split:**
   - Features → All columns except `Selling_Price`  
   - Target → `Selling_Price`  
5. **Train-Test Split:** 80% training, 20% testing  
6. **Model Building:** Random Forest Regressor  
7. **Evaluation Metrics:**  
   - R² Score  
   - Mean Absolute Error (MAE)  
8. **Visualization:**
   - Actual vs Predicted Price  
   - Feature Importance Chart  

---

### 💻 Model Used
- **Algorithm:** Random Forest Regressor  
- **Reason:** High accuracy, handles non-linear relationships, works well with small datasets  

---

### 📈 Results
| Metric | Value |
|---------|--------|
| R² Score | 0.966 |
| Mean Absolute Error | 0.589 |

**Interpretation:**  
✅ The model predicts car prices with 96.6% accuracy, and an average error of ₹0.59 lakh — highly reliable performance.

---

### 🖼️ Visual Outputs
1. **car_price_comparison.png** → Actual vs Predicted Car Prices  
2. **feature_importance_chart.png** → Top 8 factors affecting car price  

---

### 🧩 Technologies Used
- Python 🐍  
- pandas  
- seaborn  
- matplotlib  
- scikit-learn  
- tabulate  

---

### 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Mahesh-363/OIBSIP.git
   cd OIBSIP/Task3_Car_Price_Prediction


Install required libraries:

pip install pandas numpy matplotlib seaborn scikit-learn tabulate


Run the script:

python car_price_prediction.py


View saved plots in the same folder.

✨ Author

Name: Vommi Uma Mahesh
Internship: Oasis Infobyte — Data Science Internship (October–November 2025)
GitHub: Mahesh-363
