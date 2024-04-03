import pandas as pd
import json
import re
import nltk
import os
import time
import math
import logging
logger = logging.getLogger("uvicorn.info")

#loading file paths
def create_tf_idf():
    start=time.perf_counter()
    documents = pd.read_csv('./src/server/assets/content.csv')
    doc_len=[]
    titles={}
    content={}
    for x ,document in enumerate(documents["content"]):

        doc_len.append(len(document.split()))
        y=document.split('<==>')
        titles[x]=y[0]
        content[x]=y[1]
    
    docs = open('./src/server/assets/unigrams.jsonl','r').readlines()
    IDF={}
    for x,line in enumerate(docs):
        keys = json.loads(line).keys()
        values =json.loads(line)
        for y,key in enumerate(keys):
            if(re.match('^[a-zA-Z]+$',key)):
                if(IDF.get(key) is None):
                    IDF[key]={}
                IDF[key][x]=values[key]
        if((x+1)%100000==0):
            print( str(x+1)+'done')
    
    for key in IDF.keys():
        doc_freq=len(IDF[key].keys())
        for sub_key in IDF[key].keys():
            IDF[key][sub_key] = (1+math.log(IDF[key][sub_key]))*math.log(100000/doc_freq)/doc_len[sub_key]
    
    print(f"Created TF-IDF vectors in {time.perf_counter()-start} sec.")
    print("Creating assets.")
    open("./src/server/assets/IDF.json", "w").write(re.sub("\n", "", json.dumps(IDF, indent=0)))
    print("Successfully written IDFs.")
    open("./src/server/assets/content.json", "w").write(re.sub("\n", "", json.dumps(content, indent=0)))
    print("Successfully written urls.")
    open("./src/server/assets/titles.json", "w").write(re.sub("\n", "", json.dumps(titles, indent=0)))
    print("Successfully written titles.")
    return True
    