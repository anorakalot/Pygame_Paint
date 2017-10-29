#import modules / libraries
import pygame
import random
import datetime

#initialize pygame modules
pygame.init()

#make random numbers even more random
random.seed()


#for music sounds
pygame.mixer.music.load('/home/anorak/Documents/projects/pygame_learning/Sabrepulse-Turbo-City-01-Cityscape-Dreams.ogg')
#function for playing music
def play_music():
    pygame.mixer.music.play(0)

#function for stopping music
def stop_music():
    pygame.mixer.music.stop()

#main screen for drawing
screen = pygame.display.set_mode((1000,1000))


#while loop variable
done = False

#color variable for drawing
color = (255,255,255)
print("Welcome to Dylan's Paint Program!!")
print("press P to save your beautiful painting!")
print("press 1-4 for paint colors!")
print("press 9 to reset your painting!")
print("press M for some drawing music!")
print("press N to stop the music")
print("\n\n\n")
while not done:
    #check for "menu" keydown and quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                done = True
            if event.key == pygame.K_p:
                pygame.image.save(screen,"screenshot"+ str(datetime.datetime.now()) +".jpeg")
                #print in console that you saved an image
                print("You saved an image!!!")
            #white drawing option
            if event.key == pygame.K_1:
                color = (255,255,255)
            #red drawing option
            if event.key == pygame.K_2:
                color = (255,0,0)
            #green drawing option
            if event.key == pygame.K_3:
                color = (0,255,0)
            #blue drawing option
            if event.key == pygame.K_4:
                color = (0,0,255)
            #reset painting screen
            if event.key == pygame.K_9:
                screen.fill((0,0,0))
            if event.key == pygame.K_m:
                play_music()
            if event.key == pygame.K_n:
                stop_music()

    #if left mouse button is clicked
    if pygame.mouse.get_pressed() == (True,False,False):
        coordinates = pygame.mouse.get_pos()
        #draws the circle at positions given
        pygame.draw.circle(screen,color,coordinates,20,20)
        pygame.display.update()

    if pygame.mouse.get_pressed() == (False,False,True):
        erase_coordinates = pygame.mouse.get_pos()
        #erases with circles of black
        pygame.draw.circle(screen,(0,0,0),erase_coordinates,50,50)


    #need this in order to update drawing of screen
    pygame.display.flip()

    #need this to keep game at 60fps or the game is too fast
    #pygame.time.Clock().tick(180)

'''
    if pygame.key.get_pressed()[pygame.K_w]: y-= 3
    if pygame.key.get_pressed()[pygame.K_s]: y+= 3
    if pygame.key.get_pressed()[pygame.K_a]: x -= 3
    if pygame.key.get_pressed()[pygame.K_d]: x += 3
'''






    #need this so draw circle isnt just a continuing blob
    #screen.fill((0,0,0))
