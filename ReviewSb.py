import re
import csv
import xlrd
import xlwt


def read_file(path):
    # path = 'D:/Download/WorkDate/AP/APreview.xlsx'
    exdata = xlrd.open_workbook(path)
    sheet = exdata.sheet_by_index(0)
    date = []
    for i in range(0, sheet.nrows):
        a = []
        a.append(sheet.row_values(i)[0])
        a.append(sheet.row_values(i)[1])
        a.append(sheet.row_values(i)[2])
        a.append(sheet.row_values(i)[3])
        date.append(a)
    date.remove(date[0])
    return date


def datepx(data):
    months = [['Jan', 1], ['Feb', 2], ['Mar', 3], ['Apr', 4], ['May', 5], ['Jun', 6], ['Jul', 7], ['Aug', 8], ['Sep', 9], ['Oct', 10], ['Nov', 11], ['Dec', 12]]
    data1 = data[0][2]
    year1 = eval(data1[-4:])
    day1 = eval(data1[-8:-6])
    month1 = data1[0:3]
    for i in months:
        if month1 == i[0]:
            month1 = i[1]
    num = 1
    while num < len(data):
        for n in range(1, len(data)):
            data2 = data[n][2]
            year2 = eval(data2[-4:])
            day2 = eval(data2[-8:-6])
            month2 = data2[0:3]
            for j in months:
                if month2 == j[0]:
                    month2 = j[1]
                    break
            if year1 > year2:
                data[n], data[n - 1] = data[n - 1], data[n]
            elif year1 == year2:
                if month1 > month2:
                    data[n], data[n - 1] = data[n - 1], data[n]
                elif month1 == month2:
                    if day1 > day2:
                        data[n], data[n - 1] = data[n - 1], data[n]
            year1 = year2
            day1 = day2
            month1 = month2
        num += 1

    return data


def read_view(date):
    months = [['Jan', 1], ['Feb', 2], ['Mar', 3], ['Apr', 4], ['May', 5], ['Jun', 6], ['Jul', 7], ['Aug', 8],
              ['Sep', 9], ['Oct', 10], ['Nov', 11], ['Dec', 12]]
    for n in range(len(date)):
        data1 = date[n][2]
        year1 = eval(data1[-4:])
        day1 = eval(data1[-8:-6])
        month1 = data1[0:3]
        for i in months:
            if month1 == i[0]:
                month1 = i[1]
        x = str(year1)+'-'+str(month1)+'-'+str(day1)
        date[n][2] = x
        pf = re.findall(r"\d", date[n][1])
        date[n][1] = eval(pf[0])

    return date


def exal(DATA, path, re_name):
    workbook = xlwt.Workbook(encoding='utf-8')
    booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)
    for i, row in enumerate(DATA):
        for j, col in enumerate(row):
            booksheet.write(i, j, col)
    workbook.save(path+re_name)


def text_save(data):
    for i in range(1, len(data)):
        with open(str(i)+'.txt', 'a') as file_handle:
            file_handle.write(data)
            file_handle.write('\n')


def main(path, exalname):
    # path = 'D:/Download//WorkDate/PSP/PSPreviews.xlsx'
    r = read_file(path+'reviews.xlsx')
    # d = datepx(r)
    rv = read_view(r)
    exal(rv, path, exalname)