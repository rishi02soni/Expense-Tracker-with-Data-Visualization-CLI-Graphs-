import csv
from utils import get_date

FILE = "data.csv"

def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category (Food, Travel, etc.): ")
    date = get_date()

    with open(FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category])

    print("✅ Expense added!")


def view_expenses():
    try:
        with open(FILE, mode="r") as file:
            reader = csv.reader(file)
            print("\nDate | Amount | Category")
            print("--------------------------")
            for row in reader:
                print(f"{row[0]} | {row[1]} | {row[2]}")
    except FileNotFoundError:
        print("No data found.")
