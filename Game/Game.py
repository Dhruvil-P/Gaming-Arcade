#########################################################################################################################################
############################################### Project Name: - SSD ARCADE ##############################################################
############################################### Made By: - Sumeet, Shreyas and Dhruvil ##################################################

############################################### Libraries Imported: #####################################################################
from tkinter import PhotoImage
from tkinter import messagebox
import tkinter.messagebox
from PIL import ImageTk
import webbrowser
from random import randrange
import tkinter.font as font
import random 
from tkinter import *

######################## Defining Root: ###########################################
root = Tk()
root.title("SSD ARCADE")
root.config(bg="gray17")
root.geometry('1530x950')
root.resizable(0,0)
    
#########################################################################################################################################
#########################################################################################################################################
################################################### Login Page: ########################################################################
########################################################################################################################################
#########################################################################################################################################
    
def login():
    ######################## Defining Root: ########################################
    log = Toplevel()
    log.title("Registration Page")
    log.geometry("1530x930")
    log.resizable(0,0)

    ################### Defining Function: #########################################
    def alert():
        if len(login_User_Entry.get()) == 0 or len(login_Pass_Entry.get()) == 0:
            messagebox.showerror("Warning!", "Entry field can't be empty!")
        else:
            log.destroy()
            messagebox.showinfo("Message", "You Have Sucessfully Logged In...")
     
    def Show1():
        Pass_Label = Label(log, width=50, height=2, bg="#b298dc", fg="black", text = login_Pass_Entry.get()).place(x=950, y=600)

    ################# Main Frame Code #############################################
    global login
    login = ImageTk.PhotoImage(file = "Image\\Login, Registration Page\\pexels-lucie-liz-3165335.jpg")
    imagelogin = Label(log, image = login).place(x=0, y=0, relwidth=1, relheight=1)

    login_main_frame = Frame(log, bg = "#b298dc").place(x=850,y=200, width=550, height=350)

    login_label1 = Label(log, bg = "#b298dc", text = "Login", font=("Impact", 35, "bold"), fg = "#6f2dbd").place(x=1060,y=230)

    login_User_name = Label(log, bg = "#b298dc", text = "User-Name:", font=("Goudy old style", 15, "bold"), fg = "#6f2dbd").place(x=900,y=310)
    login_User_Entry = Entry(log, font = ("Times new roman", 15))
    login_User_Entry.place(x= 900,y= 340, width=350, height = 35)
    login_User_Entry.insert(0, "")

    login_Password = Label(log, bg = "#b298dc", text = "Password:", font=("Goudy old style", 15, "bold"), fg = "#6f2dbd").place(x=900,y=390)
    login_Pass_Entry = Entry(log, font = ("Times new roman", 15), show = "*")
    login_Pass_Entry.place(x=900,y=430, width=350, height = 35)
    login_Pass_Entry.insert(0, "")
    
    Show_P1 = Button(log, command = Show1, width=5, height=2, text="SHOW", bg="#b298dc", cursor="hand2").place(x=1300, y=430)

    login_forget = Button(log, text = "Forgot_Password ?", fg = "#6f2dbd", bg = "#b298dc", bd=0, font = ("Times new roman", 12), cursor="hand2").place(x=900,y=480)

    login_signin = Button(log, text = "Sign-In", fg = "#6f2dbd", bg = "#b298dc", font = ("Times new roman", 20), command = alert, cursor="hand2").place(x=900,y=520, width=190, height=50)
    
    login_Exit = Button(log, text = "Exit", fg = "#6f2dbd", bg = "#b298dc", font = ("Times new roman", 20), command = lambda : log.destroy(), cursor="hand2").place(x=1150,y=520, width=190, height=50)
    ############################# Login Page Code End ######################################
  
#########################################################################################################################################
#########################################################################################################################################  
########################################################## Registration Page: ##########################################################
#########################################################################################################################################
#########################################################################################################################################

def reg():
    ######################## Defining Root: ########################################
    reg = Toplevel()
    reg.title("Registration Page")
    reg.geometry("1530x930")
    reg.resizable(0,0)

    ################### Defining Function: #########################################
    def alert():
        if len(First_Entry.get()) == 0 or len(Last_Entry.get()) == 0 or len(Pass_Entry.get()) == 0 or len(Email_Entry.get()) == 0:
            messagebox.showerror("Warning!", "Entry field can't be empty!")
        else:
            reg.destroy()
            messagebox.showinfo("Message", "You Have Succesfully Registered...")

    def Show2():
        Pass_Label = Label(reg, width=50, height=2, bg="#b298dc", fg="black", text = Pass_Entry.get()).place(x=950, y=700)
        
    global img
    img = ImageTk.PhotoImage(file = "Image\\Login, Registration Page\\pexels-lucie-liz-3165335.jpg")
    image1 = Label(reg, image = img).place(x=0, y=0, relwidth=1, relheight=1)

    ################# Main Frame Code #############################################
    main_frame = Frame(reg, bg = "#b298dc").place(x=850,y=200, width=550, height=460)

    label1 = Label(reg, bg = "#b298dc", text = "Registration", font=("Impact", 35, "bold"), fg = "#6f2dbd").place(x=1000,y=230)

    First_name = Label(reg, bg = "#b298dc", text = "First Name:", font=("Goudy old style", 15, "bold"), fg = "#6f2dbd").place(x=900,y=310)
    First_Entry = Entry(reg, font = ("Times new roman", 15))
    First_Entry.place(x= 900,y= 340, width=350, height = 35)
    First_Entry.insert(0, "")

    last_name = Label(reg, bg = "#b298dc", text = "Last Name:", font=("Goudy old style", 15, "bold"), fg = "#6f2dbd").place(x=900,y=380)
    Last_Entry = Entry(reg, font = ("Times new roman", 15))
    Last_Entry.place(x=900,y= 410, width=350, height = 35)
    Last_Entry.insert(0, "")


    Password = Label(reg, bg = "#b298dc", text = "Password:", font=("Goudy old style", 15, "bold"), fg = "#6f2dbd").place(x=900,y=450)
    Pass_Entry = Entry(reg, font = ("Times new roman", 15), show = "*")
    Pass_Entry.place(x=900,y=480, width=350, height = 35)
    Pass_Entry.insert(0, "")

    Show_P2 = Button(reg, command = Show2, width=5, height=2, text="SHOW", bg="#b298dc", cursor="hand2").place(x=1300, y=480)

    Email = Label(reg, bg = "#b298dc", text = "Email:", font=("Goudy old style", 15, "bold"), fg = "#6f2dbd").place(x=900,y=520)
    Email_Entry = Entry(reg, font = ("Times new roman", 15))
    Email_Entry.place(x=900,y=550, width=350, height = 35)
    Email_Entry.insert(0, "")

    register_button = Button(reg, text = "Sign-Up", fg = "#6f2dbd", bg = "#b298dc", font = ("Times new roman", 20), command = alert, cursor="hand2").place(x=900,y=625, width=190, height=50)
    
    register_exit = Button(reg, text = "Exit", fg = "#6f2dbd", bg = "#b298dc", font = ("Times new roman", 20), command = lambda : reg.destroy(), cursor="hand2").place(x=1150,y=625, width=190, height=50)
    ############################# Registration Page Code End ######################################    
  
#########################################################################################################################################
#########################################################################################################################################  
######################################################### Shreyas' Guessing Game: #####################################################
#########################################################################################################################################
#########################################################################################################################################
    
def openguess():
    Shreyas = Toplevel()
    Shreyas.title("Guessing Game")
    Shreyas.geometry("1530x930")
    Shreyas.resizable(0,0)
    Shreyas.config(background = "#c1a1d3")

    Top = Frame(Shreyas, bg = '#c1a1d3', pady = 2, width = 1350, height = 100, relief = RIDGE).grid(row=0,column=0)

    Title = Label(Shreyas, font = ('arial', 50, 'bold'), text = "Guessing Game", bd = 21, bg = '#c1a1d3', fg = '#252525', justify = CENTER).place(x=480,y=10)

    MainFrame = Frame(Shreyas, bg = '#11698e', bd = 10, width = 1350, height= 600, relief = RIDGE)
    MainFrame.grid(row = 1, column = 0, pady = 20, padx = 90)

    global img
    img = PhotoImage(file = "Image\\Shreyas\\shreyas.png")

    canvas = Canvas(Shreyas, width = 335, height = 180, bg = '#11698e')      
    canvas.place(x=220, y=200)      
    canvas.create_image(-10,-10, anchor=NW, image=img)

    def openshreyas():
        Guess = Toplevel()
        Guess.title("Guessing Game")
        Guess.geometry("820x810+300+0")
        Guess.config(bg="#41aea9")
        myFont = font.Font(family='Comic Sans MS Bold')
        
        # Constantia Bold
        # Comic Sans MS Bold
        global guess
        global totalNumberOfGuesses
        global lblInst_frame
        global lblInst
        global lblLine0_frame
        global lblNoGuess_frame
        global lblNoGuess
        global lblMaxGuess
        global lblLine1
        global lblLine2
        global buttons
        global guess_row
        lblInst_frame = LabelFrame(Guess, border=5, width=300, height=45, bg="teal")
        lblInst_frame.place(x=268, y=26)
        lblInst = Label(Guess, text="Guess a number from 0 to 9",
                        bg="#41aea9", fg="#e8ffff", font=myFont)
        lblLine0_frame = LabelFrame(Guess, border=5, width=240, height=45, bg="teal")
        lblLine0_frame.place(x=130, y=155)
        lblLine0 = Label(Guess, text="---------------------------------------------------------------------",
                            bg="#41aea9", fg="#e8ffff", font=myFont)
        lblNoGuess_frame = LabelFrame(Guess, border=5, width=152, height=45, bg="teal")
        lblNoGuess_frame.place(x=591, y=155)
        lblNoGuess = Label(Guess, text="No of Guesses: 0",
                            bg="#41aea9", fg="#e8ffff", font=myFont)
        lblMaxGuess = Label(Guess, text="Max Guess: 3",
                            bg="#41aea9", fg="#e8ffff", font=myFont)
        lblLine1 = Label(Guess, text="---------------------------------------------------------------------",
                            bg="#41aea9", fg="#e8ffff", font=myFont)
        global lblLogs
        lblLogs = Label(Guess, text="Score Board",
                        bg="#41aea9", fg="#e8ffff", font=myFont)
        lblLine2 = Label(Guess, text="---------------------------------------------------------------------",
                            bg="#41aea9", fg="#e8ffff", font=myFont)
        
        Exit_shreyas1 = Button(Guess, bg="#41aea9", fg="#e8ffff", font=myFont, text="EXIT", width=10, command = lambda : Guess.destroy(), cursor="hand2").place(x= 100, y=750)
        Exit_shreyas2 = Button(Guess, bg="#41aea9", fg="#e8ffff", font=myFont, text="EXIT", width=10, command = lambda : Guess.destroy(), cursor="hand2").place(x= 600, y=750)
        
        # create the buttons
        global buttons
        buttons = []


        for index in range(0, 10):
            button = Button(Guess, text=index, command=lambda index=index: process(
                index), state=DISABLED, bg="#41aea9", fg="#e8ffff", font=myFont, padx=15, pady=15)
            buttons.append(button)

        global btnStartGameList
        btnStartGameList = []
        for index in range(0, 1):
            btnStartGame =   Button(Guess, text="Start Game", cursor="hand2", command=lambda: startgame(
                index), bg="#41aea9", fg="#e8ffff", font=myFont)  # lambda functions are one liner functions
            btnStartGameList.append(btnStartGame)
            
        # append elements to grid
        
        lblInst.grid(row=0, column=0, columnspan=5, pady=30)
        lblLine0.grid(row=1, column=0, columnspan=5, pady=10)
        lblNoGuess.grid(row=2, column=0, columnspan=3, pady=10)
        lblMaxGuess.grid(row=2, column=3, columnspan=2, pady=10)
        lblLine1.grid(row=3, column=0, columnspan=5, pady=10)
        # row 4 - 8 is reserved for showing logs
        lblLogs.grid(row=4, column=0, columnspan=5, pady=10)

        lblLine2.grid(row=9, column=0, columnspan=5, pady=10)
        
        global i
        for row in range(0, 2):
            for col in range(0, 5):
                i = row * 5 + col  # convert 2d index to 1d. 5= total number of columns
                buttons[i].grid(row=row+10, column=col, pady=10)

        btnStartGameList[0].grid(row=13, column=0, columnspan=5, pady=20)
        
        # Main game logic

        guess = 0
        totalNumberOfGuesses = 0
        secretNumber = randrange(10)
        print(secretNumber)
        lblLogs = []
        guess_row = 4

        # reset all variables
        
        def init():
            global buttons, guess, totalNumberOfGuesses, secretNumber, lblNoGuess, lblLogs, guess_row
            guess = 0
            totalNumberOfGuesses = 0
            secretNumber = randrange(10)
            print(secretNumber)
            lblNoGuess["text"] = "Number of Guesses: 0"
            guess_row = 4

            # remove all score on init
            for lblLog in lblLogs:
                lblLog.grid_forget()
            lblLogs = []
            
        global lbl
        global msg
        def process(i):
            global totalNumberOfGuesses, buttons, guess_row
            guess = i

            totalNumberOfGuesses += 1
            lblNoGuess["text"] = ("Number of Guesses: " + str(totalNumberOfGuesses))

            # check if guess match secret number
            if guess == secretNumber:
                lbl =   Label(Guess, text="Your guess was right. You won! :) ",
                            fg="green", bg="#41aea9", pady=10, font=myFont)
                lbl.grid(row=guess_row, column=0, columnspan=5)
                ########### POP_UP MESSAGE ##############################
                pop = Toplevel()
                pop.geometry('500x300+500+250')
                pop.title("Pop-up")
                pop.resizable(0,0)
                pop.configure(background = '#41aea9')
                
                title = Label(pop, font = ('arial', 20, 'bold'), text = "You Guess is right!!!", bd = 21, fg="#fff", bg="#41aea9", justify = CENTER).place(x=100,y=100)                

                def close():
                    pop.destroy()
                    
                global okkbtn
                Okkbtn = Button(pop, text="OK", width=10, fg="#fff", bg="#41aea9", command=close, cursor="hand2").place(x=200, y=200)
                lblLogs.append(lbl)
                guess_row += 1

                for b in buttons:
                    b["state"] =   DISABLED
            else:
                # give player some hints
                if guess > secretNumber:
                    lbl =   Label(
                        Guess, text="Secret number is less than your current guess :)", fg="red", bg="#41aea9", pady=10, font=myFont)
                    lbl.grid(row=guess_row, column=0, columnspan=5)
                    lblLogs.append(lbl)
                    guess_row += 1
                else:
                    lbl =   Label(
                        Guess, text="Secret number is greater than your current guess :)", fg="red", bg="#41aea9", pady=10, font=myFont)
                    lbl.grid(row=guess_row, column=0, columnspan=5)
                    lblLogs.append(lbl)
                    guess_row += 1

            # game is over when max no of guesses is reached
            if totalNumberOfGuesses == 3:
                if guess != secretNumber:
                    lbl =   Label(
                        Guess, text="Max guesses reached. You lost! :)", fg="red", bg="#41aea9", font=myFont)
                    lbl.grid(row=guess_row, column=0, columnspan=5, pady=10)
                    lblLogs.append(lbl)
                    guess_row += 1

                for b in buttons:
                    b["state"] =   DISABLED

            buttons[i]["state"] =   DISABLED
        
        global status    
        status = "none"


        def startgame(i):
            global status
            for b in buttons:
                b["state"] =   NORMAL

            if status == "none":
                status = "started"
                btnStartGameList[i]["text"] = "Restart Game"
            else:
                status = "restarted"
                init()
            print("Game started")
            
            


    Div = LabelFrame(MainFrame, width=5, height=520, bg="#0a043c", border=5).place(x=600, y=30)

    Head_Frame = LabelFrame(MainFrame, width=600, height=70, bg="#cdfffc", border=5).place(x=680, y=40)

    label1 = Label(MainFrame, text = "Description", bg='#cdfffc', fg = '#00303f', font = ('arial', 30, 'bold')).place(x = 840, y=50)

    Desc_Frame = LabelFrame(MainFrame, width=600, height=370, bg="#cdfffc", border=5).place(x=680, y=150)

    des1 = Label(MainFrame, text = "~> The Classic Game", bg='#cdfffc', fg = '#312c51', font = ('arial', 20, 'bold')).place(x = 700, y=160)

    des2 = Label(MainFrame, text = "~> SinglePlayer Mode", bg='#cdfffc', fg = '#312c51', font = ('arial', 20, 'bold')).place(x = 700, y=220)

    des3 = Label(MainFrame, text = "~> Thrilling and full of joy", bg='#cdfffc', fg = '#312c51', font = ('arial', 20, 'bold')).place(x = 700, y= 280)

    des4 = Label(MainFrame, text = "~> Not so complicated", bg='#cdfffc', fg = '#312c51', font = ('arial', 20, 'bold')).place(x = 700, y=340)

    des4 = Label(MainFrame, text = "~> Guess a number and keep playing", bg='#cdfffc', fg = '#312c51', font = ('arial', 20, 'bold')).place(x = 700, y=400)

    des5 = Label(MainFrame, text = "Have Fun!", bg='#cdfffc', fg = '#c0e218', font = ('arial', 20, 'bold')).place(x = 920, y= 450)

    Button_Frame = LabelFrame(Shreyas, border=5, width=380, height=200, bg="#e8efeb").place(x=200, y=420) 

    Rod1 = LabelFrame(Shreyas, width=5, height=50, bg="#0a043c", border=5).place(x=280, y=380)

    Rod2 = LabelFrame(Shreyas, width=5, height=50, bg="#0a043c", border=5).place(x=480, y=380)

    ############################################################################################################################
    Play_frame = LabelFrame(Shreyas, border=5, width=90, height=130, bg="#8DDAF4").place(x=240, y=455)

    global p2
    canvas = Canvas(Shreyas, width = 65, height = 75, bg="Cyan")      
    canvas.place(x=250, y=465) 
    p2 = PhotoImage(file = "Image\\Shreyas\\Play.gif")     
    canvas.create_image(-50,-40, anchor=NW, image=p2)

    Play = Button(Shreyas, text="PLAY", bg="#35DDAA", command = openshreyas, cursor="hand2").place(x=265, y=550)

    ###############################################################################################################################
    Exit_frame = LabelFrame(Shreyas, border=5, width=90, height=130, bg="#8DDAF4").place(x=440, y=455)

    global p3
    canvas = Canvas(Shreyas, width = 65, height = 75, bg="#696868")      
    canvas.place(x=450, y=465) 
    p3 = PhotoImage(file = "Image\\Shreyas\\Quit.png")     
    canvas.create_image(-10, -10, anchor=NW, image=p3)

    Exit = Button(Shreyas, text="EXIT", bg="#35DDAA", command=lambda : Shreyas.destroy(), cursor="hand2").place(x=467, y=550)

#########################################################################################################################################
#########################################################################################################################################
#################################################### Dhruvil's Color Game: #############################################################
#########################################################################################################################################
#########################################################################################################################################

def colorgame():
    Main = Toplevel()
    Main.config(background = "#009BDA")
    Main.geometry("1530x930")
    Main.resizable(0, 0)
    Main.title("Home Page")
    
    def Game():
        Game = Toplevel()
        Game.title("GAME") 
        Game.geometry("800x500+400+150") 
        Game.config(bg = "#032B39")
        Game.resizable(0, 0)
        # list of possible colour. 
        colours = ['Red','Blue','Green','Pink','Black','Cyan', 
                'Yellow','Orange','White','Purple','Brown'] 
        global score
        score = 0
        global timeleft  
        # the game time left, initially 30 seconds. 
        timeleft = 30
        
        # function that will start the game. 
        def startGame(event):   
            if timeleft == 30: 
                
                # start the countdown timer. 
                countdown() 
                
            # run the function to 
            # choose the next colour. 
            nextColour() 
        
        # Function to choose and 
        # display the next colour. 
        def nextColour(): 
        
            # use the globally declared 'score' 
            # and 'play' variables above. 
            global score 
            global timeleft 
        
            # if a game is currently in play 
            if timeleft > 0: 
        
                # make the text entry box active. 
                e.focus_set() 
        
                # if the colour typed is equal 
                # to the colour of the text 
                if e.get().lower() == colours[1].lower(): 
                    
                    score += 1
        
                # clear the text entry box. 
                e.delete(0, tkinter.END) 
                
                random.shuffle(colours) 
                
                # change the colour to type, by changing the 
                # text _and_ the colour to a random colour value 
                label.config(fg = str(colours[1]), text = str(colours[0])) 
                
                # update the score. 
                scoreLabel.config(text = "Score: " + str(score)) 
        
        
        # Countdown timer function  
        def countdown(): 
        
            global timeleft 
        
            # if a game is in play 
            if timeleft > 0: 
        
                # decrement the timer. 
                timeleft -= 1
                
                # update the time left label 
                timeLabel.config(text = "Time left: "
                                    + str(timeleft)) 
                                        
                # run the function again after 1 second. 
                timeLabel.after(1000, countdown) 
        
        def Replay():
            global timeleft
            global score
            if timeleft < 30 or score > 0 or score == 0:
                score = 0 
                # the game time left, initially 30 seconds.  
                timeleft = 30

                # function that will start the game. 
                def startGame():   
                    if timeleft == 30: 

                        # Countdown timer function  
                        def countdown(): 
                        
                            global timeleft 

                            # if a game is in play 
                            if timeleft > 0: 
                            
                                # decrement the timer. 
                                timeleft -= 0

                                # update the time left label 
                                timeLabel.config(text = "Time left: "
                                                    + str(timeleft)) 

                                # run the function again after 1 second. 
                                timeLabel.after(1000, countdown) 
                                # start the countdown timer. 
                        countdown() 

                        # Function to choose and 
                        # display the next colour. 
                        def nextColour(): 
                        
                            # use the globally declared 'score' 
                            # and 'play' variables above. 
                            global score 
                            global timeleft 
        
                            # if a game is currently in play 
                            if timeleft > 0: 
                            
                                # make the text entry box active. 
                                e.focus_set() 
        
                                # if the colour typed is equal 
                                # to the colour of the text 
                                if e.get().lower() == colours[1].lower(): 
                                
                                    score += 1
        
                                # clear the text entry box. 
                                e.delete(0, tkinter.END) 
        
                                random.shuffle(colours) 
        
                                # change the colour to type, by changing the 
                                # text _and_ the colour to a random colour value 
                                label.config(fg = str(colours[1]), text = str(colours[0])) 
        
                                # update the score. 
                                scoreLabel.config(text = "Score: " + str(score)) 
                                scoreLabel.place(x=370, y=45)
                        # run the function to 
                        # choose the next colour. 
                        nextColour() 

                startGame() 
               
        # Side Images
        global Left
        canvas = Canvas(Game, width = 400, height = 340, bg="#696868")      
        canvas.place(x=0, y=10) 
        Left = PhotoImage(file = "Image\\Dhruvil\\Run.png")     
        canvas.create_image(0, 200, anchor="w", image=Left)
        
        global Right
        canvas = Canvas(Game, width = 400, height = 340, bg="#696868")      
        canvas.place(x=400, y=10) 
        Right = PhotoImage(file = "Image\\Dhruvil\\Thanks.png")     
        canvas.create_image(280, 200, anchor="w", image=Right)
        # add an instructions label 
        global Info
        Info = tkinter.LabelFrame(Game, border=5, width=800, height=40, bg="#66EE99").place(x=0, y=0)
        Info_text = tkinter.Label(Game, text = "Type in the colour of the words, and not the word text!", bg="#66EE99", font = ('Helvetica', 12)) 
        Info_text.place(x=230, y=5)  
        
        # add a score label 
        global Score
        Score = tkinter.LabelFrame(Game, border=5, width=600, height=40, bg="#8BD1EC").place(x=100, y=40)
        scoreLabel = tkinter.Label(Game, text = "Press enter to shoot!", bg="#8BD1EC", font = ('Helvetica', 12)) 
        scoreLabel.place(x=330 ,y=45) 
        
        # add a time left label 
        global Time
        Time = tkinter.LabelFrame(Game, border=5, width=550, height=40, bg="#7F71D2").place(x=125, y=80)
        timeLabel = tkinter.Label(Game, text = "Time left: " +str(timeleft), bg="#7F71D2", font = ('Helvetica', 12)) 
                        
        timeLabel.place(x=360, y=85) 
        
        # add a label for displaying the colours 
        Label = tkinter.LabelFrame(Game, border=5, width=500, height=120, bg="#d6b0b1").place(x=150, y=120)
        label = tkinter.Label(Game, font = ('Helvetica', 60), bg="#d6b0b1") 
        label.place(x=270, y=130) 
        
        # add a text entry box for 
        # typing in colours 
        Entry = tkinter.LabelFrame(Game, border=5, width=200, height=40, bg="#E29AF2").place(x=300, y=260)
        e = tkinter.Entry(Game) 
        
        # run the 'startGame' function  
        # when the enter key is pressed 
        Game.bind('<Return>', startGame) 
        e.place(x=335, y=270) 
        
        # set focus on the entry box 
        e.focus_set() 
        
        # Restart ############################################################################################################
        _Bar1 = LabelFrame(Game, border=0, width=5, height=70, bg="white").place(x=398, y=355)
        _Bar2 = LabelFrame(Game, border=0, width=120, height=5, bg="white").place(x=345, y=420)
        Replay_Button = Button(Game, text="RESTART", bg="#35DDAA", border=5, width=40, height=3, command = lambda : Replay(), cursor="hand2").place(x=50, y=400)
        
        # Exit #################################################################################################################
        Exit = Button(Game, text="EXIT", bg="#35DDAA", command=lambda : Game.destroy(), border=5, width=40, height=3, cursor="hand2").place(x=450, y=400)
        
    # Heading ####################################################################################################
    Heading_frame = LabelFrame(Main, border=5, width=1530, height=100, bg="Cyan").place(x=0, y=0)
    Heading = Label(Main, font = ('arial', 50, 'bold') , text="WELCOME!", bg="Cyan").place(x=550, y=4)

    # Border ####################################################################################################
    Frame = LabelFrame(Main, border=5, width=1350, height=700, bg="#623CEE").place(x=80, y=120)

    # Logo #######################################################################################################3\
    Logo_frame = LabelFrame(Main, border=5, width=790, height=400, bg="#B286D6").place(x=130, y=150)

    global p1
    p1 = PhotoImage(file = "Image\\Dhruvil\\Logo.png")
    canvas = Canvas(Main, width = 440, height = 290, bg="#0a043c")      
    canvas.place(x=310, y=170)          
    canvas.create_image(-20,-10, anchor=NW, image=p1)

    Topic = Label(Main, text="Color Guessing Game", bg="#0a043c", fg="White", font = ('arial', 45, 'bold')).place(x=210, y=470)

    Rod1 = LabelFrame(Main, width=5, height=70, bg="black", border=5).place(x=390, y=550)
    Rod2 = LabelFrame(Main, width=5, height=70, bg="black", border=5).place(x=640, y=550)

    # Play #########################################################################################################

    Play_frame = LabelFrame(Main, border=5, width=90, height=130, bg="#8DDAF4").place(x=350, y=615)

    global p2
    canvas = Canvas(Main, width = 65, height = 75, bg="Cyan")      
    canvas.place(x=360, y=625) 
    p2 = PhotoImage(file = "Image\\Dhruvil\\Play.gif")     
    canvas.create_image(-50,-40, anchor=NW, image=p2)

    Play = Button(Main, text="PLAY", bg="#35DDAA", command=Game, cursor="hand2").place(x=375, y=710)

    # Exit #########################################################################################################
    Exit_frame = LabelFrame(Main, border=5, width=90, height=130, bg="#8DDAF4").place(x=600, y=615)

    global p3
    canvas = Canvas(Main, width = 65, height = 75, bg="#696868")      
    canvas.place(x=610, y=625) 
    p3 = PhotoImage(file = "Image\\Dhruvil\\Quit.png")     
    canvas.create_image(-10, -10, anchor=NW, image=p3)

    Exit = Button(Main, text="EXIT", bg="#35DDAA", command=lambda : Main.destroy(), cursor="hand2").place(x=630, y=710)
        
    # Instructions ########################################################################################################################3
    Info_frame = LabelFrame(Main, border=5, width=490, height=650, bg="#126378").place(x=940, y=120)
        
    Description = Label(Main, text="DESCRIPTION : ", bg="#126378", fg="black", font = ('arial', 20, 'bold')).place(x=960, y=140)
    Description = Label(Main, text="~> This is a very basic game", bg="#126378", fg="white", font = ('arial', 20)).place(x=960, y=190)
    Description = Label(Main, text="~> where you just need to type", bg="#126378", fg="white", font = ('arial', 20)).place(x=960, y=240)
    Description = Label(Main, text="the color displayed. Simple!", bg="#126378", fg="white", font = ('arial', 20)).place(x=1000, y=290)
        
    Line = Label(Main, text="__________________________________________", bg="#126378", fg="black", font=10).place(x=950, y=360) 
        
    Instructions = Label(Main, text="INSTRUCTIONS : ", bg="#126378", fg="black", font = ('arial', 20, 'bold')).place(x=960, y=410)
    Instructions = Label(Main, text="~> In this game a color name", bg="#126378", fg="white", font = ('arial', 20)).place(x=960, y=460)
    Instructions = Label(Main, text="will be a color name will be", bg="#126378", fg="white", font = ('arial', 20)).place(x=1000, y=510)
    Instructions = Label(Main, text="displayed and you have to", bg="#126378", fg="white", font = ('arial', 20)).place(x=1000, y=560)
    Instructions = Label(Main, text="type in what color does that", bg="#126378", fg="white", font = ('arial', 20)).place(x=1000, y=610)
    Instructions = Label(Main, text="text comes in. If you still", bg="#126378", fg="white", font = ('arial', 20)).place(x=1000, y=660)
    Instructions = Label(Main, text="didn't get it play the game", bg="#126378", fg="white", font = ('arial', 20)).place(x=1000, y=710)
    Instructions = Label(Main, text="once you'll get it.", bg="#126378", fg="white", font = ('arial', 20)).place(x=1000, y=760)

    # Remember ##########################################################################################################################
    Inst = LabelFrame(Main, border=5, width=1350, height=50, bg="#92B50D").place(x=80, y=768)
    Inst_data = Label(Main, text="NOTE : ", bg="#92B50D", fg="#AC1709", font=55).place(x=590, y=780)
    Inst_data = Label(Main, text="Only 1 player can play at a time.", bg="#92B50D", fg="#AC1709", font=10).place(x=658, y=780)

#########################################################################################################################################
#########################################################################################################################################
################################################# Sumeet's Tic Tac Toa Game: ###########################################################
#########################################################################################################################################
#########################################################################################################################################

def opentictactoa():
    ####################### Defining Root ################################
    Sun = Toplevel()
    Sun.title("Tic Tac Toe")
    Sun.geometry("1530x930")
    Sun.resizable(0,0)
    Sun.config(background = "#583d72")

    # --------------------------Declaring Global Variables----------------------------------
    global PlayerX
    global PlayerO
    global button
    global click
    global n
    global score
    global btnReset
    global btnNewGame
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9
    global txtPlayerX
    global txtPlayerO
    
    def tictac():
        ###################### Defining Root ############################
        tic = Toplevel()
        tic.geometry('1540x950')
        tic.title("Tic Tac Toe")
        tic.resizable(0,0)
        tic.configure(background = '#31326f')
        
        ############################################ Design Of Main Frame #################################################

        Top = Frame(tic, bg = '#31326f', pady = 2, width = 1350, height = 100, relief = RIDGE)
        Top.grid(row = 0, column = 0)

        Title = Label(Top, font = ('arial', 50, 'bold'), text = "Tic Tac Toe", bd = 21, bg = '#31326f', fg = 'Cornsilk', justify = CENTER)
        Title.grid(row = 0, column = 0)

        MainFrame = Frame(tic, bg = '#a8dda8', bd = 10, width = 1350, height= 600, relief = RIDGE)
        MainFrame.grid(row = 1, column = 0, padx = 60)

        LeftFrame = Frame(MainFrame, bd = 10, width = 750, height = 500, pady = 2, padx = 10, bg = '#a8dda8', relief = RIDGE)
        LeftFrame.pack(side = LEFT)

        RightFrame = Frame(MainFrame, bd = 10, width = 560, height = 500, pady = 10, padx = 2, bg = '#a8dda8', relief = RIDGE)
        RightFrame.pack(side = RIGHT)

        RightFrame1 = Frame(RightFrame, bd = 10, width = 560, height = 200, pady = 10, padx = 2, bg = '#a8dda8', relief = RIDGE)
        RightFrame1.grid(row = 0, column = 0)

        RightFrame2 = Frame(RightFrame, bd = 10, width = 560, height = 200, pady = 10, padx = 2, bg = '#a8dda8', relief = RIDGE)
        RightFrame2.grid(row = 1, column = 0)

        ##################################################### Setting Default Value: ################################################# 
        global PlayerX
        global PlayerO
        global button
        global click
        PlayerX = IntVar()
        PlayerO = IntVar()

        PlayerX.set(0)
        PlayerO.set(0)

        button = StringVar()
        click = True

        ##################################################### Defining Functions: ####################################################

        ############################## Function To check Whether There Is a X Or O In The Box: ######################################
        def checker (buttons):
            global click
            if buttons["text"] == " " and click == True:
                buttons["text"] = "X"
                click = False
                ScoreUpdater()
            
            elif buttons["text"] == " " and click == False:
                buttons["text"] ="O"
                click = True
                ScoreUpdater()

        ##############################Function To Reset The Game#########################################
        
        def reset():
            button1["text"] = " "
            button2["text"] = " "
            button3["text"] = " "
            button4["text"] = " "
            button5["text"] = " "
            button6["text"] = " "
            button7["text"] = " "
            button8["text"] = " "
            button9["text"] = " "

            button1.configure(background = "#bedcfa")
            button2.configure(background = "#bedcfa")
            button3.configure(background = "#bedcfa")
            button4.configure(background = "#bedcfa")
            button5.configure(background = "#bedcfa")
            button6.configure(background = "#bedcfa")
            button7.configure(background = "#bedcfa")
            button8.configure(background = "#bedcfa")
            button9.configure(background = "#bedcfa")

        ############################## Funtion To Get New Game ################################

        def NewGame():
            reset()
            PlayerX.set(0)
            PlayerO.set(0)

        ################### Function To Count Score Of The Player #######################

        def ScoreUpdater():
            global n
            global score
            if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X"):
                button1.configure(background = "powder blue")
                button2.configure(background = "powder blue")
                button3.configure(background = "powder blue")
                n = float(PlayerX.get())
                score = (n + 1)
                PlayerX.set(score)

                ########### POP_UP MESSAGE ##############################
                pop = Toplevel()
                pop.geometry('500x300+500+250')
                pop.title("Pop-up")
                pop.resizable(0,0)
                pop.configure(background = '#31326f')
                
                title = Label(pop, font = ('arial', 20, 'bold'), text = "Player X is Winner!!!", bd = 21, bg = '#31326f', fg = 'Cornsilk', justify = CENTER).place(x=100,y=100)                

                def close():
                    pop.destroy()
                    
                global okkbtn
                Okkbtn = Button(pop, text="OK", width=10, bg = '#31326f', fg = 'Cornsilk', command=close).place(x=200, y=200)

            if (button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X"):
                button4.configure(background = "green")
                button5.configure(background = "green")
                button6.configure(background = "green")
                n = float(PlayerX.get())
                score = (n + 1)
                PlayerX.set(score)
                
                ########### POP_UP MESSAGE ##############################
                pop = Toplevel()
                pop.geometry('500x300+500+250')
                pop.title("Pop-up")
                pop.resizable(0,0)
                pop.configure(background = '#31326f')
                
                title = Label(pop, font = ('arial', 20, 'bold'), text = "Player X is Winner!!!", bd = 21, bg = '#31326f', fg = 'Cornsilk', justify = CENTER).place(x=100,y=100)                

                def close():
                    pop.destroy()
                    
                global okkbtn
                Okkbtn = Button(pop, text="OK", width=10, bg = '#31326f', fg = 'Cornsilk', command=close).place(x=200, y=200)

            if (button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X"):
                button7.configure(background = "yellow")
                button8.configure(background = "yellow")
                button9.configure(background = "yellow")
                n = float(PlayerX.get())
                score = (n + 1)
                PlayerX.set(score)
                
                ########### POP_UP MESSAGE ##############################
                pop = Toplevel()
                pop.geometry('500x300+500+250')
                pop.title("Pop-up")
                pop.resizable(0,0)
                pop.configure(background = '#31326f')
                
                title = Label(pop, font = ('arial', 20, 'bold'), text = "Player X is Winner!!!", bd = 21, bg = '#31326f', fg = 'Cornsilk', justify = CENTER).place(x=100,y=100)                

                def close():
                    pop.destroy()
                    
                global okkbtn
                Okkbtn = Button(pop, text="OK", width=10, bg = '#31326f', fg = 'Cornsilk', command=close).place(x=200, y=200)

            if (button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X"):
                button1.configure(background = "red")
                button4.configure(background = "red")
                button7.configure(background = "red")
                n = float(PlayerX.get())
                score = (n + 1)
                PlayerX.set(score)
                
                ########### POP_UP MESSAGE ##############################
                pop = Toplevel()
                pop.geometry('500x300+500+250')
                pop.title("Pop-up")
                pop.resizable(0,0)
                pop.configure(background = '#31326f')
                
                title = Label(pop, font = ('arial', 20, 'bold'), text = "Player X is Winner!!!", bd = 21, bg = '#31326f', fg = 'Cornsilk', justify = CENTER).place(x=100,y=100)                

                def close():
                    pop.destroy()
                    
                global okkbtn
                Okkbtn = Button(pop, text="OK", width=10, bg = '#31326f', fg = 'Cornsilk', command=close).place(x=200, y=200)
                
            if (button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X"):
                button2.configure(background = "red")
                button5.configure(background = "red")
                button8.configure(background = "red")
                n = float(PlayerX.get())
                score = (n + 1)
                PlayerX.set(score)
                
                ########### POP_UP MESSAGE ##############################
                pop = Toplevel()
                pop.geometry('500x300+500+250')
                pop.title("Pop-up")
                pop.resizable(0,0)
                pop.configure(background = '#31326f')
                
                title = Label(pop, font = ('arial', 20, 'bold'), text = "Player X is Winner!!!", bd = 21, bg = '#31326f', fg = 'Cornsilk', justify = CENTER).place(x=100,y=100)                

                def close():
                    pop.destroy()
                    
                global okkbtn
                Okkbtn = Button(pop, text="OK", width=10, bg = '#31326f', fg = 'Cornsilk', command=close).place(x=200, y=200)
                
            if (button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"):
                button3.configure(background = "red")
                button6.configure(background = "red")
                button9.configure(background = "red")
                n = float(PlayerX.get())
                score = (n + 1)
                PlayerX.set(score)
                
                ########### POP_UP MESSAGE ##############################
                pop = Toplevel()
                pop.geometry('500x300+500+250')
                pop.title("Pop-up")
                pop.resizable(0,0)
                pop.configure(background = '#31326f')
                
                title = Label(pop, font = ('arial', 20, 'bold'), text = "Player X is Winner!!!", bd = 21, bg = '#31326f', fg = 'Cornsilk', justify = CENTER).place(x=100,y=100)                

                def close():
                    pop.destroy()
                    
                global okkbtn
                Okkbtn = Button(pop, text="OK", width=10, bg = '#31326f', fg = 'Cornsilk', command=close).place(x=200, y=200)

            if (button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X"):
                button3.configure(background = "purple")
                button5.configure(background = "purple")
                button7.configure(background = "purple")
                n = float(PlayerX.get())
                score = (n + 1)
                PlayerX.set(score)
                
                ########### POP_UP MESSAGE ##############################
                pop = Toplevel()
                pop.geometry('500x300+500+250')
                pop.title("Pop-up")
                pop.resizable(0,0)
                pop.configure(background = '#31326f')
                
                title = Label(pop, font = ('arial', 20, 'bold'), text = "Player X is Winner!!!", bd = 21, bg = '#31326f', fg = 'Cornsilk', justify = CENTER).place(x=100,y=100)                

                def close():
                    pop.destroy()
                    
                global okkbtn
                Okkbtn = Button(pop, text="OK", width=10, bg = '#31326f', fg = 'Cornsilk', command=close).place(x=200, y=200)
                
            if (button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X"):
                button1.configure(background = "purple")
                button5.configure(background = "purple")
                button9.configure(background = "purple")
                n = float(PlayerX.get())
                score = (n + 1)
                PlayerX.set(score)
                
                ########### POP_UP MESSAGE ##############################
                pop = Toplevel()
                pop.geometry('500x300+500+250')
                pop.title("Pop-up")
                pop.resizable(0,0)
                pop.configure(background = '#31326f')
                
                title = Label(pop, font = ('arial', 20, 'bold'), text = "Player X is Winner!!!", bd = 21, bg = '#31326f', fg = 'Cornsilk', justify = CENTER).place(x=100,y=100)                

                def close():
                    pop.destroy()
                    
                global okkbtn
                Okkbtn = Button(pop, text="OK", width=10, bg = '#31326f', fg = 'Cornsilk', command=close).place(x=200, y=200)

            
            if (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O"):
                button1.configure(background = "powder blue")
                button2.configure(background = "powder blue")
                button3.configure(background = "powder blue")
                n = float(PlayerO.get())
                score = (n + 1)
                PlayerO.set(score)
                
                ########### POP_UP MESSAGE ##############################
                pop = Toplevel()
                pop.geometry('500x300+500+250')
                pop.title("Pop-up")
                pop.resizable(0,0)
                pop.configure(background = '#31326f')
                
                title = Label(pop, font = ('arial', 20, 'bold'), text = "Player O is Winner!!!", bd = 21, bg = '#31326f', fg = 'Cornsilk', justify = CENTER).place(x=100,y=100)                

                def close():
                    pop.destroy()
                    
                global okkbtn
                Okkbtn = Button(pop, text="OK", width=10, bg = '#31326f', fg = 'Cornsilk', command=close).place(x=200, y=200)

            if (button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O"):
                button4.configure(background = "green")
                button5.configure(background = "green")
                button6.configure(background = "green")
                n = float(PlayerO.get())
                score = (n + 1)
                PlayerO.set(score)
                
                ########### POP_UP MESSAGE ##############################
                pop = Toplevel()
                pop.geometry('500x300+500+250')
                pop.title("Pop-up")
                pop.resizable(0,0)
                pop.configure(background = '#31326f')
                
                title = Label(pop, font = ('arial', 20, 'bold'), text = "Player O is Winner!!!", bd = 21, bg = '#31326f', fg = 'Cornsilk', justify = CENTER).place(x=100,y=100)                

                def close():
                    pop.destroy()
                    
                global okkbtn
                Okkbtn = Button(pop, text="OK", width=10, bg = '#31326f', fg = 'Cornsilk', command=close).place(x=200, y=200)

            if (button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O"):
                button7.configure(background = "red")
                button8.configure(background = "red")
                button9.configure(background = "red")
                n = float(PlayerO.get())
                score = (n + 1)
                PlayerO.set(score)
                
                ########### POP_UP MESSAGE ##############################
                pop = Toplevel()
                pop.geometry('500x300+500+250')
                pop.title("Pop-up")
                pop.resizable(0,0)
                pop.configure(background = '#31326f')
                
                title = Label(pop, font = ('arial', 20, 'bold'), text = "Player O is Winner!!!", bd = 21, bg = '#31326f', fg = 'Cornsilk', justify = CENTER).place(x=100,y=100)                

                def close():
                    pop.destroy()
                    
                global okkbtn
                Okkbtn = Button(pop, text="OK", width=10, bg = '#31326f', fg = 'Cornsilk', command=close).place(x=200, y=200)

            if (button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O"):
                button1.configure(background = "yellow")
                button5.configure(background = "yellow")
                button9.configure(background = "yellow")
                n = float(PlayerO.get())
                score = (n + 1)
                PlayerO.set(score)
                
                ########### POP_UP MESSAGE ##############################
                pop = Toplevel()
                pop.geometry('500x300+500+250')
                pop.title("Pop-up")
                pop.resizable(0,0)
                pop.configure(background = '#31326f')
                
                title = Label(pop, font = ('arial', 20, 'bold'), text = "Player O is Winner!!!", bd = 21, bg = '#31326f', fg = 'Cornsilk', justify = CENTER).place(x=100,y=100)                

                def close():
                    pop.destroy()
                    
                global okkbtn
                Okkbtn = Button(pop, text="OK", width=10, bg = '#31326f', fg = 'Cornsilk', command=close).place(x=200, y=200)

            if (button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O"):
                button3.configure(background = "purple")
                button5.configure(background = "purple")
                button7.configure(background = "purple")
                n = float(PlayerO.get())
                score = (n + 1)
                PlayerO.set(score)
                
                ########### POP_UP MESSAGE ##############################
                pop = Toplevel()
                pop.geometry('500x300+500+250')
                pop.title("Pop-up")
                pop.resizable(0,0)
                pop.configure(background = '#31326f')
                
                title = Label(pop, font = ('arial', 20, 'bold'), text = "Player O is Winner!!!", bd = 21, bg = '#31326f', fg = 'Cornsilk', justify = CENTER).place(x=100,y=100)                

                def close():
                    pop.destroy()
                    
                global okkbtn
                Okkbtn = Button(pop, text="OK", width=10, bg = '#31326f', fg = 'Cornsilk', command=close).place(x=200, y=200)
                
            if (button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O"):
                button1.configure(background = "red")
                button4.configure(background = "red")
                button7.configure(background = "red")
                n = float(PlayerX.get())
                score = (n + 1)
                PlayerX.set(score)
                
                ########### POP_UP MESSAGE ##############################
                pop = Toplevel()
                pop.geometry('500x300+500+250')
                pop.title("Pop-up")
                pop.resizable(0,0)
                pop.configure(background = '#31326f')
                
                title = Label(pop, font = ('arial', 20, 'bold'), text = "Player O is Winner!!!", bd = 21, bg = '#31326f', fg = 'Cornsilk', justify = CENTER).place(x=100,y=100)                

                def close():
                    pop.destroy()
                    
                global okkbtn
                Okkbtn = Button(pop, text="OK", width=10, bg = '#31326f', fg = 'Cornsilk', command=close).place(x=200, y=200)
                
            if (button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O"):
                button2.configure(background = "red")
                button5.configure(background = "red")
                button8.configure(background = "red")
                n = float(PlayerX.get())
                score = (n + 1)
                PlayerX.set(score)
                
                ########### POP_UP MESSAGE ##############################
                pop = Toplevel()
                pop.geometry('500x300+500+250')
                pop.title("Pop-up")
                pop.resizable(0,0)
                pop.configure(background = '#31326f')
                
                title = Label(pop, font = ('arial', 20, 'bold'), text = "Player O is Winner!!!", bd = 21, bg = '#31326f', fg = 'Cornsilk', justify = CENTER).place(x=100,y=100)                

                def close():
                    pop.destroy()
                    
                global okkbtn
                Okkbtn = Button(pop, text="OK", width=10, bg = '#31326f', fg = 'Cornsilk', command=close).place(x=200, y=200)
                
            if (button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O"):
                button3.configure(background = "red")
                button6.configure(background = "red")
                button9.configure(background = "red")
                n = float(PlayerX.get())
                score = (n + 1)
                PlayerX.set(score)
                
                ########### POP_UP MESSAGE ##############################
                pop = Toplevel()
                pop.geometry('500x300+500+250')
                pop.title("Pop-up")
                pop.resizable(0,0)
                pop.configure(background = '#31326f')
                
                title = Label(pop, font = ('arial', 20, 'bold'), text = "Player O is Winner!!!", bd = 21, bg = '#31326f', fg = 'Cornsilk', justify = CENTER).place(x=100,y=100)                

                def close():
                    pop.destroy()
                    
                global okkbtn
                Okkbtn = Button(pop, text="OK", width=10, bg = '#31326f', fg = 'Cornsilk', command=close).place(x=200, y=200)
                
        ##########################################Design For Inner MainFrame#####################################
        global btnReset
        global btnNewGame
        global txtPlayerX
        global txtPlayerO
        Title = Label(RightFrame1, font = ('arial', 40, 'bold'), text = "Player X :", padx = 2, pady = 2, bg = "#a8dda8")
        Title.grid(row = 0, column = 0, sticky = W)
        txtPlayerX = Entry(RightFrame1, font = ('arial', 50, 'bold'), bd = 2, fg = 'Black', textvariable = PlayerX ,width = 14, bg = "#effad3", justify = LEFT)
        txtPlayerX.grid(row = 0, column = 1)

        Title = Label(RightFrame1, font = ('arial', 40, 'bold'), text = "Player O :", padx = 2, pady = 2, bg = "#a8dda8")
        Title.grid(row = 1, column = 0, sticky = W)
        txtPlayerO = Entry(RightFrame1, font = ('arial', 50, 'bold'), bd = 2, fg = 'Black', textvariable = PlayerO ,width = 14, bg = "#effad3", justify = LEFT)
        txtPlayerO.grid(row = 1, column = 1)

        btnReset = Button(RightFrame2, text = "Reset", font = ("Times 40 bold"), height = 1, width = 20, command = reset, cursor="hand2")
        btnReset.grid(row = 0, column = 0, padx = 6, pady = 11)

        btnNewGame = Button(RightFrame2, text = "New Game", font = ("Times 40 bold"), height = 1, width = 20, command = NewGame, cursor="hand2")
        btnNewGame.grid(row = 1, column = 0, padx = 6, pady = 11)

        ######################################Design Of Buttons######################################################
        global button1
        global button2
        global button3
        global button4
        global button5
        global button6
        global button7
        global button8
        global button9
                
        button1 = Button(LeftFrame, text = " ", font = ("Times 26 bold"), height = 3, width = 8, bg = '#bedcfa', command = lambda :checker(button1))
        button1.grid(row = 1, column = 0, sticky = S+N+E+W)

        button2 = Button(LeftFrame, text = " ", font = ("Times 26 bold"), height = 3, width = 8, bg = '#bedcfa', command = lambda :checker(button2))
        button2.grid(row = 1, column = 1, sticky = S+N+E+W)

        button3 = Button(LeftFrame, text = " ", font = ("Times 26 bold"), height = 3, width = 8, bg = '#bedcfa', command = lambda :checker(button3))
        button3.grid(row = 1, column = 2, sticky = S+N+E+W)

        button4 = Button(LeftFrame, text = " ", font = ("Times 26 bold"), height = 3, width = 8, bg = '#bedcfa', command = lambda :checker(button4))
        button4.grid(row = 2, column = 0, sticky = S+N+E+W)

        button5 = Button(LeftFrame, text = " ", font = ("Times 26 bold"), height = 3, width = 8, bg = '#bedcfa', command = lambda :checker(button5))
        button5.grid(row = 2, column = 1, sticky = S+N+E+W)

        button6 = Button(LeftFrame, text = " ", font = ("Times 26 bold"), height = 3, width = 8, bg = '#bedcfa', command = lambda :checker(button6))
        button6.grid(row = 2, column = 2, sticky = S+N+E+W)

        button7 = Button(LeftFrame, text = " ", font = ("Times 26 bold"), height = 3, width = 8, bg = '#bedcfa', command = lambda :checker(button7))
        button7.grid(row = 3, column = 0, sticky = S+N+E+W)

        button8 = Button(LeftFrame, text = " ", font = ("Times 26 bold"), height = 3, width = 8, bg = '#bedcfa', command = lambda :checker(button8))
        button8.grid(row = 3, column = 1, sticky = S+N+E+W)

        button9 = Button(LeftFrame, text = " ", font = ("Times 26 bold"), height = 3, width = 8, bg = '#bedcfa', command = lambda :checker(button9))
        button9.grid(row = 3, column = 2, sticky = S+N+E+W)

        btnExit = Button(tic, text = "Exit", font = ("Times 15 bold"), width=117, command = lambda : tic.destroy(), cursor="hand2").place(x=63, y=690)

        #############################################End Of The Code###################################################### 
        
    ############# Main Frame Code ########################
    topsun = Frame(Sun, bg = '#583d72', pady = 2, width = 1350, height = 100, relief = RIDGE).grid(row=0,column=0)

    title = Label(Sun, font = ('arial', 50, 'bold'), text = "Tic Tac Toe Game", bd = 21, bg = '#583d72', fg = '#eff7e1', justify = CENTER).place(x=480,y=10)
    
    MainFrame = Frame(Sun, bg = '#98acf8', bd = 10, width = 1350, height= 600, relief = RIDGE)
    MainFrame.grid(row = 1, column = 0, pady = 20, padx = 90)

    Bar1 = LabelFrame(Sun, width=100, height=5, bg="#2c061f", border=5).place(x=150, y=270)

    Bar2 = LabelFrame(Sun, width=100, height=5, bg="#2c061f", border=5).place(x=545, y=270)

    Bar3 = LabelFrame(Sun, width=5, height=250, bg="#2c061f", border=5).place(x=150, y=270)

    Bar4 = LabelFrame(Sun, width=5, height=250, bg="#2c061f", border=5).place(x=645, y=270)

    Bar5 = LabelFrame(Sun, width=50, height=5, bg="#2c061f", border=5).place(x=150, y=520)

    Bar6 = LabelFrame(Sun, width=56, height=5, bg="#2c061f", border=5).place(x=590, y=515)

    ##################### Images: #############################
    global img
    img = PhotoImage(file = "Image\\Sumeet\\Logo.png")

    canvas = Canvas(Sun, width = 300, height = 140, bg = '#ffc764')      
    canvas.place(x=250, y=200)      
    canvas.create_image(-10,-10, anchor=NW, image=img)

    Div = LabelFrame(MainFrame, width=5, height=520, bg="#0a043c", border=5).place(x=600, y=30)

    Head_Frame = LabelFrame(MainFrame, width=600, height=70, bg="#cdfffc", border=5).place(x=680, y=40)

    label1 = Label(MainFrame, text = "Description", bg='#cdfffc', fg = '#252525', font = ('arial', 30, 'bold')).place(x = 840, y=50)

    Desc_Frame = LabelFrame(MainFrame, width=600, height=370, bg="#cdfffc", border=5).place(x=680, y=150)

    des1 = Label(MainFrame, text = "# The Classic Game In Beautiful Color", bg='#cdfffc', fg = '#214151', font = ('arial', 20, 'bold')).place(x = 700, y=160)

    des2 = Label(MainFrame, text = "# 2 Player Mode", bg='#cdfffc', fg = '#214151', font = ('arial', 20, 'bold')).place(x = 700, y=220)

    des3 = Label(MainFrame, text = "# Track Win/Loss ", bg='#cdfffc', fg = '#214151', font = ('arial', 20, 'bold')).place(x = 700, y= 280)

    des4 = Label(MainFrame, text = "# Show Live Score", bg='#cdfffc', fg = '#214151', font = ('arial', 20, 'bold')).place(x = 700, y=340)

    des5 = Label(MainFrame, text = "# Kids Love It!!!", bg='#cdfffc', fg = '#214151', font = ('arial', 20, 'bold')).place(x = 700, y= 400)

    note = Label(MainFrame, text = "# Note :- This Game Is Only For 2 Person...", bg='#cdfffc', fg = '#214151', font = ('arial', 20, 'bold')).place(x = 700, y= 460)

    Play_frame = LabelFrame(Sun, border=5, width=200, height=100, bg="#0a043c").place(x=200, y=500)

    global p2
    canvas = Canvas(Sun, width = 65, height = 75, bg="Cyan")      
    canvas.place(x=210, y=510) 
    p2 = PhotoImage(file = "Image\\Sumeet\\Play.gif")     
    canvas.create_image(-50,-40, anchor=NW, image=p2)

    Play = Button(Sun, text="PLAY", width=10, bg="#35DDAA", command=tictac, cursor="hand2").place(x=300, y=540)

    Exit_frame = LabelFrame(Sun, border=5, width=200, height=100, bg="#0a043c").place(x=400, y=500)

    global p3
    canvas = Canvas(Sun, width = 65, height = 75, bg="#696868")      
    canvas.place(x=520, y=510) 
    p3 = PhotoImage(file = "Image\\Sumeet\\Quit.png")     
    canvas.create_image(-10, -10, anchor=NW, image=p3)

    Exit = Button(Sun, text="EXIT", width=10, bg="#35DDAA", command=lambda : Sun.destroy(), cursor="hand2").place(x=420, y=540)

#########################################################################################################################################
#########################################################################################################################################
################################################# Contact/About Us Page: ###############################################################
#########################################################################################################################################
#########################################################################################################################################

def opencontent():
    ################# Defining Root ############################
    About = Toplevel()
    About.geometry("1530x930")
    About.resizable(0, 0)
    About.title("About")
    
    ############### Defining url callback function: ################
    def callback(url):
        webbrowser.open_new(url)

    global BG
    global image1
    ############# Image: ########################################
    BG = ImageTk.PhotoImage(file = "Image\\About\\pexels-lucie-liz-3165335.jpg")
    image1 = Label(About, image = BG).place(x=0, y=0, relwidth=1, relheight=1)

    ################## MainFrame Code ##########################
    global Main_Frame
    Main_Frame = LabelFrame(About, width=805, height=500, border=5 ,bg="#b298dc").place(x=370, y=180)

    Box1 = LabelFrame(About, width=265, height=400, border=5, bg="#6f2dbd").place(x=374, y=184)

    global a1
    a1 = PhotoImage(file = "Image\\About\\Logo-3.png")
    canvas = Canvas(About, width = 250, height = 270, bg="Cyan")      
    canvas.place(x=379, y=187)          
    canvas.create_image(-80,-70, anchor=NW, image=a1)

    Name1 = Label(About, text="Name : Shreyas Pahune", fg="#00303f", font=10, bg="#6f2dbd").place(x=400, y=480)
    
    global link1
    link1 = Label(About, text="My Github Profile", fg="#eff8ff", bg="#6f2dbd", font=5, cursor="hand2")
    link1.place(x=430, y=510)
    link1.bind("<Button-1>", lambda e: callback("https://github.com/shreyazz"))
    
    global Mail1
    Mail1 = Label(About, text="Mail : 20102023@nuv.ac.in", fg="#ffe3d8", font=5,bg="#6f2dbd").place(x=380, y=540)

    Box2 = LabelFrame(About, width=265, height=400, border=5, bg="#6f2dbd").place(x=639.3, y=184)

    global a2
    a2 = PhotoImage(file = "Image\\About\\Logo-3.png")
    canvas = Canvas(About, width = 250, height = 270, bg="Cyan")      
    canvas.place(x=645, y=188)          
    canvas.create_image(-80,-70, anchor=NW, image=a2)

    Name2 = Label(About, text="Name : Sumeet Yadav", fg="#00303f", font=10, bg="#6f2dbd").place(x=670, y=480)

    global link2
    link2 = Label(About, text="My Github Profile", fg="#eff8ff", bg="#6f2dbd", font=5, cursor="hand2")
    link2.place(x=690, y=510)
    link2.bind("<Button-1>", lambda e: callback("https://github.com/Sumeet16"))

    global Mail2
    Mail2 = Label(About, text="Mail : 20102025@nuv.ac.in", fg="#ffe3d8", font=5,bg="#6f2dbd").place(x=650, y=540)

    Box3 = LabelFrame(About, width=265, height=400, border=5, bg="#6f2dbd").place(x=905, y=184)

    global a3
    a3 = PhotoImage(file = "Image\\About\\Logo-2.png")
    canvas = Canvas(About, width = 250, height = 270, bg="Cyan")      
    canvas.place(x=911, y=185)          
    canvas.create_image(-5,-10, anchor=NW, image=a3)

    Name3 = Label(About, text="Name : Dhruvil Patel", fg="#00303f", font=10, bg="#6f2dbd").place(x=950, y=480)

    global link3
    link3 = Label(About, text="My Github Profile", fg="#eff8ff", bg="#6f2dbd", font=5, cursor="hand2")
    link3.place(x=960, y=510)
    link3.bind("<Button-1>", lambda e: callback("https://github.com/Dhruvil-P"))

    global Mail3
    Mail3 = Label(About, text="Mail : 20102006@nuv.ac.in", fg="#ffe3d8", font=5,bg="#6f2dbd").place(x=920, y=540)

    Footer = LabelFrame(About, width=800, height=100, border=5, bg="#e7d9ea").place(x=373, y=580)

    global link4
    link4 = Label(About, text="FEEDBACK", fg="#0a043c", bg="#e7d9ea", font=5, cursor="hand2")
    link4.place(x=730, y=600)
    link4.bind("<Button-1>", lambda e: callback("https://outlook.office.com/mail/inbox"))

    Info = Label(About, text="If you want to give feedback then click on feedback and mail us! Our mail ids are mentioned above.", fg="#03506f", bg="#e7d9ea").place(x=520, y=640)

    Cn_Bar1 = LabelFrame(About, width=5, height=20, bg= "cyan").place(x=400, y=680)
    Cn_Bar2 = LabelFrame(About, width=5, height=20, bg= "cyan").place(x=1135, y=680)
    Contact_Exit = Button(About, width=112, height=2, text="Back To HomePage", bg="#e7d9ea", command = lambda : About.destroy(), cursor="hand2").place(x=375, y=700)
    ######################### End of About Us Page ###############################

#########################################################################################################################################
#########################################################################################################################################
######################################################## Main Page Code Start: #########################################################
#########################################################################################################################################
#########################################################################################################################################

brandLabel = Label(root, text="", font="System 30", bg="gray17", fg="green")

Top_Frame = LabelFrame(root, bg="orange", width=1530, height=50, border=0).place(x=0, y=0)

################ Navbar frame: ##################################################
navRoot = Frame(root, bg="gray17", height=1000, width=300)
navRoot.place(x=-300, y=0)
Label(navRoot, font="Bahnschrift 15", bg="#FF8700", fg="black", height=2, width=300, padx=20).place(x=0, y=0)

################ Navbar Buttuons: ################################################
Home = Button(root, border=0, bg="orange", fg="black", text="HOME", font=10, activebackground="orange").place(x=1050, y=8)
Contact = Button(root, border=0, bg="orange", fg="black", text="CONTACT", font=10, activebackground="orange", command=opencontent, cursor="hand2").place(x=1160, y=8)
Login = Button(root, border=0, bg="orange", fg="black", text="LOGIN", font=10, activebackground="orange", command = login, cursor="hand2").place(x=1300, y=8)
Sign_Up = Button(root, border=0, bg="orange", fg="black", text="SIGN UP", font=10, activebackground="orange", command = reg, cursor="hand2").place(x=1400, y=8)

############### SSD ARCADE Frame: ###############################################
Bar1 = LabelFrame(root, width=5, height = 100, border=5, bg="#01c5c4").place(x=250, y=120)
Bar1_1 = LabelFrame(root, width=300, height = 5, border=5, bg="#01c5c4").place(x=250, y=120)
Head_Frame = LabelFrame(root, width=520, height=50, border=5, bg="#0f3057").place(x=500, y=110)
Head_Text = Label(root, text="SSD ARCADE", fg="#eeeeee", bg="#0f3057", font=10).place(x=700, y=120)
Bar2 = LabelFrame(root, width=5, height = 100, border=5, bg="#01c5c4").place(x=760, y=160)
Bar2_1 = LabelFrame(root, width=230, height = 5, border=5, bg="#01c5c4").place(x=1020, y=120)
Bar3 = LabelFrame(root, width=5, height = 100, border=5, bg="#01c5c4").place(x=1250, y=120)

############### Image: #########################################################
P1_Frame = LabelFrame(root, width=395, height = 420, border=0, bg="#bbf1fa").place(x=65, y=200)
P2_Frame = LabelFrame(root, width=395, height = 420, border=0, bg="#bbf1fa").place(x=570, y=200)
P3_Frame = LabelFrame(root, width=395, height = 420, border=0, bg="#bbf1fa").place(x=1060, y=200)

photo1 = PhotoImage(file = "Image\\Homepage\\shreyas.png")
canvas1 = Canvas(root, width = 350, height = 200, bg = 'gray17')      
canvas1.place(x=85, y=220)          
canvas1.create_image(5,3, anchor=NW, image=photo1)

photo2 = PhotoImage(file = "Image\\Homepage\\dhruvilcolorgame.png")
canvas2 = Canvas(root, width = 205, height = 200, bg = 'gray17')      
canvas2.place(x=665, y=220)          
canvas2.create_image(5,3, anchor=NW, image=photo2)

photo3 = PhotoImage(file = "Image\\Homepage\\images.png")
canvas = Canvas(root, width = 220, height = 200)      
canvas.place(x=1140, y=220)          
canvas.create_image(5,0, anchor=NW, image=photo3)

############## Main label text: ##################################################
brandLabel1 = Label(root, text="Tic Tac Toe Game", font="System 30", bg="#bbf1fa", fg="green")
brandLabel1.place(x=1080, y=450)

############# Main Body Button: #################################################
brandbtn = Button(root, text="Jump To Game", font="TimesRoman 15", bg="gray17", fg="white", activebackground="#FF8700", command=opentictactoa, cursor="hand2")
brandbtn.place(x=1180, y=550)

############ Main label text: ###################################################
brandLabel2 = Label(root, text="Color Game", font="System 30", bg="#bbf1fa", fg="green")
brandLabel2.place(x=650, y=450)

########### Main Body Button: ###################################################
brandbtn1 = Button(root, text="Jump To Game", font="TimesRoman 15", bg="gray17", fg="white", activebackground="#FF8700", command = colorgame, cursor="hand2")
brandbtn1.place(x=700, y=550)

########### Main label text: ####################################################
brandLabel3 = Label(root, text="Guessing Game", font="System 30", bg="#bbf1fa", fg="green")
brandLabel3.place(x=100, y=450)

########### Main Body Button: ###################################################
brandbtn2 = Button(root, text="Jump To Game", font="TimesRoman 15", bg="gray17", fg="white", activebackground="#FF8700", command=openguess, cursor="hand2")
brandbtn2.place(x=185, y=550)

########### Footer Frame: ########################################################
Footer_frame = LabelFrame(root, width="1530", height="500", bg="#FF8700", border=0).place(x=0, y=750)
Desc = Label(root, text="Description", fg="#FF8700",bg="gray17", font=10).place(x=700, y=755) 
Desc1 = Label(root, text="This is a home page of gaming website. This website consists of 3 games which are bewildering and fascinating!", fg="black", bg="#FF8700", font=5).place(x= 280, y=790) 

########### window in mainloop: #################################################
root.mainloop()

#########################################################################################################################################
#########################################################################################################################################
########################################################## END OF CODE##################################################################
#########################################################################################################################################
#########################################################################################################################################