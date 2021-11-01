import pandas as pd

pima = pd.read_csv('../data/pima2.csv')
for col in ['glucose', 'pressure', 'triceps', 'insulin', 'mass', 'pedigree']:
    print('#' * 10 + 'diabetes:' + col + ':mean')
    data = pima.groupby('diabetes').describe()[col]
    print(data['mean'])
    print('#' * 10 + 'diabetes:' + col + ':std')
    print(data['std'])


def classify(pregnant):
    if pregnant <= 5:
        return '0~5'
    elif 6 <= pregnant <= 10:
        return '6~10'
    else:
        return '10+'


pima['pregnant'] = pima['pregnant'].apply(classify)
for col in ['glucose', 'pressure', 'triceps', 'insulin', 'mass', 'pedigree']:
    print('#' * 10 + 'pregnant:' + col+':mean')
    data = pima.groupby('pregnant').describe()[col]
    print(data['mean'])
    print('#' * 10 + 'pregnant:' + col+':std')
    print(data['std'])
