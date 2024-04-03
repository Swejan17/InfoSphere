import nltk,time
import json
from logging import getLogger

logger = getLogger("uvicorn.info")

logger.info("Loading assets!! This may take sometime!! Please wait patiently!")
start = time.perf_counter()
content = json.load(open("./src/server/assets/content.json", "r"))
logger.info(f"Loaded content.json the assets in {time.perf_counter()-start} sec")
titles = json.load(open("./src/server/assets/titles.json", "r"))
logger.info(f"Loaded titles.json the assets in {time.perf_counter()-start} sec")
idf = json.load(open(f"./src/server/assets/IDF.json", "r"))
logger.info(f"Loaded IDF.json the assets in {time.perf_counter()-start} sec")

def process_query(query: str):
    start = time.perf_counter()
    lis = nltk.word_tokenize(query)
    score={}
    for x in lis:
        if not x.isalpha():
            continue
        x = x.lower()
        if idf.get(x) is not None:
            keys=idf[x].keys()
            for key in keys:
                if score.get(key) is None:
                    score[key]=idf[x][key]
                score[key]+=idf[x][key]
    sorted_Dict = sorted(score.items(),key=lambda x:x[1],reverse=True)
    k=600
    if(len(sorted_Dict)>k):
        top_k =dict(sorted_Dict[:k])
    else:
        top_k =dict(sorted_Dict)
    res = []
    for k in top_k.keys():
        res.append({
            "title": titles[k],
            "id": k
        })
    return {
        "data": res,
        "time": time.perf_counter()-start
    }

def read_by_id(id: str):
    return {
        "id": id,
        "title": titles[id],
        "content": content[id]
    }