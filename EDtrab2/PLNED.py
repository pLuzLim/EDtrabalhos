import re
import nltk
from nltk.corpus import stopwords
from collections import defaultdict

#stopwords pelo nltk
stop_words = set(stopwords.words('portuguese'))

#abrir do arquivo
arq = open("texto.txt", encoding="utf8")
#apaga o \n para ler como uma só linha
text = arq.read().lower().replace("\n", " ")
textfiltrado = re.split("[”“!`()/.,<>:;\"' ]+", text)
arq.close()

n = int(input("Quantos termos? "))

palfreq = defaultdict(int)

#removendo stopwords
stopwordstext = [palavra for palavra in textfiltrado if palavra not in stop_words]

#dicionário
for palavra in stopwordstext:
    if (palavra != "" and palavra != "\n"):
        palfreq[palavra] += 1

#lista e print
freqlista = [(f, p) for p,f in palfreq.items()]
freqlista.sort(reverse = True)
for i in range(n):
    print(freqlista[i])

#hapax legomenons
print("Hapax legomenons: ")
for k, v in palfreq.items():
    if (v == 1):
        print(k, end=" | ")



