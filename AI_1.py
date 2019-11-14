import numpy as np
from pygame import *

class AI():
  def __init__(self):
    self.pressed_key = "d"
    self.keymap = {"w":"U","a":"L","s":"D","d":"R"}

  def move(self,snake,world,keypresses = None):
    # for i in keypresses:
    #   if i.type == KEYDOWN:
    #     if i.unicode in ["w","s"] and self.pressed_key not in ["w","s"]:
    #       self.pressed_key = i.unicode
    #       break
    #     if i.unicode in ["a","d"] and self.pressed_key not in ["a","d"]:
    #       self.pressed_key = i.unicode
    #       break


    # return self.keymap[self.pressed_key]
    food_pos = world.food_pos
    snake_head = snake.head
    if snake_head[0] > food_pos[0]:
      if self.pressed_key in ["w","s"]:
        self.pressed_key = "a"
        return self.keymap[self.pressed_key]
        
    elif snake_head[0] <  food_pos[0]:
      if self.pressed_key in ["w","s"]:
        self.pressed_key = "d"
        return self.keymap[self.pressed_key]
    
    if snake_head[1] > food_pos[1]:
      if self.pressed_key in ["a","d"]:
        self.pressed_key = "w"
        return self.keymap[self.pressed_key]
        
    elif snake_head[1] < food_pos[1]:
      if self.pressed_key in ["a","d"]:
        self.pressed_key = "s"
        return self.keymap[self.pressed_key]
    
    return self.keymap[self.pressed_key]