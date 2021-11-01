import pandas as pd
import matplotlib.pyplot as plt

pima = pd.read_csv('../data/pima2.csv')


def classify(pregnant):
    if pregnant <= 5:
        return '0~5'
    elif 6 <= pregnant <= 10:
        return '6~10'
    else:
        return '10+'


pima['pregnant'] = pima['pregnant'].apply(classify)
table = pd.crosstab(index=pima['pregnant'], columns=pima['diabetes'])
print(table)
table.plot.bar(stacked=True)
plt.show()
