import random
import tkinter 
import socket
import os
import time

"""

	Projet L1 BI S2:

	BlackJack par Enzo, Mathieu , Paul et Rodrigo
	
	[Partie sur terminal pour faciliter la creation de l'engine]

"""

def give_card():
	"""
A completer 

	"""
	card_number = str(random.randint(1,13)) # 1 = A et 10+ = roi , reine etc
	card_symbol  = random.choice(['H' , 'S' ,'D' , 'C'])
	if card_number== '10':
		card_number = 'T'
	elif card_number == '11':
		card_number = 'J'
	elif card_number == '12':
		card_number = 'Q'
	elif card_number == '13':
		card_number = 'K'
	elif card_number == '1':
		card_number = 'A'
	
	return card_number + card_symbol


def shuffle_cards():
	shuffled_cards = []
	while len(shuffled_cards) != 52:
		card = give_card()
		if card not in shuffled_cards:
			shuffled_cards.append(card)

	return shuffled_cards

def calc_points(current_score , card):
	"""
	"""
	liste_number = ['K' , 'J' , 'Q' , 'T', 'A']
	if card[0] not in liste_number:
		return current_score + int(card[0])
	elif card[0] == 'A':
		return current_score +  int(input('Tas gagne un A choisi entre 1/11'))
	else:
		return current_score + 10

def game_start(liste_cards , different_Score , cards_deck ):
	"""
	"""
	for players in range(0,len(different_Score)):
		for _ in range(2):
			liste_cards[players].append(cards_deck.pop())
			different_Score[players] = calc_points(different_Score[players], liste_cards[players][-1] )

def game_turn(user_scores , user_cards , player , cards_deck):
	user_cards[player].append(cards_deck.pop())
	user_scores[player] = calc_points(user_scores[player] , user_cards[player][-1])
	

def players_turn(users_scores , users_cards , player , game_deck):
	os.system('clear')
	print(f"Jouer {player}:")
	print(f'La carte que tas obtenu est: {users_cards[player][-1]}')
	print(f'Ton score est {users_scores[player]} et tes cartes sont {users_cards[player]}')
	answer = input("Veux tu ajouter une carte? Y/N")
	if answer == 'Y' or answer =='y':
		game_turn(users_scores , users_cards , player , game_deck)
	elif answer == 'N' or answer == 'n' :
		return True
	if users_scores[player] > 21:
		os.system('clear')
		print(f'Jouer {player} as perdu')
		time.sleep(2)
		return True
	elif users_scores[player] == 21:
		os.system('clear')
		print(f'Jouer {player} as Blackjack')
		time.sleep(2)
		return True

def dealers_turn(users_scores , users_cards , player , game_deck):
	while users_scores[0] < 17:
		game_turn(users_scores , users_cards , 0 , game_deck)
	if users_scores[0] > 21:
		time.sleep(2)
		print('Le dealer a une combination de cartes superieur a 21')


def show_scores(users_scores , users_cards , player):
	os.system('clear')
	print('Score final:')
	if users_scores[0] >21:
		print('Personne perd car le dealer a un score superieur a 21')
	for player in range(1,len(users_scores)):
		if users_scores[player] == 21:
			print(f'Jouer {player} a fait un Blackjack')
		elif users_scores[player] > users_scores[0] and users_scores[player] < 22:
			print(f'Jouer {player} a gagne grace a superiorite face au dealer')
			
		elif (users_scores[player] < users_scores[0] and users_scores[0] < 21) or users_scores[player] > 21:
			print(f"Jouer {player} a perdu")
		else:
			print(f"Jouer {player} ne perd pas a cause du score du dealer superieur a 21")
	print(f'score dealer est {users_scores[0]}')

def game_engine():
	"""
Indice 0 = dealer
chaque indice apres 0 = jouers

	"""
	game_deck    = shuffle_cards()
	users_cards  = [[] , [] , []]
	users_scores = [0 , 0 , 0]
	users_bets   = [100 , 100 , 100]
	game_start(users_cards, users_scores , game_deck) 
	print(users_cards[0] , users_cards[1] , users_scores)
	game_finished = False
	while game_finished != True:
		for player in range(1 , len(users_scores)):
			if users_scores[player] < 21:
				turn_done = False
				while turn_done != True:
					turn_done = players_turn(users_scores , users_cards , player , game_deck)
		game_finished = True
	dealers_turn(users_scores , users_cards , player , game_deck)
	show_scores(users_scores , users_cards , player)

game_engine()