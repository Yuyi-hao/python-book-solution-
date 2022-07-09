words = ['abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom', 'azure', 'bagpipes', 'bandwagon', 'banjo', 'bayou', 'beekeeper', 'bikini', 'blitz', 'blizzard', 'boggle', 'bookworm', 'boxcar', 'boxful', 'buckaroo','buffalo','buffoon','buxom','buzzard','buzzing','buzzwords','caliph','cobweb','cockiness','croquet','crypt','curacao','cycle','daiquiri','dirndl','disavow','dizzying','duplex','dwarves','embezzle','equip','espionage''euouae','exodus','faking','fishhook','fixable','fjord','flapjack','flopping','fluffiness','flyby','foxglove','frazzled','frizzled','fuchsia','funny','gabby','galaxy','galvanize','gazebo','giaour','gizmo','glowworm','glyph','gnarly','gnostic','gossip','grogginess','haiku','haphazard','hyphen','iatrogenic','icebox','injury','ivory','ivy','jackpot','jaundice','jawbreaker','jaywalk','jazziest','jazzy','jelly','jigsaw','jinx','jiujitsu','jockey','jogging','joking','jovial','joyful','juicy','jukebox','jumbo','kayak','kazoo','keyhole','khaki','kilobyte','kiosk','kitsch','kiwifruit','klutz','knapsack','larynx','lengths','lucky','luxury','lymph','marquis','matrix','megahertz','microwave','mnemonic','mystify','naphtha','nightclub','nowadays','numbskull','nymph','onyx','ovary','oxidize','oxygen','pajama','peekaboo','phlegm','pixel','pizazz','pneumonia','polka','pshaw','psyche','puppy','puzzling','quartz','queue','quips','quixotic','quiz','quizzes','quorum','razzmatazz','rhubarb','rhythm','rickshaw','schnapps','scratch','shiv','snazzy','sphinx','spritz','squawk','staff','strength','strengths','stretch','stronghold','stymied','subway','swivel','syndrome','thriftless','thumbscrew','topaz','transcript','transgress','transplant','triphthong','twelfth','twelfths','unknown','unworthy','unzip','uptown','vaporize','vixen','vodka','voodoo','vortex','voyeurism','walkway','waltz','wave','wavy','waxy','wellspring','wheezy','whiskey','whizzing','whomever','wimpy','witchcraft','wizard','woozy','wristwatch','wyvern','xylophone','yachtsman','yippee','yoked','youthful','yummy','zephyr','zigzag','zigzagging','zilch','zipper','zodiac','zombie']


# hangman
from tkinter import *
import random 

def isValidWord(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

class Hangman:
    def __init__(self):
        self.word = isValidWord(words)
        self.missedLetters = []
        self.str = list("*" * len(self.word))


        window = Tk()
        window.title("Hangman")

        self.width = 500
        self.height = 500
        self.canvas = Canvas(window, height=self.height, width=self.width)
        self.canvas.pack()
        self.create_scene()
        self.canvas.bind('<Key>', self.handleInput)
        self.canvas.bind("<Return>", self.replay)
        self.canvas.focus_set()

        window.mainloop()
    
    def handleInput(self,event):
        if event.char in self.word:
            self.canvas.delete('text')
            for i in range(len(self.word)):
                if self.word[i] == event.char:
                    self.str[i] = event.char
                self.canvas.delete('text')
                text = f"Guess a word : {' '.join(self.str)}"
                self.canvas.create_text(280,380, text = text, tag = "text")
        else:
            self.canvas.delete("wrong")
            self.create_hangman(len(self.missedLetters))
            self.missedLetters.append(event.char)
            text = f"Missed letters : {' '.join(self.missedLetters)}"
        
        if "".join(self.str) == self.word or len(self.missedLetters)>6:
            self.canvas.delete("text")
            self.canvas.delete("wrong")
            text = f"This word is : {''.join(self.word)}"
            self.canvas.create_text(280,380, text= text, tag= "text")
            self.canvas.create_text(280,420, text = 'To continue game press ENTER ', tag = "text")
            
    def create_hangman(self, i):
        if i==0:
            self.canvas.create_line(260, 50, 260, 80) # Rope
        elif i==1:
            self.canvas.create_oval(230, 80, 290, 140, tag="man") # Head
        elif i == 2:
            self.canvas.create_line(260, 150, 200, 230, tag='man')  # Right arm
        elif i == 3:
            self.canvas.create_line(260, 150, 320, 230, tag='man')  # Left arm
        elif i==4:
            self.canvas.create_line(260, 140, 260, 250, tag="man") # Body
        elif i==5:
            self.canvas.create_line(260, 250, 200, 310, tag="man") # Left leg
        else:
            self.canvas.create_line(260, 250, 320, 310, tag="man") # Right leg
    
    def create_scene(self):
        self.canvas.create_arc(10,430,110,480, start = 30, extent = 120, style = CHORD)
        # self.canvas.create_line(10, 480, 110, 480)
        self.canvas.create_line(60, 430, 60, 50)
        self.canvas.create_line(60, 50, 260, 50)

        text = f"Guess a word : {'*'*len(self.word)}"
        self.canvas.create_text(280,380, text = text , tag = "text")
    
    def replay(self, event):
        self.canvas.delete('man')
        self.canvas.delete("text")
        self.word = isValidWord(words)
        self.str = list("*" * len(self.word))
        text = f"Guess a word : {'*' * len(self.word)}"
        self.canvas.create_text(280,380, text = text , tag = "text")
        self.missedLetters  = []

Hangman()




