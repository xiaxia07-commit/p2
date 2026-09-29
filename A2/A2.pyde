import random

colors_list = ["red", "blue", "green", "yellow"]

board = []
target_final_color = ""
moves_left = 12
game_state = "PLAYING"
selected_color = None
save_status_msg = ""

def setup():
    size(500, 580)
    init_game()

def init_game():
    global board, target_final_color, moves_left, game_state, selected_color, save_status_msg
    board = []
    
    r = 0
    while r < 8:
        row_data = []
        c = 0
        while c < 8:
            random_color = random.choice(colors_list)
            row_data.append(random_color)
            c += 1
        board.append(row_data)
        r += 1
        
    target_final_color = random.choice(colors_list)
    moves_left = 12
    game_state = "PLAYING"
    selected_color = None
    save_status_msg = ""

def save_game():
    global save_status_msg
    try:
        lines = [
            target_final_color,
            str(moves_left),
            str(selected_color)
        ]
        
        r = 0
        while r < 8:
            lines.append(",".join(board[r]))
            r += 1
            
        saveStrings("savegame.txt", lines)
        save_status_msg = "SAVED!"
    except:
        save_status_msg = "SAVE ERROR!"

def load_game():
    global board, target_final_color, moves_left, selected_color, game_state, save_status_msg
    
    lines = loadStrings("savegame.txt")
    if lines is None:
        save_status_msg = "NO SAVE FILE!"
        return
        
    try:
        target_final_color = lines[0].strip()
        moves_left = int(lines[1].strip())
        
        sel = lines[2].strip()
        selected_color = None if sel == "None" else sel
        
        board = []
        r = 0
        while r < 8:
            row_colors = lines[3 + r].strip().split(",")
            board.append(row_colors)
            r += 1
            
        game_state = "PLAYING"
        save_status_msg = "LOADED!"
    except:
        save_status_msg = "LOAD ERROR!"

def check_spread(x, y, colour):
    if x < 0 or x >= 8 or y < 0 or y >= 8:
        return False
    if board[y][x] == colour:
        return True
    return False

def spread(x, y, target_colour, new_colour):
    if target_colour == new_colour:
        return
    if not check_spread(x, y, target_colour):
        return
    
    board[y][x] = new_colour
    
    spread(x + 1, y, target_colour, new_colour)
    spread(x - 1, y, target_colour, new_colour)
    spread(x, y + 1, target_colour, new_colour)
    spread(x, y - 1, target_colour, new_colour)

def check_win():
    r = 0
    while r < 8:
        c = 0
        while c < 8:
            if board[r][c] != target_final_color:
                return False
            c += 1
        r += 1
    return True

def change_colour(start_x, start_y, new_colour):
    global moves_left, game_state, save_status_msg
    if game_state != "PLAYING":
        return
    
    save_status_msg = ""
    old_colour = board[start_y][start_x]
    if old_colour != new_colour:
        spread(start_x, start_y, old_colour, new_colour)
        moves_left -= 1
        
        if check_win():
            game_state = "WON"
        elif moves_left <= 0:
            game_state = "LOST"

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

def draw_hud():
    fill(0)
    textSize(14)
    text("Moves Left: " + str(moves_left), 50, 470)
    text("Target:", 180, 470)
    
    draw_block(230, 455, 20, target_final_color)
    
    fill(80)
    textSize(12)
    text("[S] Save  [L] Load", 270, 470)
    
    fill(0, 150, 0)
    text(save_status_msg, 390, 470)
    
    if game_state == "WON":
        fill(0, 200, 0)
        textSize(40)
        text("YOU WIN!", 160, 240)
    elif game_state == "LOST":
        fill(200, 0, 0)
        textSize(40)
        text("GAME OVER", 140, 240)

def draw():
    background(200)
    
    stroke(0)
    strokeWeight(1)
    
    row = 0
    while row < 8:
        col = 0
        while col < 8:
            x_pos = 50 + (col * 50)
            y_pos = 30 + (row * 50)
            color_str = board[row][col]
            
            draw_block(x_pos, y_pos, 50, color_str)
            col += 1
        row += 1

    i = 0
    while i < 4:
        btn_x = 75 + (i * 100)
        btn_y = 500
        btn_color = colors_list[i]
        
        if btn_color == selected_color:
            stroke(255)
            strokeWeight(3)
        else:
            stroke(0)
            strokeWeight(1)
            
        draw_block(btn_x, btn_y, 50, btn_color)
        i += 1
        
    stroke(0)
    strokeWeight(1)
    draw_hud()

def keyPressed():
    if key == 's' or key == 'S':
        save_game()
    elif key == 'l' or key == 'L':
        load_game()

def mousePressed():
    global selected_color, save_status_msg
    if game_state == "PLAYING":
        clicked_button = False
        
        i = 0
        while i < 4:
            btn_x = 75 + (i * 100)
            btn_y = 500
            if btn_x <= mouseX <= btn_x + 50 and btn_y <= mouseY <= btn_y + 50:
                selected_color = colors_list[i]
                clicked_button = True
                save_status_msg = ""
                break
            i += 1
            
        if not clicked_button and selected_color is not None:
            if 50 <= mouseX < 50 + (8 * 50) and 30 <= mouseY < 30 + (8 * 50):
                col = int((mouseX - 50) / 50)
                row = int((mouseY - 30) / 50)
                if 0 <= col < 8 and 0 <= row < 8:
                    change_colour(col, row, selected_color)
    else:
        init_game()