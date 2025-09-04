import turtle
import math

def draw_fractal_edge(t, length, depth, max_depth):
    """
    Koch curve implementation involves recursively
    replacing each line segment with four segments,resulting in a triangular bump.
    """
    if length <= 0 or depth < 0:
        return
        
    shade = int(255 * (depth / max_depth)) if max_depth > 0 else 0
    t.pencolor((shade, 0, 255 - shade))
    
    if depth == 0:
        t.forward(length)
    else:
        segment = length / 3
        #Koch construction has four segments:forward,turn 60°,forward,turn -120°,forward,turn 60°,forward.        draw_fractal_edge(t, segment, depth - 1, max_depth)
        t.left(60)
        draw_fractal_edge(t, segment, depth - 1, max_depth)
        t.right(120)
        draw_fractal_edge(t, segment, depth - 1, max_depth)
        t.left(60)
        draw_fractal_edge(t, segment, depth - 1, max_depth)

def trace_fractal_edge(tracer, length, depth, coords):
    """
    Invisible variant of draw_fractal_edge() that saves coordinates rather than drawing.
  Used to calculate actual fractal boundaries for centering..
    """
    if length <= 0 or depth < 0:
        return
        
    if depth == 0:
        tracer.forward(length)
        coords.append(tracer.position())
    else:
        segment = length / 3
        trace_fractal_edge(tracer, segment, depth - 1, coords)
        tracer.left(60)
        trace_fractal_edge(tracer, segment, depth - 1, coords)
        tracer.right(120)
        trace_fractal_edge(tracer, segment, depth - 1, coords)
        tracer.left(60)
        trace_fractal_edge(tracer, segment, depth - 1, coords)

def get_fractal_bounds(sides, side_length, depth):
    """
    Determines bounding box by invisibly tracing the full fractal polygon.
    Koch curves stretch beyond basic polygon borders, making this necessary.
    """
    if sides < 3 or side_length <= 0 or depth < 0:
        return (0, 0, 0, 0)
    
    tracer = turtle.Turtle()
    tracer.speed(0)
    tracer.hideturtle()
    tracer.penup()
    tracer.goto(0, 0)
    tracer.setheading(0)
    
    coords = [(0, 0)]
    angle = 360 / sides
    
    #Trace each polygon side to get all the fractal coordinates.
    for _ in range(sides):
        trace_fractal_edge(tracer, side_length, depth, coords)
        tracer.left(angle)
    
    if len(coords) > 1:
        x_coords = [pos[0] for pos in coords]
        y_coords = [pos[1] for pos in coords]
        return (min(x_coords), max(x_coords), min(y_coords), max(y_coords))
    return (0, 0, 0, 0)

def draw_polygon_fractal(sides, side_length, depth):
    """
    The main drawing function generates a regular polygon by replacing each edge with a 
    Koch curve fractal.Uses limits computation for perfect centering..
    """
    if sides < 3 or side_length <= 0 or depth < 0:
        return False
    
    screen = turtle.Screen()
    screen.setup(1000, 800)
    screen.bgcolor("white")
    screen.colormode(255)
    screen.tracer(False)
    
    #Calculate the exact fractal dimensions and center point.
    min_x, max_x, min_y, max_y = get_fractal_bounds(sides, side_length, depth)
    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2
    
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.goto(-center_x, -center_y)
    t.setheading(0)
    t.pendown()
    
    angle = 360 / sides
    
    #Draw a polygon; each side becomes a fractal edge.
    for _ in range(sides):
        draw_fractal_edge(t, side_length, depth, depth)
        t.left(angle)
    
    screen.tracer(True)
    screen.exitonclick()
    return True

if __name__ == "__main__":
    """
    Need bulletproof parameter validation for the generator to work. 
    Invalid parameters can cause a program to crash, go into infinite recursion, or produce nonsensical output. 

    Continuous retry loops with silent error handling provide 
    streamlined user experience. Alternative approaches with the error messages create a lot of clutter. 
    Exception handling ensures the program does not crash due to non-integer inputs. 

    """
    while True:  #Get the valid no of sides 
        try:
            sides = int(input("Enter number of sides (≥ 3): "))  # Get the user input
            if sides >= 3:  # Check minimum requirement [Basic Rule]
                break  # Check: Valid input, exit loop
        except ValueError:  # Handle non-integer input
            pass  # Retry silently
    #Basic Loop logic implemented

    while True:  # Get valid side length
        try:
            side_length = int(input("Enter side length: "))  # Get the user input
            if side_length > 0:  # logic: Must be positive
                break  # Valid input, exit loop
        except ValueError:  # Handle non-integer input
            pass  # Retry silently
    # Same basic checking for recursion depth logic for the code to pass the test case
    while True:  # Get valid recursion depth
        try:
            depth = int(input("Enter recursion depth: "))  # Get user input
            if depth >= 0:  # Must be non-negative
                break  # Valid input, exit loop
        except ValueError:  # Handle non-integer input
            pass  # Retry silently
    
    draw_polygon_fractal(sides, side_length, depth)  # Generate fractal with validated parameters