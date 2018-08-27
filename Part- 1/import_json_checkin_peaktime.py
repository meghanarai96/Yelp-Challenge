import json
import sqlite3
from textblob import TextBlob
import matplotlib.pyplot as plt
import os,glob
from scipy.misc import imread
from wordcloud import WordCloud,STOPWORDS
import nltk
from pandas import ExcelWriter
from pprint import pprint
from datetime import datetime
import xlsxwriter


conn = sqlite3.connect('C:\Users\hanee\Dropbox\School\Data Science\Project\Final Project\yelpdb')
c = conn.cursor()

counter=0
commit_max=9000
commit_cont=0
commit_total=0

'''
#
with open('/home/noob41/Desktop/Yelp/Test_data/business_head.json') as data_file:    
#    data = json.load(data_file)
##pprint(data)    
#print data[0]['address']
#print data[0]['attributes']
#print data[1]['address']
#print data[1]['attributes']


#with open('/home/noob41/Desktop/Yelp/Test_data/checkin.json') as data_file:
with open('/home/noob41/Desktop/Yelp/main_data_set/checkin.json') as data_file:
#with open('/home/noob41/Desktop/Yelp/') as data_file:
	for line in data_file:
		data = json.loads(line)
		#pprint(data)
		list_key=[ k for k in data.keys() ]
		list_val=[ v for v in data.values() ]
		counter=counter+1
		#print str(list_key)
		#print str(data.values())
		for n in data["time"]:
		    d,t,ch=re.split('-|:',n)
		    #print ch
		    #print d
		    #print t
		    #print data["type"];
		    #print data["business_id"]
		    c.execute('INSERT INTO yl_checkin(business_id, type, c_day, c_time, checkin) values (?,?,?,?,?)',(data["business_id"],data["type"],d,t,ch))
		    if commit_cont >= commit_max:
		    	commit_total= commit_total + commit_cont
		    	c.execute('UPDATE yla_commit_log SET commit_total = ?,commit_cont = ? WHERE job_id = "business_head"',(commit_total,commit_cont))
		    	commit_cont = 0
		    	conn.commit()
		    	print "\ncommited :",commit_total
conn.commit()
conn.close()
'''
pola = []
subj = []

import nltk
from collections import Counter


"""
USA
"""
wordsUSA = []
dictUSA = Counter()

for row in c.execute('select c_time from yl_checkin inner join yl_business_head on yl_checkin.business_id=yl_business_head.business_id WHERE yl_business_head.city="Las Vegas" or yl_business_head.city="Phoenix" LIMIT 10000'):
    wordsUSA.append(row)
    dictUSA.update(row)

print "USA"
print dictUSA

#freq graph    
freq=nltk.FreqDist(wordsUSA)
freq.plot(30)

#bar graph
plt.bar(range(len(dictUSA)), dictUSA.values())
plt.xticks(range(len(dictUSA)), dictUSA.keys())
plt.xlim([0,24])

plt.xlabel('Hour')
plt.ylabel('Amount of Check-ins')
plt.savefig('checkintimes_USA.png',dpi=300,bbox_inches='tight')

plt.show()



"""
UK
"""
wordsUK = []
dictUK = Counter()

for row in c.execute('select c_time from yl_checkin inner join yl_business_head on yl_checkin.business_id=yl_business_head.business_id WHERE yl_business_head.city="Edinburgh" LIMIT 10000'):
    wordsUK.append(row)
    dictUK.update(row)

print "UK"
print dictUK

#freq graph    
freq=nltk.FreqDist(wordsUK)
freq.plot(30)

#bar graph
plt.bar(range(len(dictUK)), dictUK.values())
plt.xticks(range(len(dictUK)), dictUK.keys())
plt.xlim([0,24])

plt.xlabel('Hour')
plt.ylabel('Amount of Check-ins')
plt.savefig('checkintimes_UK.png',dpi=300,bbox_inches='tight')

plt.show()



"""
Germany
"""
wordsGER = []
dictGER = Counter()

for row in c.execute('select c_time from yl_checkin inner join yl_business_head on yl_checkin.business_id=yl_business_head.business_id WHERE yl_business_head.city="Stuttgart" or yl_business_head.city="Ditzingen" or yl_business_head.city="Hemmingen" LIMIT 10000'):
    wordsGER.append(row)
    dictGER.update(row)

print "GERMANY"
print dictGER

#freq graph    
freq=nltk.FreqDist(wordsGER)
freq.plot(30)

#bar graph
plt.bar(range(len(dictGER)), dictGER.values())
plt.xticks(range(len(dictGER)), dictGER.keys())
plt.xlim([0,24])

plt.xlabel('Hour')
plt.ylabel('Amount of Check-ins')
plt.savefig('checkintimes_GER.png',dpi=300,bbox_inches='tight')

plt.show()




"""
Canada
"""
wordsCAN = []
dictCAN = Counter()

for row in c.execute('select c_time from yl_checkin inner join yl_business_head on yl_checkin.business_id=yl_business_head.business_id WHERE yl_business_head.city="Toronto" or yl_business_head.city="Sainte-Anne-de-Bellevue" LIMIT 10000'):
    wordsCAN.append(row)
    dictCAN.update(row)

print "CANADA"
print dictCAN

#freq graph    
freq=nltk.FreqDist(wordsCAN)
freq.plot(30)

#bar graph
plt.bar(range(len(dictCAN)), dictCAN.values())
plt.xticks(range(len(dictCAN)), dictCAN.keys())
plt.xlim([0,24])

plt.xlabel('Hour')
plt.ylabel('Amount of Check-ins')
plt.savefig('checkintimes_CAN.png',dpi=300,bbox_inches='tight')

plt.show()