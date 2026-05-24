from pygame import *

WIDTH = 900
HEIGHT = 900
FPS = 60
game = True

class GameSprite(sprite.Sprite):
    def __init__(self, image_, width, height, x, y):
        super().__init__()
        self.image = transform.scale(image.load(image_), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))


class Platform(GameSprite):
    def __init__(self, image_, width, height, x, y, speed, key_up, key_down):
        super().__init__(image_, width, height, x, y)
        self.speed = speed
        self.key_up = key_up
        self.key_down = key_down

    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[self.key_up] and self.rect.y >= 20:
            self.rect.y -= self.speed
        if key_pressed[self.key_down] and self.rect.y <= HEIGHT - self.rect.height - 20:
            self.rect.y += self.speed


class Ball(GameSprite):
    def __init__(self, image_, width, height, x, y, speed):
        super().__init__(image_, width, height, x, y)
        self.speed_x = speed
        self.speed_y = speed

    def update(self):
        if self.rect.y <= 20:
            self.speed_y *= -1
        if self.rect.y >= HEIGHT - self.rect.height - 20:
            self.speed_y *= -1
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

player_1 = Platform('racket.png', 50, 200, 50, 350, 7, K_w, K_s)
player_2 = Platform('racket.png', 50, 200, WIDTH - 50 - 50, 350, 7, K_UP, K_DOWN)
ball = Ball('tenis_ball.png', 100, 100, 400, 400, 3)

players = sprite.Group()
players.add(player_1)
players.add(player_2)

timer = time.Clock()

win = display.set_mode((WIDTH, HEIGHT))
display.set_caption('ping-pong')

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    win.fill((255, 255, 255))

    players.draw(win)
    players.update()
    ball.reset()
    ball.update()


    display.update()
    timer.tick(FPS)