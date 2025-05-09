import pandas as pd
# print('Lets get it done')

# name = input('What is your name? ')
# if name.lower() == 'tony':
#     print('Fuck you Tony')
# else:
#     print(f'Your name is {name}')

# name = 'Andreh'
# print(name.lower())

column_names = []

column_names.append('Andreh')
column_names.append('Kunta')
column_names.append('Kankan')

# print(column_names)

# for col in column_names:
#     print(col)

# for n in range(len(column_names)):
#     print(column_names[n])

# print(column_names.lower())

tenants = pd.read_excel('tenants.xlsx')
# print(tenants.head())

header_list = list(tenants.columns)
header_list = [item.lower() for item in header_list]
# print(header_list)

missing_data = pd.read_excel('missingdata.xlsx')
# print(missing_data.head(3))

# Getting the missing rows in a dataframe
missing_rows = missing_data[missing_data.isnull().any(axis=1)]
# print(missing_rows)

# missing_rows.to_excel('missing_rows.xlsx', index=False)

# Removing all the missing data in the dataframe
missing_data.dropna(ignore_index=True)

data = pd.read_excel('missingdata.xlsx')

print(data.iloc[98])

#Printing the exact columns that are missing
for index, row in data.iterrows():
    missing = row[row.isnull()].index.tolist()

    if missing:
        print(f"Error: Missing data in row {index + 2}, columns: {', '.join(missing)}")

