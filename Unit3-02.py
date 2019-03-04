# Created by: Adam Linco
# Created on: Mar 04 2019
# Created for: ICS3U
# Daily Assignment  Unit 3-02
# This is a guessing game
from tkinter import *
import random

class Application(Frame):
    """A GUI application which which generates random number and gets user input"""

    def __init__(self, master):
        """Initialize the frame"""
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.number = random.randint(1, 101)

    def create_widgets(self):
        """Get user inputs"""
       
        Label(self, text = "Im thinking of a number between 1 and 100.").grid(row = 0, column = 0, sticky = W)
        Label(self, text = " guess it in as few attempts as possible!").grid(row = 1, column = 0, sticky = W)

       
        Label(self, text = "Take a guess:").grid(row = 2, column = 0, sticky = W)
        self.guess_ent = Entry(self)
        self.guess_ent.grid(row = 2, column = 1, sticky = W)

       
        Label(self, text = "Press submit to start the game!").grid(row = 3, column = 0, sticky = W)
        Button(self, text = "Submit", command = self.run_game).grid(row = 3, column = 1, sticky = W)


      
        self.text = Text(self, width = 75, height = 10, wrap = WORD)
        self.text.grid(row = 4, column = 0, columnspan = 4)

    def run_game(self):
        """Generate number and get user input"""
        guess = int(self.guess_ent.get())

        if guess != self.number:
            print_text = "You guessed {0}.".format(guess)

            if guess > self.number:
                print_text += " That's too high. Guess lower..."
            elif guess < self.number:
                print_text += " That's too low. Guess higher..."

            self.text.delete(0.0, END)
            self.text.insert(0.0, print_text)

            self.guess_ent.delete(0, END)
        else:
            print_text = "That's the right number! Well done!"
            self.text.delete(0.0, END)
            self.text.insert(0.0, print_text)


root = Tk()
app = Application(master=root)
root.mainloop()
