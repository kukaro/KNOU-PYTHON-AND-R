import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pima = pd.read_csv('../data/pima2.csv')

describe = pima.groupby('diabetes').describe()

for col in ['glucose', 'pressure', 'triceps', 'insulin', 'mass', 'pedigree', 'age']:
    print('#' * 10 + ' ' + col)
    print(describe[col])
    sns.set(style='whitegrid')
    sns.boxplot(x='diabetes', y=col, data=pima)
    plt.gca().set(title='%s\'s boxplot' % (col))
    plt.show()
    pos_total = pima.loc[pima.diabetes == 'pos'][col]
    neg_total = pima.loc[pima.diabetes == 'neg'][col]
    args = dict(alpha=0.5, bins=10)
    plt.hist(pos_total, **args, color='b', label='pos')
    plt.hist(neg_total, **args, color='r', label='neg')
    plt.gca().set(title='%s\'s histogram' % (col))
    plt.legend()
    plt.show()
