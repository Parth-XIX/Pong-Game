import pygame
import sys
import random

player_score = 0
opponent_score = 0

def ball_movement():
    global ball_speed_x, ball_speed_y, player_score, opponent_scoreo
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= scr_height:
        ball_speed_y *= -1
    if ball.left <= 0:
        ball_restart()
        player_score += 1
    
    if ball.right >= scr_width:
        ball_restart()
        opponent_score = opponent_score + 1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_movement():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= scr_height:
        player.bottom = scr_height

def opponent_movement():
    if opponent.centery < ball.y:
        opponent.centery += opponent_speed
    if opponent.centery > ball.y:
        opponent.centery -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= scr_height:
        opponent.bottom = scr_height

def ball_restart():
    global ball_speed_y, ball_speed_x
    ball.center = (scr_width/2,scr_height/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))

pygame.init()
clock = pygame.time.Clock()

scr_width = 1200
scr_height = 720
scr = pygame.display.set_mode((scr_width,scr_height))
pygame.display.set_caption('Pong')

ball = pygame.Rect(scr_width/2 - 15,scr_height/2 - 15,30,30)
player = pygame.Rect(scr_width - 20, scr_height/2 - 70,10,140)
opponent = pygame.Rect(10, scr_height/2 - 70,10,140)

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

ball_speed_x = 5 * random.choice((1,-1))
ball_speed_y = 5 * random.choice((1,-1))
player_speed = 0
opponent_speed = 5


game_font = pygame.font.Font("freesansbold.ttf", 32)
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 5
            if event.key == pygame.K_UP:
                player_speed -= 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 5
            if event.key == pygame.K_UP:
                player_speed += 5

    ball_movement()    
    player_movement()
    opponent_movement()

    scr.fill(bg_color)
    pygame.draw.rect(scr, light_grey, player)
    pygame.draw.rect(scr, light_grey, opponent)
    pygame.draw.ellipse(scr, light_grey, ball)
    pygame.draw.aaline(scr, light_grey, (scr_width/2,0),(scr_width/2,scr_height))

    player_text = game_font.render(f"{player_score}", False, light_grey)
    scr.blit(player_text,(610,350))
    opponent_text = game_font.render(f"{opponent_score}", False, light_grey)
    scr.blit(opponent_text,(575,350))

    pygame.display.flip()
    clock.tick(60)