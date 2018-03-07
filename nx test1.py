# coding:utf-8

import matplotlib as mpl
mpl.use('TkAgg') # matplotlib v 2.2 需要，2.1.2 不需要
import matplotlib.pyplot as plt
decisionNode = dict(boxstyle="sawtooth", fc='0.8') # 决策节点描述
leafNode = dict(boxstyle='round4', fc='0.8') # 叶子节点描述
arrow_args = dict(arrowstyle="<-") # 箭头描述

# 绘制节点四个参数： 节点描述，节点中心坐标， 父节点中心坐标， 节点类型
def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction',xytext=centerPt, textcoords='axes fraction',
                            va="center", ha="center", bbox=nodeType, arrowprops=arrow_args)
def createPlot():
    fig = plt.figure(1, facecolor='white') # 创建一个新图像
    fig.clf()                               # 清空绘图区
    createPlot.ax1 = plt.subplot(111, frameon=False)
    plotNode(u'决策节点', (0.5, 0.1), (0.1, 0.5), decisionNode)
    plotNode(u'叶节点', (0.8, 0.1), (0.3, 0.8), leafNode)
    plt.show()

createPlot()