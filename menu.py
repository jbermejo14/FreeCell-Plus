import sys
import pygame

black = pygame.Color(0, 0, 0)
white = pygame.Color(0, 0, 255)

gameDisplay = pygame.display.set_mode((1024, 700))

pygame.init()
pygame.display.set_caption("CartaBlanca")
card_style = 'resources/card_images2/'
end = False
end2 = False

button1_img = pygame.image.load("resources/button1.png")
button2_img = pygame.image.load("resources/button2.png")
button3_img = pygame.image.load("resources/button3.png")
button4_img = pygame.image.load("resources/button4.png")
button5_img = pygame.image.load("resources/button5.png")
button6_img = pygame.image.load("resources/button6.png")

# GAMEMODE IMAGES FOR BUTTONS
bakers_button_img = pygame.image.load("resources/bakers_game.png")
freecell_button_img = pygame.image.load("resources/freecell.png")
double_button_img = pygame.image.load("resources/double_freecell.png")
infinite_button_img = pygame.image.load("resources/infinite_cell.png")


class InitButtons():
    def __init__(self, coords, coords2):
        self.coords2 = coords2
        self.coords = coords
        self.top_rect = pygame.Rect(self.coords[0], self.coords[1], self.coords2[0], self.coords2[1])


def personalation_menu(gameDisplay):
    global card_style, button6_img, button4_img, button5_img

    button4 = InitButtons([212, 300], [300, 200])
    button5 = InitButtons([624, 310], [300, 200])
    button6 = InitButtons([25, 625], [200, 45])

    while not end:
        posm = pygame.mouse.get_pos()
        if button6.top_rect.collidepoint(posm):
            bg = pygame.image.load("resources/bg.png")
            gameDisplay.blit(bg, (0, 0))

            font = pygame.font.SysFont(None, 50)
            img = font.render('Elige tu estilo de carta', True, black)
            gameDisplay.blit(img, (350, 225))

            button6 = InitButtons([20, 625], [200, 45])
            button6_img = pygame.image.load("resources/button6-2.png")
            gameDisplay.blit(button6_img, (button6.coords[0], button6.coords[1], 200, 45))

            button4 = InitButtons([212, 250], [300, 200])
            gameDisplay.blit(button4_img, (button4.coords[0], button4.coords[1], 300, 200))

            button5 = InitButtons([624, 260], [300, 200])
            gameDisplay.blit(button5_img, (button5.coords[0], button5.coords[1], 300, 200))
        elif button4.top_rect.collidepoint(posm):
            bg = pygame.image.load("resources/bg.png")
            gameDisplay.blit(bg, (0, 0))

            font = pygame.font.SysFont(None, 50)
            img = font.render('Elige tu estilo de carta', True, black)
            gameDisplay.blit(img, (350, 225))

            button4_img = pygame.image.load("resources/button4-2.png")
            button4 = InitButtons([205, 250], [300, 200])
            gameDisplay.blit(button4_img, (button4.coords[0], button4.coords[1], 300, 200))

            button5 = InitButtons([624, 260], [300, 200])
            gameDisplay.blit(button5_img, (button5.coords[0], button5.coords[1], 300, 200))

            button6 = InitButtons([25, 625], [200, 45])
            gameDisplay.blit(button6_img, (button6.coords[0], button6.coords[1], 200, 45))
        elif button5.top_rect.collidepoint(posm):
            bg = pygame.image.load("resources/bg.png")
            gameDisplay.blit(bg, (0, 0))

            font = pygame.font.SysFont(None, 50)
            img = font.render('Elige tu estilo de carta', True, black)
            gameDisplay.blit(img, (350, 225))

            button5_img = pygame.image.load("resources/button5-2.png")
            button5 = InitButtons([617, 260], [300, 200])
            gameDisplay.blit(button5_img, (button5.coords[0], button5.coords[1], 300, 200))

            button4 = InitButtons([212, 250], [300, 200])
            gameDisplay.blit(button4_img, (button4.coords[0], button4.coords[1], 300, 200))

            button6 = InitButtons([25, 625], [200, 45])
            gameDisplay.blit(button6_img, (button6.coords[0], button6.coords[1], 200, 45))

        else:
            bg = pygame.image.load("resources/bg.png")
            gameDisplay.blit(bg, (0, 0))

            font = pygame.font.SysFont(None, 50)
            img = font.render('Elige tu estilo de carta', True, black)
            gameDisplay.blit(img, (350, 225))

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
            elif button5.top_rect.collidepoint(posm):
                card_style = 'resources/card_images2/'
            elif button6.top_rect.collidepoint(posm):
                menu_page(gameDisplay)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

def gamemode_menu(gameDisplay):
    global card_style, button6_img, bakers_button_img, double_button_img
    bg = pygame.image.load("resources/bg.png")
    gameDisplay.blit(bg, (0, 0))

    bakers_button = InitButtons([212, 250], [100, 66])

    button6 = InitButtons([25, 625], [200, 45])
    gameDisplay.blit(button6_img, (button6.coords[0], button6.coords[1], 200, 45))

    # BAKERS GAME BUTTON AND TEXT
    font = pygame.font.SysFont(None, 50)
    bakers_text = font.render("Baker's", True, black)
    gameDisplay.blit(bakers_text, (240, 110))
    bakers_button = InitButtons([125, 150], [350, 189])
    gameDisplay.blit(bakers_button_img, (
    bakers_button.coords[0], bakers_button.coords[1], bakers_button.coords2[0], bakers_button.coords2[1]))

    # FREECELL GAME BUTTON AND TEXT
    font = pygame.font.SysFont(None, 50)
    bakers_text = font.render("Clásico", True, black)
    gameDisplay.blit(bakers_text, (660, 110))
    freecell_button = InitButtons([549, 150], [350, 190])
    gameDisplay.blit(freecell_button_img, (
        freecell_button.coords[0], freecell_button.coords[1], freecell_button.coords2[0], freecell_button.coords2[1]))

    # INFINITE GAME BUTTON AND TEXT
    font = pygame.font.SysFont(None, 50)
    bakers_text = font.render("Infinito", True, black)
    gameDisplay.blit(bakers_text, (245, 360))
    infinite_button = InitButtons([125, 400], [350, 189])
    gameDisplay.blit(freecell_button_img, (
    infinite_button.coords[0], infinite_button.coords[1], infinite_button.coords2[0], infinite_button.coords2[1]))

    # DOUBLE GAME BUTTON AND TEXT
    font = pygame.font.SysFont(None, 50)
    bakers_text = font.render("Doble", True, black)
    gameDisplay.blit(bakers_text, (670, 360))
    doble_button = InitButtons([549, 400], [350, 190])
    gameDisplay.blit(double_button_img, (
        doble_button.coords[0], doble_button.coords[1], doble_button.coords2[0], doble_button.coords2[1]))

    pygame.display.update()
    while not end:
        posm = pygame.mouse.get_pos()
        # if button6.top_rect.collidepoint(posm):
        #     table = pygame.image.load("resources/table.png")
        #     gameDisplay.blit(table, (0, 0))
        #
        #     font = pygame.font.SysFont(None, 50)
        #     img = font.render('Elige tu estilo de carta', True, black)
        #     gameDisplay.blit(img, (350, 225))
        #     pygame.display.update()
        # elif bakers_button.top_rect.collidepoint(posm):


        if pygame.mouse.get_pressed()[0] is True:
            posm = pygame.mouse.get_pos()
            if button6.top_rect.collidepoint(posm):
                menu_page(gameDisplay)
            elif freecell_button.top_rect.collidepoint(posm):
                import main
            elif infinite_button.top_rect.collidepoint(posm):
                import infinite

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

def menu_page(gameDisplay):
    global button1_img, button2_img
    button1 = InitButtons([374.5, 300], [275, 62])
    button2 = InitButtons([374.5, 375], [275, 62])
    button3 = InitButtons([374.5, 450], [275, 62])

    while not end:
        posm = pygame.mouse.get_pos()
        if button1.top_rect.collidepoint(posm):
            bg = pygame.image.load("resources/bg.png")
            gameDisplay.blit(bg, (0, 0))

            font = pygame.font.SysFont(None, 50)
            img = font.render('Bienvenido a Carta Blanca!', True, black)
            gameDisplay.blit(img, (300, 225))

            button1_img = pygame.image.load("resources/button1-2.png")
            gameDisplay.blit(button1_img, (365, 300, 275, 62))

            button2 = InitButtons([374.5, 375], [275, 62])
            gameDisplay.blit(button2_img, (button2.coords[0], button2.coords[1], 275, 62))

            button3 = InitButtons([374.5, 450], [275, 62])
            gameDisplay.blit(button3_img, (button3.coords[0], button3.coords[1], 275, 62))

            pygame.display.update()

        elif button2.top_rect.collidepoint(posm):
            bg = pygame.image.load("resources/bg.png")
            gameDisplay.blit(bg, (0, 0))

            font = pygame.font.SysFont(None, 50)
            img = font.render('Bienvenido a Carta Blanca!', True, black)
            gameDisplay.blit(img, (300, 225))

            button2_img = pygame.image.load("resources/button2-2.png")
            gameDisplay.blit(button2_img, (365, 375, 275, 62))

            button1 = InitButtons([374.5, 300], [275, 62])
            gameDisplay.blit(button1_img, (button1.coords[0], button1.coords[1], 275, 62))

            button3 = InitButtons([374.5, 450], [275, 62])
            gameDisplay.blit(button3_img, (button3.coords[0], button3.coords[1], 275, 62))

            pygame.display.update()

        else:
            bg = pygame.image.load("resources/bg.png")
            gameDisplay.blit(bg, (0, 0))

            font = pygame.font.SysFont(None, 50)
            img = font.render('Bienvenido a Carta Blanca!', True, black)
            gameDisplay.blit(img, (300, 225))

            button2_img = pygame.image.load("resources/button2.png")
            button1_img = pygame.image.load("resources/button1.png")

            gameDisplay.blit(button1_img, (button1.coords[0], button1.coords[1], 275, 62))
            gameDisplay.blit(button2_img, (button2.coords[0], button2.coords[1], 275, 62))
            gameDisplay.blit(button3_img, (button3.coords[0], button3.coords[1], 275, 62))

            pygame.display.update()

        if pygame.mouse.get_pressed()[0] is True:
            posm = pygame.mouse.get_pos()
            if button1.top_rect.collidepoint(posm):
                gamemode_menu(gameDisplay)
            elif button2.top_rect.collidepoint(posm):
                personalation_menu(gameDisplay)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


menu_page(gameDisplay)
