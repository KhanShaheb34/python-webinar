"""
Super-simple CLI Expense Tracker for absolute beginners.

What this script shows:
- Using argparse to build a tiny CLI
- Writing and reading a plain text CSV file (no csv module)

Run examples:
- Add an expense:
  python 01_cli_expense_tracker.py add --amount 500 --category food --note "Kacchi"

- View saved expenses:
  python 01_cli_expense_tracker.py view

Docs:
- argparse: https://docs.python.org/3/library/argparse.html
"""

from argparse import ArgumentParser
import os


FILENAME = "expenses.csv"  # one line per expense: amount,category,note


def ensure_file_with_header(path: str) -> None:
    """Create the file with a simple header if it doesn't exist (keeps Streamlit examples happy)."""
    if os.path.exists(path):
        return
    with open(path, "w", encoding="utf-8") as f:
        f.write("amount,category,note\n")


def main() -> None:
    parser = ArgumentParser(description="Very simple CLI Expense Tracker")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--amount", type=float, required=True)
    add_parser.add_argument("--category", type=str, required=True)
    add_parser.add_argument("--note", type=str, default="")

    subparsers.add_parser("view", help="View all expenses (raw file output)")

    args = parser.parse_args()

    ensure_file_with_header(FILENAME)

    if args.command == "add":
        # Minimal validation; keep it beginner-friendly
        if args.amount <= 0:
            print("Amount must be greater than 0.")
            return
        category = args.category.strip()
        note = (args.note or "").strip()
        if not category:
            print("Category is required.")
            return

        # Append a plain CSV line — no csv module to keep it simple
        with open(FILENAME, "a", encoding="utf-8") as f:
            f.write(f"{args.amount},{category},{note}\n")
        print(f"Expense added to {FILENAME}")
        return

    if args.command == "view":
        # Just dump the file contents for simplicity
        with open(FILENAME, "r", encoding="utf-8") as f:
            print(f.read())
        return


if __name__ == "__main__":
    main()
