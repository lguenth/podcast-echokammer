import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import os

input_path="corpus_dlf"
vectorizer = TfidfVectorizer()
raw_df = pd.DataFrame(index= [""])

for file in os.listdir(input_path):
    with open('%s/%s' %(input_path, file), 'r') as f:
        #new_date_format = file.split(".")[2] + "-" + file.split(".")[1] + "-" + file.split(".")[0]
        raw_df[file.split(".")[0]] = f.read()
        
raw_df.to_csv("results/test2.csv")


doc_vec = vectorizer.fit_transform(raw_df.iloc[0])
 
# Create dataFrame
tdm = pd.DataFrame(doc_vec.toarray().transpose(),
                   index=vectorizer.get_feature_names())
 
# Change column headers
tdm.columns = raw_df.columns
print(tdm)
#tdm.to_csv("results/tdm_dlf.csv")