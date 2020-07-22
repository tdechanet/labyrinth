from item import Item
import pygame
from pygame.locals import *


class Character(
    Item
):  # this class ininitialize the movement and the inventory of the player

    bag = []  # inventory of the player
    sedatif = False

    def move(self, map, order):  # this method allow the player to move
        x = self.get_position()[0]
        y = self.get_position()[1]

        if self.incorrect_position(
            map, order
        ):  # if the order make the player go straight in a wall, the order is cancel and an error is prompt
            return x, y
        if order == "up":  # this is the movement
            y -= 1
        if order == "left":
            x -= 1
        if order == "down":
            y += 1
        if order == "right":
            x += 1

        self.set_position(x, y)
        self.inventory(map)
        return x, y

    def incorrect_position(
        self, map, order
    ):  # this methord is used in move method to verify if the position is correct
        x = self.get_position()[0]
        y = self.get_position()[1]
        test_x = x
        test_y = y
        if order == "up":
            test_y -= 1
        if order == "left":
            test_x -= 1
        if order == "down":
            test_y += 1
        if order == "right":
            test_x += 1
        if (
            map[test_x][test_y] == "wall"
            or test_x == len(map) - 1
            or test_y == len(map[0]) - 1
            or test_x < 0
            or test_y < 0
        ):  # with this line, the player cant get out of the labyrinth
            return True
        return False

    def inventory(self, map):  # method to pickup item
        x = self.get_position()[0]
        y = self.get_position()[1]
        print(self.bag)
        if (
            map[x][y] == "aiguille" and "aiguille" not in self.bag
        ):  # if the player walk in an item, this line check if he don't already have it
            self.bag.append(
                "aiguille"
            )  # if he don't have it, this line add it in the inventory
        if map[x][y] == "éther" and "éther" not in self.bag:
            self.bag.append("éther")
        if map[x][y] == "tube" and "tube" not in self.bag:
            self.bag.append("tube")
        if len(self.bag) == 3:
            return True
