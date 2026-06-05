import curses


COLORS = [
    curses.COLOR_BLACK,
    curses.COLOR_RED,
    curses.COLOR_GREEN,
    curses.COLOR_YELLOW,
    curses.COLOR_BLUE,
    curses.COLOR_MAGENTA,
    curses.COLOR_CYAN,
    curses.COLOR_WHITE
]

def main(stdscr):
    
    curses.curs_set(0)
    
    stdscr.keypad(True)
    
    
    curses.start_color()
    for i, color in enumerate(COLORS, start=1):
        
        curses.init_pair(i, color, color)
    
    
    width, height = 16, 16
    grid = [[0 for _ in range(width)] for _ in range(height)]
    
    
    cursor_x, cursor_y = 0, 0
    current_color_index = 1  
    
    while True:
        stdscr.clear()
        
        
        stdscr.addstr(0, 0, "idk use arrows to move. press space to draw. press 1-8 to change da color. just press q to quit, unfortunately theres no save button, sorry :(  -driswillis156")
        
        
        
        for y in range(height):
            for x in range(width):
                color_pair = grid[y][x]
                if color_pair == 0:
                    
                    stdscr.addstr(y + 2, x * 2, ". ")
                else:
                    stdscr.addstr(y + 2, x * 2, "  ", curses.color_pair(color_pair))
                    
        
        stdscr.addstr(cursor_y + 2, cursor_x * 2, "[]", curses.A_REVERSE)
        
        
        stdscr.addstr(height + 4, 0, f"color: {current_color_index} ")
        stdscr.addstr(height + 4, 16, "  ", curses.color_pair(current_color_index + 1))
        
        
        stdscr.refresh()
        key = stdscr.getch()
        
        
        if key == curses.KEY_UP and cursor_y > 0:
            cursor_y -= 1
        elif key == curses.KEY_DOWN and cursor_y < height - 1:
            cursor_y += 1
        elif key == curses.KEY_LEFT and cursor_x > 0:
            cursor_x -= 1
        elif key == curses.KEY_RIGHT and cursor_x < width - 1:
            cursor_x += 1
        
        elif key == ord(' '):
            
            grid[cursor_y][cursor_x] = current_color_index + 1
            
        elif ord('1') <= key <= ord('8'):
            current_color_index = int(chr(key)) - 1
            
        elif key in (ord('q'), ord('Q')):
            break


curses.wrapper(main)
