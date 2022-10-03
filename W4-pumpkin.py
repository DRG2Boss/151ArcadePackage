import arcade

arcade.open_window(1000, 900, "Jack-o-Lantern")
arcade.set_background_color(arcade.color.PURPLE)

arcade.start_render()
# Text:
greeting = arcade.Text("Ready for Oct 31", 400, 870, arcade.color.WHITE, 16)
greeting.draw()
# Pumpkin:
arcade.draw_circle_filled(500, 450, 300, arcade.color.PUMPKIN)
# Eyes:
arcade.draw_arc_filled(355, 550, 150, 150, arcade.color.YELLOW, 0, 180)
arcade.draw_arc_filled(645, 550, 150, 150, arcade.color.YELLOW, 0, 180)
# Nose:
arcade.draw_triangle_filled(425, 385, 500, 515, 575, 385, arcade.color.YELLOW)
# Mouth:
arcade.draw_arc_filled(500, 325, 400, 250, arcade.color.YELLOW, -180, 0)
# Hat:
arcade.draw_xywh_rectangle_filled(220, 740, 560, 25, arcade.color.BLACK)
arcade.draw_xywh_rectangle_filled(330, 760, 330, 100, arcade.color.BLACK)

arcade.finish_render()
arcade.run()
