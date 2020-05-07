import xlrd
import langid



def read_file(path):
    exdata = xlrd.open_workbook(path)
    sheet = exdata.sheet_by_index(0)
    data = []
    for i in range(0, sheet.nrows):
        line = sheet.row_values(i)[0]
        lineTuple = langid.classify(line)
        if lineTuple[0] == 'en':
            data.append(line)
    return data


if __name__ == '__main__':
    a = read_file('data/UB/28bogu.xlsx')
    for i in a:
        if 'service' in i and 'time' in i:
            print(i)