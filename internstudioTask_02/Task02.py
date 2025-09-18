import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = "vgsales.csv"
df = pd.read_csv(file_path)

# Show basic info and first few rows
df_head = df.head()

df_shape = df.shape
df_columns = df.columns.tolist()

# 1. Top 10 Games by Global Sales
top10_games = df.nlargest(10, "Global_Sales")

plt.figure(figsize=(10, 6))
plt.bar(top10_games["Name"], top10_games["Global_Sales"], color="lightblue")
plt.xticks(rotation=75)
plt.title("Top 10 Games by Global Sales")
plt.xlabel("Game")
plt.ylabel("Global Sales (millions)")
plt.tight_layout()
plt.show()

# 2. Sales by Genre
genre_sales = df.groupby("Genre")["Global_Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
plt.bar(genre_sales.index, genre_sales.values, color="orange")
plt.xticks(rotation=45)
plt.title("Global Sales by Genre")
plt.xlabel("Genre")
plt.ylabel("Global Sales (millions)")
plt.tight_layout()
plt.show()

# 3. Sales by Platform (Top 10 Platforms)
platform_sales = df.groupby("Platform")["Global_Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
plt.bar(platform_sales.index, platform_sales.values, color="green")
plt.title("Top 10 Platforms by Global Sales")
plt.xlabel("Platform")
plt.ylabel("Global Sales (millions)")
plt.tight_layout()
plt.show()

# 4. Sales Trend by Year
year_sales = df.groupby("Year")["Global_Sales"].sum()

plt.figure(figsize=(12, 6))
plt.plot(year_sales.index, year_sales.values, marker="o", linestyle="-", color="red")
plt.title("Global Sales Trend by Year")
plt.xlabel("Year")
plt.ylabel("Global Sales (millions)")
plt.grid(True)
plt.tight_layout()
plt.show()
