import pandas as pd
from datetime import date, timedelta   
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import normalize
import numpy as np


dlf_corpus_path = "corpus_dlf"
top_ten_path = "results/top_ten_complete.csv"
vectorizer = CountVectorizer()


data = pd.read_csv(top_ten_path, parse_dates=True, index_col=0)
raw_df = pd.DataFrame(index= [""])

for index in data.index:
    if index not in pd.date_range(start="2020-02-26", end="2020-03-25"):
        week_before = pd.date_range(start= index - timedelta(days=6), end=index)
        week_after = pd.date_range(start= index + timedelta(days=1), end=index+timedelta(weeks=1))
    # print("%s - %s" %(index, week_before))
    # print("%s - %s" %(index, week_after))

        corpus_before = ""
        corpus_after = ""
        for file in os.listdir(dlf_corpus_path):
            if file.split(".")[0] in week_before:
                with open('%s/%s' %(dlf_corpus_path, file)) as f:
                    corpus_before += f.read()
            if file.split(".")[0] in week_after:
                with open('%s/%s' %(dlf_corpus_path, file)) as f:
                    corpus_after += f.read()
        raw_df[str(index) + "-after"] = corpus_after
        raw_df[str(index) + "-before"] = corpus_before
raw_df.to_csv("results/test.csv")


doc_vec = vectorizer.fit_transform(raw_df.iloc[0])
    # Create dataFrame
tdm = pd.DataFrame(doc_vec.toarray().transpose(), index=vectorizer.get_feature_names())

tdm.columns = raw_df.columns
print(tdm.sum(axis=0))
tdm_norm = tdm.div(tdm.sum(axis=0))
print(tdm_norm)
tdm_norm.to_csv("results/tdmnormdlf.csv")
