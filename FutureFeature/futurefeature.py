import datetime
import random

# filepath: C:/Users/jgput/OneDrive/Desktop/DevAscDemo/FutureFeature/futurefeature.py
#!/usr/bin/env python3


def generate_future_message():
    future_quotes = [
        "The future belongs to those who believe in the beauty of their dreams.",
        "Innovation distinguishes between a leader and a follower.",
        "The best way to predict the future is to invent it.",
        "Your future is created by what you do today, not tomorrow.",
        "Embrace the unknown, for it is the gateway to possibility."
    ]
    return random.choice(future_quotes)

def display_mega_awesome_feature():
    now = datetime.datetime.now()
    print("="*40)
    print("🚀 Mega Awesome Future Feature 🚀")
    print("="*40)
    print(f"Current Date & Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    print("Here's your inspiration for the future:")
    print(f"💡 {generate_future_message()}")
    print("="*40)

if __name__ == "__main__":
    display_mega_awesome_feature()