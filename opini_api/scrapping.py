import requests
import asyncio
import json
import math
from typing import TypedDict
import httpx
import re
from bs4 import BeautifulSoup
import os


def extract_page_manifest(html):
    data = re.findall(r"pageManifest:({.+?})};", html, re.DOTALL)
    if data:
        return json.loads(data[0])
    else:
        print("No pageManifest found in HTML")
        return None

def safe_get(dictionary, *keys):
    for key in keys:
        if dictionary is None:
            return None
        dictionary = dictionary.get(key)
    return dictionary



def extract_named_urql_cache(urql_cache: dict, pattern: str):
    data = json.loads(next(v["data"] for k, v in urql_cache.items() if pattern in v["data"]))
    return data

class Review(TypedDict):
    id: str
    date: str
    rating: str
    title: str
    text: str
    votes: int
    language: str

def parse_reviews(html) -> Review:
    page_data = extract_page_manifest(html)
    if page_data is None:
        print("No pageManifest found in HTML")
        return []

    page_data = extract_page_manifest(html)
    review_cache = extract_named_urql_cache(page_data["urqlCache"]["results"], '"reviewListPage"')
    parsed = []
    for review in review_cache["locations"][0]["reviewListPage"]["reviews"]:
        parsed.append(
            {
                "id": review["id"],
                "date": review["publishedDate"],
                "rating": review["rating"],
                "title": review["title"],
                "text": review["text"],
                "votes": review["helpfulVotes"],
                "language": review["language"],
            }
        )
    return parsed

async def scrape_hotel(url, session):
    try:
        first_page = await session.get(url)
        first_page.raise_for_status()  # Cela lève une exception si le statut n'est pas 200
    except httpx.HTTPStatusError:
        print(f"URL {url} non fonctionnelle.")
        return None

    first_page = await session.get(url)


    # Ajoutez le code de vérification ici

    _review_page_size = 10
    total_review_pages = int(_review_page_size)
    review_urls = [
        url.replace("-Reviews-", f"-Reviews-or{_review_page_size * i}-") for i in range(1, total_review_pages)
    ]
    assert len(set(review_urls)) == len(review_urls)
    review_responses = await asyncio.gather(*[session.get(url) for url in review_urls])
    reviews = []
    for response in [first_page, *review_responses]:
        reviews.extend(parse_reviews(response.text))

    hotel_data = {
        "reviews": reviews,
    }
    return hotel_data


def scrape_reviews(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Cela lève une exception si le statut n'est pas 200
    except requests.HTTPError:
        print(f"URL {url} non fonctionnelle.")
        return []

    reviews = []
    for i in range(0, 100,20):
        page_url = f"{url}-or{i}"
        response = requests.get(page_url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        restaurant_name_element = soup.find('h1', class_="HjBfq")
        restaurant_name = restaurant_name_element.text if restaurant_name_element is not None else 'Inconnu'
        restaurant_id = url.split('-')[1].replace('d','')

        for review in soup.find_all('div', class_='review-container'):
            id_div = review.find('div', class_="reviewSelector")
            id_ = id_div.get('data-reviewid') if id_div else ''
            rating = (review.find('span', class_='ui_bubble_rating').get('class')[1].split('_')[1])
            title = review.find('span', class_='noQuotes').text
            text = review.find('p', class_='partial_entry').text
            date = review.find('span', class_='ratingDate').get('title')
            language_div = review.find('div', class_='translationOptions')
            language = language_div.get('language') if language_div else ''
            votes_span = review.find('span', class_='thankButton hsx_thank_button')
            votes = votes_span.text.strip() if votes_span and votes_span.text.strip() else '0'

            reviews.append({
                'id': id_,
                'date': date,
                'rating': rating,
                'title': title,
                'text': text,
                'votes': votes,
                'language': language,
                'restaurant_name': restaurant_name,
                'restaurant_id': restaurant_id
            })

    return reviews

def save_to_json(data, filename):
    with open(filename, 'w') as f:
        if 'reviews' in data:
            for item in data['reviews']:
                item['rating'] = str(int(item['rating']))#note hotel
                json.dump(item, f)
                f.write('\n')
        else:
            for item in data:
                item['rating'] = str(int(item['rating']) / 10)#note resto
                json.dump(item, f)
                f.write('\n')



def delete_old_json_files():
    files_to_delete = ['output.json']
    for file in files_to_delete:
        if os.path.exists(file):
            os.remove(file)
        else:
            print(f"Le fichier {file} n'existe plus")


async def scrap(url):
    if 'Restaurant' in url:
        reviews = scrape_reviews(url)
        save_to_json(reviews, 'output.json')
    elif 'Hotel' in url:
        limits = httpx.Limits(max_connections=5)
        BASE_HEADERS = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "accept-language": "en-US,en;q=0.9,lt;q=0.8,et;q=0.7,de;q=0.6",
            "accept-encoding": "gzip, deflate, br",
        }
        async with httpx.AsyncClient(limits=limits, timeout=httpx.Timeout(15.0), headers=BASE_HEADERS) as session:
            result = await scrape_hotel(url, session)
            if result is not None:  # vérifiez si le résultat est None avant de l'envoyer à save_to_json
                save_to_json(result, 'output.json')

