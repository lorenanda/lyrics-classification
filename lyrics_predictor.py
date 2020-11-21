import pandas as pd 
import numpy as np
from pyfiglet import Figlet
from sklearn.naive_bayes import MultinomialNB
#from sklearn.model_selection import cross_val_score
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer
#import webscraper

"""
Prediction model for input lyrics
"""

df["artist"] = artist_name
df["lyrics"] = lyrics

def clean_text(text):
    new_text = ""
    df["lyrics_clean"] = hero.clean(df['lyrics'])
    return new_text

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
    print('This sounds like ' + str(mnb_pred[0]).replace('-', ' '))