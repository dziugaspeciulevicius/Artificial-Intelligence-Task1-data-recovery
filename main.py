import pandas as pd
from io import StringIO

df = pd.read_csv('data.csv')

print('\n ORIGINAL DATA: ')
print(df)

print('\n SORTED DATA BY WEIGHT: ')
print(df.sort_values('Weight', ascending=True))

print('\n')
print('Weight arithmetic mean: ')
print('Weight median: ')
