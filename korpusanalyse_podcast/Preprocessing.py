import os
from lxml import etree
import nltk 
import pickle
from HanTa import HanoverTagger as ht

tagger = ht.HanoverTagger('morphmodel_ger.pgz')
parser = etree.XMLParser(remove_blank_text=True)
input_path = 'skripte'
output_path = 'corpus'
output_path_string = 'corpus_strings'

for file in os.listdir(input_path):
    try:
        data = etree.parse('%s/%s' %(input_path, file))
    except etree.XMLSyntaxError:
        with open("errors.txt", "a") as file_object:
            file_object.write("%s \n" %file)
    text=""
    for element in list(data.iter()):
        if element.tag  == "text":
            text+=element.text

    tokens = nltk.word_tokenize(text, language='german')


    lemmata = tagger.tag_sent(tokens,taglevel= 1, casesensitive=True)



    new_lemma = []

    for lemma in lemmata:
        if lemma[1] == "--":
            continue
        new_lemma.append(lemma[1])
    
    print(new_lemma[5])
    lemma_string = ""
    for lemma in new_lemma:
        lemma_string += " %s" %lemma


    # with open('%s/%s.pkl' %(output_path, file.split(".")[0]), 'wb') as f:
    #      pickle.dump(new_lemma, f)

    with open('%s/%s.txt' %(output_path_string, file.split(".")[0]), 'w') as f:
         f.write(lemma_string)
         

   



