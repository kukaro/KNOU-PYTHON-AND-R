import pandas as pd

pima = pd.read_csv('../data/pima2.csv')
for col in ['glucose', 'pressure', 'triceps', 'insulin', 'mass', 'pedigree']:
    print('#' * 10 + ' diabetes : ' + col)
    print(pima.groupby('diabetes').describe()[col])


def classify(pregnant):
    if pregnant <= 5:
        return '0~5'
    elif 6 <= pregnant <= 10:
        return '6~10'
    else:
        return '10+'


pima['pregnant'] = pima['pregnant'].apply(classify)
for col in ['glucose', 'pressure', 'triceps', 'insulin', 'mass', 'pedigree']:
    print('#' * 10 + 'pregnant :' + col)
    print(pima.groupby('pregnant').describe()[col])
