from argparse import ArgumentParser

parser = ArgumentParser(description="CLI Expense Tracker")

subparsers = parser.add_subparsers(dest="command")

add_parser = subparsers.add_parser("add")
add_parser.add_argument("--amount", type=float, required=True)
add_parser.add_argument("--category", required=True)
add_parser.add_argument("--note")

view_parser = subparsers.add_parser("view")

args = parser.parse_args()

print("Welcome to Expense Tracker!")

filename = "expenses.csv"


def add_expense(amount, category, note):
    with open(filename, "a") as file:
        file.write(f"{amount}, {category}, {note}\n")


def view_expenses():
    with open(filename, "r") as file:
        print(file.read())


if args.command == "add":
    add_expense(args.amount, args.category, args.note)
if args.command == "view":
    view_expenses()

print(f"Expense added successfully to {filename}")
