import pandas as pd
import matplotlib.pyplot as plt

pima = pd.read_csv('../data/pima2.csv')

describe = pima.groupby('diabetes')['Unnamed: 0'].describe()
describe['rate'] = pima.groupby('diabetes')['age'].describe()['count'] / sum(
    pima.groupby('diabetes')['age'].describe()['count']) * 100

print(describe)

plt.bar(describe.index, describe['count'])
plt.show()
plt.pie(describe['count'], labels=describe.index)
plt.show()
