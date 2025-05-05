import pandas as pd

poke = pd.read_csv('pokemon_data.csv')

# print(poke.tail(5))

# print(poke.head(3))

poke_tab = pd.read_csv('pokemon_data.txt', delimiter='\t')

# print(poke_tab)
# print(poke_tab.columns)

# printing a column
# print(poke['Name'])

# printing specific columns
# print(poke[['Generation', 'Name', 'Legendary']])

# print(poke.head(2))

# printing specific row
# print(poke.iloc[0])

# printing set of rows
# print(poke.iloc[0:4])

# reading specific location
# print(poke.iloc[1, 3])

# Iterating the rows one by one using a for lop
# for index, row in poke.iterrows():
#     print(index,row['Name'])

# print(poke.loc[poke['Type 1'] == "Grass"])
# print(poke.tail(5))

# print(poke.loc[poke['HP'] == 80])

# getting general description
# print(poke.describe())

# sorting alphabetically
# print(poke.sort_values('Name', ascending=False))

# sorting different data
# print(poke.sort_values(['Name', 'Type 1']))

# making changes to the data
# adding a new column
# print(poke.head(5))

# poke['Total'] = poke['HP'] + poke['Attack'] + poke['Defense'] + poke['Sp. Atk'] + poke['Sp. Def'] + poke['Speed']
# print(poke.head(5))
# print(poke.columns)

# dropping/deleting a column, needs to be assigned
# poke = poke.drop(columns=['Name'])
# print(poke.head(5))

# print(poke.head(5))
poke['Total'] = poke.iloc[:, 4:10].sum(axis=1)
# print(poke.head(5))

# positioning the total columns just after speed
cols = list(poke.columns)
poke = poke[cols[ 0:10 ] + [cols[-1]] + cols[10:12]]
# print(poke.head(5))

poke.to_csv('modified.csv', index=False)
poke.to_csv('modified.txt', index=False, sep=('\t'))

# Filtering Data
# print(poke.loc[( poke['Type 1'] == 'Grass' ) & (poke['Type 2'] == 'Poison')])

new_poke = poke.loc[( poke['Type 1'] == 'Grass' ) & (poke['Type 2'] == 'Poison')]
# print(new_poke)
# new_poke = new_poke.reset_index(drop=True)
# new_poke.drop(columns=['#'], inplace=True)
# print(new_poke)

# Advanced Filtering
# print(poke.loc[~poke['Name'].str.contains('Mega')])
# print(poke.head(5))

# Conditional changes
# poke.loc[poke['Type 1'] == 'Fire', 'Legendary'] = False
# print( poke.loc[poke['Type 1'] == 'Fire'] )
# print(poke.head(5))

poke.loc[poke['Total'] > 500, ['Legendary', 'Generation']] = ['Noma', '4']
poke['Sum'] = 'Failed'
poke.loc[poke['Total'] > 500, 'Sum'] = 'Passed'
# print(poke.loc[poke['Total'] > 500])
# print(poke.describe())

# To be Reviewed, .sum
print( poke.groupby(['Type 1']).mean(numeric_only=True))

# print( poke.groupby(['Type 1']).count() )
