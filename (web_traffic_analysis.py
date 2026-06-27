import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("web_traffic.csv")

print("First 5 Records")
print(df.head())

print("\nDataset Info")
print(df.info())

print("\nSummary Statistics")
print(df.describe())

# Total Page Views
print("\nTotal Page Views:", df["PageViews"].sum())

# Average Session Duration
print("Average Session Duration:", df["SessionDuration"].mean())

# Bounce Rate
print("Average Bounce Rate:", df["BounceRate"].mean())

# Traffic Sources
print("\nTraffic Sources")
print(df["TrafficSource"].value_counts())

# Page Views Chart
plt.figure(figsize=(8,5))
plt.bar(df["Page"], df["PageViews"])
plt.title("Page Views")
plt.xlabel("Pages")
plt.ylabel("Views")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Session Duration
plt.figure(figsize=(8,5))
plt.plot(df["Page"], df["SessionDuration"], marker="o")
plt.title("Session Duration")
plt.xlabel("Pages")
plt.ylabel("Minutes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
