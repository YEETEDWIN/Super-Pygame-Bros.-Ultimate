# Imports
import pygame
import random, time, sys
from images import *

pygame.init()

WIDTH = 1280
HEIGHT = 720
FPS = 60
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)

pygame.display.set_caption('Super Pygame Bros. Ultimate')
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Images
bg_img = pygame.image.load("Images/bg.jpg")

def handle_players(players):
  screen.blit(bg_img, (0,0))
  screen.blit(players[0], (200,300))
  screen.blit(players[1], (800,300))
  pygame.display.update()
  

class InputBox:
  def __init__(self, x, y, w, h, text=''):
    self.rect = pygame.Rect(x, y, w, h)
    self.color = COLOR_INACTIVE
    self.text = text
    self.txt_surface = FONT.render(text, True, self.color)
    self.active = False

  def handle_event(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
      # If the user clicked on the input_box rect.
      if self.rect.collidepoint(event.pos):
        # Toggle the active variable.
        self.active = not self.active
      else:
        self.active = False
      # Change the current color of the input box.
      self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
    if event.type == pygame.KEYDOWN:
      if self.active:
        if event.key == pygame.K_RETURN:
          if self.text == "falco + mario":
            players = [falco_img,rot_mario_img]
            handle_players(players)
        elif event.key == pygame.K_BACKSPACE:
          self.text = self.text[:-1]
        else:
          self.text += event.unicode
        # Re-render the text.
        self.txt_surface = FONT.render(self.text, True, self.color)

  def update(self):
    # Resize the box if the text is too long.
    width = max(200, self.txt_surface.get_width()+10)
    self.rect.w = width

  def draw(self, screen):
    # Blit the text.
    screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
    # Blit the rect.
    pygame.draw.rect(screen, self.color, self.rect, 2)


def main():
  clock = pygame.time.Clock()
  #screen.blit(bg_img, (0,0))
  input_box = InputBox(WIDTH//2-90, HEIGHT//2-30, 60, 40, "")
  inputbox = [input_box]
  screen.fill((30, 30, 30))
  #screen.blit(falco_img, (200,300))
  #Image side chars are 200 on 300
  #screen.blit(rot_falco_img, (800,300))
  #Rotated side chars are 800 on 300
  pygame.display.update()

  done = False
  while not done:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
      for box in inputbox:
        box.handle_event(event)

    for box in inputbox:
      box.update()

    for box in inputbox:
      box.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

if __name__ == '__main__':
  main()