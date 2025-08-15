from __future__ import annotations

import random
from typing import Dict, Tuple


DifficultySettings = Dict[str, Tuple[int, int]]


DIFFICULTY_SETTINGS: DifficultySettings = {
    "easy": (10, 5),
    "medium": (50, 7),
    "hard": (100, 10),
}


def prompt_user(message: str) -> str:
    user_input = input(message).strip().lower()
    return user_input


def choose_difficulty() -> Tuple[int, int]:
    print("\nChoose difficulty: easy / medium / hard (or 'q' to quit)")
    while True:
        difficulty = prompt_user("> ")
        if difficulty in ("q", "quit", "exit"):
            raise SystemExit(0)
        if difficulty in DIFFICULTY_SETTINGS:
            max_number, max_attempts = DIFFICULTY_SETTINGS[difficulty]
            print(
                f"Selected '{difficulty}' — Guess a number between 1 and {max_number}. You have {max_attempts} attempts."
            )
            return max_number, max_attempts
        print("Invalid choice. Please type: easy, medium, or hard. (q to quit)")


def play_round(max_number: int, max_attempts: int) -> bool:
    secret_number = random.randint(1, max_number)
    attempts_remaining = max_attempts

    print(f"\nI have chosen a number between 1 and {max_number}. Can you guess it?")

    while attempts_remaining > 0:
        guess_raw = prompt_user(
            f"Attempts left {attempts_remaining}. Enter your guess (or 'q' to quit): "
        )
        if guess_raw in ("q", "quit", "exit"):
            print("Goodbye!")
            return False

        if not guess_raw.isdigit():
            print("Please enter a valid positive integer.")
            continue

        guess = int(guess_raw)
        if guess < 1 or guess > max_number:
            print(f"Your guess must be between 1 and {max_number}.")
            continue

        if guess == secret_number:
            print("🎉 Correct! You guessed the number!")
            return True

        if guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

        attempts_remaining -= 1

    print(f"\nOut of attempts! The number was {secret_number}.")
    return False


def ask_play_again() -> bool:
    print("\nPlay again? (y/n)")
    while True:
        answer = prompt_user("> ")
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no", "q", "quit", "exit"):
            return False
        print("Please answer with 'y' or 'n'.")


def main() -> None:
    print("\n=== Guess The Number ===")
    print("Type 'q' anytime to quit.")

    while True:
        max_number, max_attempts = choose_difficulty()
        _ = play_round(max_number, max_attempts)
        if not ask_play_again():
            print("Thanks for playing! 👋")
            return


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
