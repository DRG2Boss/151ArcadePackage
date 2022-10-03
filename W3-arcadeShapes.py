import arcade

arcade.open_window(1200,900, "More Shapes")

arcade.start_render()
# Rectangles:
arcade.draw_lrtb_rectangle_filled(50, 150, 200, 50, arcade.color.BITTER_LEMON)
# LRTB means left, right, top, bottom, aka the formating of the vertices changes between lines and these rectangles.
arcade.draw_lrtb_rectangle_outline(160, 360, 150, 50, arcade.color.BRIGHT_UBE, 6)
arcade.draw_xywh_rectangle_outline(10, 10, 380, 250, arcade.color.CYAN, 6)
# XYWH means x pos, y pos, width, and height. Another formatting change.
arcade.draw_xywh_rectangle_filled(405, 10, 150, 100, arcade.color.GREEN)

# Circles:
arcade.draw_circle_filled(100, 800, 50, arcade.color.LAVA)
# Format: center of circle X pos, center of circle Y pos, Radius, color, thickness (OPTIONAL)
arcade.draw_circle_outline(100, 800, 85, arcade.color.BLUE, 6)

# Triangles:
arcade.draw_triangle_outline(300, 400, 700, 800, 600, 400, arcade.color.BANANA_MANIA, 8)
# Format: x1, y1 position, x2, y2 position, x3, y3 position
arcade.draw_triangle_filled(300, 700, 100, 500, 475, 600, arcade.color.BLAST_OFF_BRONZE)

# Arcs:
arcade.draw_arc_filled(400, 700, 100, 100, arcade.color.YELLOW, 60, 330)
# Format: center x, center y, width, height, color, start angle, end angle, thickness (OPTIONAL)
arcade.draw_arc_outline(600, 700, 100, 100, arcade.color.WHITE, -180, 0, 10)
arcade.draw_parabola_filled(800, 300, 1000, 300, arcade.color.CEIL)
arcade.finish_render()

arcade.run()
