import os
import pandas as pd

data = pd.read_csv("tdm.csv").transpose()

data.rename(columns=data.iloc[0], inplace = True)
data.drop(data.index[0], inplace = True)
data.index.names = ['']


data = data.astype(float)
data.index = data.index.astype(int)
data= data.sort_index(ascending=True)

#print(data.idxmax(axis=1))
top_ten = data.apply(lambda s: s.abs().nlargest(10).index.tolist(), axis=1).to_frame("top")
top_ten = pd.DataFrame(top_ten["top"].to_list())
#print(top_ten[0].value_counts())
from collections import Counter
most_used= pd.DataFrame(Counter(top_ten.values.flatten()), index=['Count']).T
most_used.to_csv("results/most_used.csv")
top_ten.to_csv("results/top_ten.csv")