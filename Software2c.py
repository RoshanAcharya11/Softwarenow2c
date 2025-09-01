import turtle
import math

def draw_fractal_edge(t, length, depth, max_depth):
    """
    Recursively draw one fractal edge(like koch curve)
    Adds purple to blue gradient based on recursion depth.
    """
    # GCalculating color gradient: purple at start -> blue as it goes more deeper
    shade = int(255 * (depth / max_depth)) if max_depth > 0 else 0
    t.pencolor((shade, 0, 255 - shade))

    if depth == 0:
        t.forward(length)  # Base case: draws a straight line
    else:
        # breaks line further into 4 smaller segments
        segment = length / 3
        draw_fractal_edge(t, segment, depth - 1, max_depth) #left part
        t.left(60) #make peak
        draw_fractal_edge(t, segment, depth - 1, max_depth)
        t.right(120) # make valley
        draw_fractal_edge(t, segment, depth - 1, max_depth)
        t.left(60) #right part
        draw_fractal_edge(t, segment, depth - 1, max_depth)

def move_to_start(t, sides, side_length):
    """
    Moves the turtle so that the fractal polygon is centered in the screen.
    Uses polygon geometry to calculate radius.
    """
    # Distance from polygon center to a vertex (circumradius)
    radius = side_length / (2 * math.sin(math.pi / sides)) #polygon radius

    t.penup()
    t.setheading(90)         # turns face upwards
    t.backward(radius)       # Moves down by radius
    t.right(90)              # Faces east again
    t.pendown()

def draw_polygon_fractal(sides, side_length, depth, inward=True):
    """
    Draws a polygon with centered fractal polygon (no fill).
    sides: Number of polygon sides
    side_length: length of each side
    depth: recursion depth
    inward: direction of drawing (clockwise vs anticlockwise)
    """
    t = turtle.Turtle()
    t.speed(0) # fastest drawing
    t.hideturtle() # hide pointer

    # Enable RGB colors
    turtle.colormode(255) # allow RGB
    turtle.bgcolor("white") # white background
    turtle.tracer(False) # disable live drawing for speed

    # position turtle to Center the fractal
    move_to_start(t, sides, side_length)

    angle = 360 / sides # interior angle of polygon

    #Draw each fractal edge around the polygon
    for _ in range(sides):
        draw_fractal_edge(t, side_length, depth, depth)
        if inward:
            t.left(angle) # rotate left to next side
        else:
            t.right(angle) # rotate right to next side

    turtle.tracer(True) # show final deawing

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
        print("A polygon needs at least 3 sides.")

    side_length = int(input("Enter the side length: "))
    depth = int(input("Enter the recursion depth: "))

    draw_polygon_fractal(sides, side_length, depth, inward=True)
