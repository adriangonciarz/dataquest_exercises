import pandas as pd
import matplotlib.pyplot as plt
from numpy import arange

reviews = pd.read_csv("../csvs/fandango_score_comparison.csv")
norm_reviews = reviews[
    ["FILM", "RT_user_norm", "Metacritic_user_nom", "IMDB_norm", "Fandango_Ratingvalue", "Fandango_Stars"]]
print(norm_reviews.head(1))
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
bar_heights = norm_reviews[num_cols].iloc[0].values
bar_positions = arange(5) + 0.75
tick_positions = range(1, 6)

# fig, ax = plt.subplots()
# ax.bar(bar_positions, bar_heights, 0.5)
# ax.set_xticks(tick_positions)
# ax.set_xticklabels(num_cols,rotation=90)
# plt.xlabel("Rating Source")
# plt.ylabel("Average Rating")
# plt.title("Average User Rating For Avengers: Age of Ultron (2015)")
# plt.show()

# fig, ax = plt.subplots()
# ax.barh(bar_positions, bar_heights, 0.5)
# ax.set_yticks(tick_positions)
# ax.set_yticklabels(num_cols)
# plt.ylabel("Rating Source")
# plt.xlabel("Average Rating")
# plt.title("Average User Rating For Avengers: Age of Ultron (2015)")
# plt.show()

# fig, ax = plt.subplots()
# ax.scatter(reviews["Fandango_Ratingvalue"], reviews["RT_user_norm"])
# plt.ylabel("Rotten Tomatoes")
# plt.xlabel("Fandango")
# plt.show()

fig = plt.figure(figsize=(5, 10))
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)
ax1.scatter(reviews["Fandango_Ratingvalue"], reviews["RT_user_norm"])
ax1.set_xlabel("Fandango")
ax1.set_ylabel("Rotten Tomatoes")
ax1.set_xlim(0,5)
ax1.set_ylim(0,5)
ax2.scatter(reviews["Fandango_Ratingvalue"], reviews["Metacritic_user_nom"])
ax2.set_xlabel("Fandango")
ax2.set_ylabel("Metacritic")
ax2.set_xlim(0,5)
ax2.set_ylim(0,5)
ax3.scatter(reviews["Fandango_Ratingvalue"], reviews["IMDB_norm"])
ax3.set_xlabel("Fandango")
ax3.set_ylabel("IMDB")
ax3.set_xlim(0,5)
ax3.set_ylim(0,5)
plt.show()