import pandas as pd

all_ages = pd.read_csv("../csvs/all-ages.csv")
recent_grads = pd.read_csv("../csvs/recent-grads.csv")
print(all_ages.head(5))
print(recent_grads.head(5))
aa_cats = all_ages["Major_category"].unique()
rg_cats = recent_grads["Major_category"].unique()


def count_cats(categories, table):
    cats_dict = dict()
    for c in categories:
        filtered = table[table["Major_category"] == c]
        cats_dict[c] = filtered["Total"].sum()
    return cats_dict


aa_cat_counts = count_cats(aa_cats, all_ages)
rg_cat_counts = count_cats(rg_cats, recent_grads)

low_wage_proportion = float(recent_grads["Low_wage_jobs"].sum() / recent_grads["Total"].sum())
print(low_wage_proportion)

# 5/6
majors = recent_grads['Major'].unique()
rg_lower_count = 0
for m in majors:
    aa_major_row = all_ages[all_ages["Major"] == m]
    rg_major_row = recent_grads[recent_grads["Major"] == m]
    aa_unemp_rate = aa_major_row["Unemployment_rate"].sum()
    rg_unemp_rate = rg_major_row["Unemployment_rate"].sum()
    if rg_unemp_rate < aa_unemp_rate:
        rg_lower_count += 1
print(rg_lower_count)
