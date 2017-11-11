import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

columns_to_use = ["Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
titanic = pd.read_csv('../csvs/train.csv', usecols=columns_to_use).dropna()
# print(titanic.head(3))

# sns.distplot(titanic["Age"])
# sns.kdeplot(titanic["Age"], shade=True)
# sns.set_style("white")
# sns.despine(top=True, bottom=True, left=True, right=True)
# plt.xlabel("Age")
# plt.show()

print(titanic.columns.values)
g = sns.FacetGrid(titanic, col="Survived", row="Pclass", hue="Sex", size=3)
g.map(sns.kdeplot, "Age", shade=True).add_legend()
sns.despine(bottom=True, left=True)
plt.show()
