import re
import xlrd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


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


def df(word, words):
    n = 0
    for i in words:
        if word == i:
            n = n+1
    return n/len(words)


def bji(a, b):
    ab = []
    for i in a:
        if i in b and i not in ab:
            ab.append(i)
    return ab


def getmin(a, b):
    if a < b:
        return a
    else:
        return b


def qu_fuhao(views):
    lists = []
    for i in views:
        lists.append(i)
    lists_new = []
    for list in lists:
        string = re.sub("[\s+\.\!\/_,$%^*(+\"\'\d]+|[-?:);+——！，。？、~@#￥%……&*（）]+", " ", list)
        if string != ' ':
            lists_new.append(string.lower())
    return lists_new


def topiclda(path1, rzpath, rzpath2, rn):
    t = []
    newread = []
    for tn in range(1, rn+1):
        path = path1+'LDA/'+str(tn)+'.txt'
        file = open(path, encoding='utf-8')
        read = file.readlines()
        for r in read:
            newread.append(r)
    for line in newread:
        li = re.findall(r" (.+?)/", line)
        tx = []
        for x in li:
            tx.append(x)
        t.append(tx)

    file1 = open(rzpath, encoding='utf-8')
    gxrz1 = file1.readlines()
    topics = stopWord(qu_fuhao(gxrz1))
    wn = 0
    for words in t:
        for word in words:
            if word in topics:
                wn = wn + 1
                break
    precision = wn/len(gxrz1)
    recallt = wn/len(newread)
    if precision+recallt != 0:
        fhybrid = 2*((precision*recallt)/(precision+recallt))
    else:
        fhybrid = 'null'

    file2 = open(rzpath2, encoding='utf-8')
    gxrz2 = file2.readlines()
    topics2 = stopWord(qu_fuhao(gxrz2))
    wn2 = 0
    for words2 in t:
        for word2 in words2:
            if word2 in topics2:
                wn2 = wn2 + 1
                break
    precision2 = wn2 / len(gxrz2)
    if precision2 > 1:
        precision2 = 1
    recallt2 = wn2 / len(newread)
    if precision2 + recallt2 != 0:
        fhybrid2 = 2 * ((precision2 * recallt2) / (precision2 + recallt2))
    else:
        fhybrid2 = 'null'

    wn3 = 0
    for words3 in t:
        for word3 in words3:
            if word3 in topics or word3 in topics2:
                wn3 = wn3 + 1
                break
    precision3 = wn3 / len(gxrz2)
    recallt3 = wn3 / len(newread)
    if precision3 + recallt3 != 0:
        fhybrid3 = 2 * ((precision3 * recallt3) / (precision3 + recallt3))
    else:
        fhybrid3 = 'null'

    return precision, recallt, fhybrid, precision2, recallt2, fhybrid2, precision3, recallt3, fhybrid3


def getsim(path1, rzpath):
    path = path1+'bogu.xlsx'
    exdata = xlrd.open_workbook(path)
    sheet = exdata.sheet_by_index(0)
    date = []
    for i in range(0, sheet.nrows):
        date.append(sheet.row_values(i)[0])
    file = open(rzpath, encoding='utf-8')
    gxrz = file.readlines()

    ax = stopWord(qu_fuhao(date))
    bx = stopWord(qu_fuhao(gxrz))
    abx = bji(ax, bx)
    dfabx = 0
    dfax = 0
    dfbx = 0
    for i in abx:
        dfabx = dfabx + (df(i, abx))
    for j in ax:
        dfax = dfax + df(j, ax)
    for k in bx:
        dfbx = dfbx + df(k, bx)

    if getmin(dfax, dfbx) != 0:
        sim = dfabx / getmin(dfax, dfbx)
        return sim
    else:
        return 0


def main(path, rzpath, rzpath2, ldan):
    sim = getsim(path, rzpath)
    # print("sim = "+str(sim))
    p1, r1, f1, p2, r2, f2, p3, r3, f3 = topiclda(path, rzpath, rzpath2, ldan)
    print("Evaluation index(commit):")
    print(p1, r1, f1)
    print("Evaluation index(changelog):")
    print(p2, r2, f2)
    print("Evaluation index(c & com):")
    print(p3, r3, f3)



# path3 = 'WorkData/PSP/'
# rzpath = 'WorkData/PSP/commit.txt'
# rzpath2 = 'WorkData/PSP/changelog.txt'
# ldan = 11
# main(path3, rzpath, rzpath2, ldan)