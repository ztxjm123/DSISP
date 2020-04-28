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
import matplotlib.pyplot as plt
import numpy as np


def stopWord(views):
    lemmatizer = WordNetLemmatizer()
    stopWords = set(stopwords.words('english'))
    wordsFiltered = []
    for i in views:
        words = word_tokenize(i)
        for w in words:
            a = lemmatizer.lemmatize(w)
            if a not in stopWords:
                wordsFiltered.append(a)

    return wordsFiltered


def analysis(views):
    px = [-1, -0.5, 0, 0.5, 1]
    sid = SentimentIntensityAnalyzer()
    a = 0
    for sen in views:
        res = re.sub("[\s+\.\!\/_,$%^*(+\"\'\d]+|[-?:);+——！，。？、~@#￥%……&*（）]+", " ", sen[1])
        ss = sid.polarity_scores(res)
        a += int(ss['compound'])+px[int(sen[0]-1)]
    return a / len(views)


def getcipin(words):
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for i in range(15):
        word, count = items[i]
        print("{0:<10}{1:>5}".format(word, count))


def qu_fuhao(views):
    lists = []
    for i in views:
        lists.append(i[1])
    lists_new = []
    for list in lists:
        string = re.sub("[\s+\.\!\/_,$%^*(+\"\'\d]+|[-?:);+——！，。？、~@#￥%……&*（）]+", " ", list)
        lists_new.append(string)
    return lists_new


def bag_of_words(words):
    return dict([(word, True) for word in words])


def bigram(words, score_fn=BigramAssocMeasures.chi_sq, n=5):
    bigram_finder = BigramCollocationFinder.from_words(words)
    bigrams = bigram_finder.nbest(score_fn, n)
    return bag_of_words(bigrams)


def bigram_words(words, score_fn=BigramAssocMeasures.chi_sq, n=20):
    bigram_finder = BigramCollocationFinder.from_words(words)
    bigrams = bigram_finder.nbest(score_fn, n)
    return bag_of_words(words + bigrams)


def read_file(path):
    # path = 'D:/学习/python/python实例/app_houxv/APrev.xlsx'
    exdata = xlrd.open_workbook(path)
    sheet = exdata.sheet_by_index(0)
    data = []
    for i in range(0, sheet.nrows):
        data.append(sheet.row_values(i))
    return data


def plfx():
    name = []
    pf = []
    times = []
    pl = []
    data = read_file()
    for i in data:
        name.append(str(i[0]))
        pf.append(str(i[1]))
        times.append(i[2])
        pl.append(i[3])
    return name, pf, times, pl


def timecl():
    data = read_file()
    for i in data:
        string = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", " ",i[2])
        words = word_tokenize(string)
        if words[0] == 'October':
            words[0] = 2019
            words[2] = eval(words[1])
            words[1] = 10
        else:
            words[0] = 2019
            words[2] = eval(words[1])
            words[1] = 9
        i[2] = words
    num=1
    while num<len(data):
        for n in range(len(data)-1):
            if data[n][2][1] > data[n+1][2][1]:
                data[n], data[n+1] = data[n+1], data[n]
            elif data[n][2][1] == data[n+1][2][1]:
                if data[n][2][2] > data[n+1][2][2]:
                    data[n], data[n+1] = data[n+1], data[n]
        num += 1

    return data


def fxt(path):
    data = read_file(path)
    dayList = []
    day = data[0][2]
    a = []
    i = 0
    while i < len(data):
        a.append(day)
        try:
            while data[i][2] == day:
                frx = []
                frx.append(data[i][1])
                frx.append(data[i][3])
                a.append(frx)
                if i < len(data) - 1:
                    i += 1
                else:
                    i = len(data)
                    break
            dayList.append(a)
            day = data[i][2]
            a = []
        except:
            break

    return dayList


def Fln():
    squar = [0.81, 0.41, 0.54, 0.54, 0.47, 0.48, 0.51, 0.43, 0.72, 0.31, 0.50, 0.49, 0.48, 0.63]
    a = 0
    jdpc = []
    for i in range(len(squar)):
        a += squar[i]
    pj = a / len(squar)
    for j in range(len(squar)):
        l = squar[j] - pj
        if l > 0:
            jdpc.append(l)
        else:
            m =0 - l
            jdpc.append(m)
    print(jdpc)


def daycp(day1, day2):
    dx = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    n1 = []
    n2 = []
    for i in day1.split('-'):
        n1.append(eval(i))
    for j in day2.split('-'):
        n2.append(eval(j))
    m1 = 365 * (n1[0] - 2017) + dx[n1[1]-1] + n1[2]
    m2 = 365 * (n2[0] - 2017) + dx[n2[1] - 1] + n2[2]

    return m2 - m1


def Bogusb(data, rangex):
    # rangex = 3
    bof = []
    bog = []
    for i in range(0, len(data)-1):
        status = 0
        if data[i][1] > data[i+1][1]:
            status = 1
        elif data[i][1] < data[i+1][1]:
            status = 2
        data[i].append(status)
    for j in range(1, len(data)-1):
        if data[j-1][2] == 2 and data[j][2] == 1 :
            bof.append(data[j])
        elif data[j-1][2] == 1 and data[j][2] == 2:
            bog.append(data[j])
    newbf = []
    newbg = []
    if len(bof) != 0:
        newbf.append(bof[0])
        f1 = 0
        for f in range(1, len(bof)):
            if bof[f][1] > bof[f - 1][1] and (daycp(newbf[f1][0], bof[f][0])) > rangex:
                f1 = f1 + 1
                newbf.append(bof[f])
    else:
        print("bf error")
        newbf.append(0)
    if len(bog) != 0:
        newbg.append(bog[0])
        g1 = 0
        for g in range(1, len(bog)):
            if bog[g][1] < bog[g - 1][1] and (daycp(newbg[g1][0], bog[g][0])) > rangex:
                g1 = g1 + 1
                newbg.append(bog[g])
            elif bog[g][1] < newbg[g1][1] and (daycp(newbg[g1][0], bog[g][0])) <= rangex:
                newbg.remove(newbg[g1])
                newbg.append(bog[g])
    else:
        print("bg error")
        newbg.append(0)

    return newbf, newbg


def exal(DATA, path):
    workbook = xlwt.Workbook(encoding='utf-8')
    booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)
    for i, row in enumerate(DATA):
        for j, col in enumerate(row):
            booksheet.write(i, j, col)
    workbook.save(path+'bogu.xls')


def main(path, path1, appname):
    # path = 'D:/Download/WorkDate/PSP/PsPreviews.xls'
    data = fxt(path1)
    squar = []
    x = []
    dayr = []
    for i in data:
        dr = []
        x.append(i[0])
        dr.append(i[0])
        i.remove(i[0])
        review = qu_fuhao(i)
        pf = analysis(i)
        squar.append(pf)
        words = stopWord(review)
        j = bigram(words)
        dr.append(review)
        dayr.append(dr)
    bo = []
    for sn in range(len(x)):
        b =[]
        b.append(x[sn])
        b.append(squar[sn])
        bo.append(b)
    rangex = 3
    ax, bx = Bogusb(bo, rangex)
    for g in bx:
        for r in dayr:
            if g[0] == r[0]:
                g[2] = r[1]
                break
    # exal(bx, path)
    plt_x = []
    xn = 0
    for xbx in range(1, 5):
        plt_x.append(x[xn])
        xn = xn + (len(x) // 4)
    # for plx in bx:
    #     plt_x.append(plx[0])
    if len(x) == len(squar):
        plt.plot(x, squar, color='#4146d5', linewidth=3.5)
        plt.ylabel(u'ARS(score)', fontsize=18)
        plt.xlabel(u'date', fontsize=15)
        plt.title(u''+appname, fontsize=20)
        plt.tick_params(axis='x', labelsize=18)
        plt.tick_params(axis='y', labelsize=15)
        plt.xticks(plt_x)
        plt.show()


# path1 = 'D:/Download/WorkDate/PSP/PsPreviews.xls'
# appname = 'PPSSPP - PSP emulator'
# main(path1, appname)