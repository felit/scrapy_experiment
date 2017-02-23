#-*- coding:utf8 -*-
import solr
conn = solr.Solr("http://localhost:8983/solandra")
# select = solr.SearchHandler(conn, "/select")
doc = {"title": "mydoc", "title": "Me",'url':'test url'}
conn.add(doc)

r = conn.select('title:Me', hl_simple_post='</pre>')
print r