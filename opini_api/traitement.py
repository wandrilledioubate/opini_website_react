import emoji
import pandas as pd
import nltk
from tqdm import tqdm
from nltk.sentiment import SentimentIntensityAnalyzer
from datetime import datetime

def import_json(file):
    data = pd.read_json(file)
    return data

def import_json(file):
    with open(file, 'r') as f:
        data = json.load(f)
    return data


def delete_col(dataframe):
    data_del = dataframe.dropna(inplace=True)
    return data_del


def demojize_string(string):
    string = str(string)
    string = emoji.demojize(string)
    string = string.replace('_', ' ')
    string = string.replace(':', ' ')
    return string


def get_sentiment_score(row):
    facteur_note = 0.7
    facteur_titre = 0.3
    facteur_like = 0.4
    facteur_date_tres_ancienne = 0.1
    facteur_date_ancienne = 0.2                 
    facteur_date_relativement_ancienne = 0.3    
    facteur_date_récente = 0.5                  
    sia = SentimentIntensityAnalyzer() 

    text = demojize_string(row['text'])
    title = demojize_string(row['title'])

    text = nltk.word_tokenize(text)
    stopwords = nltk.corpus.stopwords.words("english")
    review = [w for w in text if w.lower() not in stopwords]
    review_str = ' '.join(review)


    score_text = sia.polarity_scores(review_str)
    score_title = sia.polarity_scores(title)

    like_score = 0

    if score_text['pos'] < 0.45:
        if 0 < float(row['votes']) < 10:
                like_score = 0.45
        if 10 < float(row['votes']) < 20:
                like_score = 0.4
        if 20 < float(row['votes']) < 30:
                like_score = 0.35
        if 30 < float(row['votes']) < 40:
                like_score = 0.3
        if 40 < float(row['votes']) < 50:
                like_score = 0.25
        if 50 < float(row['votes']) < 60:
                like_score = 0.2
        if 60 < float(row['votes']) < 70:
                like_score = 0.15
        if 70 < float(row['votes']) < 80:
                like_score = 0.1
        if 80 < float(row['votes']) < 90:
                like_score = 0.05
        if 90 < float(row['votes']):
                like_score = 0

    elif score_title['pos'] > 0.55:
        if 0 < float(row['votes']) < 10:
                like_score = 0.55
        if 10 < float(row['votes']) < 20:
                like_score = 0.6
        if 20 < float(row['votes']) < 30:
                like_score = 0.65
        if 30 < float(row['votes']) < 40:
                like_score = 0.7
        if 40 < float(row['votes']) < 50:
                like_score = 0.75
        if 50 < float(row['votes']) < 60:
                like_score = 0.8
        if 60 < float(row['votes']) < 70:
                like_score = 0.85
        if 70 < float(row['votes']) < 80:
                like_score = 0.9
        if 80 < float(row['votes']) < 90:
                like_score = 0.95
        if 90 < float(row['votes']):
                like_score = 1
    else:
        like_score = 0.5

    like_score = like_score * facteur_like

    date = datetime.strptime(row['date'], "%Y-%m-%d").date()

    date_tres_ancienne = datetime.strptime("2012-06-19", "%Y-%m-%d").date()
    date_ancienne = datetime.strptime("2019-06-19", "%Y-%m-%d").date()
    date_relativement_ancienne = datetime.strptime("2022-06-19", "%Y-%m-%d").date()

    if date < date_tres_ancienne:
        score_date = facteur_date_tres_ancienne

    elif date_tres_ancienne <= date < date_ancienne:
        score_date = facteur_date_ancienne

    elif date_ancienne <= date < date_relativement_ancienne:
        score_date = facteur_date_relativement_ancienne

    else:
        score_date = facteur_date_récente

    weighted_positive_score = (score_text['pos'] + (float(row['rating']) / 5) * facteur_note + score_title['pos']*facteur_titre +like_score + score_date) / (1 + facteur_note + facteur_titre + facteur_like + score_date)
    return weighted_positive_score


def get_sentiment_label(score):
    if score >= 0.75:
        return 'Very positive'
    elif 0.55 <= score < 0.75:
        return 'Positive'
    elif 0.45 >= score > 0.25:
        return 'Negative'
    elif score < 0.25:
        return 'Very negative'
    else:
        return 'Neutral'


def add_sentiment(df):
    df['score_sentiment'] = df.apply(get_sentiment_score, axis=1) 
    return df 

def add_label(df):
    df['score_label'] = df['score_sentiment'].progress_apply(get_sentiment_label)
    return df 


def treat(json_file):
    json_file = './output.son'
    data = import_json(json_file)
    data_del = delete_col(data)
    data_sentiment = add_sentiment(data_del)
    data_treated = add_label(data_sentiment)
    return data_treated



    


