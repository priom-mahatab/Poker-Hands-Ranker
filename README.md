# Overview
This Python script evaluates and ranks poker hands based on standard poker hand rankings. The ranking includes hands like "high card," "pair," "straight flush," and more.

# Features
### Input: 
The script takes poker hands as input, where each hand is a list of 5 cards. Each card is represented as a string containing its value and suit (e.g., '9H' for 9 of Hearts).
### Card Value and Suit:
```value(card)```: Returns the numeric value of the card. Face cards like Ace, King, Queen, and Jack are converted into 14, 13, 12, and 11, respectively.

```suit(card)```: Returns the suit of the card (Hearts, Diamonds, Clubs, or Spades).
### Flush Detection:
```is_flush(cards)```: Checks if all the cards in a hand have the same suit (flush).

# Installation
1. Clone the repository or download the poker_hands_ranker.py script.
2. Ensure Python is installed on your system (Python 3.6+ recommended).

# Usage
1. Run the script in your Python environment.

```python poker_hands_ranker.py```

2. Modify the test_case variable in the script to input your own set of poker hands for ranking.

```test_case = [['9H', '8H', '7H', '6H', '5H'], ['AH', 'AS', 'AD', 'AC', '7D'], ...]```
