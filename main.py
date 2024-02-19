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
        global append
        for i in front_row_list:
            if i.selected is True and i is not self and i.color != self.color and int(i.number) == int(self.number) - 1:
                append = 0
                if i in box_card_list:
                    box_card_list.remove(i)
                    i.in_box = False
                    for lista2 in card_list:
                        if self in lista2:
                            lista2.append(i)
                            gameDisplay.blit(table, (0, 0))
                            i.coords[0] = self.coords[0]
                            i.coords[1] = self.coords[1] + 35
                            i.top_rect = pygame.Rect(self.coords[0], self.coords[1], 102, 155)

                for lista in card_list:
                    if i in lista:
                        lista.remove(i)

                        def testttt(num, lista, num2):
                            global append
                            for col in card_list:
                                for card in col:
                                    if i.color == "red":
                                        if num == 35 or num == 105 or num == 175 or num == 245 or num == 315:
                                            if (i.coords[0] == card.coords[0] and i.coords[1] == card.coords[1] - num
                                                    and i.color != card.color and int(i.number) - num2 == int(
                                                        card.number)):
                                                lista.remove(card)
                                                append = num2
                                                return card
                                        if num == 70 or num == 140 or num == 210 or num == 280:
                                            if (i.coords[0] == card.coords[0] and i.coords[1] == card.coords[1] - num
                                                    and i.color == card.color and int(i.number) - num2 == int(
                                                        card.number)):
                                                lista.remove(card)
                                                append = num2
                                                return card
                                    elif i.color == "black":
                                        if (num == 35 or num == 105 or num == 175 or num == 245 or num == 315
                                                or num == 385):
                                            if (i.coords[0] == card.coords[0] and i.coords[1] == card.coords[1] - num
                                                    and i.color != card.color and int(i.number) - num2 == int(
                                                        card.number)):
                                                lista.remove(card)
                                                append = num2
                                                return card
                                        if (num == 70 or num == 140 or num == 210 or num == 280 or num == 350
                                                or num == 420):
                                            if (i.coords[0] == card.coords[0] and i.coords[1] == card.coords[1] - num
                                                    and i.color == card.color and int(i.number) - num2 == int(
                                                        card.number)):
                                                lista.remove(card)
                                                append = num2
                                                return card

                        aux2 = testttt(35, lista, 1)
                        aux3 = testttt(70, lista, 2)
                        aux4 = testttt(105, lista, 3)
                        aux5 = testttt(140, lista, 4)
                        aux6 = testttt(175, lista, 5)
                        aux7 = testttt(210, lista, 6)
                        aux8 = testttt(245, lista, 7)
                        aux9 = testttt(280, lista, 8)
                        aux10 = testttt(315, lista, 9)
                        aux11 = testttt(350, lista, 10)
                        aux12 = testttt(385, lista, 11)
                        aux13 = testttt(420, lista, 12)

                        for lista2 in card_list:
                            if self in lista2:
                                lista2.append(i)
                                gameDisplay.blit(table, (0, 0))
                                i.coords[0] = self.coords[0]
                                i.coords[1] = self.coords[1] + 35
                                i.top_rect = pygame.Rect(self.coords[0], self.coords[1], 102, 155)
                                if append == 1:
                                    lista2.append(aux2)
                                    gameDisplay.blit(table, (0, 0))
                                    aux2.coords[0] = i.coords[0]
                                    aux2.coords[1] = i.coords[1] + 35
                                    aux2.top_rect = pygame.Rect(aux2.coords[0], aux2.coords[1], 102, 155)
                                if append == 2:
                                    lista2.append(aux2)
                                    gameDisplay.blit(table, (0, 0))
                                    aux2.coords[0] = i.coords[0]
                                    aux2.coords[1] = i.coords[1] + 35
                                    aux2.top_rect = pygame.Rect(aux2.coords[0], aux2.coords[1], 102, 155)
                                    lista2.append(aux3)
                                    gameDisplay.blit(table, (0, 0))
                                    aux3.coords[0] = aux2.coords[0]
                                    aux3.coords[1] = aux2.coords[1] + 35
                                    aux3.top_rect = pygame.Rect(aux3.coords[0], aux3.coords[1], 102, 155)
                                if append == 3:
                                    lista2.append(aux2)
                                    gameDisplay.blit(table, (0, 0))
                                    aux2.coords[0] = i.coords[0]
                                    aux2.coords[1] = i.coords[1] + 35
                                    aux2.top_rect = pygame.Rect(aux2.coords[0], aux2.coords[1], 102, 155)
                                    lista2.append(aux3)
                                    gameDisplay.blit(table, (0, 0))
                                    aux3.coords[0] = aux2.coords[0]
                                    aux3.coords[1] = aux2.coords[1] + 35
                                    aux3.top_rect = pygame.Rect(aux3.coords[0], aux3.coords[1], 102, 155)
                                    lista2.append(aux4)
                                    gameDisplay.blit(table, (0, 0))
                                    aux4.coords[0] = aux3.coords[0]
                                    aux4.coords[1] = aux3.coords[1] + 35
                                    aux4.top_rect = pygame.Rect(aux4.coords[0], aux4.coords[1], 102, 155)
                                if append == 4:
                                    lista2.append(aux2)
                                    gameDisplay.blit(table, (0, 0))
                                    aux2.coords[0] = i.coords[0]
                                    aux2.coords[1] = i.coords[1] + 35
                                    aux2.top_rect = pygame.Rect(aux2.coords[0], aux2.coords[1], 102, 155)
                                    lista2.append(aux3)
                                    gameDisplay.blit(table, (0, 0))
                                    aux3.coords[0] = aux2.coords[0]
                                    aux3.coords[1] = aux2.coords[1] + 35
                                    aux3.top_rect = pygame.Rect(aux3.coords[0], aux3.coords[1], 102, 155)
                                    lista2.append(aux4)
                                    gameDisplay.blit(table, (0, 0))
                                    aux4.coords[0] = aux3.coords[0]
                                    aux4.coords[1] = aux3.coords[1] + 35
                                    aux4.top_rect = pygame.Rect(aux4.coords[0], aux4.coords[1], 102, 155)
                                    lista2.append(aux5)
                                    gameDisplay.blit(table, (0, 0))
                                    aux5.coords[0] = aux4.coords[0]
                                    aux5.coords[1] = aux4.coords[1] + 35
                                    aux5.top_rect = pygame.Rect(aux5.coords[0], aux5.coords[1], 102, 155)
                                if append == 5:
                                    lista2.append(aux2)
                                    gameDisplay.blit(table, (0, 0))
                                    aux2.coords[0] = i.coords[0]
                                    aux2.coords[1] = i.coords[1] + 35
                                    aux2.top_rect = pygame.Rect(aux2.coords[0], aux2.coords[1], 102, 155)
                                    lista2.append(aux3)
                                    gameDisplay.blit(table, (0, 0))
                                    aux3.coords[0] = aux2.coords[0]
                                    aux3.coords[1] = aux2.coords[1] + 35
                                    aux3.top_rect = pygame.Rect(aux3.coords[0], aux3.coords[1], 102, 155)
                                    lista2.append(aux4)
                                    gameDisplay.blit(table, (0, 0))
                                    aux4.coords[0] = aux3.coords[0]
                                    aux4.coords[1] = aux3.coords[1] + 35
                                    aux4.top_rect = pygame.Rect(aux4.coords[0], aux4.coords[1], 102, 155)
                                    lista2.append(aux5)
                                    gameDisplay.blit(table, (0, 0))
                                    aux5.coords[0] = aux4.coords[0]
                                    aux5.coords[1] = aux4.coords[1] + 35
                                    aux5.top_rect = pygame.Rect(aux5.coords[0], aux5.coords[1], 102, 155)
                                    lista2.append(aux6)
                                    gameDisplay.blit(table, (0, 0))
                                    aux6.coords[0] = aux5.coords[0]
                                    aux6.coords[1] = aux5.coords[1] + 35
                                    aux6.top_rect = pygame.Rect(aux6.coords[0], aux6.coords[1], 102, 155)
                                if append == 6:
                                    lista2.append(aux2)
                                    gameDisplay.blit(table, (0, 0))
                                    aux2.coords[0] = i.coords[0]
                                    aux2.coords[1] = i.coords[1] + 35
                                    aux2.top_rect = pygame.Rect(aux2.coords[0], aux2.coords[1], 102, 155)
                                    lista2.append(aux3)
                                    gameDisplay.blit(table, (0, 0))
                                    aux3.coords[0] = aux2.coords[0]
                                    aux3.coords[1] = aux2.coords[1] + 35
                                    aux3.top_rect = pygame.Rect(aux3.coords[0], aux3.coords[1], 102, 155)
                                    lista2.append(aux4)
                                    gameDisplay.blit(table, (0, 0))
                                    aux4.coords[0] = aux3.coords[0]
                                    aux4.coords[1] = aux3.coords[1] + 35
                                    aux4.top_rect = pygame.Rect(aux4.coords[0], aux4.coords[1], 102, 155)
                                    lista2.append(aux5)
                                    gameDisplay.blit(table, (0, 0))
                                    aux5.coords[0] = aux4.coords[0]
                                    aux5.coords[1] = aux4.coords[1] + 35
                                    aux5.top_rect = pygame.Rect(aux5.coords[0], aux5.coords[1], 102, 155)
                                    lista2.append(aux6)
                                    gameDisplay.blit(table, (0, 0))
                                    aux6.coords[0] = aux5.coords[0]
                                    aux6.coords[1] = aux5.coords[1] + 35
                                    aux6.top_rect = pygame.Rect(aux6.coords[0], aux6.coords[1], 102, 155)
                                    lista2.append(aux7)
                                    gameDisplay.blit(table, (0, 0))
                                    aux7.coords[0] = aux6.coords[0]
                                    aux7.coords[1] = aux6.coords[1] + 35
                                    aux7.top_rect = pygame.Rect(aux7.coords[0], aux7.coords[1], 102, 155)
                                if append == 7:
                                    lista2.append(aux2)
                                    gameDisplay.blit(table, (0, 0))
                                    aux2.coords[0] = i.coords[0]
                                    aux2.coords[1] = i.coords[1] + 35
                                    aux2.top_rect = pygame.Rect(aux2.coords[0], aux2.coords[1], 102, 155)
                                    lista2.append(aux3)
                                    gameDisplay.blit(table, (0, 0))
                                    aux3.coords[0] = aux2.coords[0]
                                    aux3.coords[1] = aux2.coords[1] + 35
                                    aux3.top_rect = pygame.Rect(aux3.coords[0], aux3.coords[1], 102, 155)
                                    lista2.append(aux4)
                                    gameDisplay.blit(table, (0, 0))
                                    aux4.coords[0] = aux3.coords[0]
                                    aux4.coords[1] = aux3.coords[1] + 35
                                    aux4.top_rect = pygame.Rect(aux4.coords[0], aux4.coords[1], 102, 155)
                                    lista2.append(aux5)
                                    gameDisplay.blit(table, (0, 0))
                                    aux5.coords[0] = aux4.coords[0]
                                    aux5.coords[1] = aux4.coords[1] + 35
                                    aux5.top_rect = pygame.Rect(aux5.coords[0], aux5.coords[1], 102, 155)
                                    lista2.append(aux6)
                                    gameDisplay.blit(table, (0, 0))
                                    aux6.coords[0] = aux5.coords[0]
                                    aux6.coords[1] = aux5.coords[1] + 35
                                    aux6.top_rect = pygame.Rect(aux6.coords[0], aux6.coords[1], 102, 155)
                                    lista2.append(aux7)
                                    gameDisplay.blit(table, (0, 0))
                                    aux7.coords[0] = aux6.coords[0]
                                    aux7.coords[1] = aux6.coords[1] + 35
                                    aux7.top_rect = pygame.Rect(aux7.coords[0], aux7.coords[1], 102, 155)
                                    lista2.append(aux8)
                                    gameDisplay.blit(table, (0, 0))
                                    aux8.coords[0] = aux7.coords[0]
                                    aux8.coords[1] = aux7.coords[1] + 35
                                    aux8.top_rect = pygame.Rect(aux8.coords[0], aux8.coords[1], 102, 155)
                                if append == 8:
                                    lista2.append(aux2)
                                    gameDisplay.blit(table, (0, 0))
                                    aux2.coords[0] = i.coords[0]
                                    aux2.coords[1] = i.coords[1] + 35
                                    aux2.top_rect = pygame.Rect(aux2.coords[0], aux2.coords[1], 102, 155)
                                    lista2.append(aux3)
                                    gameDisplay.blit(table, (0, 0))
                                    aux3.coords[0] = aux2.coords[0]
                                    aux3.coords[1] = aux2.coords[1] + 35
                                    aux3.top_rect = pygame.Rect(aux3.coords[0], aux3.coords[1], 102, 155)
                                    lista2.append(aux4)
                                    gameDisplay.blit(table, (0, 0))
                                    aux4.coords[0] = aux3.coords[0]
                                    aux4.coords[1] = aux3.coords[1] + 35
                                    aux4.top_rect = pygame.Rect(aux4.coords[0], aux4.coords[1], 102, 155)
                                    lista2.append(aux5)
                                    gameDisplay.blit(table, (0, 0))
                                    aux5.coords[0] = aux4.coords[0]
                                    aux5.coords[1] = aux4.coords[1] + 35
                                    aux5.top_rect = pygame.Rect(aux5.coords[0], aux5.coords[1], 102, 155)
                                    lista2.append(aux6)
                                    gameDisplay.blit(table, (0, 0))
                                    aux6.coords[0] = aux5.coords[0]
                                    aux6.coords[1] = aux5.coords[1] + 35
                                    aux6.top_rect = pygame.Rect(aux6.coords[0], aux6.coords[1], 102, 155)
                                    lista2.append(aux7)
                                    gameDisplay.blit(table, (0, 0))
                                    aux7.coords[0] = aux6.coords[0]
                                    aux7.coords[1] = aux6.coords[1] + 35
                                    aux7.top_rect = pygame.Rect(aux7.coords[0], aux7.coords[1], 102, 155)
                                    lista2.append(aux8)
                                    gameDisplay.blit(table, (0, 0))
                                    aux8.coords[0] = aux7.coords[0]
                                    aux8.coords[1] = aux7.coords[1] + 35
                                    aux8.top_rect = pygame.Rect(aux8.coords[0], aux8.coords[1], 102, 155)
                                    lista2.append(aux9)
                                    gameDisplay.blit(table, (0, 0))
                                    aux9.coords[0] = aux8.coords[0]
                                    aux9.coords[1] = aux8.coords[1] + 35
                                    aux9.top_rect = pygame.Rect(aux9.coords[0], aux9.coords[1], 102, 155)
                                if append == 9:
                                    lista2.append(aux2)
                                    gameDisplay.blit(table, (0, 0))
                                    aux2.coords[0] = i.coords[0]
                                    aux2.coords[1] = i.coords[1] + 35
                                    aux2.top_rect = pygame.Rect(aux2.coords[0], aux2.coords[1], 102, 155)
                                    lista2.append(aux3)
                                    gameDisplay.blit(table, (0, 0))
                                    aux3.coords[0] = aux2.coords[0]
                                    aux3.coords[1] = aux2.coords[1] + 35
                                    aux3.top_rect = pygame.Rect(aux3.coords[0], aux3.coords[1], 102, 155)
                                    lista2.append(aux4)
                                    gameDisplay.blit(table, (0, 0))
                                    aux4.coords[0] = aux3.coords[0]
                                    aux4.coords[1] = aux3.coords[1] + 35
                                    aux4.top_rect = pygame.Rect(aux4.coords[0], aux4.coords[1], 102, 155)
                                    lista2.append(aux5)
                                    gameDisplay.blit(table, (0, 0))
                                    aux5.coords[0] = aux4.coords[0]
                                    aux5.coords[1] = aux4.coords[1] + 35
                                    aux5.top_rect = pygame.Rect(aux5.coords[0], aux5.coords[1], 102, 155)
                                    lista2.append(aux6)
                                    gameDisplay.blit(table, (0, 0))
                                    aux6.coords[0] = aux5.coords[0]
                                    aux6.coords[1] = aux5.coords[1] + 35
                                    aux6.top_rect = pygame.Rect(aux6.coords[0], aux6.coords[1], 102, 155)
                                    lista2.append(aux7)
                                    gameDisplay.blit(table, (0, 0))
                                    aux7.coords[0] = aux6.coords[0]
                                    aux7.coords[1] = aux6.coords[1] + 35
                                    aux7.top_rect = pygame.Rect(aux7.coords[0], aux7.coords[1], 102, 155)
                                    lista2.append(aux8)
                                    gameDisplay.blit(table, (0, 0))
                                    aux8.coords[0] = aux7.coords[0]
                                    aux8.coords[1] = aux7.coords[1] + 35
                                    aux8.top_rect = pygame.Rect(aux8.coords[0], aux8.coords[1], 102, 155)
                                    lista2.append(aux9)
                                    gameDisplay.blit(table, (0, 0))
                                    aux9.coords[0] = aux8.coords[0]
                                    aux9.coords[1] = aux8.coords[1] + 35
                                    aux9.top_rect = pygame.Rect(aux9.coords[0], aux9.coords[1], 102, 155)
                                    lista2.append(aux10)
                                    gameDisplay.blit(table, (0, 0))
                                    aux10.coords[0] = aux9.coords[0]
                                    aux10.coords[1] = aux9.coords[1] + 35
                                    aux10.top_rect = pygame.Rect(aux10.coords[0], aux10.coords[1], 102, 155)
                                if append == 10:
                                    lista2.append(aux2)
                                    gameDisplay.blit(table, (0, 0))
                                    aux2.coords[0] = i.coords[0]
                                    aux2.coords[1] = i.coords[1] + 35
                                    aux2.top_rect = pygame.Rect(aux2.coords[0], aux2.coords[1], 102, 155)
                                    lista2.append(aux3)
                                    gameDisplay.blit(table, (0, 0))
                                    aux3.coords[0] = aux2.coords[0]
                                    aux3.coords[1] = aux2.coords[1] + 35
                                    aux3.top_rect = pygame.Rect(aux3.coords[0], aux3.coords[1], 102, 155)
                                    lista2.append(aux4)
                                    gameDisplay.blit(table, (0, 0))
                                    aux4.coords[0] = aux3.coords[0]
                                    aux4.coords[1] = aux3.coords[1] + 35
                                    aux4.top_rect = pygame.Rect(aux4.coords[0], aux4.coords[1], 102, 155)
                                    lista2.append(aux5)
                                    gameDisplay.blit(table, (0, 0))
                                    aux5.coords[0] = aux4.coords[0]
                                    aux5.coords[1] = aux4.coords[1] + 35
                                    aux5.top_rect = pygame.Rect(aux5.coords[0], aux5.coords[1], 102, 155)
                                    lista2.append(aux6)
                                    gameDisplay.blit(table, (0, 0))
                                    aux6.coords[0] = aux5.coords[0]
                                    aux6.coords[1] = aux5.coords[1] + 35
                                    aux6.top_rect = pygame.Rect(aux6.coords[0], aux6.coords[1], 102, 155)
                                    lista2.append(aux7)
                                    gameDisplay.blit(table, (0, 0))
                                    aux7.coords[0] = aux6.coords[0]
                                    aux7.coords[1] = aux6.coords[1] + 35
                                    aux7.top_rect = pygame.Rect(aux7.coords[0], aux7.coords[1], 102, 155)
                                    lista2.append(aux8)
                                    gameDisplay.blit(table, (0, 0))
                                    aux8.coords[0] = aux7.coords[0]
                                    aux8.coords[1] = aux7.coords[1] + 35
                                    aux8.top_rect = pygame.Rect(aux8.coords[0], aux8.coords[1], 102, 155)
                                    lista2.append(aux9)
                                    gameDisplay.blit(table, (0, 0))
                                    aux9.coords[0] = aux8.coords[0]
                                    aux9.coords[1] = aux8.coords[1] + 35
                                    aux9.top_rect = pygame.Rect(aux9.coords[0], aux9.coords[1], 102, 155)
                                    lista2.append(aux10)
                                    gameDisplay.blit(table, (0, 0))
                                    aux10.coords[0] = aux9.coords[0]
                                    aux10.coords[1] = aux9.coords[1] + 35
                                    aux10.top_rect = pygame.Rect(aux10.coords[0], aux10.coords[1], 102, 155)
                                    lista2.append(aux11)
                                    gameDisplay.blit(table, (0, 0))
                                    aux11.coords[0] = aux10.coords[0]
                                    aux11.coords[1] = aux10.coords[1] + 35
                                    aux11.top_rect = pygame.Rect(aux11.coords[0], aux11.coords[1], 102, 155)
                                if append == 11:
                                    lista2.append(aux2)
                                    gameDisplay.blit(table, (0, 0))
                                    aux2.coords[0] = i.coords[0]
                                    aux2.coords[1] = i.coords[1] + 35
                                    aux2.top_rect = pygame.Rect(aux2.coords[0], aux2.coords[1], 102, 155)
                                    lista2.append(aux3)
                                    gameDisplay.blit(table, (0, 0))
                                    aux3.coords[0] = aux2.coords[0]
                                    aux3.coords[1] = aux2.coords[1] + 35
                                    aux3.top_rect = pygame.Rect(aux3.coords[0], aux3.coords[1], 102, 155)
                                    lista2.append(aux4)
                                    gameDisplay.blit(table, (0, 0))
                                    aux4.coords[0] = aux3.coords[0]
                                    aux4.coords[1] = aux3.coords[1] + 35
                                    aux4.top_rect = pygame.Rect(aux4.coords[0], aux4.coords[1], 102, 155)
                                    lista2.append(aux5)
                                    gameDisplay.blit(table, (0, 0))
                                    aux5.coords[0] = aux4.coords[0]
                                    aux5.coords[1] = aux4.coords[1] + 35
                                    aux5.top_rect = pygame.Rect(aux5.coords[0], aux5.coords[1], 102, 155)
                                    lista2.append(aux6)
                                    gameDisplay.blit(table, (0, 0))
                                    aux6.coords[0] = aux5.coords[0]
                                    aux6.coords[1] = aux5.coords[1] + 35
                                    aux6.top_rect = pygame.Rect(aux6.coords[0], aux6.coords[1], 102, 155)
                                    lista2.append(aux7)
                                    gameDisplay.blit(table, (0, 0))
                                    aux7.coords[0] = aux6.coords[0]
                                    aux7.coords[1] = aux6.coords[1] + 35
                                    aux7.top_rect = pygame.Rect(aux7.coords[0], aux7.coords[1], 102, 155)
                                    lista2.append(aux8)
                                    gameDisplay.blit(table, (0, 0))
                                    aux8.coords[0] = aux7.coords[0]
                                    aux8.coords[1] = aux7.coords[1] + 35
                                    aux8.top_rect = pygame.Rect(aux8.coords[0], aux8.coords[1], 102, 155)
                                    lista2.append(aux9)
                                    gameDisplay.blit(table, (0, 0))
                                    aux9.coords[0] = aux8.coords[0]
                                    aux9.coords[1] = aux8.coords[1] + 35
                                    aux9.top_rect = pygame.Rect(aux9.coords[0], aux9.coords[1], 102, 155)
                                    lista2.append(aux10)
                                    gameDisplay.blit(table, (0, 0))
                                    aux10.coords[0] = aux9.coords[0]
                                    aux10.coords[1] = aux9.coords[1] + 35
                                    aux10.top_rect = pygame.Rect(aux10.coords[0], aux10.coords[1], 102, 155)
                                    lista2.append(aux11)
                                    gameDisplay.blit(table, (0, 0))
                                    aux11.coords[0] = aux10.coords[0]
                                    aux11.coords[1] = aux10.coords[1] + 35
                                    aux11.top_rect = pygame.Rect(aux11.coords[0], aux11.coords[1], 102, 155)
                                    lista2.append(aux12)
                                    gameDisplay.blit(table, (0, 0))
                                    aux12.coords[0] = aux11.coords[0]
                                    aux12.coords[1] = aux11.coords[1] + 35
                                    aux12.top_rect = pygame.Rect(aux12.coords[0], aux12.coords[1], 102, 155)
                                if append == 12:
                                    lista2.append(aux2)
                                    gameDisplay.blit(table, (0, 0))
                                    aux2.coords[0] = i.coords[0]
                                    aux2.coords[1] = i.coords[1] + 35
                                    aux2.top_rect = pygame.Rect(aux2.coords[0], aux2.coords[1], 102, 155)
                                    lista2.append(aux3)
                                    gameDisplay.blit(table, (0, 0))
                                    aux3.coords[0] = aux2.coords[0]
                                    aux3.coords[1] = aux2.coords[1] + 35
                                    aux3.top_rect = pygame.Rect(aux3.coords[0], aux3.coords[1], 102, 155)
                                    lista2.append(aux4)
                                    gameDisplay.blit(table, (0, 0))
                                    aux4.coords[0] = aux3.coords[0]
                                    aux4.coords[1] = aux3.coords[1] + 35
                                    aux4.top_rect = pygame.Rect(aux4.coords[0], aux4.coords[1], 102, 155)
                                    lista2.append(aux5)
                                    gameDisplay.blit(table, (0, 0))
                                    aux5.coords[0] = aux4.coords[0]
                                    aux5.coords[1] = aux4.coords[1] + 35
                                    aux5.top_rect = pygame.Rect(aux5.coords[0], aux5.coords[1], 102, 155)
                                    lista2.append(aux6)
                                    gameDisplay.blit(table, (0, 0))
                                    aux6.coords[0] = aux5.coords[0]
                                    aux6.coords[1] = aux5.coords[1] + 35
                                    aux6.top_rect = pygame.Rect(aux6.coords[0], aux6.coords[1], 102, 155)
                                    lista2.append(aux7)
                                    gameDisplay.blit(table, (0, 0))
                                    aux7.coords[0] = aux6.coords[0]
                                    aux7.coords[1] = aux6.coords[1] + 35
                                    aux7.top_rect = pygame.Rect(aux7.coords[0], aux7.coords[1], 102, 155)
                                    lista2.append(aux8)
                                    gameDisplay.blit(table, (0, 0))
                                    aux8.coords[0] = aux7.coords[0]
                                    aux8.coords[1] = aux7.coords[1] + 35
                                    aux8.top_rect = pygame.Rect(aux8.coords[0], aux8.coords[1], 102, 155)
                                    lista2.append(aux9)
                                    gameDisplay.blit(table, (0, 0))
                                    aux9.coords[0] = aux8.coords[0]
                                    aux9.coords[1] = aux8.coords[1] + 35
                                    aux9.top_rect = pygame.Rect(aux9.coords[0], aux9.coords[1], 102, 155)
                                    lista2.append(aux10)
                                    gameDisplay.blit(table, (0, 0))
                                    aux10.coords[0] = aux9.coords[0]
                                    aux10.coords[1] = aux9.coords[1] + 35
                                    aux10.top_rect = pygame.Rect(aux10.coords[0], aux10.coords[1], 102, 155)
                                    lista2.append(aux11)
                                    gameDisplay.blit(table, (0, 0))
                                    aux11.coords[0] = aux10.coords[0]
                                    aux11.coords[1] = aux10.coords[1] + 35
                                    aux11.top_rect = pygame.Rect(aux11.coords[0], aux11.coords[1], 102, 155)
                                    lista2.append(aux12)
                                    gameDisplay.blit(table, (0, 0))
                                    aux12.coords[0] = aux11.coords[0]
                                    aux12.coords[1] = aux11.coords[1] + 35
                                    aux12.top_rect = pygame.Rect(aux12.coords[0], aux12.coords[1], 102, 155)
                                    lista2.append(aux13)
                                    gameDisplay.blit(table, (0, 0))
                                    aux13.coords[0] = aux12.coords[0]
                                    aux13.coords[1] = aux12.coords[1] + 35
                                    aux13.top_rect = pygame.Rect(aux13.coords[0], aux13.coords[1], 102, 155)

                aux_card_list = []

                def sort_func(e):
                    for i in e:
                        return i.coords[1]

                for i in card_list:
                    if i != []:
                        aux_card_list.append(i)
                aux_card_list.sort(key=sort_func)

                for i in box_card_list:
                    gameDisplay.blit(i.card, (i.coords[0], i.coords[1], 102, 155))

                for i in house_card_list:
                    gameDisplay.blit(i.card, (i.coords[0], i.coords[1], 102, 155))

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
                    for list in card_list:
                        if i in list:
                            list.remove(i)
                            box_card_list.append(i)
                    aux_card_list = []

                    def sort_func(e):
                        for i in e:
                            return i.coords[1]

                    for i in card_list:
                        if i != []:
                            aux_card_list.append(i)
                    aux_card_list.sort(key=sort_func)

                    for i in box_card_list:
                        gameDisplay.blit(i.card, (i.coords[0], i.coords[1], 102, 155))

                    for i in house_card_list:
                        gameDisplay.blit(i.card, (i.coords[0], i.coords[1], 102, 155))

                    for i in aux_card_list:
                        for c in i:
                            gameDisplay.blit(c.card, (c.coords[0], c.coords[1], 102, 155))
                    pygame.display.update()
                    self.filled = True
        for i in front_row_list:
            i.selected = False


class Column:
    def __init__(self, coords, col):
        self.col = col
        self.coords = coords
        self.filled = False
        self.top_rect = pygame.Rect(self.coords[0], self.coords[1], 102, 155)

    def clicked(self):
        for i in front_row_list:
            if i.selected is True:
                if self.filled is False:
                    for lista in card_list:
                        if i in lista:
                            lista.remove(i)

                            def testttt(num, lista, num2):
                                global append
                                for col in card_list:
                                    for card in col:
                                        if i.color == "red":
                                            if (num == 35 or num == 105 or num == 175 or num == 245 or num == 315
                                                    or num == 420):
                                                if (i.coords[0] == card.coords[0] and i.coords[1] == card.coords[
                                                    1] - num
                                                        and i.color != card.color and int(i.number) - num2 == int(
                                                            card.number)):
                                                    lista.remove(card)
                                                    append = num2
                                                    print(card)
                                                    return card
                                            if (num == 70 or num == 140 or num == 210 or num == 280 or num == 350
                                                    or num == 420):
                                                if (i.coords[0] == card.coords[0] and i.coords[1] == card.coords[
                                                    1] - num
                                                        and i.color == card.color and int(i.number) - num2 == int(
                                                            card.number)):
                                                    lista.remove(card)
                                                    append = num2
                                                    print(card)
                                                    return card
                                        elif i.color == "black":
                                            if (
                                                    num == 35 or num == 105 or num == 175 or num == 245 or num == 315 or num == 350
                                                    or num == 420):
                                                if (i.coords[0] == card.coords[0] and i.coords[1] == card.coords[
                                                    1] - num
                                                        and i.color != card.color and int(i.number) - num2 == int(
                                                            card.number)):
                                                    lista.remove(card)
                                                    append = num2 
                                                    print(card)
                                                    return card

                                            if (num == 70 or num == 140 or num == 210 or num == 280 or num == 350
                                                    or num == 420):
                                                if (i.coords[0] == card.coords[0] and i.coords[1] == card.coords[
                                                    1] - num
                                                        and i.color == card.color and int(i.number) - num2 == int(
                                                            card.number)):
                                                    lista.remove(card)
                                                    append = num2
                                                    print(card)
                                                    return card

                            aux2 = testttt(35, lista, 1)
                            aux3 = testttt(70, lista, 2)
                            aux4 = testttt(105, lista, 3)
                            aux5 = testttt(140, lista, 4)
                            aux6 = testttt(175, lista, 5)
                            aux7 = testttt(210, lista, 6)
                            aux8 = testttt(245, lista, 7)
                            aux9 = testttt(280, lista, 8)
                            aux10 = testttt(315, lista, 9)
                            aux11 = testttt(350, lista, 10)
                            aux12 = testttt(385, lista, 11)
                            aux13 = testttt(420, lista, 12)
                            print(aux2, aux3)
                            self.col.append(i)
                            gameDisplay.blit(table, (0, 0))
                            i.coords[0] = self.coords[0]
                            i.coords[1] = self.coords[1]
                            i.top_rect = pygame.Rect(self.coords[0], self.coords[1], 102, 155)
                            if append == 1:
                                self.col.append(aux2)
                                gameDisplay.blit(table, (0, 0))
                                aux2.coords[0] = i.coords[0]
                                aux2.coords[1] = i.coords[1] + 35
                                aux2.top_rect = pygame.Rect(aux2.coords[0], aux2.coords[1], 102, 155)
                            if append == 2:
                                self.col.append(aux2)
                                gameDisplay.blit(table, (0, 0))
                                aux2.coords[0] = i.coords[0]
                                aux2.coords[1] = i.coords[1] + 35
                                aux2.top_rect = pygame.Rect(aux2.coords[0], aux2.coords[1], 102, 155)
                                self.col.append(aux3)
                                gameDisplay.blit(table, (0, 0))
                                aux3.coords[0] = aux2.coords[0]
                                aux3.coords[1] = aux2.coords[1] + 35
                                aux3.top_rect = pygame.Rect(aux3.coords[0], aux3.coords[1], 102, 155)
                            if append == 3:
                                self.col.append(aux2)
                                gameDisplay.blit(table, (0, 0))
                                aux2.coords[0] = i.coords[0]
                                aux2.coords[1] = i.coords[1] + 35
                                aux2.top_rect = pygame.Rect(aux2.coords[0], aux2.coords[1], 102, 155)
                                self.col.append(aux3)
                                gameDisplay.blit(table, (0, 0))
                                aux3.coords[0] = aux2.coords[0]
                                aux3.coords[1] = aux2.coords[1] + 35
                                aux3.top_rect = pygame.Rect(aux3.coords[0], aux3.coords[1], 102, 155)
                                self.col.append(aux4)
                                gameDisplay.blit(table, (0, 0))
                                aux4.coords[0] = aux3.coords[0]
                                aux4.coords[1] = aux3.coords[1] + 35
                                aux4.top_rect = pygame.Rect(aux4.coords[0], aux4.coords[1], 102, 155)
                            if append == 4:
                                self.col.append(aux2)
                                gameDisplay.blit(table, (0, 0))
                                aux2.coords[0] = i.coords[0]
                                aux2.coords[1] = i.coords[1] + 35
                                aux2.top_rect = pygame.Rect(aux2.coords[0], aux2.coords[1], 102, 155)
                                self.col.append(aux3)
                                gameDisplay.blit(table, (0, 0))
                                aux3.coords[0] = aux2.coords[0]
                                aux3.coords[1] = aux2.coords[1] + 35
                                aux3.top_rect = pygame.Rect(aux3.coords[0], aux3.coords[1], 102, 155)
                                self.col.append(aux4)
                                gameDisplay.blit(table, (0, 0))
                                aux4.coords[0] = aux3.coords[0]
                                aux4.coords[1] = aux3.coords[1] + 35
                                aux4.top_rect = pygame.Rect(aux4.coords[0], aux4.coords[1], 102, 155)
                                self.col.append(aux5)
                                gameDisplay.blit(table, (0, 0))
                                aux5.coords[0] = aux4.coords[0]
                                aux5.coords[1] = aux4.coords[1] + 35
                                aux5.top_rect = pygame.Rect(aux5.coords[0], aux5.coords[1], 102, 155)
                            if append == 5:
                                self.col.append(aux2)
                                gameDisplay.blit(table, (0, 0))
                                aux2.coords[0] = i.coords[0]
                                aux2.coords[1] = i.coords[1] + 35
                                aux2.top_rect = pygame.Rect(aux2.coords[0], aux2.coords[1], 102, 155)
                                self.col.append(aux3)
                                gameDisplay.blit(table, (0, 0))
                                aux3.coords[0] = aux2.coords[0]
                                aux3.coords[1] = aux2.coords[1] + 35
                                aux3.top_rect = pygame.Rect(aux3.coords[0], aux3.coords[1], 102, 155)
                                self.col.append(aux4)
                                gameDisplay.blit(table, (0, 0))
                                aux4.coords[0] = aux3.coords[0]
                                aux4.coords[1] = aux3.coords[1] + 35
                                aux4.top_rect = pygame.Rect(aux4.coords[0], aux4.coords[1], 102, 155)
                                self.col.append(aux5)
                                gameDisplay.blit(table, (0, 0))
                                aux5.coords[0] = aux4.coords[0]
                                aux5.coords[1] = aux4.coords[1] + 35
                                aux5.top_rect = pygame.Rect(aux5.coords[0], aux5.coords[1], 102, 155)
                                self.col.append(aux6)
                                gameDisplay.blit(table, (0, 0))
                                aux6.coords[0] = aux5.coords[0]
                                aux6.coords[1] = aux5.coords[1] + 35
                                aux6.top_rect = pygame.Rect(aux6.coords[0], aux6.coords[1], 102, 155)
                            if append == 6:
                                self.col.append(aux2)
                                gameDisplay.blit(table, (0, 0))
                                aux2.coords[0] = i.coords[0]
                                aux2.coords[1] = i.coords[1] + 35
                                aux2.top_rect = pygame.Rect(aux2.coords[0], aux2.coords[1], 102, 155)
                                self.col.append(aux3)
                                gameDisplay.blit(table, (0, 0))
                                aux3.coords[0] = aux2.coords[0]
                                aux3.coords[1] = aux2.coords[1] + 35
                                aux3.top_rect = pygame.Rect(aux3.coords[0], aux3.coords[1], 102, 155)
                                self.col.append(aux4)
                                gameDisplay.blit(table, (0, 0))
                                aux4.coords[0] = aux3.coords[0]
                                aux4.coords[1] = aux3.coords[1] + 35
                                aux4.top_rect = pygame.Rect(aux4.coords[0], aux4.coords[1], 102, 155)
                                self.col.append(aux5)
                                gameDisplay.blit(table, (0, 0))
                                aux5.coords[0] = aux4.coords[0]
                                aux5.coords[1] = aux4.coords[1] + 35
                                aux5.top_rect = pygame.Rect(aux5.coords[0], aux5.coords[1], 102, 155)
                                self.col.append(aux6)
                                gameDisplay.blit(table, (0, 0))
                                aux6.coords[0] = aux5.coords[0]
                                aux6.coords[1] = aux5.coords[1] + 35
                                aux6.top_rect = pygame.Rect(aux6.coords[0], aux6.coords[1], 102, 155)
                                self.col.append(aux7)
                                gameDisplay.blit(table, (0, 0))
                                aux7.coords[0] = aux6.coords[0]
                                aux7.coords[1] = aux6.coords[1] + 35
                                aux7.top_rect = pygame.Rect(aux7.coords[0], aux7.coords[1], 102, 155)
                            if append == 7:
                                self.col.append(aux2)
                                gameDisplay.blit(table, (0, 0))
                                aux2.coords[0] = i.coords[0]
                                aux2.coords[1] = i.coords[1] + 35
                                aux2.top_rect = pygame.Rect(aux2.coords[0], aux2.coords[1], 102, 155)
                                self.col.append(aux3)
                                gameDisplay.blit(table, (0, 0))
                                aux3.coords[0] = aux2.coords[0]
                                aux3.coords[1] = aux2.coords[1] + 35
                                aux3.top_rect = pygame.Rect(aux3.coords[0], aux3.coords[1], 102, 155)
                                self.col.append(aux4)
                                gameDisplay.blit(table, (0, 0))
                                aux4.coords[0] = aux3.coords[0]
                                aux4.coords[1] = aux3.coords[1] + 35
                                aux4.top_rect = pygame.Rect(aux4.coords[0], aux4.coords[1], 102, 155)
                                self.col.append(aux5)
                                gameDisplay.blit(table, (0, 0))
                                aux5.coords[0] = aux4.coords[0]
                                aux5.coords[1] = aux4.coords[1] + 35
                                aux5.top_rect = pygame.Rect(aux5.coords[0], aux5.coords[1], 102, 155)
                                self.col.append(aux6)
                                gameDisplay.blit(table, (0, 0))
                                aux6.coords[0] = aux5.coords[0]
                                aux6.coords[1] = aux5.coords[1] + 35
                                aux6.top_rect = pygame.Rect(aux6.coords[0], aux6.coords[1], 102, 155)
                                self.col.append(aux7)
                                gameDisplay.blit(table, (0, 0))
                                aux7.coords[0] = aux6.coords[0]
                                aux7.coords[1] = aux6.coords[1] + 35
                                aux7.top_rect = pygame.Rect(aux7.coords[0], aux7.coords[1], 102, 155)
                                self.col.append(aux8)
                                gameDisplay.blit(table, (0, 0))
                                aux8.coords[0] = aux7.coords[0]
                                aux8.coords[1] = aux7.coords[1] + 35
                                aux8.top_rect = pygame.Rect(aux8.coords[0], aux8.coords[1], 102, 155)
                            if append == 8:
                                self.col.append(aux2)
                                gameDisplay.blit(table, (0, 0))
                                aux2.coords[0] = i.coords[0]
                                aux2.coords[1] = i.coords[1] + 35
                                aux2.top_rect = pygame.Rect(aux2.coords[0], aux2.coords[1], 102, 155)
                                self.col.append(aux3)
                                gameDisplay.blit(table, (0, 0))
                                aux3.coords[0] = aux2.coords[0]
                                aux3.coords[1] = aux2.coords[1] + 35
                                aux3.top_rect = pygame.Rect(aux3.coords[0], aux3.coords[1], 102, 155)
                                self.col.append(aux4)
                                gameDisplay.blit(table, (0, 0))
                                aux4.coords[0] = aux3.coords[0]
                                aux4.coords[1] = aux3.coords[1] + 35
                                aux4.top_rect = pygame.Rect(aux4.coords[0], aux4.coords[1], 102, 155)
                                self.col.append(aux5)
                                gameDisplay.blit(table, (0, 0))
                                aux5.coords[0] = aux4.coords[0]
                                aux5.coords[1] = aux4.coords[1] + 35
                                aux5.top_rect = pygame.Rect(aux5.coords[0], aux5.coords[1], 102, 155)
                                self.col.append(aux6)
                                gameDisplay.blit(table, (0, 0))
                                aux6.coords[0] = aux5.coords[0]
                                aux6.coords[1] = aux5.coords[1] + 35
                                aux6.top_rect = pygame.Rect(aux6.coords[0], aux6.coords[1], 102, 155)
                                self.col.append(aux7)
                                gameDisplay.blit(table, (0, 0))
                                aux7.coords[0] = aux6.coords[0]
                                aux7.coords[1] = aux6.coords[1] + 35
                                aux7.top_rect = pygame.Rect(aux7.coords[0], aux7.coords[1], 102, 155)
                                self.col.append(aux8)
                                gameDisplay.blit(table, (0, 0))
                                aux8.coords[0] = aux7.coords[0]
                                aux8.coords[1] = aux7.coords[1] + 35
                                aux8.top_rect = pygame.Rect(aux8.coords[0], aux8.coords[1], 102, 155)
                                self.col.append(aux9)
                                gameDisplay.blit(table, (0, 0))
                                aux9.coords[0] = aux8.coords[0]
                                aux9.coords[1] = aux8.coords[1] + 35
                                aux9.top_rect = pygame.Rect(aux9.coords[0], aux9.coords[1], 102, 155)
                            if append == 9:
                                self.col.append(aux2)
                                gameDisplay.blit(table, (0, 0))
                                aux2.coords[0] = i.coords[0]
                                aux2.coords[1] = i.coords[1] + 35
                                aux2.top_rect = pygame.Rect(aux2.coords[0], aux2.coords[1], 102, 155)
                                self.col.append(aux3)
                                gameDisplay.blit(table, (0, 0))
                                aux3.coords[0] = aux2.coords[0]
                                aux3.coords[1] = aux2.coords[1] + 35
                                aux3.top_rect = pygame.Rect(aux3.coords[0], aux3.coords[1], 102, 155)
                                self.col.append(aux4)
                                gameDisplay.blit(table, (0, 0))
                                aux4.coords[0] = aux3.coords[0]
                                aux4.coords[1] = aux3.coords[1] + 35
                                aux4.top_rect = pygame.Rect(aux4.coords[0], aux4.coords[1], 102, 155)
                                self.col.append(aux5)
                                gameDisplay.blit(table, (0, 0))
                                aux5.coords[0] = aux4.coords[0]
                                aux5.coords[1] = aux4.coords[1] + 35
                                aux5.top_rect = pygame.Rect(aux5.coords[0], aux5.coords[1], 102, 155)
                                self.col.append(aux6)
                                gameDisplay.blit(table, (0, 0))
                                aux6.coords[0] = aux5.coords[0]
                                aux6.coords[1] = aux5.coords[1] + 35
                                aux6.top_rect = pygame.Rect(aux6.coords[0], aux6.coords[1], 102, 155)
                                self.col.append(aux7)
                                gameDisplay.blit(table, (0, 0))
                                aux7.coords[0] = aux6.coords[0]
                                aux7.coords[1] = aux6.coords[1] + 35
                                aux7.top_rect = pygame.Rect(aux7.coords[0], aux7.coords[1], 102, 155)
                                self.col.append(aux8)
                                gameDisplay.blit(table, (0, 0))
                                aux8.coords[0] = aux7.coords[0]
                                aux8.coords[1] = aux7.coords[1] + 35
                                aux8.top_rect = pygame.Rect(aux8.coords[0], aux8.coords[1], 102, 155)
                                self.col.append(aux9)
                                gameDisplay.blit(table, (0, 0))
                                aux9.coords[0] = aux8.coords[0]
                                aux9.coords[1] = aux8.coords[1] + 35
                                aux9.top_rect = pygame.Rect(aux9.coords[0], aux9.coords[1], 102, 155)
                                self.col.append(aux10)
                                gameDisplay.blit(table, (0, 0))
                                aux10.coords[0] = aux9.coords[0]
                                aux10.coords[1] = aux9.coords[1] + 35
                                aux10.top_rect = pygame.Rect(aux10.coords[0], aux10.coords[1], 102, 155)
                            if append == 10:
                                self.col.append(aux2)
                                gameDisplay.blit(table, (0, 0))
                                aux2.coords[0] = i.coords[0]
                                aux2.coords[1] = i.coords[1] + 35
                                aux2.top_rect = pygame.Rect(aux2.coords[0], aux2.coords[1], 102, 155)
                                self.col.append(aux3)
                                gameDisplay.blit(table, (0, 0))
                                aux3.coords[0] = aux2.coords[0]
                                aux3.coords[1] = aux2.coords[1] + 35
                                aux3.top_rect = pygame.Rect(aux3.coords[0], aux3.coords[1], 102, 155)
                                self.col.append(aux4)
                                gameDisplay.blit(table, (0, 0))
                                aux4.coords[0] = aux3.coords[0]
                                aux4.coords[1] = aux3.coords[1] + 35
                                aux4.top_rect = pygame.Rect(aux4.coords[0], aux4.coords[1], 102, 155)
                                self.col.append(aux5)
                                gameDisplay.blit(table, (0, 0))
                                aux5.coords[0] = aux4.coords[0]
                                aux5.coords[1] = aux4.coords[1] + 35
                                aux5.top_rect = pygame.Rect(aux5.coords[0], aux5.coords[1], 102, 155)
                                self.col.append(aux6)
                                gameDisplay.blit(table, (0, 0))
                                aux6.coords[0] = aux5.coords[0]
                                aux6.coords[1] = aux5.coords[1] + 35
                                aux6.top_rect = pygame.Rect(aux6.coords[0], aux6.coords[1], 102, 155)
                                self.col.append(aux7)
                                gameDisplay.blit(table, (0, 0))
                                aux7.coords[0] = aux6.coords[0]
                                aux7.coords[1] = aux6.coords[1] + 35
                                aux7.top_rect = pygame.Rect(aux7.coords[0], aux7.coords[1], 102, 155)
                                self.col.append(aux8)
                                gameDisplay.blit(table, (0, 0))
                                aux8.coords[0] = aux7.coords[0]
                                aux8.coords[1] = aux7.coords[1] + 35
                                aux8.top_rect = pygame.Rect(aux8.coords[0], aux8.coords[1], 102, 155)
                                self.col.append(aux9)
                                gameDisplay.blit(table, (0, 0))
                                aux9.coords[0] = aux8.coords[0]
                                aux9.coords[1] = aux8.coords[1] + 35
                                aux9.top_rect = pygame.Rect(aux9.coords[0], aux9.coords[1], 102, 155)
                                self.col.append(aux10)
                                gameDisplay.blit(table, (0, 0))
                                aux10.coords[0] = aux9.coords[0]
                                aux10.coords[1] = aux9.coords[1] + 35
                                aux10.top_rect = pygame.Rect(aux10.coords[0], aux10.coords[1], 102, 155)
                                self.col.append(aux11)
                                gameDisplay.blit(table, (0, 0))
                                aux11.coords[0] = aux10.coords[0]
                                aux11.coords[1] = aux10.coords[1] + 35
                                aux11.top_rect = pygame.Rect(aux11.coords[0], aux11.coords[1], 102, 155)
                            if append == 11:
                                self.col.append(aux2)
                                gameDisplay.blit(table, (0, 0))
                                aux2.coords[0] = i.coords[0]
                                aux2.coords[1] = i.coords[1] + 35
                                aux2.top_rect = pygame.Rect(aux2.coords[0], aux2.coords[1], 102, 155)
                                self.col.append(aux3)
                                gameDisplay.blit(table, (0, 0))
                                aux3.coords[0] = aux2.coords[0]
                                aux3.coords[1] = aux2.coords[1] + 35
                                aux3.top_rect = pygame.Rect(aux3.coords[0], aux3.coords[1], 102, 155)
                                self.col.append(aux4)
                                gameDisplay.blit(table, (0, 0))
                                aux4.coords[0] = aux3.coords[0]
                                aux4.coords[1] = aux3.coords[1] + 35
                                aux4.top_rect = pygame.Rect(aux4.coords[0], aux4.coords[1], 102, 155)
                                self.col.append(aux5)
                                gameDisplay.blit(table, (0, 0))
                                aux5.coords[0] = aux4.coords[0]
                                aux5.coords[1] = aux4.coords[1] + 35
                                aux5.top_rect = pygame.Rect(aux5.coords[0], aux5.coords[1], 102, 155)
                                self.col.append(aux6)
                                gameDisplay.blit(table, (0, 0))
                                aux6.coords[0] = aux5.coords[0]
                                aux6.coords[1] = aux5.coords[1] + 35
                                aux6.top_rect = pygame.Rect(aux6.coords[0], aux6.coords[1], 102, 155)
                                self.col.append(aux7)
                                gameDisplay.blit(table, (0, 0))
                                aux7.coords[0] = aux6.coords[0]
                                aux7.coords[1] = aux6.coords[1] + 35
                                aux7.top_rect = pygame.Rect(aux7.coords[0], aux7.coords[1], 102, 155)
                                self.col.append(aux8)
                                gameDisplay.blit(table, (0, 0))
                                aux8.coords[0] = aux7.coords[0]
                                aux8.coords[1] = aux7.coords[1] + 35
                                aux8.top_rect = pygame.Rect(aux8.coords[0], aux8.coords[1], 102, 155)
                                self.col.append(aux9)
                                gameDisplay.blit(table, (0, 0))
                                aux9.coords[0] = aux8.coords[0]
                                aux9.coords[1] = aux8.coords[1] + 35
                                aux9.top_rect = pygame.Rect(aux9.coords[0], aux9.coords[1], 102, 155)
                                self.col.append(aux10)
                                gameDisplay.blit(table, (0, 0))
                                aux10.coords[0] = aux9.coords[0]
                                aux10.coords[1] = aux9.coords[1] + 35
                                aux10.top_rect = pygame.Rect(aux10.coords[0], aux10.coords[1], 102, 155)
                                self.col.append(aux11)
                                gameDisplay.blit(table, (0, 0))
                                aux11.coords[0] = aux10.coords[0]
                                aux11.coords[1] = aux10.coords[1] + 35
                                aux11.top_rect = pygame.Rect(aux11.coords[0], aux11.coords[1], 102, 155)
                                self.col.append(aux12)
                                gameDisplay.blit(table, (0, 0))
                                aux12.coords[0] = aux11.coords[0]
                                aux12.coords[1] = aux11.coords[1] + 35
                                aux12.top_rect = pygame.Rect(aux12.coords[0], aux12.coords[1], 102, 155)
                            if append == 12:
                                self.col.append(aux2)
                                gameDisplay.blit(table, (0, 0))
                                aux2.coords[0] = i.coords[0]
                                aux2.coords[1] = i.coords[1] + 35
                                aux2.top_rect = pygame.Rect(aux2.coords[0], aux2.coords[1], 102, 155)
                                self.col.append(aux3)
                                gameDisplay.blit(table, (0, 0))
                                aux3.coords[0] = aux2.coords[0]
                                aux3.coords[1] = aux2.coords[1] + 35
                                aux3.top_rect = pygame.Rect(aux3.coords[0], aux3.coords[1], 102, 155)
                                self.col.append(aux4)
                                gameDisplay.blit(table, (0, 0))
                                aux4.coords[0] = aux3.coords[0]
                                aux4.coords[1] = aux3.coords[1] + 35
                                aux4.top_rect = pygame.Rect(aux4.coords[0], aux4.coords[1], 102, 155)
                                self.col.append(aux5)
                                gameDisplay.blit(table, (0, 0))
                                aux5.coords[0] = aux4.coords[0]
                                aux5.coords[1] = aux4.coords[1] + 35
                                aux5.top_rect = pygame.Rect(aux5.coords[0], aux5.coords[1], 102, 155)
                                self.col.append(aux6)
                                gameDisplay.blit(table, (0, 0))
                                aux6.coords[0] = aux5.coords[0]
                                aux6.coords[1] = aux5.coords[1] + 35
                                aux6.top_rect = pygame.Rect(aux6.coords[0], aux6.coords[1], 102, 155)
                                self.col.append(aux7)
                                gameDisplay.blit(table, (0, 0))
                                aux7.coords[0] = aux6.coords[0]
                                aux7.coords[1] = aux6.coords[1] + 35
                                aux7.top_rect = pygame.Rect(aux7.coords[0], aux7.coords[1], 102, 155)
                                self.col.append(aux8)
                                gameDisplay.blit(table, (0, 0))
                                aux8.coords[0] = aux7.coords[0]
                                aux8.coords[1] = aux7.coords[1] + 35
                                aux8.top_rect = pygame.Rect(aux8.coords[0], aux8.coords[1], 102, 155)
                                self.col.append(aux9)
                                gameDisplay.blit(table, (0, 0))
                                aux9.coords[0] = aux8.coords[0]
                                aux9.coords[1] = aux8.coords[1] + 35
                                aux9.top_rect = pygame.Rect(aux9.coords[0], aux9.coords[1], 102, 155)
                                self.col.append(aux10)
                                gameDisplay.blit(table, (0, 0))
                                aux10.coords[0] = aux9.coords[0]
                                aux10.coords[1] = aux9.coords[1] + 35
                                aux10.top_rect = pygame.Rect(aux10.coords[0], aux10.coords[1], 102, 155)
                                self.col.append(aux11)
                                gameDisplay.blit(table, (0, 0))
                                aux11.coords[0] = aux10.coords[0]
                                aux11.coords[1] = aux10.coords[1] + 35
                                aux11.top_rect = pygame.Rect(aux11.coords[0], aux11.coords[1], 102, 155)
                                self.col.append(aux12)
                                gameDisplay.blit(table, (0, 0))
                                aux12.coords[0] = aux11.coords[0]
                                aux12.coords[1] = aux11.coords[1] + 35
                                aux12.top_rect = pygame.Rect(aux12.coords[0], aux12.coords[1], 102, 155)
                                self.col.append(aux13)
                                gameDisplay.blit(table, (0, 0))
                                aux13.coords[0] = aux12.coords[0]
                                aux13.coords[1] = aux12.coords[1] + 35
                                aux13.top_rect = pygame.Rect(aux13.coords[0], aux13.coords[1], 102, 155)

                    aux_card_list = []

                    def sort_func(e):
                        for i in e:
                            return i.coords[1]

                    for i in card_list:
                        if i != []:
                            aux_card_list.append(i)
                    aux_card_list.sort(key=sort_func)

                    for i in box_card_list:
                        gameDisplay.blit(i.card, (i.coords[0], i.coords[1], 102, 155))

                    for i in house_card_list:
                        gameDisplay.blit(i.card, (i.coords[0], i.coords[1], 102, 155))

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
                    for list in card_list:
                        if i in list:
                            list.remove(i)
                            house_card_list.append(i)

        aux_card_list = []

        def sort_func(e):
            for i in e:
                return i.coords[1]

        for i in card_list:
            if i != []:
                aux_card_list.append(i)
        aux_card_list.sort(key=sort_func)

        for i in box_card_list:
            gameDisplay.blit(i.card, (i.coords[0], i.coords[1], 102, 155))

        for i in house_card_list:
            gameDisplay.blit(i.card, (i.coords[0], i.coords[1], 102, 155))

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

card_list_init = [Hearts_1, Hearts_2, Hearts_3, Hearts_4, Hearts_5, Hearts_6, Hearts_7, Claves_8, Hearts_9,
                  Hearts_10, Hearts_11, Hearts_12, Hearts_13, Diamonds_1, Diamonds_2, Diamonds_3, Diamonds_4,
                  Diamonds_5, Diamonds_6, Diamonds_7, Diamonds_8, Diamonds_9, Diamonds_10, Diamonds_11, Diamonds_12,
                  Diamonds_13, Spades_1, Spades_2, Spades_3, Spades_4, Spades_5, Spades_6, Spades_7, Spades_8, Spades_9,
                  Spades_10, Spades_11, Spades_12, Spades_13, Claves_1, Claves_2, Claves_3, Claves_4, Claves_5,
                  Claves_6, Claves_7, Hearts_8, Claves_9, Claves_10, Claves_11, Claves_12, Claves_13]

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

box_card_list = []
house_card_list = []
card_list = [c0, c1, c2, c3, c4, c5, c6, c7]
box_list = [Box1, Box2, Box3, Box4]
house_list = [House1, House2, House3, House4]

Column1 = Column([102.4, 175], c0)
Column2 = Column([204.8, 175], c1)
Column3 = Column([307.2, 175], c2)
Column4 = Column([409.6, 175], c3)
Column5 = Column([512, 175], c4)
Column6 = Column([614.4, 175], c5)
Column7 = Column([716.8, 175], c6)
Column8 = Column([819.2, 175], c7)

column_list = [Column1, Column2, Column3, Column4, Column5, Column6, Column7, Column8]


def front_row():
    front_row_list = []

    def sort_func(e):
        return e.coords[1]

    # THIS NEEDS FIXINGGGG (+3 card stack fails)
    for card_in_box in box_card_list:
        front_row_list.append(card_in_box)
    for i in card_list:
        print(len(i))
        if len(i) == 0:
            for column in column_list:
                if column.col == []:
                    column.filled = False
        elif len(i) == 1:
            front_row_list.append(i[-1])
        elif len(i) == 2:
            if i[-1].color != i[-2].color and int(i[-1].number) == int(i[-2].number) - 1:
                front_row_list.append(i[-1])
                front_row_list.append(i[-2])
            else:
                front_row_list.append(i[-1])
        elif len(i) == 3:
            if i[-1].color != i[-2].color and int(i[-1].number) == int(i[-2].number) - 1:
                if i[-2].color != i[-3].color and int(i[-2].number) == int(i[-3].number) - 1:
                    front_row_list.append(i[-1])
                    front_row_list.append(i[-2])
                    front_row_list.append(i[-3])
                else:
                    front_row_list.append(i[-1])
                    front_row_list.append(i[-2])
            else:
                front_row_list.append(i[-1])
        elif len(i) == 4:
            if i[-1].color != i[-2].color and int(i[-1].number) == int(i[-2].number) - 1:
                if i[-2].color != i[-3].color and int(i[-2].number) == int(i[-3].number) - 1:
                    if i[-3].color != i[-4].color and int(i[-3].number) == int(i[-4].number) - 1:
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
        elif len(i) == 5:
            if i[-1].color != i[-2].color and int(i[-1].number) == int(i[-2].number) - 1:
                if i[-2].color != i[-3].color and int(i[-2].number) == int(i[-3].number) - 1:
                    if i[-3].color != i[-4].color and int(i[-3].number) == int(i[-4].number) - 1:
                        if i[-4].color != i[-5].color and int(i[-4].number) == int(i[-5].number) - 1:
                            front_row_list.append(i[-1])
                            front_row_list.append(i[-2])
                            front_row_list.append(i[-3])
                            front_row_list.append(i[-4])
                            front_row_list.append(i[-5])
                        else:
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
        elif len(i) == 6:
            if i[-1].color != i[-2].color and int(i[-1].number) == int(i[-2].number) - 1:
                if i[-2].color != i[-3].color and int(i[-2].number) == int(i[-3].number) - 1:
                    if i[-3].color != i[-4].color and int(i[-3].number) == int(i[-4].number) - 1:
                        if i[-4].color != i[-5].color and int(i[-4].number) == int(i[-5].number) - 1:
                            if i[-5].color != i[-6].color and int(i[-5].number) == int(i[-6].number) - 1:
                                front_row_list.append(i[-1])
                                front_row_list.append(i[-2])
                                front_row_list.append(i[-3])
                                front_row_list.append(i[-4])
                                front_row_list.append(i[-5])
                                front_row_list.append(i[-6])
                            else:
                                front_row_list.append(i[-1])
                                front_row_list.append(i[-2])
                                front_row_list.append(i[-3])
                                front_row_list.append(i[-4])
                                front_row_list.append(i[-5])
                        else:
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
        elif len(i) == 7:
            if i[-1].color != i[-2].color and int(i[-1].number) == int(i[-2].number) - 1:
                if i[-2].color != i[-3].color and int(i[-2].number) == int(i[-3].number) - 1:
                    if i[-3].color != i[-4].color and int(i[-3].number) == int(i[-4].number) - 1:
                        if i[-4].color != i[-5].color and int(i[-4].number) == int(i[-5].number) - 1:
                            if i[-5].color != i[-6].color and int(i[-5].number) == int(i[-6].number) - 1:
                                if i[-6].color != i[-7].color and int(i[-6].number) == int(i[-7].number) - 1:
                                    front_row_list.append(i[-1])
                                    front_row_list.append(i[-2])
                                    front_row_list.append(i[-3])
                                    front_row_list.append(i[-4])
                                    front_row_list.append(i[-5])
                                    front_row_list.append(i[-6])
                                    front_row_list.append(i[-7])
                                else:
                                    front_row_list.append(i[-1])
                                    front_row_list.append(i[-2])
                                    front_row_list.append(i[-3])
                                    front_row_list.append(i[-4])
                                    front_row_list.append(i[-5])
                                    front_row_list.append(i[-6])
                            else:
                                front_row_list.append(i[-1])
                                front_row_list.append(i[-2])
                                front_row_list.append(i[-3])
                                front_row_list.append(i[-4])
                                front_row_list.append(i[-5])
                        else:
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
        elif len(i) == 8:
            if i[-1].color != i[-2].color and int(i[-1].number) == int(i[-2].number) - 1:
                if i[-2].color != i[-3].color and int(i[-2].number) == int(i[-3].number) - 1:
                    if i[-3].color != i[-4].color and int(i[-3].number) == int(i[-4].number) - 1:
                        if i[-4].color != i[-5].color and int(i[-4].number) == int(i[-5].number) - 1:
                            if i[-5].color != i[-6].color and int(i[-5].number) == int(i[-6].number) - 1:
                                if i[-6].color != i[-7].color and int(i[-6].number) == int(i[-7].number) - 1:
                                    if i[-7].color != i[-8].color and int(i[-7].number) == int(i[-8].number) - 1:
                                        front_row_list.append(i[-1])
                                        front_row_list.append(i[-2])
                                        front_row_list.append(i[-3])
                                        front_row_list.append(i[-4])
                                        front_row_list.append(i[-5])
                                        front_row_list.append(i[-6])
                                        front_row_list.append(i[-7])
                                        front_row_list.append(i[-8])
                                    else:
                                        front_row_list.append(i[-1])
                                        front_row_list.append(i[-2])
                                        front_row_list.append(i[-3])
                                        front_row_list.append(i[-4])
                                        front_row_list.append(i[-5])
                                        front_row_list.append(i[-6])
                                        front_row_list.append(i[-7])
                                else:
                                    front_row_list.append(i[-1])
                                    front_row_list.append(i[-2])
                                    front_row_list.append(i[-3])
                                    front_row_list.append(i[-4])
                                    front_row_list.append(i[-5])
                                    front_row_list.append(i[-6])
                            else:
                                front_row_list.append(i[-1])
                                front_row_list.append(i[-2])
                                front_row_list.append(i[-3])
                                front_row_list.append(i[-4])
                                front_row_list.append(i[-5])
                        else:
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
        for c in front_row_list:
            print(c.name)
        print(len(front_row_list))
        print("")

        i.sort(key=sort_func)
    return front_row_list


for i in range(52):
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
    front_row_list = front_row()
    for box in box_list:
        if box.top_rect.collidepoint(posm):
            box.clicked()
    for i in front_row_list:
        if i.top_rect.collidepoint(posm):
            i.clicked()
    for house in house_list:
        if house.top_rect.collidepoint(posm):
            house.clicked()
    for col in column_list:
        if len(col.col) == 0:
            if col.top_rect.collidepoint(posm):
                col.clicked()


while not gameExit:

    if pygame.mouse.get_pressed()[0] is True:
        check_click()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


# Boxes can't hold a card after a card has been inside
# Sometimes cards don't go home
