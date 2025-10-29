# 🧩 Unemployment Analysis with Python
# Author: Vommi Uma Mahesh
# Internship: Oasis Infobyte | Data Science
# Description: Analyze how COVID-19 lockdown impacted unemployment in India.

# 🧩 Unemployment Analysis with Python
# Author: Vommi Uma Mahesh

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Step 1: Load the dataset
data = pd.read_csv("Unemployment in India.csv")
data.columns = data.columns.str.strip()  # 🔧 remove unwanted spaces from column names
print("✅ Data Loaded Successfully!\n")

# Step 2: Basic information
print("🔍 Dataset Overview:")
print(data.head(), "\n")
print("Columns:", data.columns, "\n")

# Step 3: Data cleaning
data = data.dropna()
data["Date"] = pd.to_datetime(data["Date"], dayfirst=True)

data.rename(columns={
    "Region": "State",
    "Estimated Unemployment Rate (%)": "Unemployment_Rate",
    "Estimated Employed": "Employed_Population",
    "Estimated Labour Participation Rate (%)": "Labour_Participation"
}, inplace=True)

# Step 4: Summary statistics
print("📈 Summary Statistics:\n", data.describe(), "\n")
print("Unique States:", data["State"].nunique())

# Step 5: Line plot – Unemployment rate over time
plt.figure(figsize=(12, 6))
sns.lineplot(data=data, x="Date", y="Unemployment_Rate", hue="State", legend=False)
plt.title("Unemployment Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.tight_layout()
plt.savefig("unemployment_trend.png")
plt.close()

# Step 6: Bar plot – Average unemployment by state
state_avg = data.groupby("State")["Unemployment_Rate"].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 7))
sns.barplot(x=state_avg.values, y=state_avg.index, palette="coolwarm")
plt.title("Average Unemployment Rate by State")
plt.xlabel("Average Unemployment Rate (%)")
plt.ylabel("State")
plt.tight_layout()
plt.savefig("statewise_bar.png")
plt.close()

# Step 7: Heatmap – Correlation
plt.figure(figsize=(6, 4))
sns.heatmap(data[["Unemployment_Rate", "Employed_Population", "Labour_Participation"]].corr(),
            annot=True, cmap="YlGnBu")
plt.title("Correlation Between Employment Factors")
plt.tight_layout()
plt.savefig("unemployment_heatmap.png")
plt.close()

# Step 8: Optional Interactive Map (requires plotly)
fig = px.choropleth(
    data,
    locations="State",
    locationmode="country names",
    color="Unemployment_Rate",
    hover_name="State",
    animation_frame=data["Date"].dt.strftime("%b %Y"),
    title="Unemployment Rate in India (During COVID-19)",
    color_continuous_scale="Reds"
)
fig.write_html("unemployment_map.html")

# Step 9: Print insights
highest = data.loc[data["Unemployment_Rate"].idxmax()]
lowest = data.loc[data["Unemployment_Rate"].idxmin()]

print("💡 Insights:")
print(f"Highest Unemployment: {highest['Unemployment_Rate']:.2f}% in {highest['State']} ({highest['Date'].strftime('%b %Y')})")
print(f"Lowest Unemployment: {lowest['Unemployment_Rate']:.2f}% in {lowest['State']} ({lowest['Date'].strftime('%b %Y')})")

print("\n📊 Visualizations saved: unemployment_trend.png, statewise_bar.png, unemployment_heatmap.png")
print("🌐 Interactive map saved: unemployment_map.html")
