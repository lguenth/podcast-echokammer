import os
import nltk 
import json

from HanTa import HanoverTagger as ht
from nltk.corpus import stopwords


tagger = ht.HanoverTagger('morphmodel_ger.pgz')
input_path = 'skripte_json'
output_path_string = 'corpus_date'
german_stop_words = stopwords.words('german')
date_volume_dict = {}

with open("metadata.json") as m:
    dict = json.load(m)
    print(type(dict))

for index, item in enumerate(dict):
    
    full_date = ""
    if len(str(item["date"]["day"])) == 1:
        full_date += "0" + str(item["date"]["day"])
    else:
        full_date += str(item["date"]["day"])
    if len(str(item["date"]["month"])) == 1:
        full_date += ".0" + str(item["date"]["month"])
    else:
        full_date += "." +str(item["date"]["month"])
    full_date += "." +str(item["date"]["year"])

    date_volume_dict[item["id"]] = full_date


for file in os.listdir(input_path):
    with open("%s/%s" %(input_path, file)) as f:
        text= " ".join(list(json.load(f).values()))

    
    folge = file.split("_")[0]

    without_glossar = text.split("GLOSSAR")[0]
    

    tokens = nltk.word_tokenize(without_glossar, language='german')


    lemmata = tagger.tag_sent(tokens,taglevel= 1, casesensitive=True)



    new_lemma = []

    for lemma in lemmata:
        if lemma[1] == "--" or lemma[1] in german_stop_words or lemma[2]!="NN":
            continue
        new_lemma.append(lemma[1])
    
    print(new_lemma[5])
    lemma_string = ""
    for lemma in new_lemma:
        lemma_string += " %s" %lemma


    with open('%s/%s.txt' %(output_path_string, date_volume_dict[folge]), 'w') as f:
         f.write(lemma_string)
         
    