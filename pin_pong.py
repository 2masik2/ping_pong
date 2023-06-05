#импортируем из библиотеки pygame
from pygame import *

#создание главного окна
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('пинг-понг')
background = transform.scale(image.load('фон.webp'), (win_width,win_height))

font.init()
font1 = font.SysFont('Arial', 80)

lose_l = font1.render('LOSE LEFT!', True, (180, 0, 0))
lose_r = font1.render('LOSE RIGHT!', True, (180, 0, 0))
 
font2 = font.SysFont('Arial', 36)

game = True
finish = False
clock = time.Clock()
FPS = 60
move_ballx = 3
move_bally = 3

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
    def update_one(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 100:
            self.rect.y += self.speed 

    def update_two(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - 100:
            self.rect.y += self.speed

#класс мяча
# class Ball(GameSprite):
#     def update(self):
#         self.rect.y += self.speed
#         self.rect.x += self.speed



racket = Racket('ракетка.jpg', 20, win_height - 100, 50, 100, 10)
racket2 = Racket('ракетка.jpg', 630, win_height - 100, 50, 100, 10)
ball = Racket('ball_1.png', 100, 100, 40, 40, None)


while game:
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:

        racket.update_two()
        racket.reset()
        racket2.update_one()
        racket2.reset()
        ball.reset()
        
        ball.rect.x += move_ballx
        ball.rect.y += move_bally

        # if ball.rect.y < 0:
        #     move_bally *=-1

        if ball.rect.colliderect(racket.rect) or ball.rect.colliderect(racket2.rect):
            move_ballx *=-1

        if ball.rect.y > 450 or ball.rect.y < 0:
            move_bally *=-1

        if ball.rect.x < 10:
            finish = True
            window.blit(lose_l, (170, 100))

        if ball.rect.x > 690:
            finish = True
            window.blit(lose_r, (170, 100))
        
    
    

        display.update()
    clock.tick(FPS)
