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


sql2 = ("SELECT invested_company FROM inverst WHERE (company_stat != '吊销，未注销' "
       "and company_stat != '吊销' and company_stat != '注销' )"
       " EXCEPT SELECT COMPANY_NAME"
       " FROM baseinfo")
cu.execute(sql2)
r2 = cu.fetchall()

i = 0
# 将baseinfo中的公司加入图中
for cname, cid in r1:

   G.add_node(i, cname=cname, cid=cid)
   i = i + 1

# 继续，将inverst中没有查询的公司（最末端的公司）加入图中
for cname in r2:

    G.add_node(i, cname=cname, cid="")
    i = i + 1


print(G.nodes(data=True))
print(G.node)
print(G.node[0])
print(G.node[0]['cname'])

#nx.draw(G, data=True)
#plt.show()