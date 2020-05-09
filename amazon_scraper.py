import bs4
import time
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def get_soup(url):
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    res = session.get(url)
    soup = bs4.BeautifulSoup(res.text)
    return soup

def get(type, url):

    soup = get_soup(url)
    link = url
    if link!= None:
        lista = get_reviews(link)
    else: lista = []

    return lista

def save_list(lista,endereco):
    arq = open(endereco, 'a', encoding="utf-8")
    if lista != None:
        for i in lista:
                arq.writelines(i+"\n")

def get_reviews(url):

    soup = get_soup(url)
    elemento = str(soup.find_all(class_="a-size-base review-text"))
    lista = elemento.split("<span class=\"a-size-base review-text\" data-hook=\"review-body\">")
    url = get_next_page(soup)


    if url != None:
        url = url.replace(";","&")
        print(url)
        lista = lista + get_reviews(url)


    lista = lista[1:]
    return lista

def get_type(type, soup): #pos or neg

    if type is "pos":
        link = soup.find_all(class_="a-size-small a-link-normal 4star")
    elif type is "neg":
        link =  soup.find_all(class_="a-size-small a-link-normal 1star")
    elif type is "pos1":
        link = soup.find_all(class_="a-size-small a-link-normal 5star")

    elif type is "neu":
        link = soup.find_all(class_="a-size-small a-link-normal 2star")
    elif type is "neu1":
        link = soup.find_all(class_="a-size-small a-link-normal 3star")
    try:
        return "https://www.amazon.com.br"+ str(link).split("\"")[5]
    except: return None

def get_next_page(soup):

    x = soup.find_all(class_="a-last")
    try:
        link = "https://www.amazon.com.br" + str(x).split("\"")[3]
        link = link.split('?')
        num = link[1].split('=')
        link = link[0]+"/ref=cm_cr_arp_d_paging_btm_next_"+num[1]+"?"+link[1]
    except:
        if "Our servers are getting hit pretty " not in str(x):
            link = None
        else:
            time.sleep(4)
            x = soup.find_all(class_="a-last")
            try:
                link = "https://www.amazon.com.br" + str(x).split("\"")[3]
                link = link.split('?')
                num = link[1].split('=')
                link = link[0] + "/ref=cm_cr_arp_d_paging_btm_next_" + num[1] + "?" + link[1]
            except:
                link = None
    if link != "https://www.amazon.com.bra-letter-space" and link != None:
        link = link.replace(";", "&")

        return link
    else: return None
