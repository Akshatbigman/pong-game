import pygame, sys
from pygame.locals import QUIT

pygame.init()
pygame.display.set_caption('Welcome to the PONG game: ')
width,height = 400,300
window = pygame.display.set_mode((width,height))

background = (255,255,255)
window.fill(background)

gameover = False

black = (0,0,0)
blue = (0,0,255)
white = (255,255,255)
green = (0,255,0)

#paddle

paddle_width, paddle_height = 80,10
paddle_x, paddle_y = (width//2 - paddle_width)//2, height - paddle_height - 10

#ball

ball_radius = 5
ball_x, ball_y = width//2, height//2
ball_speed_x, ball_speed_y = 3, -3

#score
score = 0

#font for displaying scorw
font = pygame.font.Font(None,36)


while not gameover:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT] and paddle_x > 0:
    paddle_x -= 5
  if keys[pygame.K_RIGHT] and paddle_x < width - paddle_width:
    paddle_x += 5
  ball_x += ball_speed_x
  ball_y += ball_speed_y
#displaying score
  score_text = font.render(f"Score: {score}", True, black)
  window.blit(score_text, (10,10))
  pygame.display.update()
  window.fill(white)
  paddle = pygame.draw.rect(window, green, (paddle_x, paddle_y, paddle_width,paddle_height))
  ball = pygame.draw.circle(window, blue, (ball_x, ball_y), ball_radius)
  pygame.display.update()
  if ball.left<=0 or ball.right >= width:
    ball_speed_x *= -1
  if ball.top <= 0 or ball.bottom >= height:
    ball_speed_y *= -1
  if pygame.Rect.colliderect(ball,paddle):
    ball_speed_y *= -1
    score += 1
  if ball.bottom>= height:
    gameover = True
  pygame.time.delay(30)
window.fill(white)
score_text = font.render(f"Score: {score}", True, black)
window.blit(score_text, (10,10))
gameover_text = font.render("Game Over", True, black)
window.blit(gameover_text, (width//2 - 80, height//2 - 18))
pygame.display.update()
pygame.time.delay(2000)


pygame.quit()
sys.exit()
