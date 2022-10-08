import bgplot as bgp
from bgplot.entities import Point, Axes, Vector

graphics: bgp.Graphics = bgp.Graphics()

graphics.disable('grid', 'ticks', 'axes', 'walls')
graphics.set_background_color(bgp.Colors.white)

# Simple point plotting
point_1: Point = Point(0.0, 0.0, 0.0)
point_2: Point = Point(1.0, 1.0, 0.0)
point_3: Point = Point(1.0, 1.0, 1.0)

graphics.add_point(point_1, color=bgp.Colors.red)
graphics.add_point(point_2, color=bgp.Colors.green)
graphics.add_point(point_3, color=bgp.Colors.blue)

graphics.set_title('point')
graphics.show()

# Multiple points plotting
graphics.add_points([point_1, point_2, point_3], style='.-')

graphics.set_title('points')
graphics.show()

# Oriented points
axes_1: Axes = Axes(Vector(1.0, 1.0, 1.0),
                    Vector(1.0, 0.0, 0.0),
                    Vector(0.0, 0.0, 1.0))

axes_2: Axes = Axes(Vector(1.0, 1.0, 1.0),
                    Vector(1.0, 0.0, 1.0),
                    Vector(0.0, 0.0, 1.0))

axes_3: Axes = Axes(Vector(1.0, 1.0, 1.0),
                    Vector(1.0, 0.0, 0.0),
                    Vector(1.0, 0.0, -1.0))

graphics.add_oriented_point(point_1, axes_1, color=bgp.Colors.red)
graphics.add_oriented_point(point_2, axes_2, color=bgp.Colors.green)
graphics.add_oriented_point(point_3, axes_3, color=bgp.Colors.blue)

graphics.set_title('oriented point')
graphics.show()

# Multiple oriented points

graphics.set_title('oriented points')
graphics.add_oriented_points([point_1, point_2, point_3], [
                             axes_1, axes_2, axes_3], style='-o')
graphics.set_background_color(bgp.Colors.white)
graphics.show()
