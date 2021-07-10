import pandas as pd

top_ten_path = "results/top_ten_complete.csv"
tdm_path = "results/tdmnormdlf.csv"
top_path ="results/most_used_complete.csv"

data = pd.read_csv(top_ten_path, parse_dates=True, index_col=0)
tdm = pd.read_csv(tdm_path, parse_dates=True, index_col=0)
top=pd.read_csv(top_path, index_col=0)
date_count=0
changes_all=0.0
df_changes = raw_df = pd.DataFrame(index= [""])

not_in_dlf = []
for index in data.index:
    #print(index)
    if index not in pd.date_range(start="2020-02-26", end="2020-03-25"):
        word_count=0
        top_ten= data.loc[index]
        date_count+=1
        changes_per_podcast = 0.0
        for word in top_ten:
            
            try:   
                before = tdm.loc[word][str(index)+"-before"]
                print("before")
                print(before)
                if before == 0.0:
                    continue
                #wie wachstum? geteilt durch macht nicht immer sinn
                after = tdm.loc[word][str(index)+"-after"]
                # series = pd.Series(before, after)
                # series.pct_change()
                
                print("after")
                print(after)
                diff= ((after-before)/before)*100
                if after == 0.0:
                    continue
                #print("Differenz")
                print(word)
                print(diff)
                changes_per_podcast+=diff
                #print(word + "-" + str(diff))
                word_count+=1
            except KeyError:
                top.at[word, 'not'] = 1
                diff = 0.0
                changes_per_podcast+=diff
                word_count+=1
                print(word)
                print(diff)
        print("----------------------------")
        print("Wörter: " +str(changes_per_podcast/word_count))
        print("----------------------------")
        changes_all+=(changes_per_podcast/word_count)
        df_changes[index] = changes_per_podcast/word_count
print(top)

print(changes_all/date_count)
df_changes_trans = df_changes.transpose()
#df_changes_trans.to_csv("results/changes_per_month.csv")
top.to_csv("results/not_in_dlf.csv")