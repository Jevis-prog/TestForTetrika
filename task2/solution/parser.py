import re

import requests
from bs4 import BeautifulSoup
from collections import defaultdict
from urllib.parse import urljoin
from config import BASE_URL


def is_russian_letter(letter):
    return re.fullmatch(r"[А-ЯЁ]", letter.upper()) is not None

def get_soup(url):
    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")

def scrape_animals_by_letter(start_url):
    url = start_url
    letter_counts = defaultdict(int)

    while url:
        soup = get_soup(url)

        category_section = soup.find("div", class_="mw-category mw-category-columns")
        if not category_section:
            break

        groups = category_section.find_all("div", class_="mw-category-group")
        for group in groups:
            letter_tag = group.find("h3")
            if letter_tag:
                letter = letter_tag.text.strip().upper()
                if not is_russian_letter(letter):
                    continue
                count = len(group.find_all("li"))
                letter_counts[letter] += count

        next_page = soup.find("a", string="Следующая страница")
        if next_page:
            url = urljoin(BASE_URL, next_page["href"])
        else:
            break

    return letter_counts