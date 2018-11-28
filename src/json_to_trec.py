# -*- coding: utf-8 -*-


import json
# if you are using python 3, you should 
import urllib.request, urllib.error
import urllib


filename = 'D:\\MS\\1stSem\IR\\project_3\\project3_data\\testqueries.txt'

with open(filename, encoding="utf-8-sig") as f:
    content = f.readlines()
    newList = []
    newList1 =[]
    newList2 = []
    count = 0
    for i in content:
        count = count+1
        newList = i.split(' ', 1)[1]
        list2 = urllib.parse.quote_plus(newList)
        inurl = 'http://localhost:8983/solr/BM25/select?q='+list2+'&fl=id%2Cscore&wt=json&indent=true&rows=20&defType=dismax'

        # outfn = 'D:\\MS\\1stSem\IR\\project_3\\project3_data\\BM25\\' + i.split(' ', 1)[0] + '.txt'
        outfn = 'D:\\MS\\1stSem\IR\\project_3\\project3_data\\BM25\\' + str(count) + '.txt'
        outf = open(outfn, 'a+', encoding='utf-8')
        outf.seek(0)
        outf.truncate()
        qid = i.split(' ', 1)[0]
        IRModel = 'BM25'
        try:
            data = urllib.request.urlopen(inurl)
            content = data.read()
            docs = json.loads(content.decode('utf-8'))
            docs = docs['response']['docs']
            rank = 1
            for doc in docs:
                outf.write(qid + '' + ' Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\n')
                rank += 1
        except urllib.error.URLError as e:
            print(e)
            outf.close()







# qid = ["001", "002", "003", "004", "005", "006", "007", "008", "009", "010", "011", "012", "013", "014", "015"]
# # change the url according to your own corename and query
# inurl = 'http://localhost:8983/solr/BM25/select?q=*%3A*&fl=id%2Cscore&wt=json&indent=true&rows=1000'
# #outfn = 'D:/MS/1stSem/IR/project_3/project3_data/BM25/'+(x)+'.txt'
# outfn = 'D:\\MS\\1stSem\IR\\project_3\\project3_data\\BM25\\' + (x) + '.txt'
#
# # change query id and IRModel name accordingly
# qid = (inurl)
# IRModel='BM25'
# outf = open(outfn, 'a+')
# outf.seek(0)
# outf.truncate()
# # data = urllib2.urlopen(inurl)
# # if you're using python 3, you should use
# try:
# 	data = urllib.request.urlopen(inurl)
# 	content = data.read()
# 	docs = json.loads(content.decode('utf-8'))
# 	docs = docs['response']['docs']
# 	rank = 1
# 	for doc in docs:
# 		outf.write(qid + '' + ' Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(
# 			doc['score']) + ' ' + IRModel + '\n')
# 		# outf.write(qid + '' + ' 0' + ' ' + str(doc['id']) + ' ' + str(rank) +'\n')
# 		rank += 1
# except urllib.error.URLError as e:
# 	outf.close()


