from pygame import *
window display.set_mode((700, 500))
display.set_caption("Ping-Pong")
window.fill((150, 150, 180))
class Gamesprite(sprite.Sprite):
  def __init_(self, filename, x, y, speed, width, height):
    super().__init__()
    self.image = transform.scale(image.load(filename), (width, height))
    self.speed = speed 
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
  def reset(self):
    window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
  def update(self):
  keys_pressed = key.get.pressed()
  if keys_pressed[K_UP] and self.rect.y > 0:
    self.rect.y -= self.speed
  if keys pressed[K_DOWN] and self.rect.y < 500-100:
    self.rect.y += self.speed

while run:
  if finish == False:


    pass
  for i in event.get(): 
    if i.type QUIT:
      run = False
display.update()
clock.tick(FPS)
