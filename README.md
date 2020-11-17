# Predicting the artist from web-scraped music lyrics

This project was completed in week 4 of the Data Science Bootcamp at Spiced Academy.

## Description
The goal is to build a web-scraper to scrape music lyrics, preprocess the obtained text, then predict the artist from some lyrics that a user writes in the command line. The built web-scraper scraped around 100 song lyrics of Metallica and Iron Maiden from [lyrics.com](www.lyrics.com). I used this text data to train a Multinomial Naive Bayes Classifier, which predicted the artist from lyrics with 68% accuracy.

## Files
- [Web-scraper](https://github.com/lorenanda/lyrics-classification/blob/main/classifier.ipynb)
- [Text preprocessing with spaCy, NLTK, TextHero](https://github.com/lorenanda/lyrics-classification/blob/main/preprocessing.ipynb)
- [Naive Bayes Classifier](https://github.com/lorenanda/lyrics-classification/blob/main/classifier.ipynb)
- [Linguistic analysis with spaCy and NLTK](https://github.com/lorenanda/lyrics-classification/blob/main/text_analysis_lyrics.ipynb)
- The list of songs and lyrics is not included, for copyright purposes.

## Demo
![demo](https://github.com/lorenanda/lyrics-classification/blob/main/lyrics_predictor_demo.gif)
