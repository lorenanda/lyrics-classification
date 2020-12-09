""" Program that scrapes lyrics from metrolyrics.com"""

import time
import requests
from pyfiglet import Figlet
import pandas as pd
from bs4 import BeautifulSoup
import texthero as hero
from sklearn.naive_bayes import MultinomialNB
#from sklearn.model_selection import cross_val_score
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer


HEADERS = {'headers': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0"}
BASE_URL = "https://www.metrolyrics.com/"


songs_urls = []

def get_artist_link(artist):
    for artist in artist_input:
        artist_soup = BeautifulSoup(
            requests.get(f"https://www.metrolyrics.com/{artist}-lyrics.html").text, 
            'html.parser')

        for td in artist_soup.find_all('td'):
            for a in td.find_all('a'):
                songs_urls.append(a['href'])
        
        #pd.DataFrame(songs_urls).to_csv(f'data/{artist}_songurls.csv', sep='\t', index=False)
        
        time.sleep(2)



lyrics = []
artist_name = []

def get_lyrics(artist):
    for s in songs_urls:
        lyrics_soup = BeautifulSoup(requests.get(s).text,'html.parser')

        for v in lyrics_soup.find_all(attrs={'class':'verse'}):
            lyrics.append(v.get_text())
            artist_name.append(lyrics_soup.find('h2').get_text())

            #with open(f'./data/{artist}_metrolyrics.txt', 'w') as f:
                #f.writelines(lyrics)

        time.sleep(1)


def ask_user():
    if user_input in artist_input:
        print("This artist is already in the database.\nDo you want to scrape another one? (y/n)")
        # answer_input1 = input()
        # if answer_input1 == "n":
        #      break
        # elif answer_input1 == "yes":
        #     continue
    else:
        artist_input.append(user_input)
        artist_input.append(user_input2)
        print(f"OK, scraping {user_input} and {user_input2}...")
        get_artist_link(artist_input)
        print("Finished scraping the links!")
        print("Scraping lyrics...")
        get_lyrics(artist_input)
        print(f"Finished scraping the lyrics of {user_input} and {user_input2}!")


"""Command line interface where the user
can choose which artists to scrape"""

fig = Figlet(font='slant')
print(fig.renderText('Lyrics Scraper'))
print("Hi! I am a bot that can guess the artist from the lyrics.")
print("Test me! But let me prepare first. Enter the name of an artist:")

artist_input = []
user_input = input()
print("Enter the name of the second artist:")
user_input2 = input()

ask_user()

df = pd.DataFrame()
df["artist"] = artist_name
df["lyrics"] = lyrics
df['lyrics_clean'] = df['lyrics'].replace(r'\n',' ', regex=True)
df["lyrics_clean"] = hero.clean(df['lyrics'])  
X = df['lyrics_clean']
y = df['artist']

tfv = TfidfVectorizer()
X_tfv = tfv.fit_transform(X)
X_vec = pd.DataFrame(X_tfv.todense(), columns=tfv.get_feature_names())

mnb = MultinomialNB()
mnb.fit(X_vec, y)
mnb_score = mnb.score(X_vec, y)

def play():
    text = []
    print("Let's play! Write some lyrics:")
    lyrics_input = input().lower()
    text.append(lyrics_input)
    text_trans = tfv.transform(text)
    text_vector = pd.DataFrame(text_trans.todense(), columns=tfv.get_feature_names())
    mnb_pred = mnb.predict(text_vector)
    print('This sounds like ' + str(mnb_pred[0]).replace('-', ' ') + ". Am I right? (y/n)")
    check_prediction = input()
    if check_prediction == "y":
        print("Yay!")
    elif check_prediction == "n":
        print("Oh, that's embarrasing...")

def play_again():
    print("Wanna play again? (y/n)")
    ask_playagain = input()
    if ask_playagain == "y":
        play()
    elif ask_playagain == "n":
        print("Ok, that was fun!")

if __name__ == "__main__":
    play()
    play_again()
