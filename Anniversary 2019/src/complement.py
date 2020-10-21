import curses
from random import shuffle


_com_num = 0
_complements = ["You make me happy",
    "I love you",
    "I want to spend the rest of my life with you.",
    "I appreciate everything you do for me",
    "I love making food with you",
    "I like watching anime with you",
    "I love your baking",
    "I like watching you play games...you are really cute",
    "I love your voice",
    "You are my favorite human",
    "    I love when you play with my hair\n or run your nails down my back.",
    "I love spending time with you",
    "I like the way you laugh",
    "You make me unbelievably happy",
    "Time with you is time well spent",
    "        I couldn't Imagine \n  Life without you at this point",
    "I love when you like similar things to me \n so I can share my enthusiasm.",
    "I love when you like different things from me \n so I can listen to your enthusiasm.",
    "I love you're voice,\nI love when you sing.",
    "I love when you laugh, your smile is divine.",
    "I like the way you hold onto me",
    "I like how you make me feel",
    "I love when you make me food",
    "Snuggling you is my favorite thing as long as you are in my arms I can feel okay."
]
# https://asciiart.website/index.php?art=people/body%20parts/brains -Joachim Hoffmueller-
brain = '''                   __,--"""""""""--,.
             _ -'"                  _\\ ^-,_
          ,-"                     _/        \\_
         ,                    /    \\          \\
       ,'                    /_    |           \\
      /           _____,--"""     /         )   \\
     /           /               /         (     |
    |          /                /      )         |
    |         /                |                  \\
    (     (_/\\      )                 /            \\
     \\        \\_          ____,===="""    /        |
      \\                /"                /""       |
       \\_          _,-" |___,-'--------'"          |
         "`------""   --"                 ,-'      /
                /                     ---"        /
                \\___/          __,-----,___       )
                    \\     ,--'"============""""-'"
                     "-'" |  |=================/
                          /___\\===============/
                           /  |=============/"
                           \\   \\_________,-"
                           |   |
                           |   | 
'''

def show_brain(screen):
    screen.addstr(4, 0, brain, curses.color_pair(3))
    

def show_complement(screen):
    global _com_num
    global _complements
    
    y, x = screen.getmaxyx()
    
    win = curses.newwin(28, 85, 1,x - 86)
    
    w_x = (85 - len(_complements[_com_num])) // 2
    
    win.addstr(1,  w_x, _complements[_com_num], curses.color_pair(4))
    show_brain(win)
    
    win.overlay(screen, 0, 0 + (1 if _com_num %2 else 0), 0, x - 85, 28, x-1)
    
    _com_num += 1
    if _com_num == len(_complements):
        _com_num = 0
        shuffle(_complements)

def main(screen):
    shuffle(_complements)
    screen.addstr(1,  1, _complements[0], curses.color_pair(4))
    screen.refresh()
    screen.getkey()
if __name__ == '__main__':
    curses.wrapper(main)
    
