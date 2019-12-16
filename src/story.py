import curses
import os

# Hacked together as more functionality was added. Not the best format but it works and I'm satisfied with it
# Functional > everything else

bad_end = '''
 ▄▄▄▄    ▄▄▄      ▓█████▄    ▓█████  ███▄    █ ▓█████▄ 
▓█████▄ ▒████▄    ▒██▀ ██▌   ▓█   ▀  ██ ▀█   █ ▒██▀ ██▌
▒██▒ ▄██▒██  ▀█▄  ░██   █▌   ▒███   ▓██  ▀█ ██▒░██   █▌
▒██░█▀  ░██▄▄▄▄██ ░▓█▄   ▌   ▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌
░▓█  ▀█▓ ▓█   ▓██▒░▒████▓    ░▒████▒▒██░   ▓██░░▒████▓ 
░▒▓███▀▒ ▒▒   ▓▒█░ ▒▒▓  ▒    ░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒ 
▒░▒   ░   ▒   ▒▒ ░ ░ ▒  ▒     ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒ 
 ░    ░   ░   ▒    ░ ░  ░       ░      ░   ░ ░  ░ ░  ░ 
 ░            ░  ░   ░          ░  ░         ░    ░    
      ░            ░                            ░      
'''
good_end = '''
   ▄██████▄   ▄██████▄   ▄██████▄  ████████▄          ▄████████ ███▄▄▄▄   ████████▄  
  ███    ███ ███    ███ ███    ███ ███   ▀███        ███    ███ ███▀▀▀██▄ ███   ▀███ 
  ███    █▀  ███    ███ ███    ███ ███    ███        ███    █▀  ███   ███ ███    ███ 
 ▄███        ███    ███ ███    ███ ███    ███       ▄███▄▄▄     ███   ███ ███    ███ 
▀▀███ ████▄  ███    ███ ███    ███ ███    ███      ▀▀███▀▀▀     ███   ███ ███    ███ 
  ███    ███ ███    ███ ███    ███ ███    ███        ███    █▄  ███   ███ ███    ███ 
  ███    ███ ███    ███ ███    ███ ███   ▄███        ███    ███ ███   ███ ███   ▄███ 
  ████████▀   ▀██████▀   ▀██████▀  ████████▀         ██████████  ▀█   █▀  ████████▀                                                                                  
  '''
lots_text = '''
You're still reading this flipbook? Well thanks...
Its kinda dumb...and procrastination as I wrote the other parts of the letter
I'm glad you care enough about it but remember theres a letter too...
Especially because the more you read this the more shallow you will realise it is...

The barest of bones.

like I could have made it more about our relationship but I gave up and just ended up having it a joke.

so its so so.

anyways press any key to continue'''

ADVENTURE_START = 7



def give_reward():
  os.startfile(os.path.realpath("C:/Users/jawg4/Music/Set It Off"))


# format of choices
# prev page is absolute page number
# choice character, description, to page in a offset from current page or tuple of page type/description ex. (bad end, text)
class Page:
    def __init__(self, str, can_advance=True, prev_page=None, choices=None):
        self.str = str
        self.can_advance = can_advance
        self.choices = choices
        self.prev_page = prev_page
    def __str__(self):
        return self.str
    def __repr__(self):
        return self.str

book = [Page('''
  The Rambling Thoughts of Justin.

  I'm going start this off by saying I'm dumb.
  I don't know how to communicate how much I love you
  and I end up doing something like this.
'''),
Page('''
  This Can't be as easy to read as a actual letter 
  even though it ends up being more effort.
  
  But I feel like thats what you get for dating me...
  Slightly random incomprehesible garbage as 
  I attempt to show you how much you mean to me using something I like.
'''),
Page('''
  The nice thing about this option is I can turn it into a choose your own adventure novel!
''', can_advance=False, choices=[('A',"Press 'A' to read the adventures of Steve",ADVENTURE_START - 2),('B',"Press 'B' to continue reading the dumb letter",1)]),
Page('''
  Oh...you're still here...thats nice I guess. 
  Sorry I thought I could distract you for a bit while I think of what to say.
  
  Thats not to say I don't want to talk to you! 
  It's just this is important.
  and I don't want to fuck it up.
'''),
Page('''
  My life to yours my breath becomes yours.
  :3

  Cute quote from brandon sanderson books taken out of context.

  Sorry that was random. But you said its not dumb so I'll leave it in.
'''),
Page('''
  I don't want to write a letter about writing the letter.

  But the more I sit here spiraling in circles. The more it turns into that.

  The problem is I want to express my love and have you actually belive me.
  and the only way I can think of doing that is by putting in actual effort to show I care.
  This is actually V2 of my "brain" because the first dump was actually a chatbot sort of thing...
  parts of that prototype still exist in the upper right corner...
  however most of its gone and all thats left is a endless loop of complements and nice things.

'''),
Page('''
  You know I thought a lot about what to get you right?

  I was going to get you a physical album cause you like hard copies of things...
  But you seem to think I want that.

  But I can get all the songs manually and just spend a few hours 
  individually ripping and tagging them.
  ...so less of a presentation and less impact but...
''', can_advance=False, choices=[('G',"Press 'G' for a gift",(-3,'''
           .__.      .============.
         .(\\\\//).  .-[ To my Love ]
        .(\\\\()//)./  '============'
    .----(\\)\\/(/)----.
    |     ///\\\\\\     |
    |    ///||\\\\\\    |
    |   //`||||`\\\\   |
    |      ||||      |
    |      ||||      |
    |      ||||      |
    |      ||||      |
    |      ||||      |
    |      ||||      |
    '------====------'
'''))]),
Page('''
 THE GREAT ADVENTURES OF STEVE!
 Oh wait did I say steve? I meant Tony
 
 Once Upon a time there was a loan knight named tony.
 He desired nothing more than to slay a dragon for his princess.

 first off Tony had nothing more than a gold coin to his name. What will he do with it?
''', prev_page=2, can_advance=False, choices=[('A',"Press 'A' to Buy a Sword",1),('B',"Press 'B' to buy a Sheep",2), ('C',"Press 'C' to buy a XXXXXX",3)]),
Page('''
 A Sword! Good choice somthing stabby to give a dragon the 'ol one two.

 What should Tony do now?
''', prev_page=2, can_advance=False, choices=[('A',"Press 'A' to head off and find a dragon.",3),
('B',"Press 'B' to rob a random passerby",(-1,'''
YOU DRAW FORTH THE SWORD OF AVALORE
"Give me your money peasant"
You cry out... Only for the peasant to turn around slighly bigger 
...and slighly more buff than you thought.

He looks at you with a mean look then pulls the sword out of your hands and runs you through.

You died.
''')), ('B',"Press 'C' to give up and go home.",(-1,'''
You head home and hang your new sword up on the wall.
You settle down and wait for a dragon to come and attack you so you can bravely fight up off.
and wait...

Years and years later you die of old age...dragon unslayed...princess unsaved.
'''))]),
Page('''
 A Sheep! Some nice bait to catch a dragon.

 What should Tony do now?

''', prev_page=2, can_advance=False, choices=[('A',"Press 'A' to head off and find a dragon.",(-1,'''
You travel for miles and miles before finding a suitable looking field to set your trap.

tieing the sheep to a stick and pushing it into the ground you look around and decide to hide in some shrubs nearbye.

sure enough a dragon appears but after it swoops down and bites the sheep it spots you squatting in the bushes...

a tastier meal than the sheep you were to a hungry dragon.
''')),('B',"Press 'B' to ask someone for help",(-1,'''
You find a strong looking dude with a long sword and ask if he would like to catch a dragon with you.
smirking he agrees and you travel together to a hill to place your trap.

You tie up the sheep and as you move to hide the stranger pushes you agaised the sheep and ties you to it.

"can't have anyone sharing my glory" he proclaims then finishing the knot he hides in a bush.
Your last moment is watching him charge out of a bush waving about a sword as your face is ripped off by 
mr dragon.
''')), ('C',"Press 'C' to formulate a plan.",3)]),
Page('''
 Oh...why did Tony buy that?
 ish...well than.

 Next Tony decided to
''', prev_page=2, can_advance=False, choices=[('A',"Press 'A' to head off and try and **** a dragon.",(-1,'''
 This was a horrible idea...

 after finally finding a dragon you brandish your enormouse fucking ****
 ...only to be flattened by the dragons excited ****

 you died if it wasn't clear
''')),('B',"Press 'B' to try and find your princess",(-2,'''
 You show up at your princess's castle.

 "Justinaaa" you call brandishing the massive engorged ****
 after a moment a head emerges...it stairs down at you and then waves a hand to come up.

 It turns out the dragon you needed to slay was 
 (just a contrived metaphore for) your small penis all along.
'''))]),
Page('''
You head out on a brave adventure. 
At first you are worried without any bait you'll never be able to find a dragon.
and Tony dispairs.

However weeks in you find a cave smoking slightly and confident you have found a dragon
you decide to...

''', prev_page=2, can_advance=False, choices=[('A',"Press 'A' to charge in and stab the dragon.",(-1,'''
You rush into the cave yelling madly
aarrrrrrrgg you scream and stab wildly...

after coming to your senses you find a pool of water steaming slighly...
and a dead maiden laying at your feet. (oh no)

Its justina! Your fabled princesss.
struck with grief at what you'd done you take your own life.

But wait! she wasn't dead after all...and waking up in a daze she finds your body only to dispair!
and stab herself upon thine blade a final time.
''')),('B',"Press 'B' to try and sneak into the cave...",(-2,'''
Sneaking into the cave you find Justina 
--Your princess--
Bathing.
Startled she turns and screams...however after looking you up and down nods
You join her abanding all questlines for a dragon wasn't needed after all.

After the springs she brings you back to her castle where you spend the rest of your days.'''))]),
Page('''
 You decide to set a trap what do you use to do so?
''', prev_page=2, can_advance=False, choices=[('A','''Press 'A' to "Just build it" ''',(-2,'''
Your engineering skills are put to the test.
a tree is lowerd and rope is wrapped between all sorts of smart looking points and a huge masterpiece is made.
lovely.
Its bound to work!
It has to work!

You await the dragon and jump out for when it appears its immediatly tangled within your trap.
After a moment it struggles free and flies away leaving a single scale.
You head to your princess Justina! Proudly proffering the scale from the dragon to show your bravery.
she gasps and takes it. "This will make a nice plate for dinner!" and invites you to eat with her.

Together you live happily ever after and fondly think about how great a plate makes for an anniversary gift.

-- wait no sorry I didn't get you a plate --
''')),('B',"Press 'B' to design it in cad before constructing your trap",(-2,'''
You head home and markup a quick draft of a trap. It starts off great...
but after you try mating some parts everything goes to hell...

finally in a fit of rage you remove all constraints and 
move everything to a "good enough" position. You print off your plan then head into the woods and set it up.
hours pass and a dragon appears the dragon swoops down and all the magicaly designed parts crush in smooshing the dragon like a bug
You find a bloody claw and bring it to your princess Justina as a gift.
"This will make a cool knife" she exclaims and uses it to eat dinner.

Together you live happily ever after.
'''))]),
Page('''
  Do you like it?
  I'm not sure how to wrap it digitally really.
  Anyways I hope to slowly get you files for all the songs you like 
  so you can listen to them offline/don't have to use spotify.
''', prev_page=6),
Page('''
  Anyways I thought alot and I nearly got you a projector cause 
  I thought thats what you were hinting you wanted 100%
  after learning you just wanted me to think about it I did
  and decided you wouldn't like it as much as you thought you did and 
  got you a robe/kimono because I thought you would use it a bunch and really like it.

  I'm sorry if I assumed wrong >_< and I really hope you do actually like it.
'''),
Page('''
  I'm also sorry if this is a dumb letter/you would rather I wrote it out by hand...
  If thats the case please tell me and I'll remember for next time.

  If not then I guess I have a whole year to work on your next card :3
'''),
Page('''
  I love you.

  I love you so much and every moment I long for you to cuddle me.

  Thats all I wanted to say with this card.

  If you want to see how dumb I am you can try pressing keys a bunch and reading the 
  things up above I wanted to tell you.

  If you want to see me being even more dumb you can scroll back and try the flipbook. 
  (I don't recommend it)

  Otherwise press 'q' to quit and give me a snuggle kthanksbye 
''', can_advance=False)
]
endings = set()
_current_page = 0
def story_run(screen):
    global _current_page
    win = curses.newwin(20, 100, 30, 3)
    winB = curses.newwin(22, 102, 29, 2)
    winB.border()
    winB.overlay(screen)
    win.addstr(3,2, str(book[_current_page]), curses.color_pair(5))
    
    win.addstr(18, 2, 'Press "down" or "Right" for next page "up" or "left" for previous page' if (_current_page <= ADVENTURE_START or _current_page >= 13) else "press up/left to exit story or 'r' to restart story", curses.color_pair(2))
    win.addstr(18, 90, f'pg: {_current_page}', curses.color_pair(5))
    
    if book[_current_page].choices is not None:
        tmp_counter = 0
        for choice,text,to_page in book[_current_page].choices[::-1]:
            win.addstr(16-tmp_counter, 3, text, curses.color_pair(6))
            tmp_counter += 1
    
    win.overlay(screen)
    
    entered = screen.getkey()
    if entered == 'q':
        # print(f"Endings {endings}")
        return True
    elif entered.upper() == "R":
        if _current_page >= ADVENTURE_START:
            _current_page = ADVENTURE_START
    elif entered == "KEY_DOWN" or entered == "KEY_RIGHT":
        if book[_current_page].can_advance:
            _current_page += 1
    elif entered == "KEY_UP" or entered == "KEY_LEFT":
        if book[_current_page].prev_page is None:
            _current_page = max(_current_page -1, 0)
        else:
            _current_page = book[_current_page].prev_page

    if book[_current_page].choices is not None:
        for choice,text,to_page in book[_current_page].choices:
            if entered.upper() == choice:
                if isinstance(to_page, tuple):
                    
                    id, script = to_page

                    if id is -1: # bad end
                        screen.clear()
                        badscr = curses.newwin(40, 100, 30, 3)
                        badscr.addstr(0, 0, bad_end, curses.color_pair(7))
                        badscr.addstr(14, 0, script, curses.color_pair(7))
                        y, x = screen.getmaxyx()
                        
                        badscr.overlay(screen, 0, 0, y //2-10, x//2-25, y-1, x-1)
                        
                        endings.add(_current_page + ord(choice)*1000)

                        screen.getkey()
                    elif id is -2: # good end
                        screen.clear()
                        goodscr = curses.newwin(40, 160, 30, 3)
                        goodscr.addstr(0, 0, good_end, curses.color_pair(9))
                        goodscr.addstr(14, 0, script, curses.color_pair(9))
                        y, x = screen.getmaxyx()
                        
                        goodscr.overlay(screen, 0, 0, y //2-10, x//2-25, y-1, x-1)
                        
                        endings.add(_current_page + ord(choice)*1000)

                        screen.getkey()
                    elif id is -3: # gift
                        screen.clear()
                        giftscr = curses.newwin(40, 100, 30, 3)
                        giftscr.addstr(0, 0, script, curses.color_pair(10))
                        y, x = screen.getmaxyx()
                        
                        giftscr.overlay(screen, 0, 0, y //2-10, x//2-25, y-1, x-1)

                        give_reward()
                        _current_page = 13
                        screen.getkey()
                else:
                    _current_page += to_page

                if(len(endings) == 6): # out of 8-9 endings?
                    screen.clear()
                    endscr = curses.newwin(40, 100, 30, 3)
                    endscr.addstr(0, 0, lots_text, curses.color_pair(8))
                    y, x = screen.getmaxyx()

                    endscr.overlay(screen, 0, 0, y //2-10, x//2-25, y-1, x-1)
                    
                    endings.add(0)

                    screen.getkey()

                break
            
     
    return False

