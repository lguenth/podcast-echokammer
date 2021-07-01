import os
from lxml import etree
import nltk 
from HanTa import HanoverTagger as ht
from nltk.corpus import stopwords


tagger = ht.HanoverTagger('morphmodel_ger.pgz')
parser = etree.XMLParser(remove_blank_text=True)
input_path = 'coronaticker_2021_05.xml'
output_path = 'corpus_dlf'
german_stop_words = stopwords.words('german')


data = etree.parse("coronaticker_2021_05.xml")

for element in list(data.iter("text")):
    date = element.get("date")
    text = ""
    print(date)

    for p in element.getchildren():
        text += p.text




    tokens = nltk.word_tokenize(text, language='german')


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


    # with open('%s/%s.pkl' %(output_path, file.split(".")[0]), 'wb') as f:
    #      pickle.dump(new_lemma, f)

    with open('%s/%s.txt' %(output_path, date), 'w') as f:
         f.write(lemma_string)
         

   