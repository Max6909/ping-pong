from pygame import *

WIDTH = 900
HEIGHT = 900
FPS = 120
game = True

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