import pygame
import time
import sys
import SnakeGame_Class
import random
from SnakeGame_Class import Snake


pygame.init()

screen=pygame.display.set_mode((400,400))
pygame.display.set_caption("Snake Game")

# Colours
GRAY=(44,44,44)
ORANGE=(255,111,0)
CRYSTAL=(255,204,0)
WHITE=(255,255,255)
BLACK=(0,0,0)

# Fonts
UI_font=pygame.font.SysFont("Arial",20)
UI_bigFont=pygame.font.SysFont("Arial",25, bold=True)

clock=pygame.time.Clock()

snake=Snake()


def game_over(screen, font, color, screen_size):
    text=UI_bigFont.render("GAME OVER!",True,WHITE)
    screen.blit(text,(115,170))
    score=UI_font.render(f"Score: {snake.score()}",True,WHITE)
    screen.blit(score,(120, 210))
    pygame.display.update()
FOOD_COLORS = [CRYSTAL, ORANGE, WHITE, BLACK]
def generate_food_position(block_size, screen_width, screen_height,color):
    x = random.randint(0, (screen_width - block_size) // block_size) * block_size
    y = random.randint(0, (screen_height - block_size) // block_size) * block_size
    color=random.choice(FOOD_COLORS)
    return [x, y],color
def generate_bomb_position(block_size, screen_width, screen_height,color):
    x=random.randint(0,(screen_width-block_size)//block_size)*block_size
    y = random.randint(0, (screen_height - block_size) // block_size) * block_size
    return [x, y]

food_position, food_color=generate_food_position(snake.block_size,400,400,CRYSTAL)

running=True
while running:
    screen.fill(GRAY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

        elif event.type==pygame.KEYDOWN:
            
            if event.key==pygame.K_UP:
                snake.changeDirection("UP")
            elif event.key==pygame.K_DOWN:
                snake.changeDirection("DOWN")
            elif event.key==pygame.K_LEFT:
                snake.changeDirection("LEFT")
            elif event.key==pygame.K_RIGHT:
                snake.changeDirection("RIGHT")
     
    if snake.head_position() == food_position:
        snake.move(True)
        food_position,food_color = generate_food_position(snake.block_size, 400, 400,CRYSTAL)
    else:
        snake.move()
    for index,segment in enumerate(snake.body):
        if index==0:
            pygame.draw.rect(screen, BLACK, (segment[0], segment[1], snake.block_size, snake.block_size))
        else:
            pygame.draw.rect(screen, ORANGE, (segment[0], segment[1], snake.block_size, snake.block_size))
    if snake.checkCollisions() or snake.boundaryCollision():
        game_over(screen,"Times New Roman",WHITE,True)
    pygame.draw.rect(screen, food_color, (food_position[0], food_position[1], snake.block_size, snake.block_size))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
sys.exit()


