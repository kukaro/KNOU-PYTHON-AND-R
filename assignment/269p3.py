import pandas as pd
import matplotlib.pyplot as plt

diabetes = pd.read_csv('../data/pima2.csv')
result = {}

for col in diabetes.columns:
    freq_table = pd.crosstab(index=diabetes[col], colnames=[col.upper()], columns='count')
    # 비율은 백분율입니다.
    freq_table['rate'] = freq_table / sum(freq_table['count']) * 100
    result[col] = freq_table

for _, col_value in result.items():
    plt.bar(col_value.index, col_value['count'])
    plt.show()
