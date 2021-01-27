import pandas as pd
import math
from io import StringIO

# read data file
df = pd.read_csv('data.csv')

# print original data
print('\n ORIGINAL DATA: ')
print(df.to_string(index=False))

# print entries with missing data
missing_data = df[pd.isnull(df["Height"])]
print('\n MISSING DATA: ')
print(missing_data.to_string(index=False))

# print sorted by weight data
print('\n SORTED DATA BY WEIGHT: ')
print(df.sort_values('Weight', ascending=True).to_string(index=False))

if missing_data.empty:
    print("There are no missing values")
else:
    # gets the gender value of record with missing values
    gender = int(missing_data['Gender'])

    # calculates mean and median of the specific gender
    grouped = df.groupby('Gender')
    mean = round(grouped.get_group(gender)['Height'].mean(), 2)
    median = grouped.get_group(gender)['Height'].mean()

    # fills the NaN value with average of the gender
    df.fillna(mean, inplace=True)

# print sorted by weight data
print('\n SORTED DATA BY WEIGHT WITH CALCULATED MISSING VALUES: ')
print(df.sort_values('Weight', ascending=True).to_string(index=False))


def ask_user(question):
    check = str(input("Question ? (Y/N): ")).lower().strip()
    try:
        if check[0] == 'y':
            return True
        elif check[0] == 'n':
            return False
        else:
            print('Invalid Input')
            return ask_user()
    except Exception as error:
        print("Please enter valid inputs")
        print(error)
        return ask_user()


if ask_user("Do you want to save/overwrite updated info into a file?"):
    # write updated data into a file
    df.to_csv('updated_data.csv', index=False)
    print('\n\n\n *** Updated data has been saved into updated_data.csv *** \n\n\n')
else:
    print('\n\n\n *** Data has not been saved *** \n\n\n')
