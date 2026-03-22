import pandas as pd
import matplotlib.pyplot as plt

FILE = "data.csv"

def show_summary():
    try:
        df = pd.read_csv(FILE, names=["Date", "Amount", "Category"])

        df["Amount"] = df["Amount"].astype(float)

        summary = df.groupby("Category")["Amount"].sum()

        print("\nExpense Summary:")
        print(summary)

        summary.plot(kind="bar")
        plt.title("Expenses by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.show()

    except Exception as e:
        print("Error:", e)
