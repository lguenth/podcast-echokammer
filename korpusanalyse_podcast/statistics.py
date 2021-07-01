import os
import pandas as pd
from collections import Counter

data = pd.read_csv("results/tdm_dlf.csv", parse_dates=True).transpose()
print(data.iloc[0])


data.rename(columns=data.iloc[0], inplace = True)
data.drop(data.index[0], inplace = True)
print(data)


data = data.astype(float)
data= data.sort_index(ascending=True)
index = data.index

top_ten = data.apply(lambda s: s.abs().nlargest(10).index.tolist(), axis=1).to_frame("top")
top_ten = pd.DataFrame(top_ten["top"].to_list(), index=index, columns= ["Top1","Top2", "Top3", "Top4", "Top5", "Top6", "Top7", "Top8", "Top9", "Top10"])
top_ten.to_csv("results/top_ten_dlf.csv")

most_used= pd.DataFrame(Counter(top_ten.values.flatten()), index=['Count']).T
most_used.to_csv("results/most_used_dlf.csv")
