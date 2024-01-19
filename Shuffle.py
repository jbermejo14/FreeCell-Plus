from main import Card, Boxes

list = [[102.4, 175], [204.8, 175], [307.2, 175], [409.6, 175], [512, 175], [614.4, 175], [716.8, 175], [819.2, 175],
        [102.4, 210], [204.8, 210], [307.2, 210], [409.6, 210], [512, 210], [614.4, 210], [716.8, 210], [819.2, 210],
        [102.4, 245], [204.8, 245], [307.2, 245], [409.6, 245], [512, 245], [614.4, 245], [716.8, 245], [819.2, 245],
        [102.4, 280], [204.8, 280], [307.2, 280], [409.6, 280], [512, 280], [614.4, 280], [716.8, 280], [819.2, 280],
        [102.4, 315], [204.8, 315], [307.2, 315], [409.6, 315], [512, 315], [614.4, 315], [716.8, 315], [819.2, 315],
        [102.4, 350], [204.8, 350], [307.2, 350], [409.6, 350], [512, 350], [614.4, 350], [716.8, 350], [819.2, 350],
        [102.4, 385], [204.8, 385], [307.2, 385], [409.6, 385]]


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

