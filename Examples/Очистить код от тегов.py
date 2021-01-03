""" 
Очистка кода html страниц от тегов
"""
import requests
from bs4 import BeautifulSoup

r = requests.get(url)
soup = BeautifulSoup(r.text)
text = soup.get_text()