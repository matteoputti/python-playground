import pygame
import time
import random
pygame.init()

display_width = 800
display_height = 600

display=pygame.display.set_mode((display_width,display_height))

pygame.display.update()

pygame.display.set_caption('Snake game by MATTEO')

blue=(0,0,255)
red=(255,0,0)
black=(0,0,0)
white=(255,255,255)

x1 = display_width/2
y1 = display_height/2

x1_change = 0
y1_change = 0


clock = pygame.time.Clock()
snake_speed = 30

snake_display_size = 10
snake_list = []
snake_size = 1

def draw_snake(snake_display_size,snake_list):
 for x in snake_list:
     pygame.draw.rect(display,black,[x[0],x[1],snake_display_size,snake_display_size])

font_style = pygame.font.SysFont(None, 50)
 
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [display_width/2, display_height/2])

foodx = round(random.randrange(0, display_width - snake_display_size) / 10.0) * 10.0
foody = round(random.randrange(0, display_height - snake_display_size) / 10.0) * 10.0

game_over = False
while not game_over:
    print(foodx,foody)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over = True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x1_change = -snake_display_size
                y1_change = 0
            elif event.key==pygame.K_RIGHT:
                x1_change = snake_display_size
                y1_change = 0
            elif event.key==pygame.K_UP:
                x1_change = 0
                y1_change = -snake_display_size
            elif event.key==pygame.K_DOWN:
                x1_change = 0
                y1_change = snake_display_size
    
    x1 += x1_change
    y1 += y1_change

   
    snake_Head = []
    snake_Head.append(x1)
    snake_Head.append(y1)
    snake_list.append(snake_Head)

    if len(snake_list) > snake_size:
        del snake_list[0]
 
    for x in snake_list[:-1]:
        if x == snake_Head:
            game_over = True
    
    if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
        game_over = True

    display.fill(white)
    
    pygame.draw.rect(display,red,[foodx,foody,snake_display_size,snake_display_size])
    draw_snake(snake_display_size,snake_list)

    pygame.display.update()

    if x1 == foodx and y1 == foody:
            print("Yummy!!")
            snake_size += 1
            foodx = round(random.randrange(0, display_width - snake_display_size) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_display_size) / 10.0) * 10.0
    
    clock.tick(snake_speed)

message("Game over :(",red)
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()