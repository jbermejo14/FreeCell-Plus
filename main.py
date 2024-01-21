import random

import pygame
import sys

gameDisplay = pygame.display.set_mode((1024, 700))
pygame.init()
pygame.display.set_caption("CartaBlanca")
gameExit = False
table = pygame.image.load("resources/table.png")
gameDisplay.blit(table, (0, 0))


class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        self.coords = [0, 0]
        self.top_rect = pygame.Rect(self.coords[0], self.coords[1], 102, 155)
        self.name = number + "-" + suit
        self.selected = False
        self.card = pygame.image.load('resources/card_images/' + self.name + ".png")
        self.in_box = False
        if self.suit is "Hearts" or self.suit is "Diamonds":
            self.color = "red"
        elif self.suit is "Spades" or self.suit is "Claves":
            self.color = "black"

    def clicked(self):
        for i in front_row_list:
            if i.selected is True and i is not self:
                if i.color != self.color and int(i.number) == int(self.number) - 1:
                    gameDisplay.blit(table, (0, 0))
                    i.coords[0] = self.coords[0]
                    i.coords[1] = self.coords[1] + 35
                    i.top_rect = pygame.Rect(self.coords[0], self.coords[1], 102, 155)

                    for lista in card_list:
                        if i in lista:
                            lista.remove(i)
                            for lista2 in card_list:
                                if self in lista2:
                                    lista2.append(i)

                    # TODO NEEDS FIXING, IS A MESS! CARD WITH CARD STAIR UNDERNEATH THEM NEEDS TO MOVE CORRECTLY
                    # for lista in card_list:
                    #     if i in lista:
                    #         aux = i
                    #         lista.remove(i)
                    #         for col in card_list:
                    #             print("col")
                    #             for card in col:
                    #                 if aux.coords[0] == card.coords[0] and aux.coords[1] == card.coords[1] - 35:
                    #                     if aux.color != card.color and int(aux.number) == int(card.number) - 1:
                    #                         lista.remove(card)
                    #
                    #         for col in card_list:
                    #             for card in col:
                    #                 if i.coords[0] == card.coords[0] and i.coords[1] == card.coords[1] - 35:
                    #                     if i.color != card.color and int(i.number) == int(card.number) - 1:
                    #                         for lista2 in card_list:
                    #                             if self in lista2:
                    #                                 lista2.append(card)
                    #
                    #         for lista2 in card_list:
                    #             if self in lista2:
                    #                 lista2.append(i)

                    aux_card_list = []

                    def sort_func(e):
                        for i in e:
                            return i.coords[1]

                    for i in card_list:
                        aux_card_list.append(i)
                    aux_card_list.sort(key=sort_func)

                    for i in aux_card_list:
                        for c in i:
                            gameDisplay.blit(c.card, (c.coords[0], c.coords[1], 102, 155))
                    pygame.display.update()

        for i in front_row_list:
            i.selected = False
        self.selected = True


class Boxes:
    def __init__(self, coords):
        self.coords = coords
        self.filled = False
        self.top_rect = pygame.Rect(self.coords[0], self.coords[1], 102, 155)

    def clicked(self):
        for i in front_row_list:
            if i.selected is True:
                if self.filled is False:
                    i.coords = self.coords
                    gameDisplay.blit(table, (0, 0))
                    i.top_rect = pygame.Rect(self.coords[0], self.coords[1], 102, 155)
                    i.in_box = True
                    aux_card_list = []

                    def sort_func(e):
                        for i in e:
                            return i.coords[1]

                    for i in card_list:
                        aux_card_list.append(i)
                    aux_card_list.sort(key=sort_func)

                    for i in aux_card_list:
                        for c in i:
                            gameDisplay.blit(c.card, (c.coords[0], c.coords[1], 102, 155))
                    pygame.display.update()
                    self.filled = True
        for i in front_row_list:
            i.selected = False

class House:
    def __init__(self, coords, house_of):
        self.house_of = house_of
        self.coords = coords
        self.number = 1
        self.filled = False
        self.top_rect = pygame.Rect(self.coords[0], self.coords[1], 102, 155)

    def clicked(self):
        for i in front_row_list:
            if i.selected is True:
                if i.suit == self.house_of and int(i.number) == int(self.number):
                    i.coords = self.coords
                    self.number = self.number + 1
                    gameDisplay.blit(table, (0, 0))
                    i.top_rect = pygame.Rect(self.coords[0], self.coords[1], 102, 155)

        aux_card_list = []

        def sort_func(e):
            for i in e:
                return i.coords[1]

        for i in card_list:
            aux_card_list.append(i)
        aux_card_list.sort(key=sort_func)

        for i in aux_card_list:
            for c in i:
                gameDisplay.blit(c.card, (c.coords[0], c.coords[1], 102, 155))
        pygame.display.update()
        for i in front_row_list:
            i.selected = False

House1 = House((570, 0), "Diamonds")
House2 = House((686, 0), "Hearts")
House3 = House((801, 0), "Claves")
House4 = House((918, 0), "Spades")


Box1 = Boxes([4.5, 0])
Box2 = Boxes([119, 0])
Box3 = Boxes([234, 0])
Box4 = Boxes([350, 0])

Hearts_1 = Card("Hearts", "1")
Hearts_2 = Card("Hearts", "2")
Hearts_3 = Card("Hearts", "3")
Hearts_4 = Card("Hearts", "4")
Hearts_5 = Card("Hearts", "5")
Claves_6 = Card("Claves", "6")
Hearts_7 = Card("Hearts", "7")
Claves_8 = Card("Claves", "8")
Hearts_9 = Card("Hearts", "9")
Hearts_10 = Card("Hearts", "10")
Hearts_11 = Card("Hearts", "11")
Hearts_12 = Card("Hearts", "12")
Hearts_13 = Card("Hearts", "13")
Diamonds_1 = Card("Diamonds", "1")
Diamonds_2 = Card("Diamonds", "2")
Diamonds_3 = Card("Diamonds", "3")
Diamonds_4 = Card("Diamonds", "4")
Diamonds_5 = Card("Diamonds", "5")
Diamonds_6 = Card("Diamonds", "6")
Diamonds_7 = Card("Diamonds", "7")
Diamonds_8 = Card("Diamonds", "8")
Diamonds_9 = Card("Diamonds", "9")
Diamonds_10 = Card("Diamonds", "10")
Diamonds_11 = Card("Diamonds", "11")
Diamonds_12 = Card("Diamonds", "12")
Diamonds_13 = Card("Diamonds", "13")
Spades_1 = Card("Spades", "1")
Spades_2 = Card("Spades", "2")
Spades_3 = Card("Spades", "3")
Spades_4 = Card("Spades", "4")
Spades_5 = Card("Spades", "5")
Spades_6 = Card("Spades", "6")
Spades_7 = Card("Spades", "7")
Spades_8 = Card("Spades", "8")
Spades_9 = Card("Spades", "9")
Spades_10 = Card("Spades", "10")
Spades_11 = Card("Spades", "11")
Spades_12 = Card("Spades", "12")
Spades_13 = Card("Spades", "13")
Claves_1 = Card("Claves", "1")
Claves_2 = Card("Claves", "2")
Claves_3 = Card("Claves", "3")
Claves_4 = Card("Claves", "4")
Claves_5 = Card("Claves", "5")
Hearts_6 = Card("Hearts", "6")
Claves_7 = Card("Claves", "7")
Hearts_8 = Card("Hearts", "8")
Claves_9 = Card("Claves", "9")
Claves_10 = Card("Claves", "10")
Claves_11 = Card("Claves", "11")
Claves_12 = Card("Claves", "12")
Claves_13 = Card("Claves", "13")

card_list_init = [Hearts_1, Hearts_2, Hearts_2, Hearts_3, Hearts_4, Hearts_5, Hearts_6, Hearts_7, Claves_8, Hearts_9,
                  Hearts_10, Hearts_11, Hearts_12, Hearts_13, Diamonds_1, Diamonds_2, Diamonds_3, Diamonds_4,
                  Diamonds_5,
                  Diamonds_6, Diamonds_7, Diamonds_8, Diamonds_9, Diamonds_10, Diamonds_11, Diamonds_12, Diamonds_13,
                  Spades_1, Spades_2, Spades_3, Spades_4, Spades_5, Spades_6, Spades_7, Spades_8, Spades_9, Spades_10,
                  Spades_11, Spades_12, Spades_13, Claves_1, Claves_2, Claves_3, Claves_4, Claves_5, Claves_6, Claves_7,
                  Hearts_8, Claves_9, Claves_10, Claves_11, Claves_12, Claves_13]

list1 = [[102.4, 175], [204.8, 175], [307.2, 175], [409.6, 175], [512, 175], [614.4, 175], [716.8, 175], [819.2, 175],
         [102.4, 210], [204.8, 210], [307.2, 210], [409.6, 210], [512, 210], [614.4, 210], [716.8, 210], [819.2, 210],
         [102.4, 245], [204.8, 245], [307.2, 245], [409.6, 245], [512, 245], [614.4, 245], [716.8, 245], [819.2, 245],
         [102.4, 280], [204.8, 280], [307.2, 280], [409.6, 280], [512, 280], [614.4, 280], [716.8, 280], [819.2, 280],
         [102.4, 315], [204.8, 315], [307.2, 315], [409.6, 315], [512, 315], [614.4, 315], [716.8, 315], [819.2, 315],
         [102.4, 350], [204.8, 350], [307.2, 350], [409.6, 350], [512, 350], [614.4, 350], [716.8, 350], [819.2, 350],
         [102.4, 385], [204.8, 385], [307.2, 385], [409.6, 385]]

c0 = [[102.4, 175], [102.4, 210], [102.4, 245], [102.4, 280], [102.4, 315], [102.4, 350], [102.4, 385]]
c1 = [[204.8, 175], [204.8, 210], [204.8, 245], [204.8, 280], [204.8, 315], [204.8, 350], [204.8, 385]]
c2 = [[307.2, 175], [307.2, 210], [307.2, 245], [307.2, 280], [307.2, 315], [307.2, 350], [307.2, 385]]
c3 = [[409.6, 175], [409.6, 210], [409.6, 245], [409.6, 280], [409.6, 315], [409.6, 350], [409.6, 385]]
c4 = [[512, 175], [512, 210], [512, 245], [512, 280], [512, 315], [512, 350]]
c5 = [[614.4, 175], [614.4, 210], [614.4, 245], [614.4, 280], [614.4, 315], [614.4, 350]]
c6 = [[716.8, 175], [716.8, 210], [716.8, 245], [716.8, 280], [716.8, 315], [716.8, 350]]
c7 = [[819.2, 175], [819.2, 210], [819.2, 245], [819.2, 280], [819.2, 315], [819.2, 350]]

card_list = [c0, c1, c2, c3, c4, c5, c6, c7]
box_list = [Box1, Box2, Box3, Box4]
house_list = [House1, House2, House3, House4]

def front_row():
    front_row_list = []

    def sort_func(e):
        return e.coords[1]

    for i in card_list:
        for c in i:
            if c.in_box is True:
                front_row_list.append(c)
        i.sort(key=sort_func)

        if i[-1].color != i[-2].color and int(i[-1].number) == int(i[-2].number) - 1:
            if i[-2].color == i[-3].color and int(i[-2].number) == int(i[-3].number) - 2:
                if i[-3].color != i[-4].color and int(i[-3].number) == int(i[-4].number) - 3:
                    if i[-4].color == i[-5].color and int(i[-4].number) == int(i[-5].number) - 4:
                        front_row_list.append(i[-1])
                        front_row_list.append(i[-2])
                        front_row_list.append(i[-3])
                        front_row_list.append(i[-4])
                else:
                    front_row_list.append(i[-1])
                    front_row_list.append(i[-2])
                    front_row_list.append(i[-3])
            else:
                front_row_list.append(i[-1])
                front_row_list.append(i[-2])
        else:
            front_row_list.append(i[-1])
    return front_row_list


for i in range(51):
    for card in card_list_init:
        if len(list1) != 0:
            num = random.randint(0, len(list1) - 1)
            item = list1.pop(num)
            card.coords = item
            for cols in card_list:
                for coords in cols:
                    if coords == card.coords:
                        cols.remove(coords)
                        cols.append(card)

            card.top_rect = pygame.Rect(card.coords[0], card.coords[1], 102, 155)
            gameDisplay.blit(card.card, (card.coords[0], card.coords[1], 115, 160))
print(list1)
front_row_list = front_row()

aux_card_list = []


def sort_func(e):
    for i in e:
        return i.coords[1]


for i in card_list:
    aux_card_list.append(i)
aux_card_list.sort(key=sort_func)

for i in aux_card_list:
    for c in i:
        gameDisplay.blit(c.card, (c.coords[0], c.coords[1], 102, 155))

pygame.display.update()


def check_click():
    global front_row_list
    posm = pygame.mouse.get_pos()
    for box in box_list:
        if box.top_rect.collidepoint(posm):
            box.clicked()
    for i in front_row_list:
        if i.top_rect.collidepoint(posm):
            front_row_list = front_row()
            i.clicked()
    for house in house_list:
        if house.top_rect.collidepoint(posm):
            house.clicked()

while not gameExit:

    if pygame.mouse.get_pressed()[0] is True:
        check_click()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
