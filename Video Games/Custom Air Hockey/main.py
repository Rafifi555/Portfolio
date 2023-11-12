#Rafi Hossain
#ICS3U1
#Game

import pygame
from pygame import mixer
import button
import random

# pygame screen
pygame.init()
main_menu = True
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# positions
x = 500
y = 200
x2 = 500
y2 = 800
puckx = 460
pucky = 460

# Countdown
countdown = 3
last_count = pygame.time.get_ticks()
game_over = 0

# speed of player
vel = 100

# Game title and Background Image
pygame.display.set_caption("PIXEL AIR HOCKEY INTERNATIONAL DELUXE")
back = pygame.image.load('Air-Hockey-Review.jpg')
title = pygame.image.load('AIR-HOCKEY-MANIA (1).png')
back1 = pygame.image.load('map.png')
wasd = pygame.image.load(
    'computer-gamer-keyboard-wasd-keys-wasd-keys-game-control-keyboard-buttons-gaming-cybersport-symbol-vector-eps-10-isolated-white-background_399089-2574.png')
arrows = pygame.image.load('arrows1.png')

player = pygame.image.load('swedenplayer.png')
player_rect = player.get_rect()
player_rect.center = (x, y)

cpuplayer = pygame.image.load('canada.png')
opponent_rect = cpuplayer.get_rect()
opponent_rect.center = (x2, y2)

hockey_puck = pygame.Rect(puckx, pucky, 70, 70)

# point system
player_score = 0
opponent_score = 0

# speed of puck
puck_speed_x = 7
puck_speed_y = 7

# Button Image
play_button = pygame.image.load('start1.png').convert_alpha()
exit_button = pygame.image.load('exit1.png').convert_alpha()
rules_button = pygame.image.load('hello.png').convert_alpha()
back_button = pygame.image.load('backbutton.png').convert_alpha()

# background music
mixer.music.load('072 - Slushii - All I Need-[AudioTrimmer.com].mp3')
mixer.music.play(-1)
mixer.music.set_volume(0.05)

# Font and the color
font = pygame.font.SysFont("gogo poster punch bold", 60)
font1 = pygame.font.SysFont("TechnoRaceItalic-eZRWe.otf", 60)
font2 = pygame.font.SysFont("Oswald", 40)
font40 = pygame.font.SysFont('FUTURA', 40)
game_font = pygame.font.SysFont('FUTURA', 100)
font_color = (0, 0, 128)
font_color2 = (255, 255, 255)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)


# button class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        SCREEN.blit(self.image, (self.rect.x, self.rect.y))

        return action

        # return action


hockey_puck.x += puck_speed_x
hockey_puck.y += puck_speed_y


def puck_restart():
    global puck_speed_x, puck_speed_y
    hockey_puck.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    puck_speed_y *= random.choice((1, -1))
    puck_speed_x *= random.choice((1, -1))


# def puck_restart():
# global puck_speed_x, puck_speed_y, score_time

# current_time = pygame.time.get_ticks()
# hockey_puck.center = (500, 500)

# if current_time - score_time < 2100:
# puck_speed_x, puck_speed_y
# else:
# puck_speed_y *= random.choice((1, -1))
# puck_speed_x *= random.choice((1, -1))
# score_time = None


# button instances
start_button = Button(100, 900, play_button, 0.45)
end_button = Button(710, 890, exit_button, 0.5)
rule_button = Button(410, 895, rules_button, 0.5)
bak_button = Button(150, 850, back_button, 0.5)


# define function for creating text
def draw_text(text, font, text_col, x, y):
    img2 = font.render(text, True, text_col)
    SCREEN.blit(img2, (x, y))


def text_1(text, font, tex_col, x, y):
    img = font.render(text, True, font_color)
    SCREEN.blit(img, (x, y))


def text_2(text, font1, tex_col, x, y):
    img3 = font.render(text, True, font_color2)
    SCREEN.blit(img3, (x, y))


# Game

main_menu = "main"
while True:
    if main_menu == "main":
        SCREEN.blit(back, (0, 0))
        SCREEN.blit(title, (150, 310))
        text_1("2 PLAYERS REQUIRED", font1, font_color2, 300, 600)
        if start_button.draw():
            main_menu = False
            mixer.music.load('hockey-organ-melody-in-stadium-arena-SBA-300117431-preview-[AudioTrimmer.com].mp3')
            mixer.music.play(-1)
        if rule_button.draw():
            main_menu = "rules"
            pygame.display.set_caption("Rules")
            pygame.display.update()
        if end_button.draw():
            quit()
    elif main_menu == "Winner":
        SCREEN.fill(255, 255, 255)
    elif main_menu == "rules":
        SCREEN.fill(black)
        text_2("THIS ISN'T REGULAR AIR HOCKEY...", font2, white, 100, 100)
        text_2("THE PUCK HAS ITS MIND OF ITS OWN", font2, red, 100, 250)
        text_2("SWEDEN(player 1) VS CANADA(player 2)", font2, white, 100, 420)
        text_2("CONTROLS ARE SHOWN IN GAME", font2, white, 100, 600)
        text_2("BESIDE PUCK SPAWN", font2, white, 250, 650)
        text_2("HAVE FUN!!", font2, white, 350, 750)
        if bak_button.draw():
            main_menu = "main"




    else:
        keys = pygame.key.get_pressed()
        SCREEN.blit(back1, (0, 0))
        SCREEN.blit(player, player_rect)
        SCREEN.blit(cpuplayer, opponent_rect)
        pygame.draw.ellipse(SCREEN, black, hockey_puck)
        player_text = game_font.render(f"{player_score}", False, black)
        opponent_text = game_font.render(f"{opponent_score}", False, black)
        SCREEN.blit(player_text, (140, 25))
        SCREEN.blit(opponent_text, (820, 900))
        if countdown == 0:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        player_rect.x -= vel
                        if player_rect.x <= 5:
                            player_rect.x = 5
                    if event.key == pygame.K_d:
                        player_rect.x += vel
                        if player_rect.x > 750:
                            player_rect.x = 750
                    if event.key == pygame.K_s:
                        player_rect.y += vel
                        if player_rect.y >= 750:
                            player_rect.y = 750
                    if event.key == pygame.K_w:
                        player_rect.y -= vel
                        if player_rect.y <= 5:
                            player_rect.y = 5
                    if event.key == pygame.K_LEFT:
                        opponent_rect.x -= vel
                        if opponent_rect.x <= 5:
                            opponent_rect.x = 5
                    if event.key == pygame.K_RIGHT:
                        opponent_rect.x += vel
                        if opponent_rect.x > 750:
                            opponent_rect.x = 750
                    if event.key == pygame.K_DOWN:
                        opponent_rect.y += vel
                        if opponent_rect.y >= 750:
                            opponent_rect.y = 750
                    if event.key == pygame.K_UP:
                        opponent_rect.y -= vel
                        if opponent_rect.y <= 5:
                            opponent_rect.y = 5
            hockey_puck.x += puck_speed_x
            hockey_puck.y += puck_speed_y

            if hockey_puck.left <= 100 or hockey_puck.right >= 1000:
                puck_speed_x *= -1
                mixer.music.load('Goal-horn-sound-effect.mp3')
                mixer.music.play()
                player_score += 1
            if hockey_puck.top <= 50 or hockey_puck.bottom >= 1000:
                puck_restart()
                mixer.music.load('Goal-horn-sound-effect.mp3')
                mixer.music.play()
                opponent_score += 1

            collision_tolerance = 50
            if hockey_puck.colliderect(player_rect):
                if abs(hockey_puck.top - player_rect.bottom) < collision_tolerance:
                    puck_speed_y *= -1
                if abs(hockey_puck.bottom - player_rect.top) < collision_tolerance:
                    puck_speed_y *= -1
                if abs(hockey_puck.right - player_rect.left) < collision_tolerance:
                    puck_speed_x *= -1
                if abs(hockey_puck.left - player_rect.right) < collision_tolerance:
                    puck_speed_x *= -1
            if hockey_puck.colliderect(opponent_rect):
                if abs(hockey_puck.top - opponent_rect.bottom) < collision_tolerance:
                    puck_speed_y *= -1
                if abs(hockey_puck.bottom - opponent_rect.top) < collision_tolerance:
                    puck_speed_y *= -1
                if abs(hockey_puck.right - opponent_rect.left) < collision_tolerance:
                    puck_speed_x *= -1
                if abs(hockey_puck.left - opponent_rect.right) < collision_tolerance:
                    puck_speed_x *= -1

        if countdown > 0:
            draw_text('STARTS IN!', font40, black, int(SCREEN_WIDTH / 2 - 90), int(SCREEN_HEIGHT / 2 + 50))
            draw_text(str(countdown), font40, black, int(SCREEN_WIDTH / 2 - 15), int(SCREEN_HEIGHT / 2 + 100))
            SCREEN.blit(wasd, (50, 200))
            SCREEN.blit(arrows, (50, 700))
            count_timer = pygame.time.get_ticks()
            if count_timer - last_count > 1000:
                countdown -= 1
                last_count = count_timer

        if player_score == 7:
            main_menu = "main"
            mixer.music.load('Record (online-voice-recorder.com).mp3')
            mixer.music.play()
            mixer.music.set_volume(1)

        if opponent_score == 7:
            main_menu = "main"
            mixer.music.load('Record (online-voice-recorder.com) (1).mp3')
            mixer.music.play()
            mixer.music.set_volume(1)


    # Exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
