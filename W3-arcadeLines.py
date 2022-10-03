import arcade
# This imports the "arcade" package we installed via File - Settings - adding a new Python intepreter to the project.
myWindow = arcade.open_window(1200, 900, "First Window Demo")
# 1200 is the # of pixels wide the window will be. 900 is # of pixels high the winder will be.
arcade.set_background_color(arcade.color.ALMOND)
# This will change the background color to whatever you specify.
arcade.start_render()
for xloc in range(100, 900, 80):
    arcade.draw_line(xloc, 50, xloc, 900, arcade.color.CAPRI, 10)
    # Format is "x start, y start, x end, y end, color, line thickness (OPTIONAL)
for yloc in range(100, 900, 80):
    arcade.draw_line(50, yloc, 900, yloc, arcade.color.BRIGHT_UBE, 10)
arcade.finish_render()
arcade.run()
# This will give us two basic lines, with the horizontal purple line being rendered after the blue.
