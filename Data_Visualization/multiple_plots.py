import matplotlib.pyplot as plt
import pandas as pd

unrate = pd.read_csv("../csvs/unrate.csv")
unrate["DATE"] = pd.to_datetime(unrate["DATE"])

# fig = plt.figure(figsize=(12,12))
# ax48 = fig.add_subplot(5, 1, 1)
# ax49 = fig.add_subplot(5, 1, 2)
# ax50 = fig.add_subplot(5, 1, 3)
# ax51 = fig.add_subplot(5, 1, 4)
# ax52 = fig.add_subplot(5, 1, 5)
# ax48.plot(unrate[0:12]["DATE"], unrate[0:12]["VALUE"])
# ax49.plot(unrate[12:24]["DATE"], unrate[12:24]["VALUE"])
# ax50.plot(unrate[24:36]["DATE"], unrate[24:36]["VALUE"])
# ax51.plot(unrate[36:48]["DATE"], unrate[36:48]["VALUE"])
# ax52.plot(unrate[48:64]["DATE"], unrate[48:64]["VALUE"])
# plt.show()

# fig = plt.figure(figsize=(12,12))
# for i in range(5):
#     ax = fig.add_subplot(5,1,i+1)
#     start_index = i*12
#     end_index = (i+1)*12
#     subset = unrate[start_index:end_index]
#     ax.plot(subset['DATE'], subset['VALUE'])
# plt.show()

unrate["MONTH"] = unrate["DATE"].dt.month
# fig = plt.figure(figsize=(6,3))
# plt.plot(unrate[0:12]["MONTH"], unrate[0:12]["VALUE"], c="red")
# plt.plot(unrate[12:24]["MONTH"], unrate[12:24]["VALUE"], c="blue")
# plt.show()

fig = plt.figure(figsize=(10,6))
year_color = {
    0: "red",
    1: "blue",
    2: "green",
    3: "orange",
    4: "black"
}
for i in range(5):
    start = i*12
    end = (i+1)*12
    year = str(1948+i)
    subset = unrate[start:end]
    plt.plot(subset["MONTH"], subset["VALUE"], c=year_color[i], label=year)
plt.legend(loc='upper left')
plt.title("Monthly Unemployment Trends, 1948-1952")
plt.xlabel("Month, Integer")
plt.ylabel("Unemployment Rate, Percent")
plt.show()