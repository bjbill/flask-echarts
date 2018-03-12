# -*- coding: UTF-8 -*-

import sqlite3
import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()

DB_FILE_PATH = 'tyc-sh-0301.db'

conn = sqlite3.connect(DB_FILE_PATH)
cu = conn.cursor()

sql1 = "SELECT company_name as cname , organization_code AS cid FROM baseinfo"
cu.execute(sql1)
r1 = cu.fetchall()


# sql2 = ("SELECT invested_company FROM inverst WHERE (company_stat != '吊销，未注销' "
#       "and company_stat != '吊销' and company_stat != '注销' )"
#       " EXCEPT SELECT COMPANY_NAME"
#       " FROM baseinfo"
#        )

sql2 = ("SELECT baseinfo.company_name as holder,"
        "inverst.invested_company as inc FROM inverst, baseinfo "
        "WHERE (inverst.holder_org_id = baseinfo.organization_code)"
)
cu.execute(sql2)
r2 = cu.fetchall()


# 将baseinfo中的公司加入图中
for cname, cid in r1:

   G.add_node(cname, cid=cid)


# 将inverst中关系加入图中
for holder, inc in r2:

    G.add_edge(holder, inc)

print("打印G的节点list，带附加属性./n %s" %G.nodes(data=True))
print(G.nodes())
print(G.edges())
print('节点数:%s，边数:%s' %(G.number_of_nodes(), G.number_of_edges()))
print('节点数:{}，边数:{}'.format(G.number_of_nodes(), G.number_of_edges()))
# '节点0的邻居节点：
g = nx.neighbors(G,'国家能源投资集团有限责任公司')
print([x for x in g])


print(nx.degree(G))

print(G.node)
#print(G.node[''])
#print(G.node['']['cid']) # ['文本'] 因为直接用文本作为节点名称

#nx.draw(G, data=True)
#plt.show()

plt.figure() #创建一幅图
# nx.draw(G, node_color='y', with_labels=True, node_size=10)
#node_color='y'表示绘制节点的颜色为黄色，默认为红色;with_labels=True使节点上显示节点的名字，默认为False;node_size设置节点大小，默认为300
nx.draw(G, node_color='y', node_size=10)
plt.show()