import pygame
import sys

gameDisplay = pygame.display.set_mode((1024, 700))
pygame.init()
pygame.display.set_caption("CartaBlanca")
gameExit = False
table = pygame.image.load("resources/table.png")
gameDisplay.blit(table, (0, 0))


class Card:
    def __init__(self, suit, number, coords):
        self.suit = suit
        self.number = number
        self.coords = coords
        self.top_rect = pygame.Rect(self.coords[0], self.coords[1], 102, 155)
        self.name = number + "-" + suit
        self.selected = False
        self.card = pygame.image.load('resources/card_images/' + self.name + ".png")
        self.in_box = False
        gameDisplay.blit(self.card, (self.coords[0], self.coords[1], 115, 160))
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



                    # TODO NEEDS FIXING, IS A MESS! CARD WITH CARD STAIR UNDERNEATH THEM NEEDS TO MOVE CORRECTLY
                    for lista in card_list:
                        if i in lista:
                            lista.remove(i)
                            for col in card_list:
                                for card in col:
                                    if i.coords[0] == card.coords[0] and i.coords[1] == card.coords[1] - 35:
                                        if i.color != card.color and int(i.number) == int(card.number) - 1:
                                            lista.remove(card)
                                            for col in card_list:
                                                for card in col:
                                                    if (i.coords[0] == card.coords[0]
                                                            and i.coords[1] == card.coords[1] - 70):
                                                        if (i.color == card.color
                                                                and int(i.number) == int(card.number) - 2):
                                                            lista.remove(card)
                                                            for col in card_list:
                                                                for card in col:
                                                                    if (i.coords[0] == card.coords[0]
                                                                            and i.coords[1] == card.coords[1] - 105):
                                                                        if (i.color != card.color
                                                                                and int(i.number) == int(
                                                                                    card.number) - 3):
                                                                            lista.remove(card)
                            # for lista2 in card_list:
                            #     if self in lista2:
                            #         lista2.append(i)

                            for col in card_list:
                                for card in col:
                                    if i.coords[0] == card.coords[0] and i.coords[1] == card.coords[1] - 35:
                                        if i.color != card.color and int(i.number) == int(card.number) - 1:
                                            for lista2 in card_list:
                                                if self in lista2:
                                                    lista2.append(card)
                                                    for col in card_list:
                                                        for card in col:
                                                            if (i.coords[0] == card.coords[0]
                                                                    and i.coords[1] == card.coords[1] - 70):
                                                                if (i.color == card.color
                                                                        and int(i.number) == int(card.number) - 2):
                                                                    for lista2 in card_list:
                                                                        if self in lista2:
                                                                            lista2.append(card)

                            for lista2 in card_list:
                                if self in lista2:
                                    lista2.append(i)

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


Box1 = Boxes((4.5, 0))
Box2 = Boxes((119, 0))
Box3 = Boxes((234, 0))
Box4 = Boxes((350, 0))

Hearts_1 = Card("Hearts", "1", [102.4, 175])
Hearts_2 = Card("Hearts", "2", [204.8, 175])
Hearts_3 = Card("Hearts", "3", [307.2, 175])
Hearts_4 = Card("Hearts", "4", [409.6, 175])
Hearts_5 = Card("Hearts", "5", [512, 175])
Claves_6 = Card("Claves", "6", [614.4, 175])
Hearts_7 = Card("Hearts", "7", [716.8, 175])
Claves_8 = Card("Claves", "8", [819.2, 175])
Hearts_9 = Card("Hearts", "9", [102.4, 210])
Hearts_10 = Card("Hearts", "10", [204.8, 210])
Hearts_11 = Card("Hearts", "11", [307.2, 210])
Hearts_12 = Card("Hearts", "12", [409.6, 210])
Hearts_13 = Card("Hearts", "13", [512, 210])
Diamonds_1 = Card("Diamonds", "1", [614.4, 210])
Diamonds_2 = Card("Diamonds", "2", [716.8, 210])
Diamonds_3 = Card("Diamonds", "3", [819.2, 210])
Diamonds_4 = Card("Diamonds", "4", [102.4, 245])
Diamonds_5 = Card("Diamonds", "5", [204.8, 245])
Diamonds_6 = Card("Diamonds", "6", [307.2, 245])
Diamonds_7 = Card("Diamonds", "7", [409.6, 245])
Diamonds_8 = Card("Diamonds", "8", [512, 245])
Diamonds_9 = Card("Diamonds", "9", [614.4, 245])
Diamonds_10 = Card("Diamonds", "10", [716.8, 245])
Diamonds_11 = Card("Diamonds", "11", [819.2, 245])
Diamonds_12 = Card("Diamonds", "12", [102.4, 280])
Diamonds_13 = Card("Diamonds", "13", [204.8, 280])
Spades_1 = Card("Spades", "1", [307.2, 280])
Spades_2 = Card("Spades", "2", [409.6, 280])
Spades_3 = Card("Spades", "3", [512, 280])
Spades_4 = Card("Spades", "4", [614.4, 280])
Spades_5 = Card("Spades", "5", [716.8, 280])
Spades_6 = Card("Spades", "6", [819.2, 280])
Spades_7 = Card("Spades", "7", [102.4, 315])
Spades_8 = Card("Spades", "8", [204.8, 315])
Spades_9 = Card("Spades", "9", [307.2, 315])
Spades_10 = Card("Spades", "10", [409.6, 315])
Spades_11 = Card("Spades", "11", [512, 315])
Spades_12 = Card("Spades", "12", [614.4, 315])
Spades_13 = Card("Spades", "13", [716.8, 315])
Claves_1 = Card("Claves", "1", [819.2, 315])
Claves_2 = Card("Claves", "2", [102.4, 350])
Claves_3 = Card("Claves", "3", [204.8, 350])
Claves_4 = Card("Claves", "4", [307.2, 350])
Claves_5 = Card("Claves", "5", [409.6, 350])
Hearts_6 = Card("Hearts", "6", [512, 350])
Claves_7 = Card("Claves", "7", [614.4, 350])
Hearts_8 = Card("Hearts", "8", [716.8, 350])
Claves_9 = Card("Claves", "9", [819.2, 350])
Claves_10 = Card("Claves", "10", [102.4, 385])
Claves_11 = Card("Claves", "11", [204.8, 385])
Claves_12 = Card("Claves", "12", [307.2, 385])
Claves_13 = Card("Claves", "13", [409.6, 385])

# card_list = [Hearts_1, Hearts_2, Hearts_2, Hearts_3, Hearts_4, Hearts_5, Hearts_6, Hearts_7, Claves_8, Hearts_9,
#              Hearts_10, Hearts_11, Hearts_12, Hearts_13, Diamonds_1, Diamonds_2, Diamonds_3, Diamonds_4, Diamonds_5,
#              Diamonds_6, Diamonds_7, Diamonds_8, Diamonds_9, Diamonds_10, Diamonds_11, Diamonds_12, Diamonds_13,
#              Spades_1, Spades_2, Spades_3, Spades_4, Spades_5, Spades_6, Spades_7, Spades_8, Spades_9, Spades_10,
#              Spades_11, Spades_12, Spades_13, Claves_1, Claves_2, Claves_3, Claves_4, Claves_5, Claves_6, Claves_7,
#              Hearts_8, Claves_9, Claves_10, Claves_11, Claves_12, Claves_13]
#

c0 = [Hearts_1, Hearts_9, Diamonds_4, Diamonds_12, Spades_7, Claves_2, Claves_10]
c1 = [Hearts_2, Hearts_10, Diamonds_5, Diamonds_13, Spades_8, Claves_3, Claves_11]
c2 = [Hearts_3, Hearts_11, Diamonds_6, Spades_1, Spades_9, Claves_4, Claves_12]
c3 = [Hearts_4, Hearts_12, Diamonds_7, Spades_2, Spades_10, Claves_5, Claves_13]
c4 = [Hearts_5, Hearts_13, Diamonds_8, Spades_3, Spades_11, Hearts_6]
c5 = [Claves_6, Diamonds_1, Diamonds_9, Spades_4, Spades_12, Claves_7]
c6 = [Hearts_7, Diamonds_2, Diamonds_10, Spades_5, Spades_13, Hearts_8]
c7 = [Claves_8, Diamonds_3, Diamonds_11, Spades_6, Claves_1, Claves_9]

card_list = [c0, c1, c2, c3, c4, c5, c6, c7]

box_list = [Box1, Box2, Box3, Box4]


def front_row():
    front_row_list = []

    def sort_func(e):
        return e.coords[1]

    for i in card_list:
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


pygame.display.update()

front_row_list = front_row()


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


while not gameExit:

    if pygame.mouse.get_pressed()[2] is True:
        check_click()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
