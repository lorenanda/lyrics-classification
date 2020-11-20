""" 
Program that scrapes lyrics from metrolyrics.com
"""

import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from pyfiglet import Figlet


HEADERS = {'headers': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0"}
BASE_URL = "https://www.metrolyrics.com/"


"""
This function scrapes the lyrics links
of an artist page and exports them in a csv file.
"""

songs_urls = []

def get_artist_link(artist):
    for artist in artist_input:
        artist_soup = BeautifulSoup(
            requests.get(f"https://www.metrolyrics.com/{artist}-lyrics.html").text, 
            'html.parser')

        for td in artist_soup.find_all('td'):
            for a in td.find_all('a'):
                songs_urls.append(a['href'])
        
        pd.DataFrame(songs_urls).to_csv(f'data/{artist}_songurls.csv', sep='\t', index=False)
        
        time.sleep(2)


"""
This function scrapes the lyrics of each song in the artist list.
"""

lyrics = []
artist_name = []

def get_lyrics(artist):
    for s in songs_urls:
        lyrics_soup = BeautifulSoup(requests.get(s).text,'html.parser')

        for v in lyrics_soup.find_all(attrs={'class':'verse'}):
            lyrics.append(v.get_text())
            artist_name.append(lyrics_soup.find('h2').get_text())

            with open(f'./data/{artist}_metrolyrics.txt', 'w') as f:
                f.writelines(lyrics)

        time.sleep(1)


"""
Command line interface where the user 
can choose which artists to scrape
"""

fig = Figlet(font='slant')
print(fig.renderText('Lyrics Scraper'))
print("What artist's song lyrics do you want to get?\n")

artist_input = []
user_input = input()

if user_input in artist_input:
    print("This artist is already in the database.\nDo you want to scrape another one? (y/n)")
    # answer_input1 = input()
    # if answer_input1 == "n":
    #      break
    # elif answer_input1 == "yes":
    #     continue
else:
    print(f"OK, scraping {user_input}...")
    artist_input.append(user_input)
    get_artist_link(artist_input)
    print("Finished scraping the links!")
    print("Scraping lyrics...")
    get_lyrics(artist_input)
    print("Finished scraping the lyrics!\nDo you want to scrape another artist? (y/n)")
    answer_input = input()
    if answer_input == "n":
        print("OK, then my job is done.")
    elif answer_input == "y":
        print("Maybe later.")
    else:
        print("Nonsense! Just give me a y for yes or n for no.")
