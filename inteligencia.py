# Trabalho de Inteligencia Artificial.
import urllib.request
import requests
import re
def createConnectionUrl(url):
    file = urllib.request.urlopen(url)
    param=[]
    param.append(file)
    param.append(url)
    return param
def tokenize(params):
    response = requests.get(params[1])
    text = str(response.content)
    text = text.replace('\\n', ' ')
    text = text.replace('b\'A', 'A')
    text = re.sub('[^A-Za-z0-9\'\ ]+', '', text)
    return text.split()
def probability(rangex,sec,frase,textoToken):
        sec1 = readInputPhrase(frase,textoToken, rangex-1)
        sec2 = readInputPhrase(frase,textoToken, rangex-2)
        sec2 = readInputPhrase(frase,textoToken, rangex-3)
        sec3 = readInputPhrase(frase,textoToken, rangex-4)
        sec5 = readInputPhrase(frase,textoToken, rangex-5)
        sec4={}
        probability=[]
        for j in sec:
            if re.match(frase, j):
                sec[j]['secp'] = sec[j]['contador']/sec1[frase]['contador']
                probability.append([j,sec[j]['secp']])
            else:
                sec[j]['secp'] = 0
        return probability
def inputUserK(k,textoTK,index):
    word = textoTK[index]
    for xd in range(1,k+1):
        word = textoTK[index-xd]+' '+word
    return word
def readInputPhrase(frase,text, rangex):
    cont=0
    sec={}
    kep=frase.split(" ")
    for i in range(rangex,len(text)):
        spec = text[i]
        hx = inputUserK(rangex,text,i)
        if hx in sec:
            sec[hx]['contador']+=1
        else:
            sec[hx]={}
            sec[hx]['contador']=1
    if sec!=None:
        return sec
params = createConnectionUrl("http://norvig.com/ngrams/shakespeare.txt")
textoToken = tokenize(params)
dicionario = readInputPhrase("lie in",textoToken,2)
lista_de_probabilidades =probability(2,dicionario,"lie in",textoToken)
lista_de_probabilidades.sort()
lista_de_probabilidades.reverse()
for i in range(3):
    print(lista_de_probabilidades[i][0])
