import pygame, warnings, random

pygame.init()

warnings.filterwarnings("ignore", category=DeprecationWarning)

screen_width = 600
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

grey = (150, 150, 150)
black = (0, 0, 0)
white = (255, 255, 255)

def hangman(images, no, x, y):
    screen.blit(images[no], (x, y))

def optional():
    return

def message(txt, size, color, x, y):
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(txt, True, color)
    box = text.get_rect()
    box.center = (x, y)
    screen.blit(text, box)

def button(x, y, w, h, act_color, pass_color, txt, txt_color, txt_size, function = optional):
    fun_mouse = pygame.mouse.get_pos()
    fun_click = pygame.mouse.get_pressed()

    if x < fun_mouse[0] <= x + w and y < fun_mouse[1] <= y + h:
        pygame.draw.rect(screen, act_color, (x, y, w, h))  # Player (grey)
        if fun_click[0] == 1:
            function()
            return True
    else:
        pygame.draw.rect(screen, pass_color, (x, y, w, h))  # Player (black)

    font = pygame.font.Font('freesansbold.ttf', txt_size)
    text = font.render(txt, True, txt_color)
    box = text.get_rect()
    box.center = (x + w/2, y + h/2)
    screen.blit(text, box)

def main_menu():
    run = True
    R = random.randint(40, 210)
    G = random.randint(40, 210)
    B = random.randint(40, 210)
    r = True
    g = True
    b = True
    max_brightness = 200
    min_brightness = 50
    while run:
        # Create Fading background
        if R >= max_brightness:
            r = False
        elif G >= max_brightness:
            g = False
        elif B >= max_brightness:
            b = False
        elif R <= min_brightness:
            r = True
        elif G <= min_brightness:
            g = True
        elif B <= min_brightness:
            b = True
        if r:
            R += 0.1
        else:
            R -= 0.1
        if g:
            G += 0.07
        else:
            G -= 0.07
        if b:
            B += 0.09
        else:
            B -= 0.09
        screen.fill((R, G, B))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        message("IMPOSSIBLE", 60, black, screen_width / 2, 100)
        message("HANGMAN", 60, black, screen_width/2, 160)
        button(100, 300, 100, 30, (R - 40, G - 40, B - 40), (R, G, B), "Play", (0, G-40, 0), 20, main_game)
        button(400, 300, 100, 30, (R - 40, G - 40, B - 40), (R, G, B), "Exit", (R-40, 0, 0), 20, quit)

        pygame.display.update()

def pause_menu(red = 255, green = 167, blue = 137):
    pause_run = True
    R = red - 20
    G = green - 20
    B = blue - 20
    while pause_run:
        screen.fill((R, G, B))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause_run = False

        message("Paused", 50, white, screen_width/2, 50)
        if button(250, 150, 100, 30, (R - 20, G - 20, B - 20), (R, G, B), "Resume", white, 20):
            pause_run = False
        button(250, 190, 100, 30, (R - 20, G - 20, B - 20), (R, G, B), "Restart", white, 20, main_game)
        button(250, 230, 100, 30, (R - 20, G - 20, B - 20), (R, G, B), "Quit", white, 20, quit)
        pygame.display.update()

def main_game():
    game_run = True
    R, G, B = 255, 167, 137
    tries = 0
    win = 0
    hangmanImgs = [pygame.image.load('Pics\\h0.png'), pygame.image.load('Pics\\h1.png'),
                   pygame.image.load('Pics\\h2.png'), pygame.image.load('Pics\\h3.png'),
                   pygame.image.load('Pics\\h4.png'), pygame.image.load('Pics\\h5.png'),
                   pygame.image.load('Pics\\h6.png')]
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
               "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    buttonletterDict = {letters[0]: True, letters[1]: True, letters[2]: True, letters[3]: True,
                        letters[4]: True, letters[5]: True, letters[6]: True, letters[7]: True,
                        letters[8]: True, letters[9]: True, letters[10]: True, letters[11]: True,
                        letters[12]: True, letters[13]: True, letters[14]: True, letters[15]: True,
                        letters[16]: True, letters[17]: True, letters[18]: True, letters[19]: True,
                        letters[20]: True, letters[21]: True, letters[22]: True, letters[23]: True,
                        letters[24]: True, letters[25]: True, }
    letterShow = {letters[0]: False, letters[1]: False, letters[2]: False, letters[3]: False,
                  letters[4]: False, letters[5]: False, letters[6]: False, letters[7]: False,
                  letters[8]: False, letters[9]: False, letters[10]: False, letters[11]: False,
                  letters[12]: False, letters[13]: False, letters[14]: False, letters[15]: False,
                  letters[16]: False, letters[17]: False, letters[18]: False, letters[19]: False,
                  letters[20]: False, letters[21]: False, letters[22]: False, letters[23]: False,
                  letters[24]: False, letters[25]: False}
    words_list = ["abruptly", "absurd", "abyss", "affix", "askew",
                  "avenue", "awkward", "axiom", "azure", "bagpipes",
                  "bandwagon", "banjo", "bayou", "beekeeper",
                  "bikini", "blitz", "blizzard", "boggle", "bookworm",
                  "boxcar", "boxful", "buckaroo", "buffalo", "buffoon",
                  "buxom", "buzzard", "buzzing", "buzzwords", "caliph",
                  "cobweb", "cockiness", "croquet", "crypt", "curacao",
                  "cycle", "daiquiri", "dirndl", "disavow", "dizzying",
                  "duplex", "dwarves", "embezzle", "equip", "espionage",
                  "euouae", "exodus", "faking", "fishhook", "fixable",
                  "fjord", "flapjack", "flopping", "fluffiness", "flyby",
                  "foxglove", "frazzled", "frizzled", "fuchsia", "funny",
                  "gabby", "galaxy", "galvanize", "gazebo", "giaour",
                  "gizmo", "glowworm", "glyph", "gnarly", "gnostic",
                  "gossip", "grogginess", "haiku", "haphazard",
                  "hyphen", "iatrogenic", "icebox", "injury", "ivory",
                  "ivy", "jackpot", "jaundice", "jawbreaker", "jaywalk",
                  "jazziest", "jazzy", "jelly", "jigsaw", "jinx",
                  "jiujitsu", "jockey", "jogging", "joking", "jovial",
                  "joyful", "juicy", "jukebox", "jumbo", "kayak", "kazoo",
                  "keyhole", "khaki", "kilobyte", "kiosk", "kitsch",
                  "kiwifruit", "klutz", "knapsack", "larynx", "lengths",
                  "lucky", "luxury", "lymph", "marquis", "matrix",
                  "megahertz", "microwave", "mnemonic", "mystify",
                  "naphtha", "nightclub", "nowadays", "numbskull",
                  "nymph", "onyx", "ovary", "oxidize", "oxygen", "pajama",
                  "peekaboo", "phlegm", "pixel", "pizazz", "pneumonia",
                  "polka", "pshaw", "psyche", "puppy", "puzzling",
                  "quartz", "queue", "quips", "quixotic", "quiz",
                  "quizzes", "quorum", "razzmatazz", "rhubarb",
                  "rhythm", "rickshaw", "schnapps", "scratch", "shiv",
                  "snazzy", "sphinx", "spritz", "squawk", "staff",
                  "strength", "strengths", "stretch", "stronghold",
                  "stymied", "subway", "swivel", "syndrome", "thriftless",
                  "thumbscrew", "topaz", "transcript", "transgress",
                  "transplant", "triphthong", "twelfth", "twelfths",
                  "unknown", "unworthy", "unzip", "uptown", "vaporize",
                  "vixen", "vodka", "voodoo", "vortex", "voyeurism",
                  "walkway", "waltz", "wave", "wavy", "waxy",
                  "wellspring", "wheezy", "whiskey", "whizzing",
                  "whomever", "wimpy", "witchcraft", "wizard", "woozy",
                  "wristwatch", "wyvern", "xylophone", "yachtsman",
                  "yippee", "yoked", "youthful", "yummy", "zephyr",
                  "zigzag", "zigzagging", "zilch", "zipper", "zodiac", "zombie"]
    rand_word = random.choice(words_list)
    check = {}
    for i in rand_word:
        check[i] = True
    #print(rand_word)
    while game_run:
        screen.fill((R, G, B))
        letter_pos = 1
        x_pos = 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause_menu(R, G, B)

        button(10, 10, 40, 40, (R - 20, G - 20, B - 20), (R, G, B), "| |", white, 20, pause_menu)
        hangman(hangmanImgs, tries, screen_width/2 - 178, 10)


        if win == len(check):
            message(rand_word.upper(), 30, black, 350, 300)
            message("YOU WIN", 30, black, 470, 130)
            button(380, 160, 180, 30, (R - 20, G - 20, B - 20), (R, G, B), "Play Again", black, 30, main_game)
        elif tries>5:
            message(rand_word.upper(), 30, black, 350, 300)
            message("GAME OVER", 30, black, 470, 130)
            button(380, 160, 180, 30, (R - 20, G - 20, B - 20), (R, G, B), "Try Again", black, 30, main_game)
        elif tries <6:
            for i in letters:
                if buttonletterDict[i]:
                    if button(letter_pos * 22, 400, 23, 23, (R - 20, G - 20, B - 20), (R, G, B), i, white, 23):
                        buttonletterDict[i] = False
                        if i in rand_word.upper():
                            letterShow[i] = True
                            win += 1
                            #print(win)
                        else:
                            tries += 1
                letter_pos += 1

        for i in rand_word.upper():
            if letterShow[i]:
                message(i, 30, black, x_pos * 20 + 20, 300)
            else:
                message("_", 30, black, x_pos * 20 + 20, 300)
            x_pos += 1


        pygame.display.update()

main_menu()
