import re
from math import log

punct = '[.,!«»?&@"$\[\]\(\):;%#&\'—-]' #PUNCT ибо константа

def preprocessing(text):
    text_wo_punct = re.sub(punct, '', text.lower())
    words = text_wo_punct.strip().split()
    return words

with open('C:\Users\student\Desktop\rye.txt', 'r', encoding='utf-8') as f:
    words = preprocessing(f.read())

word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

bigrams = []
for ind in range(1, len(words) - 1):
    bigrams.append(' '.join([words[ind - 1], words[ind]]))
    
bigram_freq = {}
for b in bigrams:
    if b in bigram_freq:
        bigram_freq[b] += 1
    else:
        bigram_freq[b] = 1

def count_pmi(x, y):
    p_xy = bigram_freq[' '.join([x, y])]/len(bigram_freq)
    p_x, p_y = word_freq[x]/len(word_freq), word_freq[y]/len(word_freq)
    pmi = log(p_xy/(p_x * p_y))
    return pmi

pmi = {}
for bigr in bigrams:
    x, y = bigr.split()
    pmi[bigr] = count_pmi(x, y)

i = 0
for bigram in sorted(pmi, key = lambda m: -pmi[m]):
    if i > 100:
        break
    print(bigram, pmi[bigram])
    i += 1
