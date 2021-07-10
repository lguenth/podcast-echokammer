import os
import nltk 
from HanTa import HanoverTagger as ht
from nltk.corpus import stopwords


tagger = ht.HanoverTagger('morphmodel_ger.pgz')
input_path = 'new_texts_dlf'
output_path = 'corpus_dlf'
german_stop_words = stopwords.words('german')


for file in os.listdir(input_path):
    with open ("%s/%s" %(input_path, file), 'r') as f:
        text = f.read()
        date = file.split(".")[0]






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
         

   