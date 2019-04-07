import matplotlib.pyplot as plt
import numpy as np
from os import path
from matplotlib.font_manager import _rebuild
path_file = path.dirname(path.realpath(__file__))
_rebuild()  # reload一下
# from pylab import mpl

# mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
# mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
# coding:utf-8


def chart(names, values):

    plt.rcdefaults()
    fig, ax = plt.subplots()

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    # Example data
    # people = (u'旺旺', 'Dick', 'Harry', 'Slim', 'Jim')
    # y_pos = np.arange(len(people))
    # performance = 3 + 10 * np.random.rand(len(people))
    # error = np.random.rand(len(people))

    # ax.barh(y_pos, performance, xerr=error, align='center',
    #         color='green', ecolor='black')
    # ax.set_yticks(y_pos)
    # ax.set_yticklabels(people)
    # ax.invert_yaxis()  # labels read top-to-bottom
    # ax.set_xlabel('Performance')
    # ax.set_title('How fast do you want to go today?')

    ax.barh(names, values)
    plt.savefig(path_file + '/'+'re.png')
    plt.show()
