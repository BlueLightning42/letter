#The Letter.py
import curses
from curses import wrapper
from src.max_window import maximize_console
from src.complement import show_complement
from src.start import start_up
from src.story import story_run

maximize_console() # can't get resizeterm to work correctly/move the terminal too...just copied from stackoverflow

def main(screen):
    curses.start_color()
    curses.use_default_colors()
    
    #curses.init_pair(0, 1, -1)     # white
    curses.init_pair(1,   45,   -1) # blueish
    curses.init_pair(2,   100,  -1) # grey green
    curses.init_pair(3,   198,  -1) # pink
    curses.init_pair(4,   201,  -1) # pink 2
    curses.init_pair(5,   66,   -1) # grey green 2
    curses.init_pair(6,   113,  -1) # bring green 2
    curses.init_pair(7,   125,  -1) # blood red
    curses.init_pair(8,   99,   -1) # Purple
    curses.init_pair(9,   83,   -1) # bright green
    curses.init_pair(10,  210,  -1) # orange

    start_up(screen)
    curses.curs_set(0)
    while True:
        screen.clear()
        show_complement(screen)
        if story_run(screen):
            break
        screen.refresh()
        
    
wrapper(main)