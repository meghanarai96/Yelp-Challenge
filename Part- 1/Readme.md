# Yelp Challenge (Part 1)

Yelp publishes customer reviews of local businesses, and it also provides services such as Yelp Reservations and the online food delivery service known as Eat24. Additionally, it provides data about businesses, helps train small businesses, and hosts social events. 


This project was a Data science project I collaborated with 2 other classmates.
We used a series of datasets which includes information from cities in select countries, and analyzed the data to capture various cultural and seasonal trends.

# 1. Project Proposal

Using Yelp’s dataset, we attempted to answer the following questions:

1.	What are the popular times and days to eat out in different countries? 

2.	What are the most common cuisines and topics in different countries? 

3.	Which countries have the harshest and/or nicest comments on the reviews? 

4.	What are the top 25 restaurants based on number of reviews and best reviews?

5.	How about 25 restaurants with the least and worst reviews? 

6.	What are the 10 cities where Yelp is used the most?


# 2. Technology Used

Python Libraries used:

1.    Sentimental analysis using TextBlob 

2.    Matplotlib 

3.    WordCloud 

4.    Natural Language Processing (NLTK)

Database used:

1.	SQLite


# 3. Code Description

| Code File     | Description   |
| ------------- |:-------------:| 
| import_json_checkin_peaktime.py     |EDA of peak checktime in different countries  |
| import_json_checkin_weekend_trends.py      | EDA of peak checktime in different countries on weekends|
| import_json_checkin_Wordcloud.p | Creates Wordcloud based on the cuisines Yelpers rave about in different countries |
| import_json_business_sentimental.py | Runs sentimental analysis on the yelpers reviews |


# 4. Data Source

https://www.yelp.com/dataset_challenge
