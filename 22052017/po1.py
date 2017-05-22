#очистить тексты от служебных и коротких слов
import os
texts_dic = {}
for root, dirs, files in os.walk('t'):
    print("we're in")
    for f in files[:50]:
        with open(os.path.join(root, f), 'r', encoding='utf-8') as t:
            text = preprocessing(t.read())
            texts_dic[f.split('.')[0]] = text
texts = list(texts_dic.values())

import re
punct = '[.,!«»?&@"$\[\]\(\):;%#&\'—-]'
def preprocessing(text): # функция предобработки текста
    text_wo_punct = re.sub(punct, '', text.lower()) # удаляем пунктуацию, приводим в нижний регистр
    words = text_wo_punct.strip().split() # делим по пробелам
    return words


def count_tf(word, text): #частота слова в тексте
    return text.count(word) / len(text)


def count_df(word, texts): #в скольких текстах слово
    n = [1 for text in texts if word in text]
    return sum(n)


#нужна не прямая частота, а обратная
def count_idf(word, texts):
    n = len(texts) / (1 + count_df(word, texts))
    return n


from math import log
def count_tfidf(word, text, texts):
    tf = count_tf(word, text)
    idf = count_idf(word, texts)
    return log(tf, 10) * log(idf, 10)


for text in texts_dic:
    print("Top words in document {}".format(text)) 
    scores = {} # здесь будем хранить оценки для каждого текста
    for word in texts_dic[text]:
        scores[word] =  count_tfidf(word, texts_dic[text], texts)
    sorted_words = sorted(scores.items(), key=lambda x: x[1])
    for word, score in sorted_words[:5]:
        print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
