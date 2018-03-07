#!/usr/bin/env python
# encoding: utf-8


"""
@version: v1.0
@author: zz
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: nx matpolot test.py
@time: 2018/3/7 11:16
"""
import networkx as nx
import matplotlib.pyplot as plt

# matplotlib ver 2.1.2

G = nx.Graph()                 #建立一个空的无向图G
G.add_node(1)                  #添加一个节点1
G.add_edge(2, 3)                #添加一条边2-3（隐含着添加了两个节点2、3）
G.add_edge(3, 2)                #对于无向图，边3-2与边2-3被认为是一条边
print("nodes:", G.nodes())      #输出全部的节点： [1, 2, 3]
print("edges:", G.edges())      #输出全部的边：[(2, 3)]
print("number of edges:", G.number_of_edges())   #输出边的数量：1
nx.draw(G)
plt.savefig("wuxiangtu.png")
plt.show()
