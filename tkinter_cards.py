import tkinter as tk
import time
import threading
import socket
import os
from PIL import Image , ImageTk
import webbrowser
import random


from playsound import playsound


"""
	Projet L1 BI S2:

	BlackJack par Enzo, Mathieu , Paul et Rodrigo
	
	[Partie graphique + BlackJack]


"""


geometry = '900x720'

"""
20  = 0001 0100
-20 = 1110 1100


1011 0111
0100 1001

1100 1100
0011 0100

1101 1001
0010 0111

0101 1010
1010 0110

1101 0110
0010 1010

"""
bj_root = tk.Tk()
bj_root.title('BlackJack Projet L1BIS2')
bj_root.iconphoto(False, tk.PhotoImage(file='./images/icons8.png'))
background = tk.PhotoImage(file = './images/bg.png')
bj_root.geometry(geometry)
bj_root.configure()
card_back = tk.PhotoImage(file = './images/card/155.png')

background_image = tk.Label(bj_root , image = background)
background_image.pack(fill='both' , expand = True)


class card:
	def __init__(self , card_id , card_suit , card_number):
		self.card_id = card_id
		self.card_suit = card_suit
		self.card_number = card_number
	def return_id(self):
		return self.card_id

	def card_front(self):
		return (self.card_suit , self.card_number)

class deck:
	def __init__(self):
		self.deck_cards = []

	def create_deck(self):
		self.card_suits =['D' , 'C' , 'H' , 'S']
		self.card_numbers  = ['A' , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ,"T" , 'J' , 'Q' , "K"]

		for suits in range(len(self.card_suits)):
			for numbers in  range(len(self.card_numbers)):
				self.deck_cards.append(card(card_suit = self.card_suits[suits],
											card_number = self.card_numbers[numbers],
											card_id = 101+len(self.deck_cards)))

	def random_card(self):
		return random.choice(self.deck_cards)

class player:
	def __init__(self , root , player_id):
		self.player_score = 0
		self.player_id = player_id
		self.base_root = root
		self.player_deck = [deck_of_cards.random_card() , deck_of_cards.random_card()]
		player_card_image[self.player_id - 1].append(tk.PhotoImage(file = f'./images/card/{self.player_deck[-1].return_id()}.png'))
		player_card_image[self.player_id - 1].append(tk.PhotoImage(file = f'./images/card/{self.player_deck[-1].return_id()}.png'))
		self.player_frame = tk.LabelFrame(self.base_root, text = f'Player {self.player_id}' , bd = 0)
		self.player_frame.pack(anchor='w')
		self.player_labels_liste = [tk.Label(self.player_frame,
									image = card_back
									, bd = 0) , tk.Label(self.player_frame,
									image = card_back
									, bd = 0) ]
		for player_labels in self.player_labels_liste:
			player_labels.pack(anchor = 'w' , side=tk.RIGHT)
		

	def calculate_score(self):
		liste_number = ['K' , 'J' , 'Q' , 'T', 'A']
		self.player_score = 0	
		for card in self.player_deck:
			if card[0] not in liste_number:
				self.player_score + int(card[0])
			elif card[0] == 'A':
				self.player_score +  int(input('Tas gagne un A choisi entre 1/11'))
			else:
				self.player_score + 10
		return self.player_score

	def add_label(self):
		self.player_labels_liste.append(tk.Label(self.player_frame,
									image = card_back
									, bd = 0))
		self.player_labels_liste[-1].pack(anchor = 'e' , side = tk.RIGHT)
		player_card_image[self.player_id-1].append(tk.PhotoImage(file = f'./images/card/{self.player_deck[-1].return_id()}.png'))

	def player_update(self):
		self.player_deck.append(deck_of_cards.random_card())
		if len(self.player_labels_liste) < len(self.player_deck):
			self.add_label()
		for player_card_index in range(len(self.player_deck)):
			print(player_card_index , self.player_id , len(player_card_image[self.player_id-1]))
			player_card_image[self.player_id - 1][player_card_index] = tk.PhotoImage(file = f'./images/card/{self.player_deck[player_card_index].return_id()}.png')
			self.player_labels_liste[player_card_index].configure(image= player_card_image[self.player_id - 1][player_card_index])

def return_card_image(card_id):
	global card_image
	card_image = Image.open(f'./images/card/{card_id}.png')
	card_image = ImageTk.PhotoImage(card_image)
	return card_image

def game_engine():
	
	butto_frame = tk.Frame(background_image , bd = 0)
	butto_frame.pack(anchor = 'sw' , expand = True)

	hit_button = tk.Button(butto_frame,
							text = 'Hit' ,
							command = testing )
	hit_button.pack()

	stand_button = tk.Button(butto_frame,
							text = 'Stand' ,
							 command = lambda : webbrowser.open('https://www.youtube.com/watch?v=S06IYs3csWI') )
	stand_button.pack()

	print('working')


def game_start():
	os.system('clear')
	global image , player_image , card_identification , player_card_image , players_liste , deck_of_cards , number_players
	number_players = 4
	player_card_image = [[] for _ in range(number_players)]
	deck_of_cards = deck()
	deck_of_cards.create_deck()
	
	dealer_deck = [deck_of_cards.random_card() , deck_of_cards.random_card()]

	dealer_frame = tk.LabelFrame(background_image,text = 'Dealer' ,
								bd=0)
	dealer_frame.pack(anchor='w')
	dealer_label_liste = [tk.Label(dealer_frame,  image = return_card_image(dealer_deck[0].return_id()) , bd = 0) 
							, tk.Label(dealer_frame, image = card_back , bd = 0) ]
	for dealer_label in dealer_label_liste:
		dealer_label.pack(anchor = 'w' , side=tk.RIGHT)

	players_liste = [player(background_image , 1),player(background_image,2) , player(background_image,3) , player(background_image,4) ]
	

	game_engine()


def testing():
	for players in players_liste:
		players.player_update()


game_start()


bj_root.mainloop()



print('working')