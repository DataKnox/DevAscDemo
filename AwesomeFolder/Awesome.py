"""Awesome module with a small demo.
"""

from __future__ import annotations

import random
from typing import Sequence


class AwesomeGenerator:
    """Generate awesome values and messages."""

    adjectives = ["amazing", "incredible", "fantastic", "spectacular", "awesome"]
    nouns = ["code", "project", "journey", "experience", "adventure"]

    @classmethod
    def random_message(cls) -> str:
        adjective = random.choice(cls.adjectives)
        noun = random.choice(cls.nouns)
        return f"You are building {adjective} {noun}!"

    @classmethod
    def random_numbers(cls, count: int = 5, start: int = 1, end: int = 100) -> Sequence[int]:
        return [random.randint(start, end) for _ in range(count)]


def main() -> None:
    print("Welcome to the awesome generator!")
    print(AwesomeGenerator.random_message())
    print("Here are some awesome numbers:", ", ".join(str(n) for n in AwesomeGenerator.random_numbers()))


if __name__ == "__main__":
    main()
