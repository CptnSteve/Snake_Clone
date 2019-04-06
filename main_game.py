# Python Snake Clone
# Steve Olsen

from pygame.locals import *
import pygame
import os
import sys
import time

class App:
  windowWidth = 1000
  windowHeight = 800
  player = 0

  def __init__(self):
    self._running = True
    self._display_surf = None
    self._image_surf = None
    self.player = Player()
  
  def on_init(self):
    pygame.init()
    self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
    
    pygame.display.set_caption('<< Pygame example lifted from Pythonspot >>')
    self._running = True
    self._image_surf = pygame.image.load(os.path.join(os.path.dirname(__file__),"pygame.png")).convert()

  def on_event(self, event):
    if event.type == QUIT:
      self._running = False

  def on_loop(self):
    self.player.update()
    pass 

  def on_render(self):
    self._display_surf.fill((0,0,0))
    self._display_surf.blit(self._image_surf,(self.player.x, self.player.y))
    # self.player.draw(self._display_surf, self._image_surf)
    pygame.display.flip()

  def on_cleanup(self):
    pygame.quit()

  def on_execute(self):
    if self.on_init() == False:
      self._running = False

    while(self._running):
      pygame.event.pump()
      keys = pygame.key.get_pressed()

      if (keys[K_RIGHT]):
        self.player.moveRight()
      if (keys[K_LEFT]):
        self.player.moveLeft()
      if (keys[K_UP]):
        self.player.moveUp()
      if (keys[K_DOWN]):
        self.player.moveDown()

      if (keys[K_ESCAPE]):
        self._running = False

      self.on_loop()
      self.on_render()

      time.sleep (10.0/1000.0)
    self.on_cleanup()

class Player:
  x = 10
  y = 200
  speed = 6
  direction = 0
  # length = 3

  def update(self):
    if self.direction == 0:
      self.x = self.x + self.speed
    if self.direction == 1:
      self.x = self.x - self.speed
    if self.direction == 2:
      self.y = self.y - self.speed
    if self.direction == 3:
      self.y = self.y + self.speed

  def moveRight(self):
    self.direction = 0

  def moveLeft(self):
    self.direction = 1

  def moveUp(self):
    self.direction = 2

  def moveDown(self):
    self.direction = 3
  
  def draw(self, surface, image):
    for i in range(0,self.length):
      surface.blit(image,(self.x[i], self.y[i]))

if __name__ == "__main__":
  theApp = App()
  theApp.on_execute()

pygame.event.pump()
keys = pygame.key.get_pressed()


