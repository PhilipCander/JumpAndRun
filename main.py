import pygame
import random

pygame.init()

# Window settings
size = [1000, 500]
window = pygame.display.set_mode(size)
pygame.display.set_caption("You have no connection!")

# importing fonts
font = pygame.font.SysFont('comicsansms', 20)
font2 = pygame.font.SysFont('comicsansms', 60)

# pictures
pic1 = pygame.image.load("Katze1.png")
pic2 = pygame.image.load("Katze2.png")
pic3 = pygame.image.load("Katze3.png")
animation = [pic1, pic2, pic3]
sprite = pic1
i = 0
j = 1


# Player Settings
jump = False
jumpcount = 10
playerx = 30
playery = 430
playersize = 70

# Enemy Settings
enemysize = 50
enemyx = size[0]
enemyy = size[1] - enemysize
speed = 15

gameover = False
score = 0

# highscorefile
try:
    highscoreFile = open("highscore.txt", "r")
    highscore = int(highscoreFile.read())
    highscoreFile.close()
except:
    highscoreFile = open("highscore.txt", "w+")
    highscoreFile.write("0")
    highscoreFile.close()
    highscoreFile = open("highscore.txt", "r")
    highscore = int(highscoreFile.read())
    highscoreFile.close()




def enemy():
    global enemyx
    global score
    global speed
    # while enemy on screen, move
    if (enemyx + enemysize) > 0:
        pygame.draw.rect(window, (0,150,0), (enemyx, enemyy, enemysize, enemysize))
        enemyx -= speed
    # reset position
    else:
        enemyx = size[0]
        speed += 0.5
        score += 1


def hitbox():
    global enemyx
    global enemyy
    global playerx
    global playery
    global gameover
    if playerx < enemyx < (playerx + playersize) and playery < enemyy < (playery + playersize):
        gameover = True
        print("gameover")


def gameoverscreen():
    global enemyx
    global enemyy
    global playerx
    global playery
    global gameover
    global score
    global highscore
    global speed
    global sprite

    # checking for new highscore
    if score >= highscore:
        highscore = score
        # writing new highscore
        highscorefile = open("highscore.txt", "w")
        highscorefile.write(f"{highscore}")
        highscorefile.close()

    if gameover:
        enemyx = size[0]
        enemyy = size[1] - enemysize
        playerx = 30
        playery = 430
        gameover = False
        score = 0
        speed = 15
        sprite = pic1

def walking():
    global sprite
    global i
    global j

    j += 1
    if j == 2:
        i += 1
        if i == 3:
            i = 0
        sprite = animation[i]
        j = 1


# displaying score
scoreText = font.render(f"SCORE : {score}    SPEED : {speed}", True, (250, 250, 250))
highscorefile = open("highscore.txt", "r")
run = True
# Clock function
clock = pygame.time.Clock()
while run:
    highscorefile = open("highscore.txt", "r")
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if not jump:
        if keys[pygame.K_SPACE]:
            jump = True
    else:
        if jumpcount >= -10:
            neg = 1
            if jumpcount < 0:
                neg = -1
            playery -= (jumpcount ** 2) * 0.5 * neg
            jumpcount -= 1
        else:
            jump = False
            jumpcount = 10



    # displaying and updating score
    scoreText = font.render(f"SCORE : {score}    HIGHSCORE : {highscorefile.read()}    SPEED : {speed}", True, (250, 250, 250))



    window.fill((0, 0, 0))
    # player
    walking()
    window.blit(sprite, (playerx, playery))
    # enemy
    enemy()
    # score
    window.blit(scoreText, (10, 10))

    hitbox()
    gameoverscreen()

    pygame.display.update()

highscorefile.close()
pygame.quit()