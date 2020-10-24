from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
from random import randrange
import numpy as np

headers = {'headers': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0"}
#base_url = f"https://www.metrolyrics.com/{band}-lyrics.html"
#artist = input("What artist do you want to scrape? ")
artist = ('metallica')


def get_artist_link(artist):
# Get a list of song links
for b in artist:
    songs_urls = []
    artist_soup = BeautifulSoup(requests.get(f"https://www.metrolyrics.com/{artist}-lyrics.html").text,'html.parser')
        
    for td in artist_soup.find_all('td'):
        for a in td.find_all('a'):
            songs_urls.append(a['href'])
    
    pd.DataFrame(songs_urls).to_csv(f'{artist}_songurls.csv', sep='\t', index=False)
    
    time.sleep(1)


def get_lyrics(artist):
    # Get a list of song lyrics
    for s in songs_urls:
        time.sleep(1)
        lyrics = []
        lyrics_soup = BeautifulSoup(requests.get(s).text,'html.parser')
            
        for v in lyrics_soup.find_all(attrs={'class':'verse'}):
            lyrics.append(v.get_text())
        
        with open(f'{artist}_metrolyrics.txt', 'w') as f:
            f.writelines(lyrics)