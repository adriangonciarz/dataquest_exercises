import pandas as pd
from pandas import Series

fandango = pd.read_csv("../csvs/fandango_score_comparison.csv")
# print(fandango.head(2))
series_film = fandango["FILM"]
# print(series_film.head(5))
series_rt = fandango["RottenTomatoes"]
# print(series_film[5])
film_names = series_film.values
rt_scores = series_rt.values
series_custom = Series(data=rt_scores, index=film_names)
# print(series_custom.head(1))
fiveten = series_custom[5:11]
# print(fiveten)
original_index = series_custom.index
sorted_index = sorted(original_index)
sorted_by_index = series_custom.reindex(sorted_index)
# print(sorted_by_index[1:20])

sc2 = series_custom.sort_index()
sc3 = series_custom.sort_values()
# print(sc2.head(10))
# print(sc3.head(10))

series_normalized = series_custom / 20

criteria_one = series_custom > 50
criteria_two = series_custom < 75
both_criteria = series_custom[criteria_one & criteria_two]
# print(both_criteria.sort_values(ascending=False))

rt_critics = Series(fandango['RottenTomatoes'].values, index=fandango['FILM'])
rt_users = Series(fandango['RottenTomatoes_User'].values, index=fandango['FILM'])
rt_mean = (rt_users+rt_critics)/2
