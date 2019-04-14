import pyglet
from pyglet.window import key
from pyglet.window import mouse
import math
SIRKA = 1000
VYSKA = 600

window = pyglet.window.Window(width=SIRKA, height=VYSKA)
pozice_had = [100, 100]
rychlost_had=[10]

snd = pyglet.media.load('syceni2.wav') #spouští zvuk syčení hada
looper = pyglet.media.SourceGroup(snd.audio_format, None)
looper.loop = True
looper.queue(snd)
p = pyglet.media.Player()
p.queue(looper)


def tik(t):

    "' Zajišťuje otáčení hada kolem své vlastní osy a pohyb kolmo vzhůru. Když narazí do zdi, je odhozen na začátek.'"

    if pozice_had[0] < SIRKA and pozice_had[0] >0  and pozice_had[1] < VYSKA and pozice_had[1] >0:
        pozice_had[0] = pozice_had[0]+t * 40
        pozice_had[1] = pozice_had[1]+t * 40
        had.rotation = had.rotation+rychlost_had[0]
        if pozice_had[0] >=SIRKA:
            pozice_had[0] = 100
            pozice_had[1] = 100
        if pozice_had[1] >=VYSKA:
            pozice_had[0] = 100
            pozice_had[1] = 100

pyglet.clock.schedule_interval(tik, 1/30)

obrazek = pyglet.image.load('had.png')
obrazek2 = pyglet.image.load('had2.png')

def zmen(t):
    "' Funkce zmen a zmen_zpatky zajišťují vzájemné střídání dvou obrázků.'"
    had.image = obrazek2
    pyglet.clock.schedule_once(zmen_zpatky, 0.2)

def zmen_zpatky(t):
    had.image = obrazek
    pyglet.clock.schedule_once(zmen, 0.2)

pyglet.clock.schedule_once(zmen, 1)

had = pyglet.sprite.Sprite(obrazek)

def klik(x, y, tlacitko, mod):
    "'Funkce, která přijmá vstup od uživatele za pomoci myši. Levé tlačítko mění polohu obrázku, pravé zrychlí rotaci obrázku, zmáčknutí kolečka rotaci zpomalí.'"

    if tlacitko==mouse.LEFT:
        pozice_had[0] = x
        pozice_had[1] = y

    elif tlacitko==mouse.RIGHT:
        rychlost_had[0]=rychlost_had[0]+1
    elif tlacitko==mouse.MIDDLE:
        rychlost_had[0]=rychlost_had[0]-1

def rychlost(sym,mod):
    "'Funkce, která přijmá vstup od uživatele za pomoci klavesnice. Šipky posunou obrázek o 50 pixelů v daném směru, mezerník změní směr rotace hada.'"

    if sym == key.LEFT:
        pozice_had[0] = pozice_had[0] -50
        if pozice_had[0] <=-1 :
            pozice_had[0] = 100
            pozice_had[1] = 100
        if pozice_had[1] <=-1 :
            pozice_had[0] = 100
            pozice_had[1] = 100
    elif sym ==key.RIGHT:
        pozice_had[0] = pozice_had[0] + 50
        if pozice_had[0] >=SIRKA :
            pozice_had[0] = 100
            pozice_had[1] = 100
        if pozice_had[1] >=VYSKA:
            pozice_had[0] = 100
            pozice_had[1] = 100
    elif sym ==key.UP:
        pozice_had[1] = pozice_had[1] + 50
        if pozice_had[0] >=SIRKA :
            pozice_had[0] = 100
            pozice_had[1] = 100
        if pozice_had[1] >=VYSKA:
            pozice_had[0] = 100
            pozice_had[1] = 100

    elif sym ==key.DOWN:
        pozice_had[1] = pozice_had[1] - 50
        if pozice_had[0] <=-1 :
            pozice_had[0] = 100
            pozice_had[1] = 100
        if pozice_had[1] <=-1 :
            pozice_had[0] = 100
            pozice_had[1] = 100
    elif sym ==key.SPACE:
        rychlost_had[0]=rychlost_had[0]-(rychlost_had[0]*2)

def velikost(x, y, scroll_x, scroll_y):
    "' Funkce měnící velikost obrázku za pomocí rolování kolečka na myši.'"
    had.scale += float(scroll_y/4.0)

def vykresli():
    "'Funkce vzkreslující obrázky hada.'"
    had.x = pozice_had[0]
    had.y = pozice_had[1]
    had.x = had.x
    had.y = had.y
    window.clear()
    had.draw()

window.push_handlers(
    on_key_press=rychlost,
    on_draw=vykresli,
    on_mouse_press=klik,
    on_mouse_scroll=velikost,
)
p.play()
pyglet.app.run()
