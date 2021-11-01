import pandas as pd
import matplotlib.pyplot as plt

pima = pd.read_csv('../data/pima2.csv')


def classify(age):
    if age <= 19:
        return '0~19'
    elif 20 <= age <= 30:
        return '20~30'
    elif 31 <= age <= 40:
        return '31~40'
    elif 41 <= age <= 50:
        return '41~50'
    else:
        return '50+'


pima['age'] = pima['age'].apply(classify)
table = pd.crosstab(index=pima['age'], columns=pima['diabetes'])
print(table)
table.plot.bar(stacked=True)
plt.show()
