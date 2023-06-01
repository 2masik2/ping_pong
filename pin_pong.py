#импортируем из библиотеки pygame
from pygame import *

#создание главного окна
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('пинг-понг')
background = transform.scale(image.load('картинка фона(найти)'), (win_width,win_height))

game = True
finish = False
clock = time.Clock()
FPS = 60

#создание классов 
class GameSprite(sprite.Sprite):
    def __init__ (self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#класс ракетки
class Racket(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed 

#класс мяча
class Ball(GameSprite):
    def update(self):
        self.rect.y += self.speed

racket = Racket('картинка ракетки(найти)', ...)

while not finish:
    ball.fill()
    racket.fill()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_down = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_up = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_up = False

    if move_down:
        platform.rect.y += 3

    if move_up:
        platform.rect.y -= 3

    ball.rect.x += move_ballx
    ball.rect.y += move_bally