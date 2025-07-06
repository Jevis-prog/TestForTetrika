from app.config import CSV_FILENAME, START_URL
from app.parser import scrape_animals_by_letter
from app.utils import save_to_csv


def main() -> None:
    counts = scrape_animals_by_letter(START_URL)
    save_to_csv(counts, CSV_FILENAME)


if __name__ == "__main__":
    main()
