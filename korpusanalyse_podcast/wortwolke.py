import pandas as pd

import numpy as np

color_in_dlf = "#6299ff"
color_not_in_dlf = "#ff503c"
data = pd.read_csv("results/not_in_dlf.csv", parse_dates=True)
data.rename(columns={"Unnamed: 0":"word"}, inplace=True)

cols=["Count", "word", "not"]
data = data[cols] 

data['not'] = data['not'].map({1:color_not_in_dlf, np.nan:color_in_dlf})

print(data)
data.to_csv("results/wortwolke_final.csv", index=False)