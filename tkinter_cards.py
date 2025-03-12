import tkinter as tk
import time
import threading
import socket
import os
from PIL import Image , ImageTk
import webbrowser
import random


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

def test_cards():
	os.system('clear')
	global image , player_image
	card = f'./images/card/{random.randint(101,152)}.png'
	print(card)
	image_not_resized = Image.open(card)
	image = ImageTk.PhotoImage(image_not_resized.resize(image_not_resized.size))
	print(image_not_resized.size[0] , type(image_not_resized.size[0]))
	
	dealers_label['image'] = image
	dealers_label.configure(image = image , 
							width = image_not_resized.size[0] , 
							height = image_not_resized.size[1])
	card = f'./images/card/{random.randint(101,152)}.png'
	image_not_resized = Image.open(card)
	player_image = ImageTk.PhotoImage(image_not_resized.resize(image_not_resized.size))
	players_label['image']= player_image
	players_label.configure(image = player_image)


background_image = tk.Label(bj_root , image = background)
background_image.pack(fill='both' , expand = True)

cards_frame = tk.Frame(background_image , bd = 0 )
cards_frame.pack(anchor = 'w') 

butto_frame = tk.Frame(background_image , bd = 0)
butto_frame.pack(anchor = 's')


dealers_frame = tk.LabelFrame(cards_frame , text = 'Dealer' , bd = 0)
dealers_frame.grid(row = 0 , column = 0 )# anchor = 'east')


players_frame = tk.LabelFrame(cards_frame , text = 'Player' , bd = 0)
players_frame.grid(row = 1 , column = 0 )


dealers_label = tk.Label(dealers_frame , image = card_back , bd = 0)
dealers_label.pack()

players_label = tk.Label(players_frame , image = card_back , bd = 0)
players_label.pack()

hit_button = tk.Button(butto_frame, text = 'Hit' , command = test_cards)
hit_button.pack(pady = 20 ,ipadx = 20 )

stand_button = tk.Button(butto_frame, text = 'Stand' , command = lambda : webbrowser.open('https://www.youtube.com/watch?v=S06IYs3csWI') )
stand_button.pack(pady = 20  , ipadx = 20 )


bj_root.mainloop()



print('working')
