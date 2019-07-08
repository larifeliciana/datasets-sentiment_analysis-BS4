#import webbrowser

#webbrowser.open("https://www.amazon.com.br/revolu%C3%A7%C3%A3o-dos-bichos-conto-fadas/product-reviews/8535909559/")
import bs4
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
#    link = get_type(type, soup)
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
    elemento = str(soup.find_all(class_="a-size-base review-text")).replace("<br/><br/>", " ").replace("<br/>", " ").replace("</span>,", "").replace("[","").replace("</span>", "").replace("]","")
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
            print("acabou")
            print(x)
            link = None
        else:
            print("cansou")
            for i in range(1000000):
                x = soup.find_all(class_="a-last")
            print("descançou")
            try:
                link = "https://www.amazon.com.br" + str(x).split("\"")[3]
                link = link.split('?')
                num = link[1].split('=')
                link = link[0] + "/ref=cm_cr_arp_d_paging_btm_next_" + num[1] + "?" + link[1]
            except:
                print("acabou mesmo")
                print(x)
                link = None
    if link != "https://www.amazon.com.bra-letter-space" and link != None:

        z = link.replace(";", "&")

        return z
    else: return None



#links = ["https://www.amazon.com.br/Como-convencer-alguém-90-segundos-ebook/product-reviews/B00CMDEE1E/","https://www.amazon.com.br/Chefe-Máfia-Soprattuto-Livro-1-ebook/product-reviews/B07MQTNVMF/","https://www.amazon.com.br/Bela-Chefe-Ruby-Lace-ebook/product-reviews/B07124FM8C/","https://www.amazon.com.br/PROCRASTINAÇÃO-científico-sobre-procrastinar-definitivamente-ebook/product-reviews/B075JMXJLH/","https://www.amazon.com.br/startup-enxuta-Eric-Ries-ebook/product-reviews/B00A3C4GAK/","https://www.amazon.com.br/Trabalhe-4-horas-por-semana-ebook/product-reviews/B01LDPCZXU/"]

#links = ["https://www.amazon.com.br/Ceo-Indomável-Elisete-Duarte-ebook/product-reviews/B07H6VQJG6/","https://www.amazon.com.br/Benjamin-Família-Valentini-Livro-1-ebook/product-reviews/B07HLSYYNP/","https://www.amazon.com.br/Clube-luta-Chuck-Palahniuk-ebook/product-reviews/B00AC7C9LE/","https://www.amazon.com.br/DÍVIDA-Heitor-Série-Turbulência-Livro-ebook/product-reviews/B07K5J27S3/","https://www.amazon.com.br/Príncipe-Vingança-Príncipes-Castellani-Livro-ebook/product-reviews/B076KP4F55/","https://www.amazon.com.br/Tempo-Para-Aceitar-Livro-Único-ebook/product-reviews/B07MY7NJC4/","https://www.amazon.com.br/amiga-genial-Infância-adolescência-Napolitana-ebook/product-reviews/B00Y8RQ16I/","https://www.amazon.com.br/Hibisco-roxo-Chimamanda-Ngozi-Adichie-ebook/product-reviews/B01KYMLK8Y/","https://www.amazon.com.br/SEBASTIAN-Trilogia-Protetores-Livro-III-ebook/product-reviews/B07LD87FJ7/","https://www.amazon.com.br/DOM-Trilogia-Protetores-Livro-I-ebook/product-reviews/B0742RDJ9J/","https://www.amazon.com.br/Júlia-Livro-1-série-Renda-se-ebook/product-reviews/B079GFT45T/","https://www.amazon.com.br/Katarina-Livro-3-série-Renda-se-ebook/product-reviews/B07C942G2P/","https://www.amazon.com.br/Espere-me-Acordada-Spin-off-Trilogia-Protetores-ebook/product-reviews/B074YDM1L8/","https://www.amazon.com.br/Alice-Livro-2-série-Renda-se-ebook/product-reviews/B079G8BXCN/","https://www.amazon.com.br/Priscila-Livro-4-série-Renda-se-ebook/product-reviews/B07D64LCXQ/","https://www.amazon.com.br/DAMIEN-Trilogia-Protetores-Livro-II-ebook/product-reviews/B075K1D65F/","https://www.amazon.com.br/Luz-Manhã-Anne-Marck-ebook/product-reviews/B077S8DZYP/"]
links = ["https://www.amazon.com.br/Hackeando-Tudo-Hábitos-Mudar-Geração-ebook/product-reviews/B00UQP1CC4/","https://www.amazon.com.br/2001-Uma-odisséia-no-espaço-ebook/product-reviews/B015EE5N9E/","https://www.amazon.com.br/Wall-Street-Livro-Proibido-Ebook-ebook/product-reviews/B01BCHOXUC/","https://www.amazon.com.br/ESTUDA-QUE-VIDA-MUDA-Ajudando-ebook/product-reviews/B0797TQZ8C/","https://www.amazon.com.br/Imigrante-Ilegal-Negro-Sonho-Americano-ebook/product-reviews/B01MS2RVB5/","https://www.amazon.com.br/Mente-Magnética-Ciência-Riqueza-Prosperidade-ebook/product-reviews/B00Q9BM82W/","https://www.amazon.com.br/Elon-Musk-bilionário-SpaceX-moldando-ebook/product-reviews/B01555GJKE/","https://www.amazon.com.br/Arábia-Incrível-História-Brasileiro-Oriente-ebook/product-reviews/B01N6RPRD7/","https://www.amazon.com.br/Classe-Econômica-Europa-Comunista-ebook-ebook/product-reviews/B01MQI2GPG","https://www.amazon.com.br/Uma-noiva-natal-Juliana-Dantas-ebook/product-reviews/B07M5HXGLK/","https://www.amazon.com.br/Melhor-Noite-Ano-Devasso-Descarado-ebook/product-reviews/B07LGLV85V/","https://www.amazon.com.br/Recomeços-Nana-Pauvolih-ebook/product-reviews/B07KWG2BLV","https://www.amazon.com.br/Theo-Eva-Nana-Pauvolih-ebook/product-reviews/B07M63Y7XJ/","https://www.amazon.com.br/Rendida-Livro-4-Série-Segredos-ebook/product-reviews/B00XQQY7FY/","https://www.amazon.com.br/Além-do-Olhar-Nana-Pauvolih-ebook/product-reviews/B07BY8VHNB/","https://www.amazon.com.br/Seduzida-Livro-3-Série-Segredos-ebook/product-reviews/B00QSMX8GM/","https://www.amazon.com.br/você-Cobain-James-Nana-Simons-ebook/product-reviews/B07HP7MKLJ/","https://www.amazon.com.br/VOSSA-ALTEZA-Uma-promessa-honra-ebook/product-reviews/B07HDTTZB6/","https://www.amazon.com.br/Adorável-Selvagem-Valentina-K-Michael-ebook/product-reviews/B07MMW83MC/","https://www.amazon.com.br/Renda-se-Encontro-Anne-Marck-ebook/product-reviews/B06W9K5W7F/","https://www.amazon.com.br/Série-Segredos-Bônus-Natal-Pauvolih-ebook/product-reviews/B00RPOM5TI/","https://www.amazon.com.br/Volta-Ao-Prazer-Nana-Pauvolih-ebook/product-reviews/B019EWS48Y/"]
#links =["https://www.amazon.com.br/Ferida-Série-Segredos-Nana-Pauvolih-ebook/product-reviews/B00NPCC5T4/"]
diretorio = ["Nova pasta1/books_pt_UN2"]
for i in links:
    lista_pos = get("pos", i)

    save_list(lista_pos , diretorio[0])

    print("***")
