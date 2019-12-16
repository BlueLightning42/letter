import curses

delay = True


titletop = '''                                                                                 
      Justin's brain in                                                          
                                                                                 '''
title = ''' ████████╗██╗  ██╗███████╗    ██╗     ███████╗████████╗████████╗███████╗██████╗ 
 ╚══██╔══╝██║  ██║██╔════╝    ██║     ██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗
    ██║   ███████║█████╗      ██║     █████╗     ██║      ██║   █████╗  ██████╔╝
    ██║   ██╔══██║██╔══╝      ██║     ██╔══╝     ██║      ██║   ██╔══╝  ██╔══██╗
    ██║   ██║  ██║███████╗    ███████╗███████╗   ██║      ██║   ███████╗██║  ██║
    ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚══════╝╚══════╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝'''
titleend =  '''                                                                                 
                                                             Staring Steve       
                                                                                 '''

load_text = "Booting up Justin's brain."
press_text = "Press Any Key to start: "
    
def start_up(screen):
    screen.clear()
    screen.addstr(1,0, load_text, curses.color_pair(0))
    screen.refresh()
    if delay: curses.napms(300)
    screen.addstr(1,len(load_text), ".", curses.color_pair(0))
    screen.refresh()
    if delay: curses.napms(300)
    screen.addstr(1,len(load_text)+1, ".", curses.color_pair(0))
    screen.refresh()
    if delay: curses.napms(300)
    screen.clear()
    
    y, x = screen.getmaxyx()
    start_y = max(y//2-14, 0)
    start_x = max(x//2-79//2-10, 0)
    for line in titletop.split("\n"):
        screen.addstr(start_y, start_x, line, curses.color_pair(1) | curses.A_REVERSE)
        start_y += 1
    start_y += 1
    for line in title.split("\n"):
        screen.addstr(start_y, start_x, line, curses.color_pair(1))
        start_y += 1
    start_y += 1
    for line in titleend.split("\n"):
        screen.addstr(start_y, start_x, line, curses.color_pair(1) | curses.A_REVERSE)
        start_y += 1
    screen.addstr(start_y, start_x, press_text, curses.color_pair(2))
    screen.refresh()
    screen.getkey()



    