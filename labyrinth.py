# coding=utf-8

from character import Character
import random
import pygame
from pygame.locals import *

# this two variables will be the graphic reference
WIDTH = 1080
HEIGHT = 660



def set_item_position(map, item_string):
    '''this function give a random position to the game's items'''
    x = random.randint(0, len(map) - 2)
    y = random.randint(0, len(map[0]) - 2)
    if map[x][y] == "path":
        map[x][y] = item_string
        return x, y
    else:
        return set_item_position(map, item_string)


def start():  
    '''this fonction create 2D array from a txt file'''
    x = 1  # abscissa
    y = 1  # orderly

    map_dict = ""  # this dict will concatenate the model of the list

    # this line read the txt file and transcrib it into dict
    map_txt = open("map.txt")
    start.col = 0
    start.line = 0
    for number in map_txt:  # we run through line of the file
        number = number if "\n" in number else number + "\n"
        map_dict += number
        start.line = start.line + 1
        # verification that every column have the same amount of character
        if start.col == len(number) or start.col == 0:
            start.col = len(number)
        # if not the same amount, we raise errors message
        else:
            raise "Le nombre de colonnes doit être égal pour chaque lignes."
    # creation of the 2D array
    start.map_overview = [[0 for i in range(start.line)] for j in range(start.col)]

    map_txt.close()

    start.fenetre = pygame.display.set_mode((WIDTH, HEIGHT))

    # assignation of the characters to their function in the map
    for number in map_dict:
        poswidth = (
            (x - 1) * WIDTH / (start.col - 1)
        )  # this two variable give the graphic placement of the objects
        posheight = (y - 1) * HEIGHT / (start.line - 1)
        wall = pygame.image.load("image/mur.png").convert_alpha()
        wall = pygame.transform.scale(
            wall, (int(WIDTH / (start.col - 1)), int(HEIGHT / (start.line - 1)))
        )
        if number == "1":
            start.map_overview[x - 1][y - 1] = "wall"
            start.fenetre.blit(wall, (poswidth, posheight))
        elif number == "M":
            start.map_overview[x - 1][y - 1] = "MacGyver"
            start.macGyver = Character("MacGyver", (x - 1, y - 1))
            start.position_macgyver = (poswidth, posheight)
        elif number == "G":
            start.map_overview[x - 1][y - 1] = "Guardian"
            start.x_y_guard = (x - 1, y - 1)
            start.position_guard = (poswidth, posheight)
        elif number == "0":
            start.map_overview[x - 1][y - 1] = "path"

        if x == start.col:  # counter
            y += 1
            x = 1
        else:
            x += 1



def display_layout():
    '''this function glue the images to their graphic place'''
    display_layout.scale_col_general = int(WIDTH / (start.col - 1))
    display_layout.scale_line_general = int(HEIGHT / (start.line - 1))

    display_layout.black = pygame.image.load("image/carre_noir.png").convert_alpha()
    display_layout.black = pygame.transform.scale(display_layout.black, (display_layout.scale_col_general, display_layout.scale_line_general))
    
    display_layout.mac_gyver = pygame.image.load("image/MacGyver.png").convert_alpha()
    display_layout.mac_gyver = pygame.transform.scale(
        display_layout.mac_gyver, (display_layout.scale_col_general, display_layout.scale_line_general)
    )
    start.fenetre.blit(display_layout.mac_gyver, start.position_macgyver)

    guard = pygame.image.load("image/Gardien.png").convert_alpha()
    guard = pygame.transform.scale(guard, (display_layout.scale_col_general, display_layout.scale_line_general))
    start.fenetre.blit(guard, start.position_guard)

    position = set_item_position(start.map_overview, "aiguille")
    x, y = position
    position = (x * display_layout.scale_col_general, y * display_layout.scale_line_general)
    aiguille = pygame.image.load("image/aiguille.png").convert_alpha()
    aiguille = pygame.transform.scale(aiguille, (display_layout.scale_col_general, display_layout.scale_line_general))
    start.fenetre.blit(aiguille, (position))

    position = set_item_position(start.map_overview, "tube")
    x, y = position
    position = (x * display_layout.scale_col_general, y * display_layout.scale_line_general)
    tube = pygame.image.load("image/tube_plastique.png").convert_alpha()
    tube = pygame.transform.scale(tube, (display_layout.scale_col_general, display_layout.scale_line_general))
    start.fenetre.blit(tube, (position))

    position = set_item_position(start.map_overview, "éther")
    x, y = position
    position = (x * display_layout.scale_col_general, y * display_layout.scale_line_general)
    ether = pygame.image.load("image/ether.png").convert_alpha()
    ether = pygame.transform.scale(ether, (display_layout.scale_col_general, display_layout.scale_line_general))
    start.fenetre.blit(ether, (position))

    display_layout.x, display_layout.y = start.macGyver.get_position()

    pygame.display.flip()
    


def key_order():
    # this loop make take the deplacement order and make macgyver move
    continuer = 1
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = 0
            if event.type == KEYDOWN:
                start.fenetre.blit(
                    display_layout.black, (display_layout.x * display_layout.scale_col_general, display_layout.y * display_layout.scale_line_general)
                )

                if event.key == K_UP:
                    order = "up"
                    pos = start.macGyver.move(start.map_overview, order)
                if event.key == K_LEFT:
                    order = "left"
                    pos = start.macGyver.move(start.map_overview, order)
                if event.key == K_DOWN:
                    order = "down"
                    pos = start.macGyver.move(start.map_overview, order)
                if event.key == K_RIGHT:
                    order = "right"
                    pos = start.macGyver.move(start.map_overview, order)
                if order:
                    display_layout.x = pos[0]
                    display_layout.y = pos[1]

                    start.fenetre.blit(
                        display_layout.mac_gyver, (display_layout.x * display_layout.scale_col_general, display_layout.y * display_layout.scale_line_general)
                    )
                    pygame.display.flip()

                # when you step on the guard, this condition decide if you win or lose
                if start.x_y_guard == (display_layout.x, display_layout.y):
                    continuer = 0
                    if start.macGyver.inventory(start.map_overview) == True:
                        print("You win !")
                    else:
                        print("You lose !")
