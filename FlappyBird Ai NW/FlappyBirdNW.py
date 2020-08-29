import pygame as pg
import random
from pygame import *

pg.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
windowheight = 500
windowwidth = 400
FPS = 30
BackGround = (0, 0, 0)

screen = pg.display.set_mode((windowheight, windowwidth))
background = pg.Surface(screen.get_size())
pg.display.set_caption("FlappyBird")


class Bird:
    def __init__(self, x, y):
        self.x = 150
        self.y = 200
        self.r = 10
        self.VEL = 10
        self.Jump = 30
        self.isJump = False

    def jump(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            self.isJump = True
            self.y -= self.Jump
        self.isJump = False

    def move(self):
        if self.y > windowwidth - 10:
            self.VEL = 0

        if self.y < 30:
            self.Jump = 0

        else:
            self.Jump = 30
        self.y += self.VEL

    def draw_bird(self):
        pg.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.r)


class Pipe:

    def __init__(self):
        self.x = windowwidth
        self.y = 0
        self.width = 50
        self.height = 100
        self.vel = 10
        self.gap = 200

    def move(self):
        self.x -= self.vel

    def draw(self):
        pg.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))
        # pg.draw.rect(screen, WHITE, (self.x, (windowwidth - self.width), self.width, self.height))


def create_Pipes():
    pass


def run():
    bird = Bird(0, 0)
    runing = True
    while runing:
        pg.time.delay(100)
        for event in pg.event.get():
            if event.type == QUIT:
                runing = False
                pg.quit()
                exit()

        bird.draw_bird()
        bird.move()
        bird.jump()
        pg.display.update()
        screen.fill(BackGround)

run()
