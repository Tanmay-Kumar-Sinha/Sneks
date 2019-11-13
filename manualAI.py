import numpy as np
from pygame import *

class manualAI():
  def __init__(self):
    self.pressed_key = "d"
    self.keymap = {"w":"U","a":"L","s":"D","d":"R"}

  def move(self,world,keypresses = None):
    for i in keypresses:
      # print(i)
      if i.type == KEYDOWN:
        if i.unicode in ["w","s"] and self.pressed_key not in ["w","s"]:
          self.pressed_key = i.unicode
          break
        if i.unicode in ["a","d"] and self.pressed_key not in ["a","d"]:
          self.pressed_key = i.unicode
          break

    # print(self.pressed_key)

    return self.keymap[self.pressed_key]