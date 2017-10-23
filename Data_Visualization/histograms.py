import pandas as pd
import matplotlib.pyplot as plt
from numpy import arange

reviews = pd.read_csv("../csvs/fandango_score_comparison.csv")
# fandango_distribution = reviews["Fandango_Ratingvalue"].value_counts().sort_index()
# imdb_distribution = reviews["IMDB_norm"].value_counts().sort_index()
# print(fandango_distribution)
# print(imdb_distribution)
#
# fig, ax = plt.subplots()
# ax.hist(reviews['Fandango_Ratingvalue'], range=(0, 5))
# plt.show()

#
# fig = plt.figure(figsize=(5,20))
# ax1 = fig.add_subplot(4,1,1)
# ax2 = fig.add_subplot(4,1,2)
# ax3 = fig.add_subplot(4,1,3)
# ax4 = fig.add_subplot(4,1,4)
# ax1.hist(reviews["Fandango_Ratingvalue"],bins=20, range=(0,5))
# ax1.set_title("Distribution of Fandango Ratings")
# ax1.set_ylim(0,50)
# ax2.hist(reviews["RT_user_norm"],bins=20, range=(0,5))
# ax2.set_title("Distribution of Rotten Tomatoes Ratings")
# ax2.set_ylim(0,50)
# ax3.hist(reviews["Metacritic_user_nom"],bins=20, range=(0,5))
# ax3.set_title("Distribution of Metacritic Ratings")
# ax3.set_ylim(0,50)
# ax4.hist(reviews["IMDB_norm"],bins=20, range=(0,5))
# ax4.set_title("Distribution of IMDB Ratings")
# ax4.set_ylim(0,50)
# plt.show()

num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']
fig, ax = plt.subplots()
ax.boxplot(reviews[num_cols].values)
ax.set_ylim(0,5)
ax.set_xticklabels(num_cols, rotation=90)
plt.show()