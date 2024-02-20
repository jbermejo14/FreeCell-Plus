import sys
import pygame

black = pygame.Color(0, 0, 0)
white = pygame.Color(0, 0, 255)

gameDisplay = pygame.display.set_mode((1024, 700))

pygame.init()
pygame.display.set_caption("CartaBlanca")
card_style = 'resources/card_images/'
end = False
end2 = False
table = pygame.image.load("resources/table.png")
gameDisplay.blit(table, (0, 0))

button1_img = pygame.image.load("resources/button1.png")
button2_img = pygame.image.load("resources/button2.png")
button3_img = pygame.image.load("resources/button2.png")
button4_img = pygame.image.load("resources/button4.png")
button5_img = pygame.image.load("resources/button5.png")
button6_img = pygame.image.load("resources/button6.png")


class InitButtons():
    def __init__(self, coords, coords2):
        self.coords2 = coords2
        self.coords = coords
        self.top_rect = pygame.Rect(self.coords[0], self.coords[1], self.coords2[0], self.coords2[1])


def personalation_menu(gameDisplay):
    global card_style, button6_img, button4_img, button5_img

    table = pygame.image.load("resources/table.png")
    font = pygame.font.SysFont(None, 50)
    img = font.render('Elige tu estilo de carta', True, black)

    gameDisplay.blit(table, (0, 0))
    gameDisplay.blit(img, (350, 225))

    button4 = InitButtons([212, 300], [300, 200])
    gameDisplay.blit(button4_img, (button4.coords[0], button4.coords[1], 300, 200))

    button5 = InitButtons([624, 310], [300, 200])
    gameDisplay.blit(button5_img, (button5.coords[0], button5.coords[1], 300, 200))

    button6 = InitButtons([25, 625], [200, 45])
    gameDisplay.blit(button6_img, (button6.coords[0], button6.coords[1], 200, 45))

    pygame.display.update()

    while not end:
        posm = pygame.mouse.get_pos()
        if button6.top_rect.collidepoint(posm):
            table = pygame.image.load("resources/table.png")
            gameDisplay.blit(table, (0, 0))
            button6 = InitButtons([20, 625], [200, 45])
            button6_img = pygame.image.load("resources/button6-2.png")
            gameDisplay.blit(button6_img, (button6.coords[0], button6.coords[1], 200, 45))

            button4 = InitButtons([212, 250], [300, 200])
            gameDisplay.blit(button4_img, (button4.coords[0], button4.coords[1], 300, 200))

            button5 = InitButtons([624, 260], [300, 200])
            gameDisplay.blit(button5_img, (button5.coords[0], button5.coords[1], 300, 200))
        elif button4.top_rect.collidepoint(posm):
            table = pygame.image.load("resources/table.png")
            gameDisplay.blit(table, (0, 0))

            button4_img = pygame.image.load("resources/button4-2.png")
            button4 = InitButtons([205, 250], [300, 200])
            gameDisplay.blit(button4_img, (button4.coords[0], button4.coords[1], 300, 200))

            button5 = InitButtons([624, 260], [300, 200])
            gameDisplay.blit(button5_img, (button5.coords[0], button5.coords[1], 300, 200))

            button6 = InitButtons([25, 625], [200, 45])
            gameDisplay.blit(button6_img, (button6.coords[0], button6.coords[1], 200, 45))
        elif button5.top_rect.collidepoint(posm):
            table = pygame.image.load("resources/table.png")
            gameDisplay.blit(table, (0, 0))

            button5_img = pygame.image.load("resources/button5-2.png")
            button5 = InitButtons([617, 260], [300, 200])
            gameDisplay.blit(button5_img, (button5.coords[0], button5.coords[1], 300, 200))

            button4 = InitButtons([212, 250], [300, 200])
            gameDisplay.blit(button4_img, (button4.coords[0], button4.coords[1], 300, 200))

            button6 = InitButtons([25, 625], [200, 45])
            gameDisplay.blit(button6_img, (button6.coords[0], button6.coords[1], 200, 45))

        else:
            table = pygame.image.load("resources/table.png")
            gameDisplay.blit(table, (0, 0))

            button4 = InitButtons([212, 250], [300, 200])
            button4_img = pygame.image.load("resources/button4.png")
            gameDisplay.blit(button4_img, (button4.coords[0], button4.coords[1], 300, 200))

            button5 = InitButtons([624, 260], [300, 200])
            button5_img = pygame.image.load("resources/button5.png")
            gameDisplay.blit(button5_img, (button5.coords[0], button5.coords[1], 300, 200))

            button6 = InitButtons([25, 625], [200, 45])
            button6_img = pygame.image.load("resources/button6.png")
            gameDisplay.blit(button6_img, (button6.coords[0], button6.coords[1], 200, 45))
            pygame.display.update()

        if pygame.mouse.get_pressed()[0] is True:
            posm = pygame.mouse.get_pos()
            if button4.top_rect.collidepoint(posm):
                card_style = 'resources/card_images/'
                print("4")
            elif button5.top_rect.collidepoint(posm):
                card_style = 'resources/card_images2/'
                print("5")
            elif button6.top_rect.collidepoint(posm):
                menu_page(gameDisplay)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


def menu_page(gameDisplay):
    global button1_img, button2_img
    table = pygame.image.load("resources/table.png")
    gameDisplay.blit(table, (0, 0))
    font = pygame.font.SysFont(None, 50)
    img = font.render('Bienvenido a Carta Blanca!', True, black)
    gameDisplay.blit(img, (300, 225))

    button1 = InitButtons([374.5, 300], [275, 62])
    gameDisplay.blit(button1_img, (button1.coords[0], button1.coords[1], 275, 62))

    button2 = InitButtons([374.5, 375], [275, 62])
    gameDisplay.blit(button2_img, (button2.coords[0], button2.coords[1], 275, 62))

    button3 = InitButtons([374.5, 450], [275, 62])
    gameDisplay.blit(button3_img, (button3.coords[0], button3.coords[1], 275, 62))

    while not end:
        posm = pygame.mouse.get_pos()
        if button1.top_rect.collidepoint(posm):
            table = pygame.image.load("resources/table.png")
            gameDisplay.blit(table, (0, 0))

            button1_img = pygame.image.load("resources/button1-2.png")
            gameDisplay.blit(button1_img, (365, 300, 275, 62))

            button2 = InitButtons([374.5, 375], [275, 62])
            gameDisplay.blit(button2_img, (button2.coords[0], button2.coords[1], 275, 62))

            button3 = InitButtons([374.5, 450], [275, 62])
            gameDisplay.blit(button3_img, (button3.coords[0], button3.coords[1], 275, 62))

            pygame.display.update()
        elif button2.top_rect.collidepoint(posm):
            table = pygame.image.load("resources/table.png")
            gameDisplay.blit(table, (0, 0))

            button2_img = pygame.image.load("resources/button2-2.png")
            gameDisplay.blit(button2_img, (365, 375, 275, 62))

            button1 = InitButtons([374.5, 300], [275, 62])
            gameDisplay.blit(button1_img, (button1.coords[0], button1.coords[1], 275, 62))

            button3 = InitButtons([374.5, 450], [275, 62])
            gameDisplay.blit(button3_img, (button3.coords[0], button3.coords[1], 275, 62))

            pygame.display.update()
        else:
            table = pygame.image.load("resources/table.png")
            gameDisplay.blit(table, (0, 0))
            button2_img = pygame.image.load("resources/button2.png")
            button1_img = pygame.image.load("resources/button1.png")

            gameDisplay.blit(button1_img, (button1.coords[0], button1.coords[1], 275, 62))
            gameDisplay.blit(button2_img, (button2.coords[0], button2.coords[1], 275, 62))
            gameDisplay.blit(button3_img, (button3.coords[0], button3.coords[1], 275, 62))

            pygame.display.update()

        if pygame.mouse.get_pressed()[0] is True:
            posm = pygame.mouse.get_pos()
            if button1.top_rect.collidepoint(posm):
                import main
            elif button2.top_rect.collidepoint(posm):
                personalation_menu(gameDisplay)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


menu_page(gameDisplay)
