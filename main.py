import pygame
import math
import random

pygame.init()

#define the width and height of the game itself
WIDTH,HEIGHT=800,500   #constants
wind=pygame.display.set_mode((WIDTH,HEIGHT)) #window

pygame.display.set_caption("Hangman")

#buttons
rad=20
gap=15
letters=[]

startx=round((WIDTH-(rad*2+gap)*13)/2)
starty=400
A=65

for i in range(26):
    x=startx+gap*2+((rad*2+gap)*(i%13))
    y=starty+((i//13)*(gap+rad*2))
    letters.append([x,y,chr(A+i),True])

#fonts
LETTER_FONT=pygame.font.SysFont('comicsans',40)
WORD_FONT=pygame.font.SysFont('comicsans',60)
TITLE_FONT=pygame.font.SysFont('comicsans',70)

#images
images=[]
for i in range(7):
    image=pygame.image.load("hangman"+str(i)+".png")
    images.append(image)

#game variables
hangman_stat=0
words=["PYTHON","JAVA","PROGRAMMER","IDE","DEVELOPER","CONSOLE"]
word=random.choice(words)
guessed=[]
FPS=60

clock=pygame.time.Clock()
run=True

#function
def draw():
    wind.fill(WHITE)
    text=TITLE_FONT.render("HANGMAN",1,BLACK)
    wind.blit(text,(WIDTH/2-text.get_width()/2,20))

    #drawing the word

    display_word=""
    for letter in word:
        if letter in guessed:
            display_word+=letter+" "
        else:
            display_word+="_ "
    text=WORD_FONT.render(display_word,1,BLACK)
    wind.blit(text,(400,200))

    # drawing buttons
    for letter in letters:
        x, y, ltr,visible= letter
        if visible:
            pygame.draw.circle(wind, BLACK, (x, y), rad, 3)
            #render the text
            text=LETTER_FONT.render(ltr,1,BLACK) #anti-aliasing as 1
            wind.blit(text,(x-text.get_width()/2,y-text.get_height()/2))

    wind.blit(images[hangman_stat], (150, 100))
    pygame.display.update()

def display_message(message):
    #pygame.time.delay(1000)
    wind.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    wind.blit(text, (WIDTH/2-text.get_width()/2, HEIGHT/2-text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)


#colors
WHITE=(255,255,255)
BLACK=(0,0,0)

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
       if event.type==pygame.QUIT:
           run=False
       if event.type==pygame.MOUSEBUTTONDOWN:
           m_x,m_y=pygame.mouse.get_pos()
           for letter in letters:
               x,y,ltr,visible=letter
               if visible:
                   dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                   if dis < rad:
                       letter[3]=False
                       guessed.append(ltr)
                       if ltr not in word:
                           hangman_stat += 1

    draw()
    won=True
    for letter in word:
        if letter not in guessed:
            won=False
            break

    if won:
        display_message("YOU WON")
        break

    if hangman_stat==6:
        display_message("YOU LOST")
        break


pygame.quit()




