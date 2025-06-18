from config import START_URL, CSV_FILENAME
from parser import scrape_animals_by_letter
from utils import save_to_csv

def main():
    counts = scrape_animals_by_letter(START_URL)
    save_to_csv(counts, CSV_FILENAME)

if __name__ == "__main__":
    main()