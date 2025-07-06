import csv

from app.utils import save_to_csv


def test_save_to_csv_writes_correct_data(
    sample_letter_counts: dict[str, int],
    tmp_csv_file: str,
) -> None:
    save_to_csv(sample_letter_counts, tmp_csv_file)

    with open(tmp_csv_file, encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)

    assert rows == [["А", "2"], ["Б", "3"], ["В", "1"]]


def test_save_to_csv_with_empty_dict(
    empty_letter_counts: dict[str, int],
    tmp_csv_file: str,
) -> None:
    save_to_csv(empty_letter_counts, tmp_csv_file)

    with open(tmp_csv_file, encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)

    assert rows == []
