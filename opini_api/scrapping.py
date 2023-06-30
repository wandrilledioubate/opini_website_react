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


def scrape_reviews_resto(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while scraping {url}: {e}")
        return []

    reviews = []
    for i in range(0, 100, 100):  # Change this to change the number of pages you scrape
        page_url = f"{url}-or{i}"
        response = requests.get(page_url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract restaurant name and id
        restaurant_name_element = soup.find('h1', class_="HjBfq")
        restaurant_name = restaurant_name_element.text if restaurant_name_element is not None else 'Inconnu'
        for review in soup.find_all('div', class_='review-container'):
            id_div = review.find('div', class_="reviewSelector")
            id_ = id_div.get('data-reviewid') if id_div else ''
            rating = (review.find('span', class_='ui_bubble_rating').get('class')[1].split('_')[1])
            title = review.find('span', class_='noQuotes').text
            text = review.find('p', class_='partial_entry').text
            date = review.find('span', class_='ratingDate').get('title')
            votes_span = review.find('span', class_='thankButton hsx_thank_button')
            votes = votes_span.text.strip() if votes_span and votes_span.text.strip() else '0'

            reviews.append({
                'id': id_,
                'date': date,
                'rating': int(int(rating) / 10),
                'title': title,
                'text': text,
                'votes': votes,
                'name': restaurant_name
            })

    return reviews


def generate_random_id():
    id_length = 9
    random_id = ''.join(random.choices('0123456789', k=id_length))
    return random_id


def scrape_reviews_rental(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers, verify=False)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Une erreur s'est produite lors de la récupération des données à partir de {url}: {e}")
        return []

    reviews = []
    page_url = url
    while page_url:
        response = requests.get(page_url, headers=headers, verify=False)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract rental name and id
        rental_name_element = soup.find('h1', class_="biGQs _P fiohW uuBRH")
        rental_name = rental_name_element.text if rental_name_element is not None else 'Inconnu'

        for review in soup.find_all('div', class_="_c"):
            review_id = generate_random_id()
            if review.find('svg', class_="UctUV d H0"):
                rating_element = review.find('svg', class_="UctUV d H0")
            elif review.find('svg', class_="JXZuC d H0"):
                rating_element = review.find('svg', class_="JXZuC d H0")
            else:
                rating_element = None

            if rating_element:
                rating = rating_element.get('aria-label').split(' ')[0]
                # Reste du code
            else:
                rating = None
            title = review.find('div', class_="biGQs _P fiohW alXOW NwcxK GzNcM ytVPx UTQMg RnEEZ uuBRH").text.strip()
            text = review.find('div', class_="biGQs _P pZUbB KxBGd").text.strip()
            div_content = soup.find('div', class_='biGQs _P pZUbB ncFvv osNWb').contents[0]
            date_pattern = r'Written (\w+ \d{1,2}, \d{4})'
            match = re.search(date_pattern, div_content)
            if match:
                date = match.group(1)
            else:
                date = None

            reviews.append({
                'id': review_id,
                'date': date,
                'rating': int(float(rating)),
                'title': title,
                'text': text,
                'vote': 0,
                'rental_name': rental_name,
            })

        next_button = soup.find('a', class_="_3fPsSAYi")
        page_url = next_button['href'] if next_button else None

    return reviews


def scrape_hotel(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers, verify=False)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Une erreur s'est produite lors de la récupération des données à partir de {url}: {e}")
        return []

    reviews = []
    page_url = url
    while page_url:
        for i in range(0, 100, 100):  # Change this to change the number of pages you scrape
            page_url = f"{url}-or{i}"
            response = requests.get(page_url, headers=headers, verify=False)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract rental name and id
            rental_name_element = soup.find('h1', class_="biGQs _P rRtyp")
            rental_name = rental_name_element.text if rental_name_element is not None else 'Inconnu'

            for review in soup.find_all('div', class_="YibKl MC R2 Gi z Z BB pBbQr"):
                div_element = review.find('div', class_="WAllg _T")
                review_id = int(div_element.get('data-reviewid'))
                rating = (review.find('span', class_='ui_bubble_rating').get('class')[1].split('_')[1])
                title_element = review.find('div', class_="KgQgP MC _S b S6 H5 _a")
                title = title_element.find('span').text.strip()
                text = review.find('span', class_="QewHA H4 _a").text.strip()
                date_element = review.find('span', class_="teHYY _R Me S4 H3")
                try:
                    date_text = date_element.text.strip()
                except:
                    date_text = "01/01/2019"
                try:
                    date = date_text.split(':')[1].strip()
                except IndexError:
                    date = "01/01/2019"
                vote = 0

                reviews.append({
                    'id': review_id,
                    'date': date,
                    'rating': int(int(rating) / 10),
                    'title': title,
                    'text': text,
                    'vote': vote,
                    'name': rental_name,
                })

            next_button = soup.find('a', class_="ui_button nav next primary ")
            page_url = next_button['href'] if next_button else None

    return reviews


def scrap(url):
    if 'Restaurant_Review' in url:
        reviews = scrape_reviews_resto(url)
    elif 'Hotel_Review' in url:
        reviews = scrape_hotel(url)
    elif 'VacationRentalReview' in url:
        reviews = scrape_reviews_rental(url)
    else:
        print("Invalid URL")
        return

    if reviews:
        with open('reviews.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=reviews[0].keys())
            writer.writeheader()
            writer.writerows(reviews)
        print("Data saved successfully as CSV.")
    else:
        print("No reviews found.")


