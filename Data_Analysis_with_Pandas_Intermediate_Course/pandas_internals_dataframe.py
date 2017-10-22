import pandas as pd
import numpy as np

fandango = pd.read_csv("../csvs/fandango_score_comparison.csv")
# print(fandango.head(2))
# print(fandango.index.values)
last_row_idx = len(fandango.index) - 1
first_last = fandango.iloc[[0, last_row_idx]]

fandango_films = fandango.set_index("FILM", drop=False)
# print(fandango_films.index.values)

best_movies_ever = fandango_films.loc[
    ["The Lazarus Effect (2015)", "Gett: The Trial of Viviane Amsalem (2015)", "Mr. Holmes (2015)"]]

types = fandango_films.dtypes
float_columns = types[types.values == 'float64'].index
float_df = fandango_films[float_columns]
percentiles = float_df.apply(lambda x: np.average(x))
# print(percentiles)

double_df = float_df.apply(lambda x: x * 2)
halved_df = float_df.apply(lambda x: x / 2)
# print(halved_df.head(1))

rt_mt_user = float_df[['RT_user_norm', 'Metacritic_user_nom']]
rt_mt_deviations = rt_mt_user.apply(lambda x: np.std(x), axis=1)
print(rt_mt_deviations[0:5])
rt_mt_means = rt_mt_user.apply(lambda x: np.mean(x), axis=1)
rt_mt_means.sort_values(inplace=True, ascending=False)
print(rt_mt_means[0:5])
