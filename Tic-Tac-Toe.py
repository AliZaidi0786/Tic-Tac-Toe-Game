from tkinter import *
import pygame

root=Tk()
root.resizable(True,True)
root.title("Tic-Tac-Toe")
root.configure(bg="#03001C")

frame1=Frame(root)
frame1.pack()
titleLabel=Label(frame1, text="Tic-Tac-Toe",font=("Arial",30),bg="white",relief=RAISED,borderwidth=10)
titleLabel.pack()

frame2=Frame(root)
frame2.pack()

global winLabel
global tieLabel

pygame.mixer.init()
button_sound=pygame.mixer.Sound(r'button.wav')
win_sound=pygame.mixer.Sound(r'win.mp3')
tie_sound=pygame.mixer.Sound(r'tie.mp3')
game_sound=pygame.mixer.Sound(r'The7Seas.mp3')
game_sound.play()
game_sound.set_volume(0.1)

def reset():
   #global winLabel
   #global tieLabel
   global board
   global turn
   

   for button in buttons:
        button["text"]=" "  
    
   board ={1:" ",2:" ",3:" ",
           4:" ",5:" ",6:" ",
           7:" ",8:" ",9:" "}
   #count=count+1
   
   turn="X"

   winLabel.after(10,winLabel.destroy())
   tieLabel.after(10,tieLabel.destroy())

   #winLabel.grid_remove()
   #tieLabel.grid_remove()
   #game_sound.stop()
   #game_sound.play()

    

def check_tie():
    for i in board.keys():
        if board[i] == " " and checkwin(turn)==False:
            return False
        
    return True



#def button_disable():
    #button1.config(state=DISABLED)
    #button2.config(state=DISABLED)
    #button3.config(state=DISABLED)
    #button4.config(state=DISABLED)
    #button5.config(state=DISABLED)
    #button6.config(state=DISABLED)
    #button7.config(state=DISABLED)
    #button8.config(state=DISABLED)
    #button9.config(state=DISABLED)

#def non_click():
    #button1.destroy()

board ={1:" ",2:" ",3:" ",
        4:" ",5:" ",6:" ",
        7:" ",8:" ",9:" "}

#player='X'
turn = "X"
#count=0

def checkwin(player):
    #count=count+1
    #rows
    if board[1]==board[2]==board[3]==player: return True
    elif board[4]==board[5]==board[6]==player: return True
    elif board[7]==board[8]==board[9]==player: return True
    #columns
    elif board[1]==board[4]==board[7]==player:return True
    elif board[2]==board[5]==board[8]==player: return True
    elif board[3]==board[6]==board[9]==player: return True
    #diagonals
    elif board[1]==board[5]==board[9]==player: return True
    elif board[3]==board[5]==board[7]==player: return True
    
    return False
    

#play
def play(event):
    global turn
    global winLabel
    global tieLabel
    #global count
    button = event.widget
    buttoncheck = str(button)
    clicked = buttoncheck[-1]
    if clicked == "n":
        clicked = 1
    else:
        clicked = int(clicked)
    if clicked>=1:
        button_sound.play()
        #count=count+1
    




    if button["text"]==" ":
        if turn == "X" :
             button["text"] = "X"
             board[clicked]=turn
             if checkwin(turn):
                winLabel=Label(frame2,text=f"{turn}(Player 1) Wins The Game!",bg="cyan",font=("Italic",22))
                winLabel.grid(row=1,column=0,columnspan=3)
                #game_sound.stop()
                #win_sound.play()
                #button_disable()
                #non_click()
                #print(turn,"(Player 1) Wins The Game!")
                #print("Game Over!")
                #quit()
             turn = "O"

        else:
             button["text"] = "O"
             board[clicked]=turn
             if checkwin(turn):
                winLabel=Label(frame2,text=f"{turn}(Player 2) Wins The Game!",bg="cyan",font=("Italic",22))
                winLabel.grid(row=1,column=0,columnspan=3)
                #game_sound.stop()
                #win_sound.play()
                #button_disable()
                #non_click()
                #print(turn,"(Player 2) Wins The Game!")
                #print("Game Over!")
                #quit()
             turn = "X"
             
        #print(board)
    #if checkwin(turn):
        #print(turn,"Wins The Game!")
        #print("Game Over!")
        if check_tie()==False and checkwin(turn)==True:
            tieLabel=Label(frame2,text=f"It's a Tie!",bg="cyan",font=("Italic",50))
            tieLabel.grid(row=1,column=0,columnspan=3)
            #game_sound.stop()
            #tie_sound.play()
            turn="X"

          


#first row

button1=Button(frame2,text=" ",width=5,height=2,font=("Arial",30),bg="#474E68",relief=RAISED,borderwidth=5)
button1.grid(row=0,column=0)
button1.bind("<Button-1>",play)

button2=Button(frame2,text=" ",width=5,height=2,font=("Arial",30),bg="#474E68",relief=RAISED,borderwidth=5)
button2.grid(row=0,column=1)
button2.bind("<Button-1>",play)

button3=Button(frame2,text=" ",width=5,height=2,font=("Arial",30),bg="#474E68",relief=RAISED,borderwidth=5)
button3.grid(row=0,column=2)
button3.bind("<Button-1>",play)

#second row

button4=Button(frame2,text=" ",width=5,height=2,font=("Arial",30),bg="#474E68",relief=RAISED,borderwidth=5)
button4.grid(row=1,column=0)
button4.bind("<Button-1>",play)

button5=Button(frame2,text=" ",width=5,height=2,font=("Arial",30),bg="#474E68",relief=RAISED,borderwidth=5)
button5.grid(row=1,column=1)
button5.bind("<Button-1>",play)

button6=Button(frame2,text=" ",width=5,height=2,font=("Arial",30),bg="#474E68",relief=RAISED,borderwidth=5)
button6.grid(row=1,column=2)
button6.bind("<Button-1>",play)

#third row

button7=Button(frame2,text=" ",width=5,height=2,font=("Arial",30),bg="#474E68",relief=RAISED,borderwidth=5)
button7.grid(row=2,column=0)
button7.bind("<Button-1>",play)

button8=Button(frame2,text=" ",width=5,height=2,font=("Arial",30),bg="#474E68",relief=RAISED,borderwidth=5)
button8.grid(row=2,column=1)
button8.bind("<Button-1>",play)

button9=Button(frame2,text=" ",width=5,height=2,font=("Arial",30),bg="#474E68",relief=RAISED,borderwidth=5)
button9.grid(row=2,column=2)
button9.bind("<Button-1>",play)

#reset-button
buttonreset=Button(frame2,text="RESET",width=5,height=1,font=("Ariel",20),bg="#2c6acc",relief=RAISED,borderwidth=5,command=reset)
buttonreset.grid(row=3,column=1)

buttons=[button1,button2,button3,button4,button5,button6,button7,button8,button9]


root.mainloop()