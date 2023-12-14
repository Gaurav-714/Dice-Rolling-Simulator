import random
import tkinter
from PIL import Image, ImageTk # Python Imaging Library

root = tkinter.Tk()
root.geometry('600x600') # For Tkinter Window
root.title("Roll The Dice")
root.configure(bg='#36652F') # Window's Background

line0 = tkinter.Label(root, text=".", fg='#36652F', bg='#36652F')
line0.pack() # packs widget relative to the earlier widget

line1 = tkinter.Label(root, text="Welcome To The\nDice Rolling Simulator", 
                      fg = 'white', bg='#36652F', font = 'Algerian 25')
line1.pack()

dice = [
        'Dice-Rolling-Simulator\\Die1.png',
        'Dice-Rolling-Simulator\\Die2.png',
        'Dice-Rolling-Simulator\\Die3.png',
        'Dice-Rolling-Simulator\\Die4.png',
        'Dice-Rolling-Simulator\\Die5.png',
        'Dice-Rolling-Simulator\\Die6.png'
        ]

image1 = ImageTk.PhotoImage(file='Dice-Rolling-Simulator\\Dice.png')

label1 = tkinter.Label(root, image = image1, width=400, height=400)
label1.image = image1
label1.pack()

def roll_dice(): # Function called by hitting the Button
    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image = image2, bg='#36652F') # To Update Image
    label1.image = image2 # To keep a Reference

button = tkinter.Button(root, text="Roll The Dice", font=('Algerian 12'), 
                        width=20, height=2, bg='#FE3939', fg='white', 
                        command = roll_dice)
button.pack(expand=True)

root.mainloop() # To Open Main Window