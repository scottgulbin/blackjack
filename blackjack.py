import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
             'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'
		
class Deck:
    
    def __init__(self):
        self.deck = [] 
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += '\n'+ card.__str__()
        return deck_comp
        pass

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()
		
class Hand:
    def __init__(self):
        self.cards = []  
        self.value = 0   
        self.aces = 0    
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces +=1
        pass
    
    def adjust_for_ace(self):
        if self.value>21 and self.aces:
            self.value-=10
            self.aces-=1
			
class Chips:
    
    def __init__(self, total):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0
    
    def win_bet(self):
        self.total+= self.bet
    
    def lose_bet(self):
        self.total-= self.bet
		
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Please type the amount you wish to bet: "))
            
        except:
            Print('Please insert a number')
        else:
            if chips.bet>chips.total:
                print(f'You do not have enough chips. You have {chips.total} chips')
            else:
                break
				
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
	
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while 
    if hand==player:
        y = input('Hit or stand? (y/n))')
        if y=='y':
            hit(deck, hand)
        else:
            playing = False
    else:
        hit(deck,hand)

def show_some(player,dealer):
    print("\nPlayer's cards are: ")
    for card in player.cards:
        print(card)
    print("\nDealer's cards are: ")
    for num, card in enumerate(dealer.cards):
        if num != 0:
            print(card)
        else:
            print("Hiden Card")
    
def show_all(player,dealer):
    print("\nPlayer's cards are: ")
    for card in player.cards:
        print(card)
    print("\nDealer's cards are: ")
    for card in dealer.cards:
        print(card)
		
def player_busts(player,dealer,chips):
    print('Player has gone over 21')
    chips.lose_bet()
    pass

def player_wins(player,dealer,chips):
    print('Player has won!')
    chips.win_bet()
    pass

def dealer_busts(player,dealer,chips):
    print("Player has won! Dealer busts")
    chips.win_bet()
    pass
    
def dealer_wins(player,dealer,chips):
    print("Dealer has won!")
    chips.lose_bet()
    pass
    
def push(player,dealer):
    print('Dealer and Player tie')
	
	
#Main Game
leave = False
while not leave:
    
    print("welcome to blackjack!")
    playing = True
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player = Hand()
    dealer = Hand()
    
    hit(deck, player)
    hit(deck, player)
    hit(deck, dealer)
    hit(deck, dealer)
        
    # Set up the Player's chips
    chips = Chips(int(input('How many chips do you have?')))
    
    # Prompt the Player for their bet
    player.bet = take_bet(chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player, dealer)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player, dealer)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value>21:
            player_busts(player,dealer,chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    while dealer.value<17:
        hit_or_stand(deck, dealer)
        show_some(player, dealer)           
    if dealer.value>21:
        dealer_busts(player,dealer,chips)
    
    show_all(player,dealer)
    # Winning scenarios
    if player.value == dealer.value:
        push(player,dealer)
    elif player.value>dealer.value and player.value<=21:
        print('Player wins')
        player_wins(player,dealer,chips)
    elif player.value<dealer.value and dealer.value<=21:
        print('Dealer Wins')
        dealer_wins(player,dealer,chips)
 
    print(f'Total chips = {chips.total}')
# Ask to play again
    leaveIn = input('Play again? (y/n)')
    if  leaveIn == "n":
        leave = True
	
