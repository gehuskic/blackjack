# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 20:28:41 2022

@author: Gejnemin Huskic
website: www.gejnem.in
"""

import random
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
          'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
suits = ('Heats', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 
        'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Card():
    # card: suit, rank, value
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck():
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # creates card object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        popped = self.all_cards.pop()
        return popped

class Player():
    def __init__(self, name, money):
        self.name = name
        self.all_cards = []
        self.money = money
        self.wins = 0
    
    def remove_one(self):
        popped = self.all_cards.pop()
        return popped
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            for card in new_cards:
                self.all_cards.insert(0, card)
        else:
            self.all_cards.insert(0, new_cards)
    
    def flush_cards(self):
        self.all_cards = []
    
    def change_name(self, name):
        self.name = name
    
    def add_win(self):
        self.wins += 1
    
    def deposit(self, amount):
        self.money += amount
    
    def withdraw(self, amount):
        self.money -= amount
    
    def __str__(self):
        return (f"Player {self.name} has {len(self.all_cards)} cards")


# function checks if the player has hit below 21
def check_for_under_21(player):
    statement = False
    result = 0
    
    # checks to see if the current player has any Aces
    for cards in player.all_cards:
        if cards.rank == 'Ace':
            result += 1
        else: 
            result += cards.value
        
        if (result < 21):
            statement = True
    return statement

# function checks if the player has hit over 21
def check_for_over_21(player):
    statement = False
    result = 0
    
    # checks to see if the current player has any Aces
    for cards in player.all_cards:
        if cards.rank == 'Ace':
            result += 1
        else: 
            result += cards.value
        
        if (result > 21):
            statement = True
    return statement

# functions checks if the player has hit exactly the value of 21,
# checks if the player has an Ace and compares multiple different 
# combinations of sums
def check_for_21(player):
    statement = False
    result = 0
    
    # checks to see if the current player has any Aces
    aces = 0
    for cards in player.all_cards:
        if cards.rank == 'Ace':
            aces += 1

    # If there are no Aces, adds values of cards together and returns True if sum == 21.
    # If there are Aces in the deck, looks at all possible combinations to see if sum == 21.
    if (aces == 0):
        for cards in player.all_cards:
            result = result + cards.value
        if result == 21:
            statement = True
    else:
        # adds values of all non-Ace cards first, and stores it in none_ace_result
        none_ace_result = 0
        for cards in player.all_cards:
            if cards.rank != 'Ace':
                none_ace_result += cards.value
                
        # all possible combinations of ace additions
        possible_ace_results = ((1,11), (2,12,22), (3,13,23,33), (4,15,24,34,44))
        
        # unpacks possible_ace_results[aces - 1]
        # adds none_ace_result to numbers in tuple to see if anything equals 21
        for nums in possible_ace_results[aces - 1]:
            if (nums + none_ace_result) == 21:
                statement = True
                break
    return statement

def player_action(move):
    if (move == 'hit'):
        pass
    if (move == 'stay'):
        pass
        

def print_cards(player, mask):
    if mask == False:
        print(f"[+] {player.name}'s current cards:")
        for card in player.all_cards:
            print(f" - {card}")
    else:
        print(f"[+] {player.name}'s current cards:")
        x = 0
        for card in player.all_cards:
            if x == 0:
                print(" - [Hidden Card]")
                x += 1
            else:
                print(f" - {card}")

def player_name_input():
    new_name = str()
    while True:
        try:
            x = str(input(">>> "))
            new_name = (x[0].upper() + x[1::])
            break
        except:
            print("[!] Please supply a name.")
    return new_name 

def bet_amount(player):
    print(f"[+] Your current balance is ${player.money}.")
    print("[+] How much are you willing to bet?")
    while True:
        try:
            bet = int(input(">>> $"))
            if bet >= player.money:
                print("[!] Cannot be greater or equal to your funds!")
        except ValueError:
            print("[!] Can only be a whole number.")
        except:
            pass
        else:
            if bet < player.money:
                break
    return bet

def funds(p1,p2):
    print("[+] Current funds: ")
    print(f"[+] {p1.name}: ${p1.money}")
    print(f"[+] {p2.name}: ${p2.money}")

def stats(p1,p2):
    if (p1.wins == 0) and (p2.wins == 0):
        print("[!] No games have been played yet!")
    elif (p1.wins > p2.wins):
        print(f"[+] {p1.name} is ahead with {p1.wins} wins.")
        print(f"[+] {p2.name} has {p2.wins} wins.")
    elif (p1.wins < p2.wins):
        print(f"[+] {p2.name} is ahead with {p2.wins} wins.")
        print(f"[+] {p1.name} has {p1.wins} wins.")

def toriel():
    print('''
          \n[+] This is a game of blackjack!
          \n[+] Albeit with a simplified ruleset. 
        \n[+] Here is how the gameplay goes:
            
        \n    1) Player places the $ bet.
        
        \n    2) Dealer gets one card placed up, and one placed down.
    
        \n    3) Player gets two cards placed up. 
    
        \n    4) Player can take a 'hit' meaning they take a card, or they
        \n      'stay' meaning they stop taking cards. If they are at a value
        \n       of 21, they win. If they are above 21, they 'bust'. Busting means
        \n       they lose their bet and funds go to the winner. If they are
        \n       below 21, the dealer starts hitting.
        
        \n    5) If the dealer hits to 21, they win. If they get over 21, they
        \n       lose and bust. 
        
        \n    7) This version of the game ignores casino rules such as: 
        \n       insurance, split, and doubledown.
        
        \n    8) Face cards (jack, queen, or king) have a value of 10. 
    
        \n   10) Aces can count as either 1 or 11, whichever is 
        \n       preferable to the player.
          ''')

def play_black_jack(p1,p2):
    p1.flush_cards()
    p2.flush_cards()
    bid = bet_amount(p1)
    print("\n[+] Shuffling the deck...")
    print(f"[+] Dealing two cards to {p1.name} and {p2.name}...")
    black_jack = Deck()
    black_jack.shuffle()
    for x in range(2):
        p1.add_cards(black_jack.deal_one())
        p2.add_cards(black_jack.deal_one())
    
    while True:
        print("\n")
        print_cards(p2, mask = True)
        print("\n")
        print_cards(p1, mask = False)
        print("\n[!] Keeping bidding or stay.\n1 = bid\n2 = stay")
        x = input(">>> ")
        if x == '1':
            p1.add_cards(black_jack.deal_one())
        elif x == '2':
            break
        else:
            print("Enter 1 to bid or 2 to stay.")
        
    if check_for_21(p1) == True:
        print(f"[!] {p1.name}'s sum is 21!")
        print(f"[!] {p1.name} has won!")
        p1.add_win()
        p2.withdraw(bid)
        p1.deposit(bid)
    elif check_for_over_21(p1) == True:
        print(f"[!] {p1.name}'s sum is over 21.")
        print(f"[!] {p2.name} has won!")
        p2.add_win()
        p1.withdraw(bid)
        p2.deposit(bid)
    elif check_for_under_21(p1) == True:
        print(f"[!] {p1.name}'s sum is under 21.")
        print(f"[!] {p2.name}, what will you do?")
        while True:
            print(f"[!] {p2.name} took a hit...")
            card_delt = black_jack.deal_one()
            print(f"[+] A {card_delt} was dealt.")
            p2.add_cards(card_delt)
            print_cards(p2, mask = False)
            if check_for_21(p2) == True:
                print(f"[!] {p2.name}'s sum is 21!")
                print(f"[!] {p2.name} has won!")
                p2.add_win()
                p1.withdraw(bid)
                p2.deposit(bid)
                break
            elif check_for_over_21(p2) == True:
                print(f"[!] {p2.name}'s sum is over 21.")
                print(f"[!] {p1.name} has won!")
                p1.add_win()
                p2.withdraw(bid)
                p1.deposit(bid)
                break

def main():
    while True:
        print("\n----------------")
        print("| Black - Jack |")
        print("----------------")
        print("1 = Play Game")
        print("2 = View Stats")
        print("3 = View funds")
        print("4 = How to play")
        print("5 = Change name")
        print("6 = Quit")
        menu = input("\n>>> ")
        if (menu == '1'):
            play_black_jack(p1, p2)
        if (menu == '2'):
            stats(p1,p2)
        if (menu == '3'):
            funds(p1,p2)
        if (menu == '4'):
            toriel()
        if (menu == '5'):
            print("\n[+] Enter the new name you desire: ")
            p1.change_name(player_name_input())
        if (menu == '6'):
            break
        else:
            pass

p1 = Player('Player', 250)
p2 = Player('Cpu Dealer', 250)
main()





'''
Checklist:

game attributes:
----------------
    - standard deck of 52 cards, shuffled
    - ignore blackjack rules such as: insurance, split, and doubledown


special rules:
--------------
    - face cards (jack, queen, or king) have a value of 10
    - Aces can count as either 1 or 11, whichever is preferable to the player
    - players have a bank roll
    

gameplay: 
---------
1 - player places a monetary bet
2 - dealer starts with 1 card faced up and 1 faced down
3 - player starts with 2 cards faced up
4 - player goes first in gameplay
5 - player goal is to get closer to the value of 21 than the dealer
    (sum of two cards)
8 - the player can either take a hit or stay:
    hit:  recieve another card
    stay: stop receiving cards
10 - after the players turn, if the player is under 21, the computer dealer
    will keep hitting until they either beat the player or the dealer busts.
        busts: meaning a player goes over 21 and loses. winner collects money. 

how the game can end:
---------------------
[!] the player keeps hitting before the computer dealer can even play, and
    goes over 21.
[!] the computer can beat the dealer, the computer sum is higher than the player
    and is still under 21. 
[!] the computer wins because the dealer keeps hitting and busts.

'''