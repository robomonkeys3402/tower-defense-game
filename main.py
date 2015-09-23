#!/bin/env python2

# TODO: grid based map system

import pygame
from pygame.locals import QUIT, KEYDOWN, MOUSEBUTTONDOWN, K_q
from ui.button import ImageButton, TextButton
#from ui.menus import Menu
from ui.enums import RESOURCES


def test():
    print('okay')


def start_game():
    print('game started')


def open_options():
    print('options opened')


def quit_game():
    global running
    running = False

pygame.init()

screen = pygame.display.set_mode((640, 480))
bg = pygame.image.load(RESOURCES + 'white_bg.png').convert()
monkey = pygame.image.load(RESOURCES + 'monkey.png').convert_alpha()

running = True

screen.blit(bg, (0, 0))
screen.blit(monkey, (300, 300))
pygame.display.update()

buttons = [ImageButton(RESOURCES + 'ok_button.png', (300, 200), test),
           TextButton("Start", (300, 100), (0, 0, 0), callback=test)]

for btn in buttons:
    btn.draw(screen)

#mn1 = Menu(("New Title", (300, 200)),
#           ("Start", "Options", "Quit"),
#           ((310, 300),
#            (310, 340),
#            (310, 380)),
#           (start_game, open_options, quit_game))

#mn1.draw(screen)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN and event.key == K_q:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
#            mn1.handle_clicks()
            for btn in buttons:
                btn.click()
    pygame.display.update()

pygame.quit()
