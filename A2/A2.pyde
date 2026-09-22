board = [
    ["red", "blue", "green", "yellow", "red", "blue", "green", "yellow"],
    ["blue", "red", "yellow", "green", "blue", "red", "yellow", "green"],
    ["green", "yellow", "blue", "red", "green", "yellow", "blue", "red"],
    ["yellow", "green", "red", "blue", "yellow", "green", "red", "blue"],
    ["red", "yellow", "green", "blue", "red", "yellow", "green", "blue"],
    ["blue", "green", "yellow", "red", "blue", "green", "yellow", "red"],
    ["green", "blue", "red", "yellow", "green", "blue", "red", "yellow"],
    ["yellow", "red", "blue", "green", "yellow", "red", "blue", "green"]
]

def setup():
    size(500, 500)
    background(200)

def draw():
    row = 0
    while row < 8:
        col = 0
        while col < 8:
            x_pos = 30 + (col * 55)
            y_pos = 30 + (row * 55)
            color_str = board[row][col]
            
            draw_block(x_pos, y_pos, 50, color_str)
            col += 1
        row += 1

def draw_block(x, y, sizee, colour):
    if colour == "red":
        fill(255, 100, 100)
    elif colour == "blue":
        fill(100, 100, 255)
    elif colour == "green":
        fill(100, 255, 100)
    elif colour == "yellow":
        fill(255, 255, 100)
    else:
        fill(255)
        
    rect(x, y, sizee, sizee)
    
    fill(255, 255, 255, 50)
    ellipse(x + sizee/2, y + sizee/2, sizee*0.6, sizee*0.6)

def change_colour(colour):
    pass

def check_spread(x, y, colour):
    return False

