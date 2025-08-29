import turtle

def draw_fractal_edge(t, length, depth):
    # Draw one edge of the fractal using recursion.
    if depth == 0:
        t.forward(length)                 # Base case: just draw a straight segment.
    else:
        segment = length / 3              # Each edge becomes 4 segments, each 1/3 long.

        # Replace the single edge with four smaller edges + turns:
        draw_fractal_edge(t, segment, depth - 1)
        t.left(60)                        # build the triangular "dent"
        draw_fractal_edge(t, segment, depth - 1)
        t.right(120)                      # turn through the tip of the triangle
        draw_fractal_edge(t, segment, depth - 1)
        t.left(60)                        # re-align with original heading
        draw_fractal_edge(t, segment, depth - 1)

def draw_polygon_fractal(sides, side_length, depth, inward=True):
    t = turtle.Turtle()
    t.speed(0)                            # fastest drawing
    t.hideturtle()
    turtle.tracer(False)                  # instant draw (turn on later with tracer(True))
    turtle.bgcolor("white")
    t.color("black")

    # For a regular polygon, the exterior turn between sides is 360 / sides.
    angle = 360 / sides

    # If we want the triangle "dent" to point inward, we must traverse the polygon CCW.
    # (Interior stays on the turtle's left.) So we turn LEFT between sides.
    # If you prefer outward bumps, set inward=False to turn RIGHT instead.
    for _ in range(sides):
        draw_fractal_edge(t, side_length, depth)
        if inward:
            t.left(angle)                 # counter-clockwise polygon => dents point inward
        else:
            t.right(angle)                # clockwise polygon => bumps point outward

    turtle.tracer(True)
    turtle.done()

if __name__ == "__main__":
    sides = int(input("Enter the number of sides: "))
    side_length = int(input("Enter the side length: "))
    depth = int(input("Enter the recursion depth: "))

    draw_polygon_fractal(sides, side_length, depth, inward=True)