import turtle
import functools as ft
from Game.game import Game 
import datetime

game = Game()

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

pressed_keys = []
def add_key(key):
    if key not in pressed_keys:   
        pressed_keys.append(key)
    
def remove_key(key):
    pressed_keys.remove(key)

window.listen()
window.onkeypress(ft.partial(add_key, "w" ),"w")
window.onkeypress(ft.partial(add_key, "s" ),"s")
window.onkeypress(ft.partial(add_key, "Up" ),"Up")
window.onkeypress(ft.partial(add_key, "Down" ),"Down")
window.onkeypress(ft.partial(add_key, "d" ),"d")
window.onkeypress(ft.partial(add_key, "Left" ),"Left")
window.onkey(ft.partial(remove_key, "w"), "w")
window.onkey(ft.partial(remove_key, "s"), "s")
window.onkey(ft.partial(remove_key, "Up"), "Up")
window.onkey(ft.partial(remove_key, "Down"), "Down")
window.onkey(ft.partial(remove_key, "Left"), "Left")
window.onkey(ft.partial(remove_key, "d"), "d")



while True:
    window.update()
    game.read_input(pressed_keys)
    game.ball_collision()
    game.players_collision()
    game.movement_ball()



