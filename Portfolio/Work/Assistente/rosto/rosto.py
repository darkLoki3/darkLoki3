import RPi.GPIO as gpio
import pyglet

gpio.setmode(gpio.BCM)
gpio.setup(29, gpio.IN)

def fala():
    animation = pyglet.image.load_animation('falando.gif')
    animSprite = pyglet.sprite.Sprite(animation)
    w = animSprite.width
    h = animSprite.height
    window = pyglet.window.Window(width=1600, height=900, fullscreen=True)
    r, g, b, alpha = 0.5, 0.5, 0.8, 0.5
    pyglet.gl.glClearColor(r, g, b, alpha)
    @window.event
    def on_draw():
        window.clear()
        animSprite.draw()
    pyglet.app.run()

def pisca():
    animation = pyglet.image.load_animation('piscando.gif')
    animSprite = pyglet.sprite.Sprite(animation)
    w = animSprite.width
    h = animSprite.height
    window = pyglet.window.Window(width=1600, height=900, fullscreen=True)
    r, g, b, alpha = 0.5, 0.5, 0.8, 0.5
    pyglet.gl.glClearColor(r, g, b, alpha)
    @window.event
    def on_draw():
        window.clear()
        animSprite.draw()
    pyglet.app.run()
    
if(gpio.input(29)==True):
    fala()
    else:
        pisca()
