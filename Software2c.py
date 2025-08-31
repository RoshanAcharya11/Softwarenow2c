import turtle
import math

def draw_fractal_edge(t, length, depth, max_depth):
    """
    Recursively draw one edge of the fractal.
    Adds color gradient based on depth.
    """
    # Gradient color: purple -> blue
    shade = int(255 * (depth / max_depth)) if max_depth > 0 else 0
    t.pencolor((shade, 0, 255 - shade))

    if depth == 0:
        t.forward(length)  # Base case
    else:
        segment = length / 3
        draw_fractal_edge(t, segment, depth - 1, max_depth)
        t.left(60)
        draw_fractal_edge(t, segment, depth - 1, max_depth)
        t.right(120)
        draw_fractal_edge(t, segment, depth - 1, max_depth)
        t.left(60)
        draw_fractal_edge(t, segment, depth - 1, max_depth)

def move_to_start(t, sides, side_length):
    """
    Moves the turtle so that the fractal polygon is centered in the screen.
    Uses polygon geometry to calculate radius.
    """
    # Distance from polygon center to a vertex (circumradius)
    radius = side_length / (2 * math.sin(math.pi / sides))

    t.penup()
    t.setheading(90)         # Face upwards
    t.backward(radius)       # Move down by radius
    t.right(90)              # Face east again
    t.pendown()

def draw_polygon_fractal(sides, side_length, depth, inward=True):
    """
    Draws a centered fractal polygon (no fill).
    """
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    # Enable RGB colors
    turtle.colormode(255)
    turtle.bgcolor("white")
    turtle.tracer(False)

    # Center polygon
    move_to_start(t, sides, side_length)

    angle = 360 / sides

    for _ in range(sides):
        draw_fractal_edge(t, side_length, depth, depth)
        if inward:
            t.left(angle)
        else:
            t.right(angle)

    turtle.tracer(True)

    # Save result
    ts = turtle.getcanvas()
    ts.postscript(file="fractal_output.eps")

    turtle.done()

if __name__ == "__main__":
    # Input with validation
    while True:
        sides = int(input("Enter the number of sides (≥ 3): "))
        if sides >= 3:
            break
        print("❌ A polygon needs at least 3 sides.")

    side_length = int(input("Enter the side length: "))
    depth = int(input("Enter the recursion depth: "))

    draw_polygon_fractal(sides, side_length, depth, inward=True)
