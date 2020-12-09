# Predicting the artist from web-scraped music lyrics

This project was completed in week 4 of the Data Science Bootcamp at Spiced Academy.

## Description
The goal is to build a web-scraper to scrape music lyrics, preprocess the obtained text, then predict the artist from some lyrics that a user writes in the command line. For testing, I scraped around 100 song lyrics of Metallica and Iron Maiden from [metrolyrics.com](www.metrolyrics.com) and used the texts to train a Multinomial Naive Bayes Classifier, which predicted the band from input lyrics with 68% accuracy.

You can read more details about this project [on my blog](https://lorenaciutacu.com/2020/10/24/week-4-datasciencebootcamp/).

## Files
- [Scraper and prediction game](https://github.com/lorenanda/lyrics-classification/blob/main/scrape_and_predict.py)
- [Linguistic analysis with spaCy and NLTK](https://github.com/lorenanda/lyrics-classification/blob/main/text_analysis_lyrics.ipynb)
- The list of songs and lyrics is not included, for copyright purposes.

## How to use
1. Clone this repo: `git clone https://github.com/lorenanda/lyrics-classification.git`
2. Install the necessary libraries: `pip install -r requirements.txt`
3. Run `scrape_and_predict.py` and follow the bot's instructions

## Demo
<img src = "https://github.com/lorenanda/lyrics-classification/blob/main/images/demo.gif" width="450px" height="400px">
