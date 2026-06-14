import csv
import random
import os
import sys

NUM_ROWS = 67

COLUMNS = ["Вид животного", "Уровень пушистости", "Вид голоса", "Преступление"]


def generate_row():
    return {
        "Вид животного": random.choice([
            "Капибара", "ЧЕРЕМША", "Муравьед",
            "Лысый кот", "Горилла", "Голубь"
        ]),
        "Уровень пушистости": round(random.uniform(0.0, 100.0), 2),

        "Вид голоса": random.choice([
            "Урчание",
            "В России всё делали не спеша",
            "Ультразвуковой писк",
            "Сопение",
            "Дикий крик",
            "Курлыканье",
            "Молчание"
        ]),

        "Преступление": random.choice([
            "Не послушал рэп перед сном",
            "Делал six-seven руками",
            "Сделал укус",
            "Громко орал в 3 ночи",
            "Сделал заднее сальто",
            "Бил себя в грудь"
        ]),
    }


OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

rows = [generate_row() for _ in range(NUM_ROWS)]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)