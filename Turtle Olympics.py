############################################################
# Programmer:       Jennifer Chung
#
# Program Name: TurtleOlympics
#
#Description:   A program that stimulates the 100 meter dash at 
#               the Olympics but for turtles.
#############################################################
import turtle #allows us to use all built in functions from the turtle module
import time #allows us to use all built in functions from the time module
import tkinter #allows us to use all built in functions from the tkinter module
from random import randint #allows us to use the randint function from the random module

wn = turtle.Screen() #creates the GUI the graphics appear in
wn.bgcolor('lightblue') #changes the background colour of the screen to light blue
wn.title("Turtle Olympics") #gives the title to the pop up screen

#initializations of counters to add up and keep track of the amount of times each turtle wins
winsTim = 0 
winsDave = 0
winsManny = 0
winsAndy = 0
winsCarlos = 0

#initializations of counters to add up and keep track of the amount of times each turtle ties
tiesTim = 0
tiesDave = 0
tiesManny = 0
tiesAndy = 0
tiesCarlos = 0

#initializations of counter to add up and keep track of the amount of times the user guessed 
guesses = 0

#initializations of counter to add up and keep track of the amount of times the user guessed correctly
correct = 0

#intialization of accumulator to keep track of the user's money
totalMoney = 500

#creates turtle to write the title of the game on the screen of the pop up
title = turtle.Turtle()
title.penup()
title.color("Black")
title.goto(0,375)
title.pendown()
title.write("Olympic Turtle Race", font = ("Arial Black", 50, "normal"), align = "center")
title.ht()


#creates turtle to draw the Olympic flag
olympic = turtle.Turtle()
olympic.speed(0) 

#creates the white background of the flag
olympic.color("White")
olympic.pensize(3)
olympic.penup()
olympic.goto(-200,260)
olympic.pendown()
olympic.right(90)
olympic.begin_fill()
olympic.forward(90)
olympic.right(180)
olympic.forward(190)
olympic.right(90)
olympic.forward(400)
olympic.right(90)
olympic.forward(190)
olympic.right(90)
olympic.forward(400)
olympic.end_fill()
olympic.right(180) 

#creates the black border of the flag
olympic.color("Black")
olympic.pensize(3)
olympic.left(90)
olympic.forward(190)
olympic.right(90)
olympic.forward(400)
olympic.right(90)
olympic.forward(190)
olympic.right(90)
olympic.forward(400)
olympic.right(180)

#draws the Olympic rings
#draws the black ring
olympic.penup()
olympic.goto(0,240)
olympic.pendown()
olympic.pensize(10)
olympic.color("Black")
olympic.circle(50)

#draws the red ring
olympic.color("red")
olympic.penup()
olympic.forward(128)
olympic.pendown()
olympic.circle(50)

#draws the blue ring
olympic.color("DodgerBlue")
olympic.penup()
olympic.backward(256)
olympic.pendown()
olympic.circle(50)

#draws the green ring
olympic.color("Green")
olympic.penup()
olympic.forward(128)
olympic.forward(14)
olympic.right(90)
olympic.pendown()
olympic.circle(50)

#draws the yellow ring
olympic.color("Gold")
olympic.penup()
olympic.left(90)
olympic.backward(128)
olympic.right(90)
olympic.pendown()
olympic.circle(50)


#creates turtle to write the instructions for the game
instructions = turtle.Turtle()

#draws white box for the instructions to be written in
instructions.speed(9)
instructions.color("White")
instructions.penup()
instructions.goto(-650, -350)
instructions.pendown()
instructions.begin_fill()
instructions.forward(1285)
instructions.right(90)
instructions.forward(125)
instructions.right(90)
instructions.forward(1285)
instructions.end_fill()

#writes the instructions for the game
instructions.penup()
instructions.color("Black")
instructions.goto(-575, -375)
instructions.pendown()
instructions.write("How to play:", font = ("Arial", 14, "bold"), align = "center")
instructions.penup()
instructions.goto(-630, -400)
instructions.pendown()
instructions.write("There are 5 turtles, each turtle representing a colour of the rings in the Olympic Flag. The turtles will all start on the starting line and cross the finish line. You will have the opportunity to bet money,", font = ("Arial", 11, "normal"), align = "left")
instructions.penup()
instructions.goto(-630, -425)
instructions.pendown()
instructions.write("with your starting value of $500 on who you think will win. The amount of money you bet on is the amount of money you will receive if you have guessed correctly or lose if you have guessed", font = ("Arial", 11, "normal"), align = "left")
instructions.penup()
instructions.goto(-630, -450)
instructions.pendown()
instructions.write("incorrectly. Although if there has been a tie with another turtle you have betted on, you will unfortunately lose the money you betted and the tie won't count as a correct guess. There is no", font = ("Arial", 11, "normal"), align = "left")
instructions.penup()
instructions.goto(-630, -475)
instructions.pendown()
instructions.write("minimum amount you have to bet, but you can only bet up to the amount you have left. You can play until you want to stop or until you have $0 left.", font = ("Arial", 11, "normal"), align = "left")
instructions.ht()


#creates turtle to draw the race track for the turtle race
lanes = turtle.Turtle()
lanes.speed(10)
lanes.penup()

#fills the track blue
lanes.color("Blue")
lanes.begin_fill()
lanes.goto(-350,80)
lanes.forward(700)
lanes.right(90)
lanes.forward(375)
lanes.right(90)
lanes.forward(700)
lanes.right(90)
lanes.forward(375)
lanes.end_fill()

#creates the outline of the lanes in the track
lanes.penup()
lanes.right(90)
lanes.color("White")
lanes.pensize(3)
lanes.goto(-350,80)
lanes.pendown()
lanes.forward(700)
lanes.ht()
lanes.penup()
lanes.pensize(1)
lanes.goto(-350,5)
lanes.pendown()
lanes.forward(700)
lanes.penup()
lanes.goto(-350,-70)
lanes.pendown()
lanes.forward(700)
lanes.penup()
lanes.goto(-350,-145)
lanes.pendown()
lanes.forward(700)
lanes.penup()
lanes.goto(-350,-220)
lanes.pendown()
lanes.forward(700)
lanes.penup()
lanes.pensize(3)
lanes.goto(-350,-295)
lanes.pendown()
lanes.forward(700)

lanes.penup()
lanes.pensize(3)
lanes.goto(-300,80)
lanes.pendown()
lanes.right(90)
lanes.forward(375)

lanes.pensize(3)
lanes.right(90)
lanes.forward(50)
lanes.right(90)
lanes.forward(375)
lanes.right(90)
lanes.forward(50)

lanes.penup()
lanes.goto(300,80)
lanes.pendown()
lanes.right(90)
lanes.goto(300,-295)

lanes.right(90)
lanes.forward(-50)
lanes.right(90)
lanes.forward(375)
lanes.left(90)
lanes.forward(50)
lanes.ht()


#creates turtle to write the number on the lanes of the race track
nums = turtle.Turtle()
nums.color("White")
nums.penup()
nums.goto(-325,40)
nums.pendown()
nums.write("1", font = ("Arial", 14, "bold"), align = "center")

nums.penup()
nums.goto(-325,-35)
nums.pendown()
nums.write("2", font = ("Arial", 14, "bold"), align = "center")

nums.penup()
nums.goto(-325,-110)
nums.pendown()
nums.write("3", font = ("Arial", 14, "bold"), align = "center")

nums.penup()
nums.goto(-325,-185)
nums.pendown()
nums.write("4", font = ("Arial", 14, "bold"), align = "center")

nums.penup()
nums.goto(-325,-255)
nums.pendown()
nums.write("5", font = ("Arial", 14, "bold"), align = "center")
nums.ht()


#creates turtle to draw the finish flag 
flag = turtle.Turtle()

#draws the outline of the flag
flag.color("White")
flag.pensize(3)
flag.penup()
flag.right(90)
flag.goto(300,80)
flag.pendown()
flag.backward(180)
flag.left(90)

#fills the flag part red
flag.color("Red")
flag.begin_fill()
flag.forward(100)
flag.right(90)
flag.forward(75)
flag.right(90)
flag.forward(100)
flag.right(90)
flag.forward(75)
flag.end_fill()

#displays finish on the flag
flag.color("Black")
flag.penup()
flag.goto(352,205)
flag.write("Finish", font = ("Arial", 18, "bold"), align = "center")
flag.ht()


#creates turtles for the racers
tim = turtle.Turtle()
dave = turtle.Turtle()
manny = turtle.Turtle()
andy = turtle.Turtle()
carlos = turtle.Turtle()
tim.color("DodgerBlue")
dave.color("Gold")
manny.color("Black")
andy.color("Green")
carlos.color("Red")
tim.shape("turtle")
dave.shape("turtle")
manny.shape("turtle")
andy.shape("turtle")
carlos.shape("turtle")
 
#places each of the turtles to the starting position       
tim.up()               
dave.up()
manny.up()
andy.up()
carlos.up()
tim.goto(-320,25)
dave.goto(-320,-50)
manny.goto(-320,-125)
andy.goto(-320,-200)
carlos.goto(-320,-270)


#creates turtle to introduce each of the turtle's name.
introduction = turtle.Turtle()
introduction.penup()
introduction.goto(-425,25)
introduction.write("This is Tim.")
introduction.goto(-425,-55)
introduction.write("This is Dave.")
introduction.goto(-425,-125)
introduction.write("This is Manny.")
introduction.goto(-425,-200)
introduction.write("This is Andy.")
introduction.goto(-425,-270)
introduction.write("This is Carlos.")
introduction.ht()
    
    
#creates turtle to write count down for race
countdown = turtle.Turtle()
countdown.color ("red")
countdown.ht()
countdown.penup()
countdown.goto(0,100)
countdown.pendown()   


#creates turtle to be the announcer 
announcer = turtle.Turtle()
announcer.ht()
announcer.penup()


#creates turtle to display the amount of money user has
money = turtle.Turtle()
money.speed(0)
money.color("ForestGreen")
money.penup()
money.goto(515,435)
money.pendown()
money.write("Cash: $" + str('%1.2f'%totalMoney), font = ("Arial", 25, "bold"), align = "center")
money.ht()    


#makes a dialogue box on Turtle screen to ask if the user would like to play
playGame = tkinter.messagebox.askyesno("Play Game?", "Would you like to play the turtle olympics?")

#while the user's answer is equal to yes and they still have money it enters the loop
while playGame != False and totalMoney != 0: 
    
    #initialization of index
    index = -1

    #increments the counter to keep track of the number of guesses made
    guesses = guesses + 1
    
    #asks user to guess the turtle that will win
    userGuess = wn.textinput("Guess", "Please enter in the name of who you think will win (Tim, Dave, Manny, Andy or Carlos):") #asks the user who they think will 
    
    #asks the user how much money they would like to bet
    betAmount = wn.numinput("Bet", "Enter in the amount of money you would like to bet for which turtle you think will win :", minval = 0, maxval = totalMoney)
        
    #tells the user to enter go once they are ready to start the race
    userInput = wn.textinput("Go", "When ready type 'go': ") #asks the user to start the race
   
   
    #once user enters go, count down will start for the race and race will begin
    if userInput == "go":
        
        #displays a countdown
        for i in ["READY", "SET", "GO"]:
            countdown.write (i, font = ("Arial", 35, "normal"), align = "center")
            time.sleep(1)
            countdown.clear()
       
        #makes turtles race    
        for i in range (400):
            
            #turtles moves a random number of steps
            
            if tim.xcor() < 320:
                tim.forward(randint(1,8))   
                orderTim = i
    
            if dave.xcor() < 320:
                dave.forward(randint(1,8))  
                orderDave = i
           
            if manny.xcor() < 320:
                manny.forward(randint(1,8))
                orderManny = i   
                
            if andy.xcor() < 320:
                andy.forward(randint(1,8))
                orderAndy = i   
                
            if carlos.xcor() < 320:
                carlos.forward(randint(1,8))
                orderCarlos = i            
         
        #initialization of list to hold the ranking of the turtles                  
        rank = [orderTim, orderDave, orderManny, orderAndy, orderCarlos]
        
        #initialization of list to hold the colors/names of turtles    
        rankColour = [orderTim , orderDave, orderManny, orderAndy, orderCarlos]
         
        #ranks the turtles in order of crossing the finish line   
        rank.sort()
        rankColour.sort()
         
        #adds the colours of the turtles into the list in order of crossing the finish line   
        indexTim = rankColour.index(orderTim)
        rankColour[indexTim] = "Tim"
        indexDave = rankColour.index(orderDave)
        rankColour[indexDave] = "Dave"
        indexManny = rankColour.index(orderManny)
        rankColour[indexManny] = "Manny"
        indexAndy = rankColour.index(orderAndy)
        rankColour[indexAndy] = "Andy"
        indexCarlos = rankColour.index(orderCarlos)
        rankColour[indexCarlos] = "Carlos"   
            
        winnerCount = rank.count(rank[0])
        rankIndex = 0

        #checks if there is more than one winner
        if winnerCount > 1:
            
            #assigns ranks if there is a tie between 2 turtles        
            if winnerCount == 2:            
                firstPlace = "1st Place Tied: " + rankColour[0] + ", " + rankColour[1]
                secondPlace = "2nd Place: " + rankColour[2]
                thirdPlace = "3rd Place: " + rankColour[3]
                fourthPlace = "4th Place: " + rankColour[4]         
               
                winner = rankColour[0:2]
                if winner == "Tim":
                    winsTim = winsTim + 1
                elif winner == "Dave":
                    winsDave = winsDave + 1
                elif winner == "Manny":
                    winsManny = winsManny + 1
                elif winner == "Andy":
                    winsAndy = winsAndy + 1
                else:
                    winsCarlos = winsCarlos + 1 
                           
                #displays the ranking of the turtles in a pop up box
                tkinter.messagebox.showinfo("Results", firstPlace + "\n" + secondPlace + "\n" + thirdPlace + "\n"  + fourthPlace)
                
            #assigns ranks if there is a tie between 3 turtles    
            elif winnerCount == 3:
                firstPlace = "1st Place Tied between: " + rankColour[0] + ", " + rankColour[1] + " and " + rankColour[2]
                secondPlace = "2nd Place: " + rankColour[3]
                thirdPlace = "3rd Place: " + rankColour[4]
                      
                winner = rankColour[0:3]
                if winner == "Tim":
                    winsTim = winsTim + 1
                elif winner == "Dave":
                    winsDave = winsDave + 1
                elif winner == "Manny":
                    winsManny = winsManny + 1
                elif winner == "Andy":
                    winsAndy = winsAndy + 1
                else:
                    winsCarlos = winsCarlos + 1      
                    
                #displays the ranking of the turtles in a pop up box   
                tkinter.messagebox.showinfo("Results", firstPlace + "\n" + secondPlace + "\n" + thirdPlace)
                    
            #assigns ranks if there is a tie between 4 turtles
            elif winnerCount == 4:
                firstPlace = "1st Place Tied: " + rankColour[0] + ", " + rankColour[1] + ", " + rankColour[2] + ", " + rankColour[3]
                secondPlace = "2nd Place: " + rankColour[4]
                    
                winner = rankColour[0:4]
                if winner == "Tim":
                    winsTim = winsTim + 1
                elif winner == "Dave":
                    winsDave = winsDave + 1
                elif winner == "Manny":
                    winsManny = winsManny + 1
                elif winner == "Andy":
                    winsAndy = winsAndy + 1
                else:
                    winsCarlos = winsCarlos + 1          
                    
                #displays the ranking of the turtles in a pop up box
                tkinter.messagebox.showinfo("Results", firstPlace + "\n" + secondPlace)
                        
            #assigns ranks if there is a tie between 5 turtles
            else:
                firstPlace = "There has been a tie between all 5 turtles. Tim, Dave, Manny, Andy, Carlos all got 1st place!"    
                winner = rankColour[0:]
                winsTim = winsTim + 1
                winsDave = winsDave + 1
                winsManny = winsManny + 1
                winsAndy = winsAndy + 1
                winsCarlos = winsCarlos + 1         
                    
                #displays the ranking of the turtles in a pop up box
                tkinter.messagebox.showinfo("Results", firstPlace)       
            
            #keeps track of the number of ties per turtle  
            for rank in range (winnerCount):
                winner = rankColour[rankIndex]
                if winner == "Tim":
                    tiesTim = tiesTim + 1
                elif winner == "Dave":
                    tiesDave = tiesDave + 1
                elif winner == "Manny":
                    tiesManny = tiesManny + 1
                elif winner == "Andy":
                    tiesAndy = tiesAndy + 1
                else:
                    tiesCarlos = tiesCarlos + 1
       
                rankIndex = rankIndex + 1            
            
        #checks if there is only one winner
        else:    
            #increments the counter to keep track of the number of wins per turtle
            winner = rankColour[0]
            if winner == "Tim":
                winsTim = winsTim + 1
            elif winner == "Dave":
                winsDave = winsDave + 1
            elif winner == "Manny":
                winsManny = winsManny + 1
            elif winner == "Andy":
                winsAndy = winsAndy + 1
            else:
                winsCarlos = winsCarlos + 1    
                    
            #assigns the ranks        
            firstPlace = ("1st Place: " + rankColour[0])
            secondPlace = ("2nd Place: " + rankColour[1])
            thirdPlace = ("3rd Place: " + rankColour[2])
            fourthPlace = ("4th Place: " + rankColour[3])
            fifthPlace = ("5th Place: " + rankColour[4])     
            
            #displays the ranking of the turtles in a pop up box
            tkinter.messagebox.showinfo("Results", firstPlace + "\n" + secondPlace + "\n" + thirdPlace + "\n"  + fourthPlace + "\n" + fifthPlace)
            
            
        #checks if the user's guess is not the winner       
        if userGuess != winner:
            totalMoney = totalMoney - betAmount #subtracts the money user betted from the total money they have
            announcer.goto(0,100)
            announcer.write("You guessed incorrectly.", align = "center", font = ("Arial", 20, "normal")) #write that the user guessed incorrectly
            time.sleep(2)
            announcer.clear()   
            
        elif userGuess == winner and winnerCount > 1:
            totalMoney = totalMoney - betAmount #subtracts the money user betted from the total money they have
            announcer.goto(0,100)
            announcer.write("You guessed incorrectly.", align = "center", font = ("Arial", 20, "normal")) #write that the user guessed incorrectly 
            time.sleep(2)
            announcer.clear()              
       
        #checks if the user guessed correctly and if there is only one winner
        else:
            correct = correct + 1 #adds to the users correct guesses 
            totalMoney = totalMoney + betAmount #adds to the money user betted to the total money they have
            announcer.goto(0,100)
            announcer.write("You guessed correctly!", align = "center", font = ("Arial", 20, "normal")) #write that the user guessed correctly
            time.sleep(2)
            announcer.clear()
    
    
    #displays the new amount of money the have on the screen
    money.clear()
    money.goto(515,435)
    money.write("Cash: $" + str('%1.2f'%totalMoney), font = ("Arial", 25, "bold"), align = "center")
    money.ht()        
   
    #places each of the turtles back to the starting position      
    tim.clear()
    dave.clear()
    manny.clear()
    andy.clear()
    carlos.clear()
    tim.up()               
    dave.up()
    manny.up()
    andy.up()
    carlos.up()
    tim.goto(-320,25)
    dave.goto(-320,-50)
    manny.goto(-320,-125)
    andy.goto(-320,-200)
    carlos.goto(-320,-270) 
    
    #asks the user if they would like to play again
    playGame = tkinter.messagebox.askyesno("Play Game?", "Would you like to play again?")
 
 
#checks if the user has money and if they don't but still wrote yes to playing again, it'll display that they can't play   
if totalMoney == 0 and playGame == True:
    announcer.goto(0,100)
    announcer.write("Unfortunately you ran out of money :( Thank you for playing! Here are your results...", align = "center", font = ("Arial", 12, "normal"))
    time.sleep(3.5)
    
#thanks the user for playing and displays their results
else:
    announcer.goto(0,100)
    announcer.write("Thank you for playing! Here are your results...", align = "center", font = ("Arial", 20, "normal"))
    time.sleep(3)

#clears screen
wn.clear()


#creates turtle to write the title of the results on the screen of the pop up
title.penup()
title.color("Black")
title.goto(0,375)
title.pendown()
title.write("RESULTS", align = "center", font = ("Terminal", 75, "bold"))
title.ht()


#creates turtle to display the scores of the game on the screen
score = turtle.Turtle()
score.speed(8)

#displays how many wins each turtle got
score.penup()
score.goto(-180,100)
score.pendown()
score.write("NUMBER OF WINS", align = "left", font = ("Arial", 18, "bold"))

#amount Tim got
score.color("DodgerBlue")
score.penup()
score.goto(-180,80)
score.pendown()
score.write("Tim:", align = "left", font = ("Arial", 14, "normal"))
score.color("Black")
score.penup()
score.goto(35,80)
score.pendown()
score.write(winsTim, align = "right", font = ("Arial", 14, "normal"))

#amount Dave got
score.color("Gold")
score.penup()
score.goto(-180,60)
score.pendown()
score.write("Dave:", align = "left", font = ("Arial", 14, "normal"))
score.color("Black")
score.penup()
score.goto(35,60)
score.pendown()
score.write(winsDave, align = "right", font = ("Arial", 14, "normal"))

#amount Manny got
score.color("Black")
score.penup()
score.goto(-180,40)
score.pendown()
score.write("Manny:", align = "left", font = ("Arial", 14, "normal"))
score.penup()
score.goto(35,40)
score.pendown()
score.write(winsManny, align = "right", font = ("Arial", 14, "normal"))

#amount Andy got
score.color("Green")
score.penup()
score.goto(-180,20)
score.pendown()
score.write("Andy:", align = "left", font = ("Arial", 14, "normal"))
score.color("Black")
score.penup()
score.goto(35,20)
score.pendown()
score.write(winsAndy, align = "right", font = ("Arial", 14, "normal"))

#amount Carlos got
score.color("Red")
score.penup()
score.goto(-180,0)
score.pendown()
score.write("Carlos:", align = "left", font = ("Arial", 14, "normal"))
score.color("Black")
score.penup()
score.goto(35,0)
score.pendown()
score.write(winsCarlos, align = "right", font = ("Arial", 14, "normal"))


#displays how many ties each turtle got
score.color("Black")
score.penup()
score.goto(-180,-60)
score.pendown()
score.write("NUMBER OF TIES", align = "left", font = ("Arial", 18, "bold"))

#amount Tim got
score.color("DodgerBlue")
score.penup()
score.goto(-180,-80)
score.pendown()
score.write("Tim:", align = "left", font = ("Arial", 14, "normal"))
score.color("Black")
score.penup()
score.goto(25,-80)
score.pendown()
score.write(tiesTim, align = "right", font = ("Arial", 14, "normal"))

#amount Dave got
score.color("Gold")
score.penup()
score.goto(-180,-100)
score.pendown()
score.write("Dave:", align = "left", font = ("Arial", 14, "normal"))
score.color("Black")
score.penup()
score.goto(25,-100)
score.pendown()
score.write(tiesDave, align = "right", font = ("Arial", 14, "normal"))

#amount Manny got
score.color("BlacK")
score.penup()
score.goto(-180,-120)
score.pendown()
score.write("Manny:", align = "left", font = ("Arial", 14, "normal"))
score.penup()
score.goto(25,-120)
score.pendown()
score.write(tiesManny, align = "right", font = ("Arial", 14, "normal"))

#amount Andy got
score.color("Green")
score.penup()
score.goto(-180,-140)
score.pendown()
score.write("Andy:", align = "left", font = ("Arial", 14, "normal"))
score.color("Black")
score.penup()
score.goto(25,-140)
score.pendown()
score.write(tiesAndy, align = "right", font = ("Arial", 14, "normal"))

#amount Carlos got
score.color("Red")
score.penup()
score.goto(-180,-160)
score.pendown()
score.write("Carlos:", align = "left", font = ("Arial", 14, "normal"))
score.color("Black")
score.penup()
score.goto(25,-160)
score.pendown()
score.write(tiesCarlos, align = "right", font = ("Arial", 14, "normal"))

#displays the how many guesses they have guessed correctly overall
score.color("Black")
score.penup()
score.goto(-180,-220)
score.pendown()
score.write("NUMBER OF CORRECT GUESSES", align = "left", font = ("Arial", 18, "bold"))
score.penup()
score.goto(-180,-240)
score.pendown()
score.write(correct, align = "left", font = ("Arial", 14, "normal"))
score.penup()
score.goto(-150,-240)
score.pendown()
score.write("out of", align = "left", font = ("Arial", 14, "normal"))
score.penup()
score.goto(-90,-240)
score.pendown()
score.write(guesses, align = "left", font = ("Arial", 14, "normal"))
score.ht()
time.sleep(10)

#clears screen
wn.clear()

#writes goodbye to the user
announcer.goto(0,0)
announcer.write("GOODBYE :)", align = "center", font = ("Arial Black", 70, "normal"))
announcer.goto(0,-10)
announcer.write("(You may click to exit now.)", align = "center", font = ("Arial Black", 10, "normal"))

#keeps the screen open until user clicks the screen to close
wn.exitonclick()