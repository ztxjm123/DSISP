from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
from collections import defaultdict, Counter
import xlrd
import pprint
import langid
import re
import xlrd
import xlwt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.stem import WordNetLemmatizer
import pandas as pd
import matplotlib.pyplot as pl


def stopWord(views):
    lemmatizer = WordNetLemmatizer()
    stopWords = set(stopwords.words('english'))
    newstop = ['app', 'please', 'android', 'google', 'cool', 'fine', 'hello', 'alright', 'poor', 'plz', 'pls', 'thank',
                'old', 'new', 'asap', 'someone', 'love', 'like', 'bit', 'annoying', 'beautiful', 'dear', 'I']
    wordmapper = []
    with open("data/wordMapper.txt", encoding='UTF-8') as Mapper:
        for line in Mapper:
            li = line.split(',')
            li[1] = li[1][0:-1]
            wordmapper.append(li)
    for news in newstop:
        stopWords.add(news)
    wordsFiltered = []
    for i in views:
        words = word_tokenize(i)
        st = []
        for w in words:
            a = lemmatizer.lemmatize(w)
            a2 = a.lower()
            if a2 not in stopWords:
                st.append(a2)
        if len(st) > 3:
            for s in range(len(st)):
                for mi in wordmapper:
                    if st[s] == mi[0]:
                        st[s] = mi[1]
            wordsFiltered.append(st)

    return wordsFiltered


def qu_fuhao(views):
    lists = []
    for i in views:
        lists.append(i)
    lists_new = []
    for list in lists:
        string = re.sub("[\s+\.\!\/_,$%^*(+\"\'\d]+|[-?:);+——！，。？、~@#￥%……&*（）]+", " ", list)
        lists_new.append(string)
    return lists_new


def read_file(path):
    # data = []
    # with open(path, encoding='UTF-8') as text_file:
    #     for index, line in enumerate(text_file):
    #         lineTuple = langid.classify(line)
    #         if lineTuple[0] == 'en':
    #             data.append(line)
    # return data
    exdata = xlrd.open_workbook(path)
    sheet = exdata.sheet_by_index(0)
    data = []
    for i in range(0, sheet.nrows):
        line = sheet.row_values(i)[0]
        lineTuple = langid.classify(line)
        if lineTuple[0] == 'en':
            data.append(line)

    return data


def Sma1(la):
    k0 = 1
    k1 = 1
    U0 = 10
    max_distance = 5

    eng_stopwords = set(stopwords.words('english'))
    eng_symbols = '{}"\'()[].,:;+!?-*/&|<>=~$'

    def ngram_is_valid(ngram):
        first, last = ngram[0], ngram[-1]
        if first in eng_stopwords or last in eng_stopwords: return False
        if any(num in first or num in last for num in '0123456789'): return False
        if any(eng_symbol in word for word in ngram for eng_symbol in eng_symbols): return False
        return True

    # 求句子的n-gram
    def to_ngrams(unigrams, length):
        return zip(*[unigrams[i:] for i in range(length)])

    ngram_counts = defaultdict(Counter)
    for line in la:
        words = line
        for n in range(2, max_distance + 2):
            ngram_counts[n].update(filter(ngram_is_valid, to_ngrams(words, n)))

    skip_bigram_info = defaultdict(lambda: defaultdict(Counter))
    for dist in range(2, max_distance + 2):
        for ngram, count in ngram_counts[dist].items():
            skip_bigram_info[ngram[0]][ngram[-1]] += Counter({dist - 1: count})
            skip_bigram_info[ngram[-1]][ngram[0]] += Counter({1 - dist: count})

    print('----------------------')
    newla = []
    for ladata in la:
        for l in ladata:
            newl = []
            a = skip_bigram_info[l]
            for ax in a:
                nax = str(l) + '_' + str(ax)
                newl.append(nax)
        newla.append(newl)

    return newla


def Langid(path):
    data1 = read_file(path)
    data2 = stopWord(qu_fuhao(data1))

    return data2


def text_save(data, path):  # 转化为TwitterLDA需要的txt文件
    num = 0
    while num < len(data):
        with open(path + 'lda.txt', 'a', encoding='utf-8') as file_handle:
            for n in data[num]:
                file_handle.write(n+' ')
            file_handle.write('\n')
        num = num + 1


if __name__ == '__main__':
    # appname = ['ASK', 'FB', 'KW', 'PSP', 'SH', 'TFSE', 'UB', 'YT']
    # for app in appname:
    #     path = 'data/' + app
    #     la = Langid(path + '/bogu.xlsx')
    #     print(len(la))
    #     Sma1(la)
    #     text_save(la, path)
    appname = ['16', '21', '28'] #
    for app in appname:
        path = 'data/UB'
        la = Langid(path + '/' + app + 'bogu.xlsx')
        print(len(la))
        newla = Sma1(la)
        text_save(newla, path+app)
