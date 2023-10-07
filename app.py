import pygame

pygame.init()

#Initials
WIDTH, HEIGHT = 1000, 600
wn = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("PING-PONG")
run = True

#Color
VIOLET =  (115, 41, 210)
LUSH_TEAL = (51, 255, 173)
BACKGROUND_COLOR = (29, 30, 34)

#BALL
radius = 15
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
ball_val_x, ball_val_y = 0.5, 0.5

#PADDLE
paddle_width, paddle_height = 20, 120
left_paddle_y = right_paddle_y = HEIGHT/2 - paddle_height/2
left_paddle_x = 100 - paddle_width/2
right_paddle_x = WIDTH - 100 - paddle_width/2
wn.fill(BACKGROUND_COLOR)

# paddle velocities
right_paddle_vel = left_paddle_vel = 1

#Primary loop
while run:
  wn.fill(BACKGROUND_COLOR)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pressed = pygame.key.get_pressed()
  if pressed[pygame.K_DOWN]: 
    right_paddle_y += right_paddle_vel
  if pressed[pygame.K_UP]: 
    right_paddle_y -= right_paddle_vel
  if pressed[pygame.K_w]: 
    left_paddle_y -= left_paddle_vel
  if pressed[pygame.K_s]: 
    left_paddle_y += left_paddle_vel

  # paddle movement
  if right_paddle_y < 0:
    right_paddle_y = 0
  elif right_paddle_y > HEIGHT - paddle_height:
    right_paddle_y = HEIGHT - paddle_height

  if left_paddle_y < 0:
    left_paddle_y = 0
  elif left_paddle_y > HEIGHT - paddle_height:
    left_paddle_y = HEIGHT - paddle_height

  #collisions
  #left
  if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
    if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
      ball_x = left_paddle_x + paddle_width
      ball_val_x *= -1
  #right
  if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
    if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
      ball_val_x *= -1


  #Movements
  ball_x += ball_val_x
  ball_y += ball_val_y  

  #Ball control
  if ball_y <= 0 + radius or ball_y >= HEIGHT - radius:
    ball_val_y *= -1
  if ball_x >= WIDTH - radius: # if the ball has hit the right edge
    ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
    ball_val_x, ball_val_y = 0.5, 0.5
  if ball_x <= 0 + radius: # if the ball has hit the left edge
    ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
    ball_val_x, ball_val_y = 0.5, 0.

  #Objects  
  pygame.draw.circle(wn, VIOLET, (int(ball_x), int(ball_y)), radius) 
  pygame.draw.rect(wn, LUSH_TEAL, pygame.Rect(int(left_paddle_x), int(left_paddle_y), paddle_width, paddle_height))
  pygame.draw.rect(wn, LUSH_TEAL, pygame.Rect(int(right_paddle_x), int(right_paddle_y), paddle_width, paddle_height))

  pygame.display.update()
