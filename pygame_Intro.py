import pygame 
import time
import random

pygame.init()

pause=False

crash_sound=pygame.mixer.Sound("vehicle105.wav")
pygame.mixer.music.load("BMW+DRIVEBY.wav")


display_width=800
display_height=600

black=(0,0,0)          #Tuple          
white=(255,255,255)    #Maximum of all colors

red=(200,0,0)
green=(0,200,0)

bright_red=(255,0,0)
bright_green=(0,255,0)
bc=(112,0,0)
block_color= (53,115,255)



car_width=75

gamedisplay=pygame.display.set_mode((display_width,display_height))                                                                                                                        
pygame.display.set_caption('Racing Game!!!')
clock= pygame.time.Clock()

carImg=pygame.image.load('racingcar.jpg')
pygame.display.set_icon(carImg)

def thing_dodged(count):    # Function to print score
    font=pygame.font.SysFont(None,25)
    text=font.render('Dodged : '+str(count),True,black)
    gamedisplay.blit(text,(0,0))


def things(thingx,thingy,thingh,thingw,color):
    pygame.draw.rect(gamedisplay,color,[thingx,thingy,thingh,thingw])


def car(x,y):
    gamedisplay.blit(carImg,(x,y))


def text_objects(text,font):
    font.set_underline(1)
    textSurface=font.render(text,True,black)
    return textSurface,textSurface.get_rect()

##def message_display(text):
##    largetext=pygame.font.Font('freesansbold.ttf',115)
##    TextSurf,TextRect=text_objects(text,largetext)
##    TextRect.center=((display_width/2),(display_height/2))
##    gamedisplay.blit(TextSurf,TextRect)
##    pygame.display.update()
##
##    time.sleep(2)
##
##    game_loop()
     
def crash():

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    
    text="Crashed!!"
    LargeText=pygame.font.Font('freesansbold.ttf',115)
    TextSurf,TextRect=text_objects(text,LargeText)
    TextRect.center=((display_width/2),(display_height/2))
    gamedisplay.blit(TextSurf,TextRect)
    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        #gamedisplay.fill(white)
       

        button("Play Again",150,450,100,50,green,bright_green,game_loop)
        button("Quit!",550,450,100,50,red,bright_red,quitgame)



        pygame.display.update()
        clock.tick(15)

def button(msg,x,y,w,h,ic,ac,action='None'):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()    # To Check whether left click is pressed or right
    #print(click)
    
    

    
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
            pygame.draw.rect(gamedisplay,ic,(x,y,w,h))
            if click[0]==1 and action!="None":
                action()
##                if action=="Play":
##                    game_loop()
##                elif action=="quit":
##                    pygame.quit()
##                    quit()
    else:
            pygame.draw.rect(gamedisplay,ac,(x,y,w,h))

    #if x+w>mouse[0]>x and y+h>mouse[1]>y:
     #   pygame.draw.rect(gamedisplay,bright_red,(550,450,100,50))
    #else:
   # pygame.draw.rect(gamedisplay,green,(x,y,w,h))

    largetext=pygame.font.Font('freesansbold.ttf',15)
    TextSurf,TextRect=text_objects(msg,largetext)
    TextRect.center=((x+(w/2)),(y+(h/2)))
    gamedisplay.blit(TextSurf,TextRect)

def unpaused():
    global pause
    pygame.mixer.music.unpause()
    pause=False
    


def paused():
    
    pygame.mixer.music.pause()
    
    text="PAUSED!!"
    LargeText=pygame.font.Font('freesansbold.ttf',115)
    TextSurf,TextRect=text_objects(text,LargeText)
    TextRect.center=((display_width/2),(display_height/2))
    gamedisplay.blit(TextSurf,TextRect)
    while pause:
        for event in pygame.event.get():
            #print(event)
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        #gamedisplay.fill(white)
       

        button("Continue",150,450,100,50,green,bright_green,unpaused)
        button("Quit!",550,450,100,50,red,bright_red,quitgame)



        pygame.display.update()
        clock.tick(15)



def quitgame():
    pygame.quit()
    quit()

def game_intro(text):

    intro=True
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gamedisplay.fill(bc)
        LargeText=pygame.font.Font('freesansbold.ttf',115)
        TextSurf,TextRect=text_objects(text,LargeText)
        TextRect.center=((display_width/2),(display_height/2))
        gamedisplay.blit(TextSurf,TextRect)

        carImg=pygame.image.load('car.jpg')
        gamedisplay.blit(carImg,(300,0))

        button("Go!",150,450,100,50,green,bright_green,game_loop)
        button("Quit!",550,450,100,50,red,bright_red,quitgame)



        pygame.display.update()
        clock.tick(15)

    

def game_loop():
    global pause
    pygame.mixer.music.play(-1)
    pause=False
    x=(display_width * 0.5)
    y=(display_height * 0.8)

    x_change=0

    thing_startx=random.randrange(0,display_width)
    thing_starty=-600
    thing_speed=4
    thing_width=100
    thing_height=100

    things_count=1

    dodged=0       #Initilize score with Zero
    
    gameExit=False

    

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:            #Any key press
                if event.key==pygame.K_LEFT:
                    x_change=-10
                if event.key==pygame.K_RIGHT:
                    x_change=10
                if event.key==pygame.K_p:
                    pause=True
                    paused()
              
            if event.type==pygame.KEYUP:              #Key Realse
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0

       


        x+=x_change        #To change position of car

        gamedisplay.fill(bc)   #To make background color White

        bg=pygame.image.load('car.jpg')                             #To add bg image
        bg=pygame.transform.scale(bg,(display_width,display_height))    #To resize image
        gamedisplay.blit(bg,(0,0))                                #To display image

        
    
        
        things(thing_startx,thing_starty, thing_width,thing_height,block_color)   #Obstacle in the path
        thing_starty+=thing_speed      #To move obstacle down
        car(x,y)
        thing_dodged(dodged)            

        if x>display_width-car_width or x<0:   # Crash when car hits boundary
            #gameExit=True
            crash()

        if thing_starty>display_height:   # To set position of obstacle when obstacle goes beyond screen
            thing_starty=0-thing_height
            thing_startx=random.randrange(0,display_width)
            dodged+=1       #Incrementing Score
            thing_speed+=1        #Incresing Speed
           # thing_width+=(dodged *1.2)

        if y<thing_starty+thing_height:
           # print('Y crossover')

            if x>thing_startx and x< thing_startx+thing_width or x+car_width>thing_startx and x+car_width<thing_startx+thing_width:
               # print('x crossover')
                crash()

        
                    
        pygame.display.update()
        clock.tick(60)

game_intro("Racing Game!!")
game_loop()
pygame.quit()
quit()
