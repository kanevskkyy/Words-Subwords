import random
import json
import requests
from basic_word import BasicWord

def load_random_word(url):
    """random load word from json and create an instance of the class"""
    response = requests.get(url)
    data = response.json()
    random_entry = random.choice(data)
    return BasicWord(random_entry["word"], random_entry["subwords"])