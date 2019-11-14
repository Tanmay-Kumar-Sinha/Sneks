from pygame import *
from snake import *
from world import *
from time import sleep
from manualAI import *
from AI_1 import AI
init()
clock = time.Clock()
h = 600
w = 600

gameDisplay = display.set_mode((h,w))

crashed = False

world = World(gameDisplay,n = 50)
snake = Snake(np.array([20,25]),AI())

while not crashed:
  keypresses = []
  for i in event.get():
    keypresses.append(i)
    if i.type == KEYDOWN:
      if i.unicode == "q":
        crashed = True


  crashed = snake.move(world,keypresses = keypresses) or crashed
  # gameDisplay.fill((0,0,0))
  world.draw(snake)


  display.update()
  clock.tick(20)