"""Interactive greeter with a small DevNet/Cisco info helper.

This module provides `greet` for programmatic use and an interactive
flow when executed as a script: ask the user's name, greet them, present
three options, and show information depending on the selection.
"""

from __future__ import annotations

import logging
from typing import Optional

logger = logging.getLogger(__name__)
_DEFAULT_FORMAT = "Hello, {name}!"


def greet(name: str, *, template: str = _DEFAULT_FORMAT) -> str:
    """Return a greeting for ``name`` using ``template``.

    Raises ``TypeError`` if ``name`` is not a string and ``ValueError``
    if the (stripped) name is empty.
    """
    if not isinstance(name, str):
        raise TypeError("`name` must be a string")

    cleaned = name.strip()
    if not cleaned:
        raise ValueError("`name` must not be empty or whitespace")

    return template.format(name=cleaned)


def _explain_devnet_courses() -> None:
    """Print a short, helpful list of DevNet/Cisco course titles and topics."""
    print("\nDevNet / Cisco learning path suggestions:")
    print("1) DevNet Associate (entry-level):")
    print("   - Focus: Python basics, REST APIs, JSON, basic automation and scripting.")
    print("   - Good first certification for automating Cisco platforms.")
    print("\n2) DevNet Professional (intermediate/advanced):")
    print("   - Focus: advanced automation, application design, CI/CD, infrastructure-as-code.")
    print("   - Useful for engineers building scalable automation solutions.")
    print("\n3) Platform / Specialist courses (platform-specific):")
    print("   - Examples: Cisco DNA Center automation, SD-WAN automation, Webex/Unified Communications APIs.")
    print("   - These teach automation for particular Cisco products and platforms.\n")


def _explain_improvements() -> None:
    print("\nIf you want me to improve this feature, here are three options:")
    print("A) Add CLI flags: --template to customize the greeting, --format for title/upper/lower.")
    print("B) Convert this to a small installable package (pyproject) so it can be imported cleanly.")
    print("C) Keep it minimal: a single clean function with docs and no CLI.")
    print("\nTell me which letter you prefer (A/B/C) and I will implement it.")


def _offer_help() -> None:
    print("\nWhat would you like to do?")
    print("1) Learn about DevNet/Cisco courses")
    print("2) Discuss improvement options for this feature")
    print("3) Exit")


def interactive_flow(name: Optional[str] = None) -> None:
    """Run an interactive session: greet user and handle their choice."""
    try:
        if not name:
            name = input("What's your name? ")
    except (EOFError, KeyboardInterrupt):
        print("\nInput cancelled. Bye!")
        return

    try:
        print(greet(name))
    except (TypeError, ValueError) as exc:
        print(f"Invalid name: {exc}")
        return

    while True:
        _offer_help()
        try:
            choice = input("Enter 1/2/3: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled. Bye!")
            return

        if choice == "1":
            _explain_devnet_courses()
        elif choice == "2":
            _explain_improvements()
        elif choice == "3":
            print("Goodbye!")
            return
        else:
            print("Invalid choice — please enter 1, 2, or 3.")


def main(argv: Optional[list[str]] = None) -> int:
    """Simplified entrypoint that starts the interactive flow.

    This function returns 0 on clean exit.
    """
    logging.basicConfig(level=logging.INFO)
    # If argv is provided we could parse flags — keep simple for now.
    try:
        interactive_flow()
    except Exception as exc:  # pragma: no cover - top-level safety
        logger.exception("Unexpected error in interactive flow: %s", exc)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())