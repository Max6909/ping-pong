from pygame import *

WIDTH = 900
HEIGHT = 900
FPS = 120
game = True

class GameSprite(sprite.Sprite):
    def __init__(self, image_, width, height, x, y):
        self.image = transform.scale(image.load(image_), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

timer = time.Clock()

win = display.set_mode((WIDTH, HEIGHT))
display.set_caption('ping-pong')

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    win.fill((255, 255, 255))

    display.update()
    timer.tick(FPS)