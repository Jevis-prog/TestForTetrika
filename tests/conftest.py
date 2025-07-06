from pathlib import Path
from unittest.mock import Mock

import pytest
from bs4 import BeautifulSoup


@pytest.fixture
def mock_response_html_multipage() -> dict[str, str]:
    return {
        "page1": """
        <div class="mw-category mw-category-columns">
            <div class="mw-category-group">
                <h3>А</h3>
                <ul>
                    <li>Акула</li>
                    <li>Аист</li>
                </ul>
            </div>
        </div>
        <a href="/page2" title="Следующая страница">Следующая страница</a>
        """,
        "page2": """
        <div class="mw-category mw-category-columns">
            <div class="mw-category-group">
                <h3>Б</h3>
                <ul>
                    <li>Бобр</li>
                    <li>Барсук</li>
                    <li>Буйвол</li>
                </ul>
            </div>
        </div>
        <a href="/page3" title="Следующая страница">Следующая страница</a>
        """,
        "page3": """
        <div class="mw-category mw-category-columns">
            <div class="mw-category-group">
                <h3>В</h3>
                <ul>
                    <li>Волк</li>
                </ul>
            </div>
        </div>
        """,
    }


@pytest.fixture
def mock_get_soup_multipage(monkeypatch: pytest.MonkeyPatch, mock_response_html_multipage: dict[str, str]) -> Mock:
    def fake_get_soup(url: str) -> BeautifulSoup:
        if "page1" in url or "start" in url:
            html = mock_response_html_multipage["page1"]
        elif "page2" in url:
            html = mock_response_html_multipage["page2"]
        elif "page3" in url:
            html = mock_response_html_multipage["page3"]
        else:
            html = ""
        return BeautifulSoup(html, "html.parser")

    monkeypatch.setattr("app.parser.get_soup", fake_get_soup)
    return Mock()


@pytest.fixture
def sample_letter_counts() -> dict[str, int]:
    return {"Б": 3, "А": 2, "В": 1}


@pytest.fixture
def empty_letter_counts() -> dict[str, int]:
    return {}


@pytest.fixture
def tmp_csv_file(tmp_path: Path) -> str:
    return str(tmp_path / "test_output.csv")
