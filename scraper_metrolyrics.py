""" 
Program that scrapes lyrics from metrolyrics.com
"""

import time
import requests
import pandas as pd
import csv
from bs4 import BeautifulSoup
import texthero as hero
import spacy
import re
from pyfiglet import Figlet
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

HEADERS = {'headers': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0"}
BASE_URL = f"https://www.metrolyrics.com/{band}-lyrics.html"


"""
This function scrapes the lyrics links
of an artist page and exports them in a csv file.
"""
songs_urls = []
def get_artist_link(artist):
    for artist in artist_input:
        #songs_urls = []
        artist_soup = BeautifulSoup(requests.get(f"https://www.metrolyrics.com/{artist}-lyrics.html").text,'html.parser')
            
        for td in artist_soup.find_all('td'):
            for a in td.find_all('a'):
                songs_urls.append(a['href'])
        
        pd.DataFrame(songs_urls).to_csv(f'{artist}_songurls.csv', sep='\t', index=False)
        
        time.sleep(1)



"""
This function scrapes the lyrics of each song in the artist list.
"""
lyrics = []
artist_name = []
def get_lyrics(artist):
    for s in songs_urls:
        time.sleep(1)
        lyrics_soup = BeautifulSoup(requests.get(s).text,'html.parser')
            
        for v in lyrics_soup.find_all(attrs={'class':'verse'}):
            lyrics.append(v.get_text())
        
        for b in lyrics_soup.find_all('h2'):
            artist_name.append(b.get_text())
        
        df = pd.DataFrame(list(zip(lyrics, artist_name)), columns=['lyrics','artist'])

        with open(f'{artist}_metrolyrics.txt', 'w') as f:
            f.writelines(lyrics)


# Clean the lyrics
def clean_text(review, model):
    new_doc = ''
    doc = model(review)
    for word in doc:
        if not word.is_stop and word.is_alpha:
            new_doc = f'{new_doc} {word.lemma_.lower()}'
    return new_doc



"""
Command line interface
"""
fig = Figlet(font='slant')
print(fig.renderText('Scrape & Predict'))
artist_input = ['the-knife']


"""
Prediction model for input lyrics
"""
df = pd.read_csv('/home/lorena/Documents/bootcamp/W04/lyrics_artists_clean.csv')

X = df['lyrics_clean']
y = df['artist']
    
tfv = TfidfVectorizer()
    
X_tfv = tfv.fit_transform(X)
X_vec = pd.DataFrame(X_tfv.todense(), columns=tfv.get_feature_names())
    
mnb = MultinomialNB()
mnb.fit(X_vec, y)
mnb_score = mnb.score(X_vec, y)

#  
while True:
    text = []
    lyrics_input = input('Write some lyrics: ').lower()
    text.append(lyrics_input)
    text_trans = tfv.transform(text)
    text_vector = pd.DataFrame(text_trans.todense(), columns=tfv.get_feature_names())
    mnb_pred = mnb.predict(text_vector)
    print('This sounds like '+str(mnb_pred[0]).replace('-', ' '))