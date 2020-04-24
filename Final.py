from tkinter import *
import tkinter.messagebox
import random

""" STARTING TKINTER INTERFACE"""
tk = Tk()
tk.title("Tic Tac Toe")

#Variables
Turn = "x"
countForTie = 0
winner = " "
buttonPicker = 0



def AI_V1():
    """Basic AI"""
    global countForTie, Turn, buttonPicker
    buttonPicker = random.randint(1,9)
    if buttonPicker == 1:
        if button1["text"] == " ":
            button1["text"] = "O"
            Turn = "x"
            countForTie += 1
        else:
            AI_V1()
    elif buttonPicker == 2:
        if button2["text"] == " ":
            button2["text"] = "O"
            Turn = "x"
            countForTie += 1
        else:
            AI_V1()
    elif buttonPicker == 3:
        if button3["text"] == " ":
            button3["text"] = "O"
            Turn = "x"
            countForTie += 1
        else:
            AI_V1()
    elif buttonPicker == 4:
        if button4["text"] == " ":
            button4["text"] = "O"
            Turn = "x"
            countForTie += 1
        else:
            AI_V1()
    elif buttonPicker == 5:
        if button5["text"] == " ":
            button5["text"] = "O"
            Turn = "x"
            countForTie += 1
        else:
            AI_V1()
    elif buttonPicker == 6:
        if button6["text"] == " ":
            button6["text"] = "O"
            Turn = "x"
            countForTie += 1
        else:
            AI_V1()
    elif buttonPicker == 7:
        if button7["text"] == " ":
            button7["text"] = "O"
            Turn = "x"
            countForTie += 1
        else:
            AI_V1()
    elif buttonPicker == 8:
        if button8["text"] == " ":
            button8["text"] = "O"
            Turn = "x"
            countForTie += 1
        else:
            AI_V1()
    elif buttonPicker == 9:
        if button9["text"] == " ":
            button9["text"] = "O"
            Turn = "x"
            countForTie += 1
        else:
            AI_V1()

def end_text():
    """Text Displayed in the messagebox after the game is finished"""
    global winner

    if winner == "X":
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "You Win! \n Press \"Ok\" To See The Final Results!")

    elif winner == "O":
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "AI Win! \n Press \"Ok\" To See The Final Results!")

    elif winner == "tie":
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Its A Tie! \n Press \"Ok\" To See The Final Results!")

#Main Loop
def startGame(buttons):
    global Turn, countForTie, winner

    if buttons["text"] == " " and Turn == 'x':
        buttons["text"] = "X"
        Turn = 'o'
        countForTie += 1

    #AI
    elif Turn == "o":
        AI_V1()




    #Winning Combinations for X
    if button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X':
        button1["fg"] = "#32CD32"
        button2["fg"] = "#32CD32"
        button3["fg"] = "#32CD32"
        button4.configure(state=DISABLED)
        button5.configure(state=DISABLED)
        button6.configure(state=DISABLED)
        button7.configure(state=DISABLED)
        button8.configure(state=DISABLED)
        button9.configure(state=DISABLED)
        winner = "X"
        end_text()

    elif button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X':
        button1.configure(state=DISABLED)
        button2.configure(state=DISABLED)
        button3.configure(state=DISABLED)
        button4["fg"] = "#32CD32"
        button5["fg"] = "#32CD32"
        button6["fg"] = "#32CD32"
        button7.configure(state=DISABLED)
        button8.configure(state=DISABLED)
        button9.configure(state=DISABLED)
        winner = "X"
        end_text()

    elif button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X':
        button1.configure(state=DISABLED)
        button2.configure(state=DISABLED)
        button3.configure(state=DISABLED)
        button4.configure(state=DISABLED)
        button5.configure(state=DISABLED)
        button6.configure(state=DISABLED)
        button7["fg"] = "#32CD32"
        button8["fg"] = "#32CD32"
        button9["fg"] = "#32CD32"
        winner = "X"
        end_text()

    elif button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X':
        button1["fg"] = "#32CD32"
        button5["fg"] = "#32CD32"
        button9["fg"] = "#32CD32"
        button2.configure(state=DISABLED)
        button3.configure(state=DISABLED)
        button4.configure(state=DISABLED)
        button6.configure(state=DISABLED)
        button7.configure(state=DISABLED)
        button8.configure(state=DISABLED)
        winner = "X"
        end_text()

    elif button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X':
        button3["fg"] = "#32CD32"
        button5["fg"] = "#32CD32"
        button7["fg"] = "#32CD32"
        button1.configure(state=DISABLED)
        button2.configure(state=DISABLED)
        button4.configure(state=DISABLED)
        button6.configure(state=DISABLED)
        button8.configure(state=DISABLED)
        button9.configure(state=DISABLED)
        winner = "X"
        end_text()

    elif button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X':
        button1["fg"] = "#32CD32"
        button4["fg"] = "#32CD32"
        button7["fg"] = "#32CD32"
        button2.configure(state=DISABLED)
        button3.configure(state=DISABLED)
        button5.configure(state=DISABLED)
        button6.configure(state=DISABLED)
        button8.configure(state=DISABLED)
        button9.configure(state=DISABLED)
        winner = "X"
        end_text()

    elif button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X':
        button2["fg"] = "#32CD32"
        button5["fg"] = "#32CD32"
        button8["fg"] = "#32CD32"
        button1.configure(state=DISABLED)
        button3.configure(state=DISABLED)
        button4.configure(state=DISABLED)
        button6.configure(state=DISABLED)
        button7.configure(state=DISABLED)
        button9.configure(state=DISABLED)
        winner = "X"
        end_text()

    elif button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X':
        button3["fg"] = "#32CD32"
        button6["fg"] = "#32CD32"
        button9["fg"] = "#32CD32"
        button1.configure(state=DISABLED)
        button2.configure(state=DISABLED)
        button4.configure(state=DISABLED)
        button5.configure(state=DISABLED)
        button7.configure(state=DISABLED)
        button8.configure(state=DISABLED)
        winner = "X"
        end_text()


    #What to do for a tie
    if(countForTie == 9):
        button1.configure(state=DISABLED)
        button2.configure(state=DISABLED)
        button3.configure(state=DISABLED)
        button4.configure(state=DISABLED)
        button5.configure(state=DISABLED)
        button6.configure(state=DISABLED)
        button7.configure(state=DISABLED)
        button8.configure(state=DISABLED)
        button9.configure(state=DISABLED)
        winner = "tie"
        end_text()

    # Winning Combinations for O
    if button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O':
        button1["fg"] = "#32CD32"
        button2["fg"] = "#32CD32"
        button3["fg"] = "#32CD32"
        button4.configure(state=DISABLED)
        button5.configure(state=DISABLED)
        button6.configure(state=DISABLED)
        button7.configure(state=DISABLED)
        button8.configure(state=DISABLED)
        button9.configure(state=DISABLED)
        winner = "O"
        end_text()

    elif button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O':
        button1.configure(state=DISABLED)
        button2.configure(state=DISABLED)
        button3.configure(state=DISABLED)
        button4["fg"] = "#32CD32"
        button5["fg"] = "#32CD32"
        button6["fg"] = "#32CD32"
        button7.configure(state=DISABLED)
        button8.configure(state=DISABLED)
        button9.configure(state=DISABLED)
        winner = "O"
        end_text()

    elif button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'X':
        button1.configure(state=DISABLED)
        button2.configure(state=DISABLED)
        button3.configure(state=DISABLED)
        button4.configure(state=DISABLED)
        button5.configure(state=DISABLED)
        button6.configure(state=DISABLED)
        button7["fg"] = "#32CD32"
        button8["fg"] = "#32CD32"
        button9["fg"] = "#32CD32"
        winner = "O"
        end_text()

    elif button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O':
        button1["fg"] = "#32CD32"
        button5["fg"] = "#32CD32"
        button9["fg"] = "#32CD32"
        button2.configure(state=DISABLED)
        button3.configure(state=DISABLED)
        button4.configure(state=DISABLED)
        button6.configure(state=DISABLED)
        button7.configure(state=DISABLED)
        button8.configure(state=DISABLED)
        winner = "O"
        end_text()

    elif button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O':
        button3["fg"] = "#32CD32"
        button5["fg"] = "#32CD32"
        button7["fg"] = "#32CD32"
        button1.configure(state=DISABLED)
        button2.configure(state=DISABLED)
        button4.configure(state=DISABLED)
        button6.configure(state=DISABLED)
        button8.configure(state=DISABLED)
        button9.configure(state=DISABLED)
        winner = "O"
        end_text()

    elif button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O':
        button1["fg"] = "#32CD32"
        button4["fg"] = "#32CD32"
        button7["fg"] = "#32CD32"
        button2.configure(state=DISABLED)
        button3.configure(state=DISABLED)
        button5.configure(state=DISABLED)
        button6.configure(state=DISABLED)
        button8.configure(state=DISABLED)
        button9.configure(state=DISABLED)
        winner = "O"
        end_text()

    elif button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O':
        button2["fg"] = "#32CD32"
        button5["fg"] = "#32CD32"
        button8["fg"] = "#32CD32"
        button1.configure(state=DISABLED)
        button3.configure(state=DISABLED)
        button4.configure(state=DISABLED)
        button6.configure(state=DISABLED)
        button7.configure(state=DISABLED)
        button9.configure(state=DISABLED)
        winner = "O"
        end_text()

    elif button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O':
        button3["fg"] = "#32CD32"
        button6["fg"] = "#32CD32"
        button9["fg"] = "#32CD32"
        button1.configure(state=DISABLED)
        button2.configure(state=DISABLED)
        button4.configure(state=DISABLED)
        button5.configure(state=DISABLED)
        button7.configure(state=DISABLED)
        button8.configure(state=DISABLED)
        winner = "O"
        end_text()

#Making the Buttons
button1 = Button(tk, text=" ", font='Times 20 bold', bg='white', fg='blue', height=4, width=8, command=lambda: startGame(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=' ', font='Times 20 bold', bg='white', fg='blue', height=4, width=8, command=lambda: startGame(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=' ',font='Times 20 bold', bg='white', fg='blue', height=4, width=8, command=lambda: startGame(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=' ', font='Times 20 bold', bg='white', fg='blue', height=4, width=8, command=lambda: startGame(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=' ', font='Times 20 bold', bg='white', fg='blue', height=4, width=8, command=lambda: startGame(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=' ', font='Times 20 bold', bg='white', fg='blue', height=4, width=8, command=lambda: startGame(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=' ', font='Times 20 bold', bg='white', fg='blue', height=4, width=8, command=lambda: startGame(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=' ', font='Times 20 bold', bg='white', fg='blue', height=4, width=8, command=lambda: startGame(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=' ', font='Times 20 bold', bg='white', fg='blue', height=4, width=8, command=lambda: startGame(button9))
button9.grid(row=5, column=2)

tk.mainloop()