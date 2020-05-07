import ReviewSb as resb
import cs_web as csw
import LDAdata as lda
import Topicinrz as top

if __name__ == '__main__':
    APPname = ['ASK', 'FB', 'KW', 'PSP', 'SH', 'TFSE', 'UB', 'YT']
    for i in range(len(APPname)):
        name = APPname[i]
        # resb参数
        path = 'data/' + name + '/'
        exalname = 'reviewall.xlsx'
        # csw参数
        path1 = path + name + exalname
        appname = APPname[i]
        print('------'+appname+'------')
        # lda参数
        path2 = path + name + 'bogu.xls'
        # top参数
        rzpath = path + 'commit.txt'
        rzpath2 = path + 'changelog.txt'

        # resb.main(path+name, exalname)
        # pdc = input("Reviews is OK?(1 or 0)")
        csw.main(path + name, path1, appname)
        # pdl = input("CSW is OK? and then get lda(1 or 0)")
        # lda.main(path, path2)
        # pdt = input("bogu.xlsx is OK?(1 or 0)")
        t = top.main(path, rzpath, rzpath2, i+1)



