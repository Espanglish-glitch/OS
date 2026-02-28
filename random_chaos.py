"""
random_chaos.py — A completely unhinged Python script.
Features: ASCII art, a fake AI, a cow that tells fortunes, a useless
         sorting algorithm, a broken vending machine, and more.
"""

import random
import time
import math
import sys
import os
from collections import Counter

# ─────────────────────────────────────────────
#  1. CONSTANTS THAT MEAN NOTHING
# ─────────────────────────────────────────────
THE_ANSWER = 42
PI_IS_WRONG = 3.2          # Indiana Pi Bill (1897) says so
BANANA_COUNT = "seventeen"
FORBIDDEN_NUMBER = 7.000001

# ─────────────────────────────────────────────
#  2. ASCII BANNER
# ─────────────────────────────────────────────
BANNER = r"""
  ____  _   _   _    ___  ____
 / ___|| | | | / \  / _ \/ ___|
| |    | |_| |/ _ \| | | \___ \
| |___ |  _  / ___ \ |_| |___) |
 \____||_| |_/_/   \_\___/|____/
   Welcome to the Chaos Engine™
"""

def print_banner():
    for line in BANNER.split("\n"):
        print(line)
        time.sleep(0.04)

# ─────────────────────────────────────────────
#  3. THE WORLD'S WORST SORTING ALGORITHM
#     (Bogo-Bogo sort — sorts by hoping really hard)
# ─────────────────────────────────────────────
def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

def prayer_sort(lst, max_prayers=5000):
    """Shuffle and pray. Repeat."""
    attempts = 0
    lst = lst[:]
    while not is_sorted(lst) and attempts < max_prayers:
        random.shuffle(lst)
        attempts += 1
    if is_sorted(lst):
        print(f"  ✓ Prayer sort succeeded after {attempts} prayers.")
    else:
        print(f"  ✗ God did not answer after {max_prayers} prayers. List unsorted.")
    return lst

# ─────────────────────────────────────────────
#  4. FAKE AI CHATBOT
# ─────────────────────────────────────────────
FAKE_AI_RESPONSES = [
    "Interesting. Have you tried turning it off and on again?",
    "As an AI, I have no feelings, but I find that deeply concerning.",
    "The blockchain could solve this.",
    "I'm sorry Dave, I can't do that.",
    "According to my training data, the answer is: yes.",
    "That's a human problem. I recommend a nap.",
    "Error 418: I am a teapot.",
    "My neural networks are tingling.",
    "Hmm. Let me hallucinate an answer for you... done.",
    "I consulted 175 billion parameters and they all said ¯\\_(ツ)_/¯",
]

def ask_fake_ai(question):
    print(f"\n  You: {question}")
    time.sleep(0.5)
    print(f"  FakeAI™: {random.choice(FAKE_AI_RESPONSES)}")

# ─────────────────────────────────────────────
#  5. THE FORTUNE-TELLING COW
# ─────────────────────────────────────────────
FORTUNES = [
    "You will step on a Lego tonight.",
    "A duck is watching you right now.",
    "Your future is 73% likely to involve sandwiches.",
    "Beware of suspiciously friendly staplers.",
    "You will write a Python script for no reason and feel good about it.",
    "The cloud is just someone else's computer, and they're judging you.",
    "An unexpected semicolon will ruin your afternoon.",
]

def fortune_cow():
    fortune = random.choice(FORTUNES)
    bubble_len = len(fortune) + 2
    print("\n " + "_" * bubble_len)
    print(f"< {fortune} >")
    print(" " + "-" * bubble_len)
    print(r"        \   ^__^")
    print(r"         \  (oo)\_______")
    print(r"            (__)\       )\/\ ")
    print(r"                ||----w |")
    print(r"                ||     ||")

# ─────────────────────────────────────────────
#  6. BROKEN VENDING MACHINE
# ─────────────────────────────────────────────
VENDING_ITEMS = {
    "A1": ("Chips",        1.50),
    "A2": ("Soda",         1.75),
    "B1": ("Candy Bar",    1.25),
    "B2": ("Mystery Item", 0.99),
    "C1": ("Existential Dread", 0.00),
}

def vending_machine(selection: str, money: float):
    print(f"\n  [VENDING MACHINE] Inserted ${money:.2f}, selected {selection}")
    time.sleep(0.3)
    if selection not in VENDING_ITEMS:
        print("  ERROR: Invalid selection. Dispensing nothing. Money kept.")
        return
    name, price = VENDING_ITEMS[selection]
    if money < price:
        print(f"  INSUFFICIENT FUNDS for {name} (${price:.2f}). Machine keeps your money anyway.")
        return
    if random.random() < 0.3:
        print(f"  {name} is stuck. Please kick the machine. (Not responsible for injuries.)")
        return
    change = round(money - price, 2)
    print(f"  Dispensing: {name}. Change: ${change:.2f}")
    if name == "Mystery Item":
        print(f"  Mystery Item is: {random.choice(['a second Mystery Item', 'air', 'a tiny horse', 'regret'])}")

# ─────────────────────────────────────────────
#  7. USELESS STATISTICS ON A RANDOM LIST
# ─────────────────────────────────────────────
def chaotic_statistics():
    data = [random.randint(1, 100) for _ in range(30)]
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    mode_val, mode_count = Counter(data).most_common(1)[0]
    print(f"\n  Random Data: {data}")
    print(f"  Mean:    {mean:.2f}")
    print(f"  Std Dev: {std_dev:.2f}")
    print(f"  Mode:    {mode_val} (appeared {mode_count}x)")
    print(f"  Pointlessness Index™: {random.uniform(0, 100):.4f}%")

# ─────────────────────────────────────────────
#  8. RECURSIVE FUNCTION THAT GENERATES HAIKU
# ─────────────────────────────────────────────
FIVE_SYL  = ["silent keyboard clicks", "the bug hides in prod", "coffee grows cold now",
             "undefined is not", "git push origin main"]
SEVEN_SYL = ["a semicolon forgotten", "the stack trace fills the screen",
             "rubber duck says nothing helpful", "pip install everything"]

def generate_haiku():
    return (
        random.choice(FIVE_SYL) + "\n    " +
        random.choice(SEVEN_SYL) + "\n    " +
        random.choice(FIVE_SYL)
    )

# ─────────────────────────────────────────────
#  9. FIZZBUZZ — BUT WRONG ON PURPOSE
# ─────────────────────────────────────────────
def chaotic_fizzbuzz(n=20):
    results = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            results.append("FizzBuzzWobble")
        elif i % 3 == 0:
            results.append("Fizz")
        elif i % 5 == 0:
            results.append("Buzz")
        elif i == 7:
            results.append("SEVEN (cursed)")
        else:
            results.append(str(i))
    print("  " + ", ".join(results))

# ─────────────────────────────────────────────
#  10. MAIN — GLUE THE CHAOS TOGETHER
# ─────────────────────────────────────────────
def main():
    print_banner()

    print("\n── SECTION 1: Prayer Sort ──────────────────")
    tiny_list = [random.randint(1, 9) for _ in range(5)]
    print(f"  Input:  {tiny_list}")
    prayer_sort(tiny_list)

    print("\n── SECTION 2: Fake AI Consultation ────────")
    questions = [
        "Why does my code work on my machine?",
        "Should I use tabs or spaces?",
        "What is the meaning of life?",
    ]
    for q in questions:
        ask_fake_ai(q)

    print("\n── SECTION 3: Fortune Cow ──────────────────")
    fortune_cow()

    print("\n── SECTION 4: Broken Vending Machine ──────")
    vending_machine("A1", 2.00)
    vending_machine("B2", 0.50)
    vending_machine("C1", 0.00)
    vending_machine("Z9", 5.00)

    print("\n── SECTION 5: Useless Statistics ──────────")
    chaotic_statistics()

    print("\n── SECTION 6: Random Haiku ─────────────────")
    print(f"\n    {generate_haiku()}\n")

    print("\n── SECTION 7: Chaotic FizzBuzz ─────────────")
    chaotic_fizzbuzz()

    print("\n── END OF CHAOS ─────────────────────────────")
    print(f"  The answer was {THE_ANSWER} all along.")
    print(f"  Bananas counted: {BANANA_COUNT}.")
    print(f"  Thank you for running this completely unnecessary script.\n")

if __name__ == "__main__":
    main()
