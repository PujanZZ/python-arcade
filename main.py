import pygame
import os
import sys,random,time
import math
pygame.mixer.init()
pygame.font.init()
from pygame.locals import *



WIDTH,HEIGHT = 450,650
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Car game?!?")

SCORE_C = (0,0,0)
LIFE_C = 	(88, 90, 253)

FPS = 60
VEL = 5
E_VEL = 12

RED=(255,0,0)

CRASH_COLOR = (0,0,0)

CAR_WIDTH,CAR_HEIGHT = 40,90

CAR_SOUND = pygame.mixer.Sound(os.path.join('Assets','car_s.mp3'))
CRASH_SOUND = pygame.mixer.Sound(os.path.join('Assets','car_c.mp3'))



SCORE_FONT = pygame.font.SysFont("comicsans",60)
LIFE_FONT = pygame.font.SysFont("arial",60)


CAR_1 = pygame.transform.scale(pygame.image.load(
  os.path.join('Assets','car_1.png')),(CAR_WIDTH,CAR_HEIGHT))


ENEMY_1 = pygame.transform.scale(pygame.image.load(
  os.path.join('Assets','enemy_car1.png')),(CAR_WIDTH,CAR_HEIGHT))
ENEMY_2 = pygame.transform.scale(pygame.image.load(
  os.path.join('Assets','enemy_car2.png')),(CAR_WIDTH,CAR_HEIGHT))
ENEMY_3 = pygame.transform.scale(pygame.image.load(
  os.path.join('Assets','enemy_car3.png')),(CAR_WIDTH,CAR_HEIGHT))





ROAD_1 = pygame.transform.scale(pygame.image.load(
  os.path.join('Assets', 'road1.png')), (WIDTH, HEIGHT))




def draw_window(car1,e1,e2,e3):
  WIN.blit(CAR_1,(car1.x,car1.y))
  

  
  
  WIN.blit(ENEMY_1, (e1.x,e1.y))
  
  WIN.blit(ENEMY_2, (e2.x,e2.y))

  WIN.blit(ENEMY_3, (e3.x,e3.y))

pygame.display.update()


def car1_movement(keys_pressed,car1):
  if keys_pressed[pygame.K_a] and car1.x - VEL > 0:
    car1.x -= VEL
  if keys_pressed[pygame.K_d] and car1.x + car1.width < WIDTH:
    car1.x += VEL
  if keys_pressed[pygame.K_w]:
    car1.y -= VEL
  if keys_pressed[pygame.K_s] and car1.y + VEL + car1.height < HEIGHT - 15:
    car1.y += VEL

""" COUNTDOWN """

def countdown():
  font2 = pygame.font.Font('freesansbold.ttf',85)
  countdownBackground = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets','loading.png')),(WIDTH,HEIGHT))

  three = font2.render('3', 1, (187,30,16))
  two = font2.render('2', 1, (187,30,16))
  one = font2.render('1', 1, (187,30,16))
  go = font2.render('GO!!!', 1, (0,255,0))

  ## DISPLAYING BLANK BACKGROUD ##
  WIN.blit(countdownBackground, (0,0))
  pygame.display.update()

  ## DISPLAYING 3,2,1,GO ##

  WIN.blit(three,(185,100))
  pygame.display.update()
  time.sleep(1)
  
  WIN.blit(countdownBackground, (0,0))
  pygame.display.update()

  WIN.blit(two,(185,100))
  pygame.display.update()
  time.sleep(1)
  
  WIN.blit(countdownBackground, (0,0))
  pygame.display.update()
  
  WIN.blit(one,(185,100))
  pygame.display.update()
  time.sleep(1)

  WIN.blit(countdownBackground, (0,0))
  pygame.display.update()
  
  WIN.blit(go,(155,100))
  pygame.display.update()
  time.sleep(1)
  main()
  pygame.display.update()

"""COUNTDOWN END"""

"""GAMER OVER TEXT"""


# def draw_winner(text):
#     font3 = pygame.font.Font('freesansbold.ttf',85)

#     game_over = font3.render('GAME OVER!!', 1, (187,30,16))
#     WIN.blit(game_over,(WIDTH//2,350))
#     pygame.display.update()
#     pygame.time.delay(5000)


"""GAME OVER TEXT"""


def main():


  """MUSIC """

  pygame.mixer.music.load('Assets\BackgroundMusic.mp3')
 
  pygame.mixer.music.play(-1)
  pygame.mixer.music.set_volume(0.1)

  """MUSIC"""
    
  def show_score(x,y):
    score = SCORE_FONT.render(str(score_value), 1, SCORE_C)
    WIN.blit(score, (x,y))
  score_value = 0
    
  def life(s1,s2):
    score = LIFE_FONT.render("Life: " + str(lives), 1, LIFE_C)
    WIN.blit(score, (s1,s2))
  lives = 50
  




  car1 = pygame.Rect(80,500,CAR_WIDTH,CAR_HEIGHT)
  e1 = pygame.Rect(random.randint(20,130), 50, CAR_WIDTH, CAR_HEIGHT)
  e2 = pygame.Rect(random.randint(170,240 ), 50, CAR_WIDTH, CAR_HEIGHT)
  e3 = pygame.Rect(random.randint(280,360 ), 50, CAR_WIDTH, CAR_HEIGHT)


  

  i = 0
  clock = pygame.time.Clock()
  run = True
  while run:
   
    WIN.blit(ROAD_1,(0,i))
    WIN.blit(ROAD_1,(0,-HEIGHT+i))

    if i == HEIGHT:
      i=0


    i+=5
    
    
    
    clock.tick(FPS)
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
          
    e1.y +=E_VEL
    e2.y +=E_VEL
    e3.y +=E_VEL
    
    
    if e1.y > 670:
      e1.y = -500
      e1 = pygame.Rect(random.randint(20,130), e1.y, CAR_WIDTH, CAR_HEIGHT)
      score_value +=1
    if e2.y > 670:
      e2.y = -250
      e2 = pygame.Rect(random.randint(170,240), e2.y, CAR_WIDTH, CAR_HEIGHT)
      score_value +=1
    if e3.y > 670:
      e3.y = -100
      e3 = pygame.Rect(random.randint(280,360), e3.y, CAR_WIDTH, CAR_HEIGHT)
      score_value +=1

   
    
    colliding = car1.colliderect(e1)
    if colliding:
      lives -= 1
      car1.x = WIDTH/2  - 20
      
      CRASH_SOUND.set_volume(0.2)
      CRASH_SOUND.play()
      

      pygame.time.delay(850)
      car1.y = 550
      e1.x = random.randint(20,100)
      e1.y = -550
      e2.y = -350
      e3.y = -100
      
      
      if lives <=0:

        pygame.quit()


    colliding = car1.colliderect(e2)
    if colliding:
      lives -= 1
      car1.x = WIDTH/2  - 20
      
      CRASH_SOUND.set_volume(0.2)
      CRASH_SOUND.play()

      pygame.time.delay(850)
      car1.y = 550
      e2.x = random.randint(200,280)
      e1.y = -550
      e2.y = -350
      e3.y = -100

      if lives <=0:

        pygame.quit()
      

    colliding = car1.colliderect(e3)
    if colliding:
      lives -= 1
      car1.x = WIDTH/2  - 20
      
      CRASH_SOUND.set_volume(0.2)
      CRASH_SOUND.play()


      pygame.time.delay(850)
      car1.y = 550
      e3.x = random.randint(280,360)
      e1.y = -550
      e2.y = -350
      e3.y = -100

      if lives <=0:

       pygame.quit()
    


  
    keys_pressed = pygame.key.get_pressed()

    draw_window(car1,e1,e2,e3)
    car1_movement(keys_pressed,car1)
    
    show_score(0,0)
    life(280,-5)
    
   
    
    pygame.display.update()


    




if __name__ == '__main__':
 countdown()
 main()
 