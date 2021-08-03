# Imports
import pygame
import random, time, sys
from pygame.locals import *

pygame.init()
pygame.font.init()

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

# Images/Powerups
superball_img = pygame.image.load("Images/Powerups/super.png")
containheart_img = pygame.image.load("Images/Powerups/heart.png")
smartbomb_img = pygame.image.load("Images/Powerups/smartbomb.png")
freezie_img = pygame.image.load("Images/Powerups/freezie.png")
tomato_img = pygame.image.load("Images/Powerups/tomato.png")

# Images/Chars
falco_img = pygame.image.load("Images/Chars/falco.webp")
game_img = pygame.image.load("Images/Chars/game.webp")
ganondorf_img = pygame.image.load("Images/Chars/ganondorf.webp")
mario_img = pygame.image.load("Images/Chars/mario.webp")
metaknight_img = pygame.image.load("Images/Chars/meta_knight.webp")
ness_img = pygame.image.load("Images/Chars/ness.webp")
olimar_img = pygame.image.load("Images/Chars/olimar.webp")
pit_img = pygame.image.load("Images/Chars/pit.webp")
rob_img = pygame.image.load("Images/Chars/rob.webp")
sonic_img = pygame.image.load("Images/Chars/sonic.webp")
wolf_img = pygame.image.load("Images/Chars/wolf.webp")

# Images/Chars Rotated
rot_falco_img = pygame.transform.flip(falco_img, True, False)
rot_game_img = pygame.transform.flip(falco_img, True, False)
rot_ganondorf_img = pygame.transform.flip(falco_img, True, False)
rot_mario_img = pygame.transform.flip(falco_img, True, False)
rot_metaknight_img = pygame.transform.flip(falco_img, True, False)
rot_ness_img = pygame.transform.flip(falco_img, True, False)
rot_olimar_img = pygame.transform.flip(falco_img, True, False)
rot_pit_img = pygame.transform.flip(falco_img, True, False)
rot_rob_img = pygame.transform.flip(falco_img, True, False)
rot_sonic_img = pygame.transform.flip(falco_img, True, False)
rot_wolf_img = pygame.transform.flip(falco_img, True, False)

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
          print(self.text)
          self.text = ''
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


  # screen.blit(falco_img, (200,300))
  # Image side chars are 200 on 300
  # screen.blit(rot_falco_img, (880,300))
  # Rotated side chars are 800 on 300

  pygame.display.update()


  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
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
  pygame.quit()