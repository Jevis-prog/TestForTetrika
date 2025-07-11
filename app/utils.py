import csv


def save_to_csv(letter_counts: dict[str, int], filename: str) -> None:
    with open(filename, mode="w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        for letter in sorted(letter_counts):
            writer.writerow([letter, letter_counts[letter]])
