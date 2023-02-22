import pandas as pd

df = pd.read_csv('../../Datasets/DataScience/baseball.csv')

print(df)

pd_mean_weight = df["Weight"].mean()
pd_median_weight = df['Weight'].median()
print(pd_mean_weight)
print(pd_median_weight)