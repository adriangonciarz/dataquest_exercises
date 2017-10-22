import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv("../csvs/unrate.csv")
unrate["DATE"] = pd.to_datetime(unrate["DATE"])
print(unrate.head(12))

plt.plot(unrate["DATE"].head(12), unrate["VALUE"].head(12))
plt.xticks(rotation=90)
plt.xlabel("Month")
plt.ylabel("Unemployment Rate")
plt.title("Monthly Unemployment Trends, 1948")
plt.show()
