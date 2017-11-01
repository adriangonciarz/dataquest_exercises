import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('../csvs/percent-bachelors-degrees-women-usa.csv')
# fig, ax = plt.subplots()
# ax.plot(women_degrees["Year"], women_degrees["Biology"],'blue', label="Women")
# ax.plot(women_degrees["Year"], 100-women_degrees["Biology"], 'green', label="Men")
# ax.tick_params(bottom="off", top="off", left="off", right="off")
# ax.spines["left"].set_visible(False)
# ax.spines["right"].set_visible(False)
# ax.spines["top"].set_visible(False)
# ax.spines["bottom"].set_visible(False)
# ax.set_title("Percentage of Biology Degrees Awarded By Gender")
# ax.legend(loc='upper right')
# plt.show()


stem_cats = ['Engineering', 'Computer Science', 'Psychology', 'Biology', 'Physical Sciences', 'Math and Statistics']
fig = plt.figure(figsize=(18, 3))
cb_dark_blue = (0/255,107/255,164/255)
cb_orange = (255/255,128/255,14/255)

for sp in range(0,6):
    ax = fig.add_subplot(1,6,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[sp]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100 - women_degrees[stem_cats[sp]], c=cb_orange, label='Men', linewidth=3)
    ax.set_xlim(1986,2011)
    ax.set_ylim(0,100)
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_title(stem_cats[sp])
    if sp == 0:
        ax.text(2005, 87, "Men")
        ax.text(2002, 8, "Women")
    if sp == 5:
        ax.text(2005, 62, "Men")
        ax.text(2001, 35, "Women")

plt.show()
