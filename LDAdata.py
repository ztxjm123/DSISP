import re
import csv
import xlrd
import xlwt


def read_file(path):
    exdata = xlrd.open_workbook(path)
    sheet = exdata.sheet_by_index(0)
    date = []
    for i in range(0, sheet.nrows):
        a = []
        a.append(sheet.row_values(i)[0])
        a.append(sheet.row_values(i)[1])
        a.append(sheet.row_values(i)[2])
        # a.append(sheet.row_values(i)[3])
        date.append(a)
    # date.remove(date[0])
    return date


def text_save(data, path):  # 转化为TwitterLDA需要的txt文件
    num = 0
    n = 1
    while num < len(data):
        with open(path+str(n) + '.txt', 'a', encoding='utf-8') as file_handle:
            # file_handle.write(data[num][0])
            file_handle.write(data[num][2])
            file_handle.write('\n')
        n = n + 1
        num = num + 1


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


def exal(DATA):
    workbook = xlwt.Workbook(encoding='utf-8')
    booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)
    for i, row in enumerate(DATA):
        for j, col in enumerate(row):
            booksheet.write(i, j, col)
    workbook.save('AOAreviewhe.xls')



def hebin(da):
    x = []
    x.append(da[0])
    n = 0
    for i in range(1, len(da)):
        if da[i][1] == x[n][1]:
            x[n][3] = da[i][3]+x[n][3]
        else:
            x.append(da[i])
            n = n+1
    return x


def main(path, path1):
    r = read_file(path1)
    text_save(r, path)

