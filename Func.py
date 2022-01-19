import pygame

resol = ['800*600', '1366*768']
chall = ['None', 'Darkness']
sou = ['On', 'Off']
Black = (0, 0, 0)
Yellow = (255, 255, 0)
display = [800, 600]
FPS = 60
WIDTH, HEIGHT = display
pygame.init()
button = pygame.mixer.Sound('data/switched.mp3')
end = pygame.mixer.Sound('data/end.mp3')
key_got = pygame.mixer.Sound('data/key_got.mp3')
switch = pygame.mixer.Sound('data/on_key.mp3')
fon = pygame.mixer.Sound("data/fon.mp3")
game_fon = pygame.mixer.Sound("data/game_fon.mp3")
ending = pygame.mixer.Sound("data/ending.mp3")


class Button:
    def __init__(self, x, y, image, scale):
        self.x = image.get_width()
        self.y = image.get_height()
        self.image1 = image
        self.scale = scale
        self.hider = pygame.image.load('data/hider.png').convert_alpha()
        self.image = pygame.transform.scale(image, (int(self.x * self.scale), int(self.y * self.scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.clickable = True

    def __call__(self, *args):
        self.__init__(*args)

    def pressed(self, surface):
        if self.clickable:
            pressed = False
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                    self.clicked = True
            if pygame.mouse.get_pressed()[0] == 0 and self.clicked:
                self.clicked = False
                pressed = True
            surface.blit(self.image, (self.rect.x, self.rect.y))
            return pressed

    def hide(self):
        self.image = pygame.transform.scale(self.hider, (int(self.x * self.scale), int(self.x * self.scale)))
        self.clickable = False

    def show(self):
        if not self.clickable:
            self.image = pygame.transform.scale(self.image, (int(self.x * self.scale), int(self.x * self.scale)))
            self.clickable = True


def read(num=-1):
    with open("stats.txt", mode="r") as f:
        data = f.readlines()
        if num == -1:
            return len(data)
        return data[num].strip('\n')


def write(num, string):
    data = []
    ra = read()
    for i in range(ra):
        data.append(read(i))
    with open("stats.txt", mode="w") as f:
        for i in range(ra):
            print(string, file=f) if i == num else print(data[i], file=f)


def stats(arg):
    values = {'money': read(0), 'levels': read(1).split(), 'skins': read(2).split(), 'song': read(3),
              'challenge': read(4), 'skin': read(5), 'sound': read(6), 'tile': int(read(7)), 'mission': read(8),
              'player': read(9), 'thick': int(read(10)), 'time': read(11).split(), 'score': read(12).split()}
    return values[arg]


sk = ['blue', 'green', 'fiol']
WALL_THICK = stats('thick')


def other(arg, orig):
    return arg[0] if arg[-1] == orig else arg[1]


def ranged(vals, name, num1):
    num = vals.index(name)
    return vals[num + num1 - len(vals)] if num + num1 > len(vals) else vals[num + num1 - 1]


def skin(name, scale=1, conv=True):
    if conv:
        skin = pygame.image.load(f'data/{name}.png').convert_alpha()
    else:
        return pygame.image.load(f'data/{name}.png')
    if scale != 1:
        x = skin.get_width()
        y = skin.get_height()
        return pygame.transform.scale(skin, (scale, scale))
    return pygame.image.load(f'data/{name}.png').convert_alpha()


def time(time):
    return time - 1


def info(pos1):
    skins = ['blue', '500', 'green', '0', 'fiol', '200']
    if pos1[-4:] == 'cost':
        return skins[skins.index(pos1[:-4]) + 1]
    num = skins.index(pos1[1].replace('_f', ''))
    skin1 = skins[num]
    cost = skins[num + 1]
    if skin1 == stats('skin'):
        return 0
    elif skin1 in stats('skins'):
        return 1
    return 2 if float(stats('money')) >= int(cost) else 3


def move(vals, num):
    while num > len(vals):
        num -= len(vals)
    return vals[num:] + vals[:num]


def buy_b(a, choosed, choose, buy, notm):
    if a == 0:
        return Button(285, 450, choosed, 0.4)
    elif a == 1:
        return Button(285, 450, choose, 0.4)
    elif a == 2:
        return Button(285, 450, buy, 0.4)
    else:
        return Button(285, 450, notm, 0.4)