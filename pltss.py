import matplotlib.pyplot as plt


if __name__ == '__main__':
    x = ['2018-12-12', '2018-12-15', '2018-12-18', '2018-12-21', '2018-12-23', '2018-12-25', '2018-12-28', '2018-12-31',
         '2019-1-3', '2019-1-6', '2019-1-9', '2019-1-12', '2019-1-15', '2019-1-18', '2019-1-21']
    squar = [1.7, -1.4, -2.2, 0.65, -0.3, -0.29, -0.15, -0.48, -0.4, -0.65, -0.41, -0.42, -0.1, -0.25, -0.29]
    plt_x = ['2018-12-12', '2018-12-21', '2018-12-28', '2019-1-6', '2019-1-15']
    if len(x) == len(squar):
        plt.plot(x, squar, color='#4146d5', linewidth=3.5)
        plt.ylabel(u'ARS(score)', fontsize=18)
        plt.xlabel(u'date', fontsize=15)
        plt.title(u'Uber', fontsize=20)
        plt.tick_params(axis='x', labelsize=18)
        plt.tick_params(axis='y', labelsize=15)
        plt.xticks(plt_x)
        plt.show()



# if __name__ == '__main__':
#     x = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
#     squar = [0.472, 0.509, 0.514, 0.561, 0.586, 0.638, 0.554, 0.524, 0.424, 0.0, 0.0]
#     plt.plot(x, squar, color='#4146d5', linewidth=3.5, marker='o', linestyle='solid')
#     plt.ylabel(u'Fhybrid', fontsize=15)
#     plt.grid(axis='y', linestyle='-.')
#     plt.xlabel(u'Threshold', fontsize=15)
#     plt.show()


# if __name__ == '__main__':
#     x = [3, 5, 7, 9, 11, 13, 15]
#     squar = [0.564, 0.641, 0.579, 0.525, 0.505, 0.476, 0.419]
#     plt_y = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
#     plt_x = [3, 5, 7, 9, 11, 13, 15]
#     plt.plot(x, squar, color='#4146d5', linewidth=3.5, marker='o', linestyle='solid')
#     plt.ylabel(u'Fhybrid', fontsize=15)
#     plt.grid(axis='y', linestyle='-.')
#     plt.xlabel(u'V t', fontsize=15)
#     plt.yticks(plt_y)
#     plt.xticks(plt_x)
#     plt.show()



# if __name__ == '__main__':
#     # -*- coding: utf-8 -*-
#     """
#     Created on Wed Dec  4 21:50:38 2019
#
#     @author: muli
#     """
#
#     import matplotlib.pyplot as plt
#     from pylab import *
#
#     mpl.rcParams['font.sans-serif'] = ['SimHei']  # 支持中文
#
#     names = ["1", "2", "3", "4", "5"]  # 刻度值命名
#
#     x = [1, 2, 3, 4, 5]  # 横坐标
#
#     y3 = [2, 3, 1, 4, 5]  # 纵坐标
#     y4 = [4, 6, 8, 5, 9]  # 纵坐标
#     y5 = [24, 27, 22, 26, 28]  # 纵坐标
#
#     f, (ax3, ax) = plt.subplots(2, 1, sharex=False)  # 绘制两个子图
#     plt.subplots_adjust(wspace=0, hspace=0.08)  # 设置 子图间距
#     ax.plot(x, y3, color='red', marker='o', linestyle='solid', label=u'1')  # 绘制折线
#     ax.plot(x, y4, color='g', marker='o', linestyle='solid', label=u'2')  # 绘制折线
#
#     plt.xticks(x, names, rotation=45)  # 刻度值
#     ax3.xaxis.set_major_locator(plt.NullLocator())  # 删除坐标轴的刻度显示
#
#     ax3.plot(x, y5, color='blue', marker='o', linestyle='solid', label=u'3')  # 绘制折线
#     ax3.plot(x, y3, color='red', marker='o', linestyle='solid', label=u'1')  # 起图例作用
#     ax3.plot(x, y4, color='g', marker='o', linestyle='solid', label=u'2')  # 起图例作用
#
#     ax3.set_ylim(21, 30)  # 设置纵坐标范围
#     ax.set_ylim(0, 10)  # 设置纵坐标范围
#
#     ax3.grid(axis='both', linestyle='-.')  # 打开网格线
#     ax.grid(axis='y', linestyle='-.')  # 打开网格线
#
#     ax3.legend()  # 让图例生效
#     plt.xlabel(u"λ")  # X轴标签
#     plt.ylabel("mAP")  # Y轴标签
#
#     ax.spines['top'].set_visible(False)  # 边框控制
#     ax.spines['bottom'].set_visible(True)  # 边框控制
#     ax.spines['right'].set_visible(False)  # 边框控制
#
#     ax3.spines['top'].set_visible(False)  # 边框控制
#     ax3.spines['bottom'].set_visible(False)  # 边框控制
#     ax3.spines['right'].set_visible(False)  # 边框控制
#
#     # ax.tick_params(labeltop='off')
#
#     # # 绘制断层线
#     # d = 0.01  # 断层线的大小
#     # kwargs = dict(transform=ax3.transAxes, color='k', clip_on=False)
#     # ax3.plot((-d, +d), (-d, +d), **kwargs)  # top-left diagonal
#     #
#     # kwargs.update(transform=ax.transAxes, color='k')  # switch to the bottom axes
#     # ax.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
#
#     plt.show()
