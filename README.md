# Overview
The Poker Hands Ranker ranks two randomly generated poker hands and outputs the result along with the name of the produced combinations.
# Functionality
The numeric and suit values are extracted from each card. The program uses a dictionary where the numeric value of each card acts as the key and their frequency is the value. Thereree functions cover all the hands from Straight Flush to a High Card and a separate function covers Flush.

There is a separate portion dedicated to deck formation and shuffling. Two hands are generated through a dealing function and the deck is also adjusted after each deal.

# Features
Produces output comparing two poker hands. The hands are generated using random. All combinations from Straight Flush to One pair are covered. However, Royal Flush and High Card have not been implemented yet. So, hands of the same tier, e.g. Two two pairs or two straights is considered a tie.

# Built With
Built with Python 3.12
