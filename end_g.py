from Func import *


def records(time):
    al = []
    tiles = [100, 50, 40, 20]
    screen = pygame.display.set_mode(display)
    pygame.display.set_caption('Results')
    if stats('sound') == 'On':
        end.play(0)
    men = Button(10, 560, skin('v_men'), 0.2)
    save = Button(640, 540, skin('save'), 0.3)
    font = pygame.font.SysFont('Comic Sans MS', 40)
    font1 = pygame.font.SysFont('Comic Sans MS', 34)
    al.append(int(time))
    time1 = font.render(str(time), True, (255, 255, 0))
    ch = 0 if stats('challenge') != 'Darkness' else 1
    al.append(ch + 1)
    chal = font.render(str(ch) + ' / 1', True, (255, 255, 0))
    level = tiles.index(stats('tile'))
    m = '1.' + str(level + 1)
    al.append(float(m))
    mult = font.render(m, True, (255, 255, 0))
    inf = f'{al[0]} * {al[1]} * {al[2]}'
    mon = round(eval(inf), 1)
    inf = inf + ' = ' + str(mon)
    total = str(mon)
    total1 = font.render(total, True, (255, 255, 0))
    tim = stats('time')
    scor = stats('score')
    if int(time) > int(tim[level]):
        tim[level] = str(int(time) + int(read(11)[level]))
        write(11, ' '.join(tim))
    if float(total) > float(scor[level]):
        scor[level] = str(float(total) + float(read(12)[level]))
        write(12, ' '.join(scor))
    write(0, str(round(float(read(0)), 1) + mon))
    run = True
    while run:
        menu_bg = pygame.image.load('data/last.png')
        screen.blit(menu_bg, (0, 0))
        screen.blit(time1, (405, 162))
        screen.blit(chal, (430, 205))
        screen.blit(mult, (480, 250))
        screen.blit(font1.render(inf, True, (255, 255, 0)), (215, 320))
        screen.blit(total1, (490, 500))
        if save.pressed(screen):
            if stats('sound') == 'On':
                button.play(0)
            rect = pygame.Rect(0, 0, 800, 600)
            sub = screen.subsurface(rect)
            n = read(10)
            pygame.image.save(sub, f"screenshots/My_record_{n}.png")
            write(10, str(int(n) + 1))
        if men.pressed(screen):
            if stats('sound') == 'On':
                button.play(0)
            return 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
        pygame.display.update()