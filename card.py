global values,suits,ranks

suits=('Heart','Diamond','Spades','Clubs')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}

class Card:
    def __init__(self,suit,rank) -> None:
        self.suit=suit
        self.rank=rank
        self.value=values[self.rank]
    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
##################################################################
import random

class Deck:

    def __init__(self) -> None:
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                card_obj=Card(suit,rank)
                self.all_cards.append(card_obj)

    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    def display_cards(self):
        for i in self.all_cards:
            print(i)

    def deal_one(self):
        return self.all_cards.pop()

############################################################################
        
class player:

    def __init__(self,name) -> None:
        self.name=name
        self.all_cards=[]

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if isinstance(new_cards,list):

            return self.all_cards.extend(new_cards)
        else:
            return self.all_cards.append(new_cards)

    def __str__(self) -> str:
        return f'{self.name} has {len(self.all_cards)} cards'

    def display_cards(self):
        for i in self.all_cards:
            print(i)

##############################################

player_one=player('one')
player_two=player('two')

new_deck=Deck()
new_deck.shuffle_deck()

for card in range(0,(len(new_deck.all_cards))//2):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

print(player_one)
player_one.display_cards()

print('\n')

print(player_two)
player_two.display_cards()

####################################
game_on=True
round_num=0
while game_on:

    round_num+=1

    print(f'Round {round_num}')

    if len(player_one.all_cards)==0:
        print(f'player one has lost the game! player two WINS')
        game_on=False
        break
    if len(player_two.all_cards)==0:
        print(f'player two has lost the game! player one WINS')
        game_on=False
        break

    # starting a new round
        
    player_1_card=[]
    player_1_card.append(player_one.remove_one())
    player_2_card=[]
    player_2_card.append(player_two.remove_one())



    #war
    at_war=True
    while at_war:
        if player_1_card[-1].value>player_2_card[-1].value:

            player_one.add_cards(player_1_card)
            player_one.add_cards(player_2_card)
            at_war=False
            break

        elif player_1_card[-1].value<player_2_card[-1].value:
            player_two.add_cards(player_1_card)
            player_two.add_cards(player_2_card)
            at_war=False
            break
        else:
            print('WAR!')

            if len(player_one.all_cards)<5:
                print('player one unable to declare war')
                print('Player TWO WINS!!')
                game_on=False
                break
            elif len(player_two.all_cards)<5:
                print('player two unable to declare war')
                print('Player ONE WINS!!')
                game_on=False
                break

            else:
                for i in range(5):
                    player_1_card.append(player_one.remove_one())
                    player_2_card.append(player_two.remove_one())





    