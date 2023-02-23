import pandas as pd

df = pd.read_csv('../../Datasets/DataScience/baseball.csv')

print(df)

pd_mean_weight = df["Weight"].mean()
pd_median_weight = df['Weight'].median()
pd_position = df[['Position', "Age"]]

print(pd_mean_weight)
print(pd_median_weight)
print(pd_position)

row_loc = df.loc[5]
print(row_loc)