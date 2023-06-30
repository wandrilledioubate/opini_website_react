from scrapping import scrap
from flask import Flask, request, jsonify
import json
import pandas as pd 
import tensorflow_hub as hub
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup
import re
import random
import csv
import pandas as pd
import numpy as np
import tensorflow_hub as hub
import keras.layers
from keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import tensorflow_text as text
import os


import ssl
ssl._create_default_https_context = ssl._create_unverified_context

app = Flask(__name__)
cors = CORS(app)


@app.route('/predict', methods=['POST'])
def predict():
    url = request.json['url']
    scrap(url)
    df_balanced = pd.read_csv('./data_comment.csv')
    if 'Unnamed: 0' in df_balanced.columns:
        df_balanced.drop(['Unnamed: 0'], axis=1, inplace=True)

    print(df_balanced)
    # Convertir les labels en entiers avec LabelEncoder.
    le = LabelEncoder()
    labels_encoded = le.fit_transform(df_balanced['label_sentiment'])

    # Utiliser ces entiers pour créer les labels one-hot.
    labels_one_hot = to_categorical(labels_encoded, num_classes=5)

    X_train, X_test, y_train, y_test = train_test_split(df_balanced['text'], labels_one_hot, test_size= 0.3)
    bert_preprocess = hub.KerasLayer("https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3")
    # bert_encoder = hub.KerasLayer("https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/4") 
    new_model = keras.models.load_model("modelBERT_02.h5", custom_objects={'KerasLayer':hub.KerasLayer})
    new_data = pd.read_csv("reviews.csv")
    new_data_text = new_data['text']


    # Preprocessing the text
    # bert_inputs = bert_preprocess(new_data_text)

    # Making the prediction
    predictions = new_model.predict(new_data_text)

    # Convertir les prédictions en labels lisibles
    predicted_labels_encoded = np.argmax(predictions, axis=-1)
    predicted_labels = le.inverse_transform(predicted_labels_encoded)

    s = predicted_labels.mean()
    m = s/len(predicted_labels) * 100

    '''
    phrases_df = pd.read_csv('./phrase.csv')


    # Selectionner des phrases positives et négatives au hasard pour le type de lieu donné
    positive_phrases = phrases_df[(phrases_df['type'] == type_lieu) & (phrases_df['sentiment'] == 'positif')]
    negative_phrases = phrases_df[(phrases_df['type'] == type_lieu) & (phrases_df['sentiment'] == 'negatif')]

    random_positive_phrases = positive_phrases.sample(3)['phrase'].tolist()
    random_negative_phrases = negative_phrases.sample(3)['phrase'].tolist()
    ''' 

    if os.path.isfile('./reviews.csv'):
        os.remove('./reviews.csv')

    return jsonify({
        'Taux de satisfaction': m,
        #'Points positifs': random_positive_phrases,
        #'Points négatifs': random_negative_phrases
    })  



if __name__ == '__main__':
    app.run(debug=True)
