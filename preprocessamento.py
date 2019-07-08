import nltk
import re
import os
nltk.download('rslp')


##testar também só com algumas stopwords
def preprocessamento(texto, stopwords1, stem):
    stopwords = nltk.corpus.stopwords.words('portuguese')
    stemmer = nltk.stem.RSLPStemmer()
    lista1 = ['mais', 'mas', 'não', 'já', 'sem', 'nem', 'mesmo']
    for i in lista1:
        stopwords.remove(i)
    dict = {'n':'não','nao':'não', 'eh':'é', 'q':'que', 'pq':'porque','nd':'nada','ja':'já','tao':'tão','blz':'beleza', 'caralho':'insulto','puta':'insulto','ero':'erro','eros':'erros','horivel':'horrível','horiveis':'horríveis','vc':'você','vcs':'vocês'}

    texto.replace("."," ")
    tokens = nltk.tokenize.word_tokenize(texto, language='portuguese')

    lista = []
    for i in range(len(tokens)):
        if tokens[i].isalpha():

            if tokens[i] in dict.keys():
                tokens[i] = dict[tokens[i]]

            x = tokens[i]  not in stopwords
            if x or not stopwords1:

                if stem:
                    lista.append(stemmer.stem(tokens[i]))
    return lista


def save_list(lista,endereco):
    try:
        arq = open(endereco, 'a', encoding="utf-8")
    except:
        arq = open(endereco, 'w', encoding='utf-8')
    if lista != None:
        for i in lista:
                arq.writelines(i)

def read_list(endereco):
    lista = []
    for i in open(endereco, 'r', encoding="utf-8"):
        lista.append(i)
    return lista


def processando(textos):
    lista = []
    for i in textos:
        tokens = nltk.tokenize.word_tokenize(i, language='portuguese')
        if len(tokens) > 4:
            lista.append(i)

    return lista

#def selecionar_textos_steam()
def substitui(lista1):
    lista2 = []
    lista1 = checar_repetidos(lista1)
    for texto in lista1:
        try:
              if len(texto)>5 and langdetect.detect(texto) == 'pt':

                texto = re.sub('<[^>]*>', "", texto)
                texto = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', texto) #tirando links
                texto = re.sub('[a-z]*[♥]+[a-z]*', ' AMOR ', texto) #tirando os simbolos de palavrões
                texto = re.sub(r'([^soSOrRPp])\1+', r'\1', texto) #tirar letras repetidas
             #   texto = re.sub('\s\s', " ", texto)

                texto = re.sub(r'([^sS])\1{2,}', r'\1', texto)  # tirar letras repetidas
                texto = re.sub(r'([^rR])\1{2,}', r'\1', texto)  # tirar letras repetidas
                texto = re.sub(r'([^oO])\1{2,}', r'\1', texto)  # tirar letras repetidas
                texto = re.sub('\s([@#][\w_-]+)', " TAG ", texto)
              #  texto = re.sub('([$]?[0-9]+,*[0-9]*)+', " NUMBER ", texto)
                texto.replace("🏻","")
                texto = re.sub('(\.)', " ", texto)
                texto.replace("  ", " ")
                dict = {'n': 'não', 'nao': 'não', 'eh': 'é', 'q': 'que', 'pq': 'porque', 'nd': 'nada', 'ja': 'já',
                        'tao': 'tão', 'blz': 'beleza', 'caralho': 'insulto', 'puta': 'insulto', 'ero': 'erro',
                        'eros': 'erros', 'horivel': 'horrível', 'horiveis': 'horríveis', 'vc': 'você', 'vcs': 'vocês'}



                #lista = []
                tokens = nltk.tokenize.word_tokenize(texto, language='portuguese')
                for i in range(len(tokens)):

                        if tokens[i] in dict.keys():
                            tokens[i] = dict[tokens[i]]

                lista2.append(lista(tokens))
        except:
            print(texto)
    return  lista2

def checar_repetidos(lista):
    #print(len(lista))
    lista1 = []
    for i in lista:
        if i not in lista1:
            lista1.append(i)
    #print(len(lista1))
    return lista1

def lista(lista):
    str1 = ""
    for i in lista:
        str1=str1+str(i)+" "
    return str1+"\n"


def clean(endereco):
    caminhos  = endereco
    lista = read_list(endereco)
    lista = substitui(lista)
    save_list(lista, "Final Raw Data/Clean/"+caminhos.split("/")[2]+"_clean1")
    print(caminhos.split("/")[2]+"_clean1")


def split(endereco1):
    endereco = 'Final Raw Data/Raw Data/'+endereco1+'_pt'
    pos = read_list(endereco+"_pos_clean")
    neg = read_list(endereco+"_neg_clean")
    save_list(pos[0:1000],'Split/'+endereco1+'/positive.parsed')
    save_list(neg[0:1000],'Split/'+endereco1+'/negative.parsed')
    save_list(pos[1000:]+neg[1000:], 'Split/'+endereco1+'/'+endereco1+'Un')

def carregar(pasta):

    caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    lista = []
    for i in caminhos:
                lista.append(read_list(i))
    return caminhos, lista
#primeiro steam
#endereco = 'Final Raw Data/Raw Data/itunes_pt_neg'
enderecos =['Final Raw Data/Raw Data/itunes_pt_neg', 'Final Raw Data/Raw Data/itunes_pt_pos','Final Raw Data/Raw Data/skoob_pt_pos','Final Raw Data/Raw Data/neg_pt_pos']
import langdetect
#clean(enderecos[0])
#for endereco in enderecos:
#    clean(endereco)
#clean(endereco1)
stopwords = nltk.corpus.stopwords.words('portuguese')



def td(endereco1):

    endereco = 'Final Raw Data/Clean/'+endereco1+'_pt'
    save = 'Final Raw Data/Processed/'+endereco1+'_pt'
    pos = read_list(endereco+"_pos_clean")
    neg = read_list(endereco+"_neg_clean")
    pos1= []
    neg1= []
    for i in pos:
       pos1.append(preprocessamento(i, True,True))
    for i in neg:
       neg1.append(preprocessamento(i, True, True))
    save_list(pos1,save+"pos_clean")
    save_list(pos1,save+"neg_clean")

palavra = "walking on"
import spacy
nlp = spacy.load('en')
palavra= nlp(palavra)

for i in palavra:
    if i.is_stop:
        print(i)