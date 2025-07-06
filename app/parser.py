import re
from collections import defaultdict
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup, Tag

from app.config import BASE_URL


def is_russian_letter(letter: str) -> bool:
    return re.fullmatch(r"[А-ЯЁ]", letter.upper()) is not None


def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def scrape_animals_by_letter(start_url: str) -> dict[str, int]:
    url: str | None = start_url
    letter_counts: defaultdict[str, int] = defaultdict(int)

    while url:
        soup = get_soup(url)

        category_section = soup.find("div", class_="mw-category mw-category-columns")
        if not isinstance(category_section, Tag):
            break

        groups = category_section.find_all("div", class_="mw-category-group")
        for group in groups:
            if not isinstance(group, Tag):
                continue

            letter_tag = group.find("h3")
            if not isinstance(letter_tag, Tag):
                continue

            letter = letter_tag.text.strip().upper()
            if not is_russian_letter(letter):
                continue

            count = len(group.find_all("li"))
            letter_counts[letter] += count

        next_page = soup.find("a", string="Следующая страница")
        if isinstance(next_page, Tag) and "href" in next_page.attrs:
            href_value = next_page["href"]
            if isinstance(href_value, (list | tuple)):
                href_str = href_value[0] if href_value else ""
            else:
                href_str = str(href_value)

            url = urljoin(BASE_URL, href_str)
        else:
            break

    return dict(letter_counts)
