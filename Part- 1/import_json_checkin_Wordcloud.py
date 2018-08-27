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
review=''
global STOPWORDS
for row in c.execute('select distinct categories from yl_business_head WHERE city="Hemmingen" or city="Stuttgart" or city="Ludwigsburg"  or    city="Esslingen am Neckar" and categories like "%Food%" and categories like "%Restaurants%"'):
      
        review+='{}'.format(row)
        #review=review.split()
        
 

         
STOPWORDS = ('Restaurants','Food','Restaurant')
#a = review.decode('ascii','ignore')

def cleanWords(s):
    s = s.replace('(', '').replace(')', '').replace("u'", "").replace('"', '').replace("'", "").replace('u[', ' ').replace(']', '')
    return s

a = cleanWords(review)
#b = a.replace(' ', '')
#c = b.split(',')

#print type(c)
#print a


wordcloud = WordCloud(
                          stopwords=STOPWORDS,
                          max_font_size=40,
                          background_color='white').generate(a)
        #print 'a8'
        #print comwords

        # Display the generated image:
plt.figure()
plt.imshow(wordcloud)
plt.savefig('Cleaveland_wordcloud_1.png',dpi=300)
plt.axis('off')
plt.show()

