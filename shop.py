from Func import *


def rotating(vals):
    screen = pygame.display.set_mode(display)
    im = vals[1]
    lst = ['_f', '_r', '_b', '_l']
    lst_s = [im + lst[i] for i in range(4)]
    im = lst_s[0]
    lt = Button(280, 100, skin('r_sk'), 2.7)
    rt = Button(401, 100, skin('r_sk'), 2.7)
    main = Button(280, 100, skin(im), 2.7)
    l = skin('b_l', 0.4)
    r = skin('b_r', 0.4)
    font = pygame.font.SysFont('Comic Sans MS', 40)
    font_s = pygame.font.SysFont('Comic Sans MS', 18)
    t = im[:-2] if im != 'fiol_f' else 'purple'
    f = 'fiol' if t == 'purple' else t
    if t == 'green':
        t1 = 'Original skin'
    elif t == 'blue':
        t1 = 'Heavenly sky skin'
    else:
        t1 = 'Aerospace skin'
    name = font.render(t.capitalize() + ' elf warrior', True, pygame.Color(t))
    text = font_s.render('Legendary Fearless Warrior', True, pygame.Color(t))
    text1 = font_s.render(t1, True, pygame.Color(t))
    c = info(f + 'cost') + '$'
    if c == '0$':
        c = 'Basic'
    cost = font.render(c, True, pygame.Color('yellow'))
    run = True
    menu_bg = skin('rotate')
    lst_s = move(lst_s, -1)
    while run:
        if pygame.mouse.get_pressed()[0] == 1 and not (lt.rect.collidepoint(pygame.mouse.get_pos())
                                                       or rt.rect.collidepoint(pygame.mouse.get_pos())):
            pygame.time.delay(120)
            run = False
        screen.blit(menu_bg, (0, 0))
        screen.blit(name, (235, 10))
        screen.blit(text, (540, 210))
        screen.blit(text1, (590, 240))
        screen.blit(cost, (356, 530))
        if lt.rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(l, (220, 410))
        if rt.rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(r, (500, 410))
        if lt.pressed(screen):
            lst_s = move(lst_s, -1)
            main = Button(280, 100, skin(lst_s[1]), 2.7)
        if rt.pressed(screen):
            lst_s = move(lst_s, 1)
            main = Button(280, 100, skin(lst_s[1]), 2.7)
        if main.pressed(screen):
            pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
        pygame.display.update()


def magaz():
    screen = pygame.display.set_mode(display)
    pygame.display.set_caption('Shop')

    shop_r = skin('b_r')
    shop_l = skin('b_l')
    choosed = skin('b_choosed')
    choose = skin('b_choose')
    notm = skin('b_notm')
    buy = skin('b_buy')
    b_exit = skin('exit_b')

    shopr_b = Button(550, 460, shop_r, 0.3)
    shopl_b = Button(200, 460, shop_l, 0.3)
    choosed_b = Button(285, 450, choosed, 0.4)
    font = pygame.font.SysFont('Comic Sans MS', 36)
    coins = font.render(stats('money') + '$', True, Yellow)
    inf = font.render('Tap for Info', True, pygame.Color('gray33'))
    pos = [ranged(sk, stats('skin'), 0), stats('skin'), ranged(sk, stats('skin'), -1)]
    left, mid, righ = skin(pos[0] + '_f'), skin(pos[1] + '_f'), skin(pos[2] + '_f')
    s_left = Button(85, 110, left, 2)
    s_middle = Button(280, 100, mid, 2.7)
    s_right = Button(535, 110, righ, 2)
    exit_b = Button(10, 530, b_exit, 0.3)
    a = 0
    run = True
    while run:
        menu_bg = skin('shop1')
        screen.blit(menu_bg, (0, 0))
        screen.blit(coins, (22, 5))
        if s_middle.rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(inf, (290, 30))
        if shopr_b.pressed(screen):
            if stats('sound') == 'On':
                button.play(0)
            left, mid, righ = mid, righ, left
            s_left = Button(85, 110, left, 2)
            s_middle = Button(280, 100, mid, 2.7)
            s_right = Button(535, 110, righ, 2)
            pos = move(pos, 1)
            a = info(pos)
            choosed_b = buy_b(a, choosed, choose, buy, notm)
        if shopl_b.pressed(screen):
            if stats('sound') == 'On':
                button.play(0)
            left, mid, righ = righ, left, mid
            s_left = Button(85, 110, left, 2)
            s_middle = Button(280, 100, mid, 2.7)
            s_right = Button(535, 110, righ, 2)
            pos = move(pos, -1)
            a = info(pos)
            choosed_b = buy_b(a, choosed, choose, buy, notm)
        if choosed_b.pressed(screen):
            if a == 1:
                if stats('sound') == 'On':
                    button.play(0)
                write(5, pos[1])
                a = 0
                choosed_b = buy_b(a, choosed, choose, buy, notm)
            elif a == 2:
                if stats('sound') == 'On':
                    button.play(0)
                write(0, float(stats('money')) - float(info(pos[1] + 'cost')))
                write(2, ' '.join(stats('skins')) + ' ' + pos[1])
                a = 1
                choosed_b = buy_b(a, choosed, choose, buy, notm)
        if s_left.pressed(screen):
            if stats('sound') == 'On':
                button.play(0)
            left, mid, righ = righ, left, mid
            s_left = Button(85, 110, left, 2)
            s_middle = Button(280, 100, mid, 2.7)
            s_right = Button(535, 110, righ, 2)
            pos = move(pos, -1)
            a = info(pos)
            choosed_b = buy_b(a, choosed, choose, buy, notm)
        if s_middle.pressed(screen):
            if stats('sound') == 'On':
                button.play(0)
            rotating(pos)
        if s_right.pressed(screen):
            if stats('sound') == 'On':
                button.play(0)
            left, mid, righ = mid, righ, left
            s_left = Button(85, 110, left, 2)
            s_middle = Button(280, 100, mid, 2.7)
            s_right = Button(535, 110, righ, 2)
            pos = move(pos, 1)
            a = info(pos)
            choosed_b = buy_b(a, choosed, choose, buy, notm)
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
        pygame.display.update()
