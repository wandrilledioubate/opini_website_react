from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import requests
import asyncio
import json
import math
from typing import TypedDict
import httpx
import re
from bs4 import BeautifulSoup
import os
import json
import emoji
import pandas as pd
import nltk
from tqdm import tqdm
from nltk.sentiment import SentimentIntensityAnalyzer
from datetime import datetime

from scrapping import scrap
from traitement import treat
# from deep_model import apply_model


app = Flask(__name__)
cors = CORS(app)

@app.route('/process_url', methods=['POST'])
def process_url():
    data = request.get_json()
    
    if 'url' not in data:
        return jsonify({'error': 'No URL provided'}), 400
    
    url = data['url']
    
    # Scrap the data
    scraped_data = scrap(url)
    if not scraped_data:
        return jsonify({'error': 'Failed to scrap data'}), 500
    
    # Treat the data
    treated_data = treat(scraped_data)
    if not treated_data:
        return jsonify({'error': 'Failed to treat data'}), 500
    
    data_final = treated_data.to_csv('hotel_data.csv', index=False)

    """
    # Apply the model
    model_result = apply_model(treated_data)
    if model_result is None:
        return jsonify({'error': 'Failed to apply model'}), 500

    # If everything is successful, return the result
    return jsonify({'result': model_result}), 200
    """
    return jsonify({'result': data_final}), 200



if __name__ == "__main__":
    app.run(debug=True)