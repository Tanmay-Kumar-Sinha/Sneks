from pygame import *
import numpy as np

class Snake():
  def __init__(self,position,AI,length = 3,direction = "R",n = 50):
    self.dir2vec = {"L": np.array([-1,0]),"U": np.array([0,-1]),"R": np.array([1,0]),"D": np.array([0,1])}
    self.length = length
    self.head = position # position of the head
    self.direction = direction # direction which head faces 
    self.tail = self.head - self.length * self.dir2vec[direction]
    self.body = [np.array(self.tail) + i*self.dir2vec[self.direction] for i in range(self.length)] # positions where the body exists
    self.body.append(np.array(self.head))
    self.body.reverse()
    self.AI = AI
    # print(self.body)
    self.last_pos = np.array([1,1])
    self.n = n
    self.score = 0

  # def draw_snake(self,world):
  #   print(self.last_pos)
  #   for i in range(self.length):
  #     pos = self.body[i]
  #     print(i,pos)
  #     world.grid[pos[0]%world.n,pos[1]%world.n] = 1
  #   world.grid[self.last_pos[0]%50,self.last_pos[1]%50] = 0

  def move(self,world,keypresses = None):
    # print(self.body)
    food_pos = world.food_pos
    self.direction = self.AI.move(world,keypresses = keypresses)
    self.last_pos = self.tail
    self.head += self.dir2vec[self.direction]
    for vec in self.body:
      if vec[0] == self.head[0] and vec[1] == self.head[1]:
        return True
    if self.head[0] == food_pos[0] and self.head[1] == food_pos[1]:
      self.score += 1
      world.food_pos = np.random.randint(0,50,size = 2)
      pos = world.scale * world.food_pos
      world.grid[world.food_pos[0],world.food_pos[1]] = 2
      draw.rect(world.gameDisplay,world.colors[2],Rect(pos[0],pos[1],world.scale - 1,world.scale - 1))
      self.length += 1
      print("Score = ",self.score)
    else:
      self.body.pop()
    self.body.insert(0,np.array(self.head))
    self.tail = self.body[self.length - 1]
    if self.head[0] >= self.n:
      return True
    if self.head[0] < 0:
      return True
    if self.head[1] >= self.n:
      return True
    if self.head[1] < 0:
      return True
    return False