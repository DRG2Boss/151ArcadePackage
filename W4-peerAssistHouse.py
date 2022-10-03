import arcade

arcade.open_window(1200, 900, "House")
arcade.set_background_color(arcade.color.CYAN)

arcade.start_render()
# Base Square
arcade.draw_xywh_rectangle_filled(250, 10, 700, 500, arcade.color.BITTER_LEMON)

# Door:
arcade.draw_xywh_rectangle_filled(550, 10, 100, 200, arcade.color.BLUE)
arcade.draw_circle_filled(625, 100, 15, arcade.color.YELLOW_ROSE)

# Chimney:
arcade.draw_xywh_rectangle_filled(400, 510, 80, 365, arcade.color.BRICK_RED)

# Windows:
arcade.draw_xywh_rectangle_filled(350, 250, 100, 100, arcade.color.WHITE)
arcade.draw_xywh_rectangle_filled(750, 250, 100, 100, arcade.color.WHITE)
arcade.draw_line(350, 300, 450, 300, arcade.color.BLACK, 5)
arcade.draw_line(400, 250, 400, 350, arcade.color.BLACK, 5)
arcade.draw_line(750, 300, 850, 300, arcade.color.BLACK, 5)
arcade.draw_line(800, 250, 800, 350, arcade.color.BLACK, 5)

# Roof:
arcade.draw_triangle_filled(250, 510, 600, 800, 950, 510, arcade.color.BLAST_OFF_BRONZE)

arcade.finish_render()
arcade.run()
