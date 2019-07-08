    import requests

    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry
    import json

def get_soup(url):
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    res = session.get(url)

    return res.text

def get_reviews(appid, offset, page,language, type):
    url = "https://store.steampowered.com/appreviews/"+appid+"?json=1&day_range=223372036854775807&num_per_page="+page+"&l=brazilian&review_type="+type
    try:
        print(url)
        x = get_soup(url)
        print(x)
        lista = []
        j = json.loads(x)['reviews']
        for i in j:
            lista.append(i['review'].replace("\n","").replace("\r","")+"\n")
    except:
        return []
    return lista


def save_list(lista,endereco):
    arq = open(endereco, 'a', encoding="utf-8")
    if lista != None:

        for i in lista:
                arq.writelines(i)

txt = open("appid", 'r',encoding='utf-8').read().split("appid\":")[1:]
ids = []
for i in txt:
    ids.append(i.split(',')[0])
print(ids[-1])
pos = []
neg = []
for i in ids:
    x = get_reviews(i,"0","100","brazilian","positive")
    y = get_reviews(i,"0","100","brazilian","negative")
    pos.append(x)
    neg.append(y)

save_list(pos, "pos_steam")
save_list(neg, "neg_steam")


#https://store.steampowered.com/appreviews/570?json=1&num_per_page=100&review_type=negative&filter=recent