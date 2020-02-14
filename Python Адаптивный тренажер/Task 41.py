"""
A poker deck contains 52 cards. Each card has a suit of either clubs, diamonds, hearts, or spades (denoted C, D, H, S).
Each card also has a value of either 2 through 10, jack, queen, king, or ace (denoted 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q,
K, A). For scoring purposes card values are ordered as above, with 2 having the lowest and ace the highest value.
The suit has no impact on value.
A poker hand consists of five cards. Poker hands are ranked by the following partial order from lowest to highest.
High Card
Hands which do not fit any higher category are ranked by the value of their highest card.
Pair
Two of the five cards in the hand have the same value.
Two Pairs
The hand contains two different pairs.
Three of a Kind
Three of the cards in the hand have the same value.
Straight
Hand contains five cards with consecutive values.
Flush
Hand contains five cards of the same suit.
Full House
Three cards of the same value, with the remaining two cards forming a pair.
Four of a Kind
Four cards with the same value.
Straight Flush
Five cards of the same suit in numerical order.
Royal Flush
Consists of the ace, king, queen, jack and ten of a suit.
﻿Напишите программу, которая получает на вход пять карт и выводит старшую покерную комбинацию,
которая образуется этими картами.
Формат ввода:
Одна строка, на которой указаны пять карт в формате <value><suit>, записанные через пробел.
Формат вывода:
Название старшей комбинации, сформировавшейся на пришедшем наборе.

Sample Input:
10C JC QC KC AC

Sample Output:
Royal Flush
"""


carts = input().split()
value = [i[:-1] for i in carts]
suit = [i[-1] for i in carts]
order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
straights = [sorted(order[i] for i in range(j, j + 5)) for j in range(9)]
if len(set(suit)) == 1 and sorted(value) in straights:
    print('Royal Flush' if 'A' in value else 'Straight Flush')
elif len(set(value)) == 2:
    print('Four of a Kind' if value.count(value[0]) in [1, 4] else 'Full House')
elif len(set(suit)) == 1:
    print('Flush')
elif sorted(value) in straights:
    print('Straight')
elif len(set(value)) == 3:
    print('Two Pairs' if 2 in [value.count(value[0]), value.count(value[1])] else 'Three of a Kind')
elif len(set(value)) == 4:
    print('Pair')
else:
    print('High Card')
