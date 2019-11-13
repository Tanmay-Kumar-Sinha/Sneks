import numpy as np
from pygame import *

class World():
  def __init__(self,gameDisplay,n = 100):
    # n is the number of cells along each i.e. the grid has size n x n
    self.n = n
    self.grid = np.zeros((n,n))
    self.gameDisplay = gameDisplay
    self.w,self.h = display.get_surface().get_size()
    self.scale = self.w // self.n
    self.food_pos = np.random.randint(0,50,size = 2)
    self.grid[self.food_pos[0],self.food_pos[1]] = 2
    self.colors = {1:(255,255,255),0:(0,0,0),2:(255,0,0)}
    # 0 : nothing, 1 : snake, 2 : food
    for i in range(self.n):
      for j in range(self.n):
        val = self.grid[i,j]
        pos = self.scale*np.array([i,j])
        draw.rect(self.gameDisplay,self.colors[val],Rect(pos[0],pos[1],self.scale - 1,self.scale - 1))


  def draw(self,snake):
    # draw.rect(self.gameDisplay,(0,255,255),Rect(self.h//2,self.w//2,self.scale,self.scale))
    # draw.rect(self.gameDisplay,(0,255,255),Rect(0,0,self.scale,self.scale))

    # for i in range(self.n):
    #   for j in range(self.n):
    #     val = self.grid[i,j]
    #     pos = self.scale*np.array([i,j])
    #     draw.rect(self.gameDisplay,self.colors[val],Rect(pos[0],pos[1],self.scale - 1,self.scale - 1))
    self.grid[snake.last_pos[0]%self.n,snake.last_pos[1]%self.n] = 0
    val = 0
    pos = self.scale * snake.last_pos
    # print(snake.last_pos,snake.head)
    draw.rect(self.gameDisplay,self.colors[val],Rect(pos[0],pos[1],self.scale - 1,self.scale - 1))
    self.grid[snake.head[0]%self.n,snake.head[1]%self.n] = 1
    val = 1
    pos = self.scale * snake.head
    draw.rect(self.gameDisplay,self.colors[val],Rect(pos[0],pos[1],self.scale - 1,self.scale - 1))
