import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = np.random.randint(5000, 15000, 12)
profit = np.random.randint(1000, 5000, 12)
df = pd.DataFrame({
    "Month": months,
    "Sales": sales,
    "Profit": profit
})
total_sales = sales.sum()
total_profit = profit.sum()
avg_sales = int(sales.mean())
print("=" * 50)
print("INTERACTIVE EXECUTIVE DASHBOARD")
print("=" * 50)
print(f"Total Sales      : ${total_sales:,}")
print(f"Total Profit     : ${total_profit:,}")
print(f"Average Sales    : ${avg_sales:,}")
print("=" * 50)
print("\nMonthly Performance Data:")
print(df)
plt.figure(figsize=(10, 5))
plt.plot(months, sales, marker='o', label='Sales')
plt.plot(months, profit, marker='s', label='Profit')
plt.title("Sales and Profit Trends")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.legend()
plt.grid(True)
plt.show()
departments = ["Marketing", "Sales", "Finance", "HR", "Operations"]
performance = [85, 92, 78, 70, 88]
plt.figure(figsize=(8, 5))
plt.bar(departments, performance)
plt.title("Department Performance")
plt.xlabel("Department")
plt.ylabel("Performance (%)")
plt.show()
regions = ["North", "South", "East", "West"]
revenue = [120000, 95000, 110000, 105000]
plt.figure(figsize=(8, 5))
plt.pie(revenue, labels=regions, autopct='%1.1f%%')
plt.title("Regional Revenue Distribution")
plt.show()
print("\nDashboard Analysis Completed Successfully!")