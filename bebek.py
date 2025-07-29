import pgzero
import random

WIDTH = 700
HEIGHT = 355
TITLE = "Bebeğin koşusu"
FPS = 30

# Aktörlerin tanımlanması
bebek = Actor('bebek', (50, 240))
egilmek = Actor('egilmek', (50, 240))
sag = Actor('sag', (50, 240))
sol = Actor('sol', (50, 240))
yarali = Actor('yarali',(50,240))
yurumek = Actor('yurumek', (50, 240))
ziplamak = Actor('ziplamak', (50, 240))
arkaplan1 = Actor('arkaplan')
ob = Actor('oyun bitti')
oje = Actor('oje',(550,265))
allik = Actor('allik', (550, 265))
ruj = Actor('ruj', (550, 265))
toka = Actor('toka', (550, 265))
etek = Actor('etek', (550, 265))
firca = Actor('firca', (550, 265))
ayakkabi = Actor('ayakkabi', (550, 265))
duzlestirici = Actor('duzlestirici', (550, 265))
parfum = Actor('parfum', (550, 265))
giris_ekrani = Actor("baslangic")
oyna = Actor("basla" ,(320,160))
carpi = Actor("carpi", (660, 20))
background = Actor('background',(320,245))
arkaplan2 = Actor('arkaplan2')
arkaplan3 = Actor('arkaplan3')
arkaplan4 = Actor('arkaplan4')
baslangic = Actor('baslangic')
yeni_resim = 'bebek'
arkaplanbutton = Actor('arkaplanbutton',(150,100))
arkaplan2button = Actor('arkaplan2button',(500,100))
arkaplan3button = Actor('arkaplan3button',(150,280))
arkaplan4button = Actor('arkaplan4button',(500,280))
engel_turleri = ['oje', 'etek', 'ruj', 'toka', 'firca', 'ayakkabi', 'duzlestirici', 'parfum', 'allik']
engel = Actor(random.choice(engel_turleri), (550, 265))

# Oyun değişkenleri
mod = 'menü'
puan = 0
hiz = 5
can = 5

def oyun_baslat():
    global puan, hiz, can, mod, engel, bebek, yeni_resim
    puan = 0
    hiz = 5
    can = 5
    bebek.pos = (50, 240)
    engel.pos = (550, 265)
    engel.image = random.choice(engel_turleri)
    bebek.image = 'bebek'
    yeni_resim = 'bebek'
    mod = 'oyun'

def draw():
    screen.clear()
    if mod == 'menü':
        baslangic.draw()
        background.draw()
        oyna.draw()
        carpi.draw()
    elif mod == 'oyun':
        arkaplan1.draw()
        bebek.draw()
        engel.draw()
        screen.draw.text(f"Puan: {puan}", pos=(10, 10), color="black", fontsize=25)
        screen.draw.text(f"Can: {can}", pos=(10, 40), color="black", fontsize=25)


    elif mod == 'bitti':
        ob.draw()

    elif mod == 'background':

        arkaplanbutton.draw()
        arkaplan2button.draw()
        arkaplan3button.draw()
        arkaplan4button.draw()
        carpi.draw()

def update(dt):
    global yeni_resim, hiz, can, puan, mod

    if mod != 'oyun':
        return

    if engel.x > -20:
        engel.x -= hiz
    else:
        engel.x = WIDTH + 20
        engel.image = random.choice(engel_turleri)
        engel.y = random.randint(75, 200)
        puan += 1

    if (keyboard.left or keyboard.a) and bebek.x > 20:
        bebek.x -= 5
        if yeni_resim != 'sol':
            bebek.image = 'sol'
            yeni_resim = 'sol'
    elif (keyboard.right or keyboard.d) and bebek.x < WIDTH - 20:
        bebek.x += 5
        if yeni_resim != 'sag':
            bebek.image = 'sag'
            yeni_resim = 'sag'
    elif keyboard.down or keyboard.s:
        if yeni_resim != 'egilmek':
            bebek.image = 'egilmek'
            yeni_resim = 'egilmek'
            bebek.y = 320
    else:
        if bebek.y > 240 and yeni_resim == 'egilmek':
            bebek.image = 'bebek'
            yeni_resim = 'bebek'
            bebek.y = 240

    if bebek.colliderect(engel) and yeni_resim != 'ziplamak':
        bebek.image = 'yarali'
        can -= 1
        if can <= 0:
            mod = 'bitti'
        else:
            engel.x = WIDTH + 20
            engel.image = random.choice(engel_turleri)
            bebek.image = 'bebek'
            yeni_resim = 'bebek'

def on_key_down(key):
    global yeni_resim, mod

    if mod == 'oyun' and (key == keys.SPACE or key == keys.UP or key == keys.W):
        bebek.image = 'ziplamak'
        yeni_resim = 'ziplamak'
        bebek.y = 120
        animate(bebek, tween="bounce_end", duration=0.8, y=240, on_finished=ziplamayi_bitir)
    elif mod == 'bitti' and key == keys.RETURN:
        mod = 'menü'

def on_mouse_down(button, pos):
    global mod

    if mod == 'menü':
        if background.collidepoint(pos):
            mod = 'background'
        elif oyna.collidepoint(pos):
            oyun_baslat()  # Oyunu başlatmak için fonksiyonu çağır
        elif carpi.collidepoint(pos):
            exit()
    elif mod == 'background' and button == mouse.LEFT:
        if carpi.collidepoint(pos):
            mod = 'menü'
        elif arkaplan2button.collidepoint(pos):
            arkaplan1.image = 'arkaplan2'
            mod = 'oyun'
        elif arkaplan3button.collidepoint(pos):
            arkaplan1.image = 'arkaplan3'
            mod = 'oyun'
        elif arkaplan4button.collidepoint(pos):
            arkaplan1.image = 'arkaplan4'
            mod = 'oyun'

def ziplamayi_bitir():
    global yeni_resim
    bebek.image = 'bebek'
    yeni_resim = 'bebek'
