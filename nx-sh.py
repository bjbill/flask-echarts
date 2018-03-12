#!/usr/bin/env python
# encoding: utf-8


"""
@version: v1.0
@author: zz
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: nx-sh.py
@time: 2018/3/9 15:40
"""

import networkx as nx
import csv
from networkx.readwrite import json_graph
from pyecharts import Graph

g = nx.Graph()


with open('tyc-SH01-node.csv', newline='', encoding='utf-8') as csvfile: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default;
    # in version 3.6: Returned rows are now of type OrderedDict.
    dr = csv.DictReader(csvfile) # comma is default delimiter
#   to_db = [(i['col1'], i['col2']) for i in dr]
    for row in dr:
        g.add_node(row['Id'], name=row['Label'])

with open('tyc-SH01-eg.csv', newline='', encoding='utf-8') as csvfile1: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default;
    # in version 3.6: Returned rows are now of type OrderedDict. Source,Target
    dr = csv.DictReader(csvfile1) # comma is default delimiter
#   to_db = [(i['col1'], i['col2']) for i in dr]
    for row in dr:
        g.add_edge(row['Source'], row['Target'])


g_data = json_graph.node_link_data(g)
#print(g_data)
#eg = Graph('公司结构图')
#eg.add('SHENHUA', nodes=g_data['nodes'], links=g_data['links'])
#eg.render()

graph = Graph("公司关系图", width=1200, height=600)
graph.add("SHENHUA", nodes=g_data['nodes'], links=g_data['links'], label_pos="right",
          graph_repulsion=50, is_legend_show=False, edgeSymbol=['circle', 'arrow'],graph_edge_symbolsize=[4, 10],
          line_curve=0, label_text_color=None)
graph.render()