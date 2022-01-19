from Func import *
from Labirint import game_cycle


def levels():
    screen = pygame.display.set_mode(display)
    pygame.display.set_caption('Levels')

    text = 'This level is Locked! Complete previous levels first!'
    text1 = 'This level is New! Click to play!'
    font = pygame.font.SysFont('Comic Sans MS', 30)
    option = font.render('', True, Yellow)

    b1 = skin('b1')
    b2 = skin('b2')
    b3 = skin('b3')
    b4 = skin('b4')
    bl = skin('b_locked')
    exit_b = skin('exit_b')

    one_b = Button(40, 400, b1, 0.4)
    two_b = Button(270, 285, b2, 0.4)
    three_b = Button(445, 425, b3, 0.4)
    final_b = Button(670, 332, b4, 0.4)
    exit_b = Button(10, 530, exit_b, 0.3)
    run = True
    lev = stats('levels')
    for i in range(len(lev)):
        if '2' not in lev:
            three_b = Button(445, 425, bl, 0.4)
            final_b = Button(670, 332, bl, 0.4)
            a = 2
        elif '3' not in lev:
            final_b = Button(670, 332, bl, 0.4)
            a = 3
    level = 'Choose a level'
    while run:
        menu_bg = pygame.image.load('data/lev.png')
        screen.blit(menu_bg, (0, 0))
        screen.blit(font.render(level, True, Yellow), (50, 40))
        screen.blit(option, (50, 80))
        if one_b.rect.collidepoint(pygame.mouse.get_pos()):
            level = 1
            if str(level) not in lev:
                option1 = text
            else:
                option1 = f"Completed! Best time: {stats('time')[level - 1]} Best score: {stats('score')[level - 1]}"
            option = font.render(option1, True, Yellow)
            level = 'Level 1'
        elif two_b.rect.collidepoint(pygame.mouse.get_pos()):
            level = 2
            if lev[-1] == '1':
                option1 = text1
            elif '2' not in lev:
                option1 = text
            else:
                option1 = f"Completed! Best time: {stats('time')[level - 1]} Best score: {stats('score')[level - 1]}"
            option = font.render(option1, True, Yellow)
            level = 'Level 2'
        elif three_b.rect.collidepoint(pygame.mouse.get_pos()):
            level = 3
            if lev[-1] == '2':
                option1 = text1
            elif '3' not in lev:
                option1 = text
            else:
                option1 = f"Completed! Best time: {stats('time')[level - 1]} Best score: {stats('score')[level - 1]}"
            option = font.render(option1, True, Yellow)
            level = 'Level 3'
        elif final_b.rect.collidepoint(pygame.mouse.get_pos()):
            level = 4
            if lev[-1] == '3':
                option1 = text1
            elif '4' not in lev:
                option1 = text
            else:
                option1 = f"Completed! Best time: {stats('time')[level - 1]} Best score: {stats('score')[level - 1]}"
            option = font.render(option1, True, Yellow)
            level = 'Level 4'
        if one_b.pressed(screen):
            if level[-1] == '1' and option1 != text:
                pygame.mixer.pause()
                if stats('sound') == 'On':
                    button.play(0)
                write(10, '4')
                write(7, '100')
                game_cycle()
        if two_b.pressed(screen):
            if level[-1] == '2' and option1 != text:
                pygame.mixer.pause()
                if stats('sound') == 'On':
                    button.play(0)
                write(10, '3')
                write(7, '50')
                game_cycle()
        if three_b.pressed(screen):
            if level[-1] == '3' and option1 != text:
                pygame.mixer.pause()
                if stats('sound') == 'On':
                    button.play(0)
                write(10, '3')
                write(7, '40')
                game_cycle()
        if final_b.pressed(screen):
            if level[-1] == '4' and option1 != text:
                pygame.mixer.pause()
                if stats('sound') == 'On':
                    button.play(0)
                write(10, '1')
                write(7, '20')
                game_cycle()
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
        pygame.display.update()