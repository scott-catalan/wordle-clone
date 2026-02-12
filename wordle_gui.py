import os
from tkinter import *
from wordle_logic import WORDCHOICE, WORDS, GUESSES, CALCULATE

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
WORDS_PATH = os.path.join(ASSETS_DIR, 'words.txt')
GUESSES_PATH = os.path.join(ASSETS_DIR, 'guesses.txt')
ICON_PATH = os.path.join(ASSETS_DIR, 'logo.png')

colors = {0: '#3A3A3C', 1: "#B59F3B", 2: '#538D4E'}
currentRow = 0
words = WORDS()
guesses = GUESSES()
word = WORDCHOICE(words)
streak = 0
winCheck = 0

def RESET():
    global currentRow, word, streak, winCheck
    currentRow = 0
    word = WORDCHOICE(words)  

    for row in grid:
        for tile in row:
            tile.config(text="", bg="#1C1C1C")
    
    if winCheck == 0:
        streak = 0
    winCheck = 0

    winLoss.config(text="", fg="#FFFFFF")
    streakLabel.config(text = f"Streak:\n{streak}")

    userInput.config(state="normal")
    userInput.delete(0, END)
    userInput.focus_set()

def GUESS():
    global currentRow, streak, winCheck
    user = userInput.get().lower()
    if user.lower() in guesses:
        winLoss.config(text = "")
        guess = CALCULATE(user, word)
        for i in range(5):
            grid[currentRow][i].config(text = user[i].upper(), bg = colors[guess[i]])
        currentRow += 1
        
        if guess == [2, 2, 2, 2, 2]:
            winLoss.config(text = "WIN")
            userInput.config(state = "disabled")
            streak += 1
            winCheck = 1
            streakLabel.config(text = f"Streak:\n{streak}")
        elif currentRow == 6:
            winLoss.config(text = f"WORD WAS {word.upper()}")
            userInput.config(state = "disabled")

        userInput.delete(0, END)
    else:
        winLoss.config(text = "NOT IN DICTIONARY")

window = Tk()
window.geometry("620x860")
window.title("Wordle")
window.config(background = "#131313")
icon = PhotoImage(file = ICON_PATH)
window.iconphoto(True, icon)

frame1 = Frame(window, bg="#131313")
frame1.grid(row = 0, column = 0, pady = 10, padx = 20)

frame2 = Frame(window, bg="#131313")
frame2.grid(row = 1, column = 0, padx = 20)

frame3 = Frame(window, bg="#131313")
frame3.grid(row = 2, column = 0, pady = 5, padx = 20)

winLoss = Label(frame1, text = "", font = ("Helvetica", 42, "bold"), fg = "#FFFFFF", bg = "#131313")
winLoss.pack()

grid = []
for row in range(6):
    rowLabels = []
    for col in range(5):
        label = Label(frame2, text = "", width = 2, height = 1, font = ("Helvetica", 60, "bold"), fg = "#FFFFFF", bg = "#1C1C1C", relief="raised", borderwidth=4)
        label.grid(row = row, column = col, padx = 4, pady = 4)
        rowLabels.append(label)
    grid.append(rowLabels)
    
streakLabel = Label(frame3, width = 5, text = f"Streak:\n{streak}", font=("Helvetica", 23, "bold"), fg = "#FFFFFF", bg = "#131313")
streakLabel.grid(row = 0, column = 0, padx = 10)

userInput = Entry(frame3, width = 8, font=("Helvetica", 47, "bold"), justify = "center", fg = "#FFFFFF", bg = "#131313", relief="raised", borderwidth=4)
userInput.bind('<Return>', lambda event: GUESS())
userInput.grid(row = 0, column = 1)
userInput.focus_set()

resetBtn = Button(frame3, width = 6, height = 1, text = "RESET", font = ("Helvetica", 30, "bold"),
                  bg = "#B59F3B", fg = "white", command = RESET, relief = "raised", borderwidth = 2)
resetBtn.grid(row = 0, column = 2, padx = 10)

window.mainloop()