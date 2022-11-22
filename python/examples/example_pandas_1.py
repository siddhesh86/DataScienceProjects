import pandas as pd

#create DataFrame
df = pd.DataFrame({'team': ['A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
                   'points': [5, 7, 7, 9, 12, 9, 9, 4],
                   'rebounds': [11, 8, 10, 6, 6, 5, 9, 12],
                   'blocks': [4, 7, 7, 6, 5, 8, 9, 10]})

#view DataFrame
print("df: {}".format(df))

#select rows where 'points' column is equal to 7
df1 = df.loc[df['points'] == 7]
print("df1: {}".format(df1))

#select rows where 'points' column is equal to 7
df2 = df.loc[df['points'].isin([7, 9, 12])]
print("df2: {}".format(df2))

#select rows where 'team' is equal to 'B' and points is greater than 8
df3 = df.loc[(df['team'] == 'B') & (df['points'] > 8)]
print("df3: {}".format(df3))

# select rows where 'team' is not equal to B
df4 = df.loc[df['team'] != 'B']
df5 = df.loc[~df['team'].isin(['A', 'B'])]
print("df4: {}".format(df4))
print("df5: {}".format(df5))
