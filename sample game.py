from ursina import *


app = Ursina()

Entity(model='cube', color=color.red, texture='white_cube', scale=10)

EditorCamera()

# this is a sample game
# made by me

app.run()