from unittest.mock import Mock

import pytest
from bs4 import BeautifulSoup

from app.parser import get_soup, is_russian_letter, scrape_animals_by_letter


@pytest.mark.parametrize(
    "letter, expected",
    [
        ("А", True),
        ("ё", True),
        ("я", True),
        ("Ж", True),
        ("Z", False),
        ("1", False),
        ("ЖЖ", False),
    ],
)
def test_is_russian_letter(letter: str, expected: bool) -> None:
    assert is_russian_letter(letter) == expected


def test_get_soup(monkeypatch: pytest.MonkeyPatch) -> None:
    class MockResponse:
        text = "<html><body><h1>Test</h1></body></html>"

        def raise_for_status(self) -> None:
            pass

    monkeypatch.setattr("requests.get", lambda url: MockResponse())
    soup = get_soup("http://example.com")
    assert isinstance(soup, BeautifulSoup)
    assert soup.h1 is not None
    assert soup.h1.text == "Test"


def test_scrape_animals_by_letter_multipage(mock_get_soup_multipage: Mock) -> None:
    result = scrape_animals_by_letter("https://example.com/start")
    assert result == {"А": 2, "Б": 3, "В": 1}
