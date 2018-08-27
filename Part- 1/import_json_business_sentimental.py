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
print 'a'

conn = sqlite3.connect('C:\Users\megha_5tn8db4\Desktop\School\DataScience\main project\yelpdb')
c = conn.cursor()

counter=0
commit_max=9000
commit_cont=0
commit_total=0
print 'b'
#
#with open('/home/noob41/Desktop/Yelp/Test_data/business_head.json') as data_file:    
#    data = json.load(data_file)
##pprint(data)    
#print data[0]['address']
#print data[0]['attributes']
#print data[1]['address']
#print data[1]['attributes']


#with open('/home/noob41/Desktop/Yelp/Test_data/business_head_2.json') as data_file:
#with open('/home/noob41/Desktop/Yelp/main_data_set/business.json') as data_file:
#	for line in data_file:	
#		data = json.loads(line)
#		#pprint(data)
#		list_key=[ k for k in data.keys() ]
#		list_val=[ v for v in data.values() ]
#		counter=counter+1
#		#print str(list_key)
#		#print str(data.values())
#		#query="Isert into yl_business_head "str(list_key)
#		#print query
#		#query= "INSERT INTO yl_business_head("list_key") values ("list_val")"
#		#print query
#		#print data['city']
#		#c.execute('INSERT INTO yl_business_head(city, neighborhood, name, business_id, longitude, hours, state, postal_code, categories, stars, address, latitude, review_count, attributes, type, is_open) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',list_val)
#		c.execute('INSERT INTO yl_business_head(city, neighborhood, name, business_id, longitude, hours, state, postal_code, categories, stars, address, latitude, review_count, attributes, type, is_open) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(data['city'],data['neighborhood'],data['name'],data['business_id'],data['longitude'],str(data['hours']),data['state'],data['postal_code'],str(data['categories']),data['stars'],data['address'],data['latitude'],data['review_count'],str(data['attributes']),data['type'],data['is_open']))
#		commit_cont=commit_cont+1
#		#print "\nNEXTTTT\n"
#		if commit_cont == commit_max:
#			commit_total= commit_total + commit_cont
#			c.execute('UPDATE yla_commit_log SET commit_total = ?,commit_cont = ? WHERE job_id = "business_head"',(commit_total,commit_cont))
#			commit_cont = 0
#			conn.commit()
#			print "\ncommited :",commit_total
#

#conn.commit()
#conn.close()
pola = []
subj = []
review=''
polarity =''
subjectivity = ''
for row in c.execute('select distinct comm_text from yl_usr_review inner join yl_business_head on yl_usr_review.business_id=yl_business_head.business_id  WHERE yl_business_head.city="Las Vegas" or yl_business_head.city="Phoenix" LIMIT 2000'):
    print 'x'
    review+=str(row)
    print 'y'
    a=review.split()
    blob=TextBlob(str(a))
    pola1=blob.sentiment.polarity
    print 'c'
    pola.append(pola1)
    polarity=([ round(num, 5) for num in pola ])
    #print type(polarity)
    subj1=blob.sentiment.subjectivity
    subj.append(subj1)
    subjectivity=([ round(num, 5) for num in subj ]) 
    print 'z'    
    #else:
        #print "More than 10"
        #break
        #polarity graph
#print len(review)  
#print subjectivity,polarity
plt.hist(polarity, bins=15, alpha=0.75)
plt.xlabel('polarity score USA')
plt.ylabel('REVIEWS')
plt.grid(True)
plt.savefig('polarity_USA.pdf')
plt.show()
print 'e'
        
        #subjectivity graph
plt.hist(subjectivity, bins=15, alpha=0.75)
plt.xlabel('subjectivity score USA')
plt.ylabel('REVIEWS')
plt.grid(True)
plt.savefig('subjectivity_USA.pdf')
plt.show() 
    #print len(review)        

print 'f' 

        
        
        

