from Func import *
from pygame.locals import *
from time import time


def settings():

    screen = pygame.display.set_mode(display)
    pygame.display.set_caption('Settings')

    diff_r = skin('b_r')
    diff_l = skin('b_l')
    sound_off = skin('b_no')
    sound_on = skin('b_yes')
    song_off = skin('b_no')
    song_on = skin('b_yes')
    exit_b = skin('exit_b')
    change_b = skin('b_ch')

    difr_b = Button(615, 290, diff_r, 0.15)
    difl_b = Button(457, 290, diff_l, 0.15)
    if read(6) == 'Off':
        sound_b = Button(370, 340, sound_off, 0.4)
    else:
        sound_b = Button(370, 340, sound_on, 0.4)
    if read(3) == 'Off':
        bg_b = Button(405, 230, song_off, 0.4)
    else:
        bg_b = Button(405, 230, song_on, 0.4)
    exit_b = Button(10, 530, exit_b, 0.3)
    ch_b = Button(615, 125, change_b, 0.1)
    font = pygame.font.SysFont('Comic Sans MS', 36)
    font1 = pygame.font.SysFont('Comic Sans MS', 30)
    name = font.render(stats('player'), True, Yellow)
    coins = font.render(str(round(float(stats('money')), 1)), True, Yellow)
    chal = stats('challenge')
    if chal == 'None':
        chal = '   ' + chal
    challenge = font1.render(chal, True, Yellow)

    rect = name.get_rect()
    rect.topleft = (405, 110)
    cursor = Rect(rect.topright, (3, rect.height))

    run = True
    pr = False
    text = str(stats('player'))

    while run:
        menu_bg = pygame.image.load('data/set.png')
        screen.blit(menu_bg, (0, 0))
        screen.blit(name, (405, 110))
        screen.blit(coins, (420, 170))
        screen.blit(challenge, (488, 285))
        if pr:
            screen.blit(cancel, (10, 10))
            if time() % 1 > 0.5:
                pygame.draw.rect(screen, (255, 255, 0), cursor)
        if pygame.mouse.get_pressed()[0] == 1 and pr and not ch_b.rect.collidepoint(pygame.mouse.get_pos()):
            if stats('sound') == 'On':
                button.play(0)
            pr = False
            ch_b = Button(615, 125, change_b, 0.1)
            text = stats('player')
            name = font.render(text, True, Yellow)
            rect.size = name.get_size()
            cursor.topleft = rect.topright
        if bg_b.pressed(screen):
            if stats('sound') == 'On':
                button.play(0)
            song = True if stats('song') == 'On' else False
            if not song:
                bg_b = Button(405, 230, song_on, 0.4)
                pygame.mixer.pause()
                pygame.mixer.Sound.play(fon)
            else:
                bg_b = Button(405, 230, song_off, 0.4)
                pygame.mixer.stop()
            song = not song
            change = other(sou, stats('song'))
            write(3, change)
        if difr_b.pressed(screen) or difl_b.pressed(screen):
            if stats('sound') == 'On':
                button.play(0)
            change = other(chall, stats('challenge'))
            if change == 'None':
                change = '   ' + change
            challenge = font1.render(change, True, Yellow)
            write(4, change)
        if ch_b.pressed(screen):
            if stats('sound') == 'On':
                button.play(0)
            if pr:
                ch_b = Button(615, 125, change_b, 0.1)
                pr = False
                write(9, text)
                rect.size = name.get_size()
                cursor.topleft = rect.topright
            else:
                ch_b = Button(615, 125, sound_on, 0.3)
                pr = True
                cancel = font1.render('Нажмите куда угодно для отмены', True, (255, 0, 0))
        if sound_b.pressed(screen):
            sound = True if stats('sound') == 'On' else False
            if not sound:
                sound_b = Button(370, 340, sound_on, 0.4)
            else:
                if stats('sound') == 'On':
                    button.play(0)
                sound_b = Button(370, 340, sound_off, 0.4)
            sound = not sound
            change = other(sou, stats('sound'))
            write(6, change)
        if exit_b.pressed(screen):
            if stats('sound') == 'On':
                button.play(0)
            run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            if pr:
                if event.type == pygame.KEYDOWN:
                    if stats('sound') == 'On':
                        switch.play(0)
                    if event.key == pygame.K_BACKSPACE:
                        if len(text) > 0:
                            text = text[:-1]
                            name = font.render(text, True, Yellow)
                    else:
                        if len(text) < 10:
                            text += event.unicode
                            name = font.render(text, True, Yellow)
                rect.size = name.get_size()
                cursor.topleft = rect.topright
        pygame.display.update()