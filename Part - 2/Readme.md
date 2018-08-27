# Yelp Challenge (Part 2)

Part 2 of the Yelp Challenge I, along with my classmates mainly worked on how can we help business based on the just yelper reviews.
To demonstrate this, we choose 3 hotels and we concentrated on the reviews of these 3 hotels to provide the right feedback.

# 1. Project Proposal
Using Yelp’s businesses and reviews datasets, we attempt to answer the following question: 

1. What are the restaurant's’ biggest problems which brings down the ratings the most, based on customer reviews?


Business Dataset: The business dataset provides information about different businesses from different countries. 
Review Dataset:   The review dataset provides information about the different reviews posted by different users for different business establishments. 


# 2.Technology Used
We use 3 main Python libraries:
1.	NLTK
2.	Sklearn (KNN &TF-IDF)
3.	TextBlob


NLTK (Natural Language Toolkit) is a suite of libraries and programs for symbolic and statistical natural language processing (NLP) for English written in the Python programming language. This tool allows us import word_tokenize from nltk, import PorterStemmer from nltk. stem and import stopwords from nltk.corpus. 
Sklearn, a Machine Learning library in Python is a simple and efficient tool for data mining and data analysis.  Sklearn library provides us with function such as Kmeans and TfidfVectorizer thru which we can perform analysis on the data.
Textblob, which is our last tool, provides us with text translation as the reviews come from different countries.

To collect and analyze the keywords in the businesses and review dataset, we apply text mining as one of our technologies. 
Using K-means clustering, we are able to tell the most frequent keywords and problems customer mentioned in their reviews and collect the most influential problems restaurants always have. 


# 3. Code Description

| Code File     | Description   |
| ------------- |:-------------:| 
| main.py |EDA of businesses based on their reviews  |


# 4. Data Source
https://www.yelp.com/dataset_challenge
