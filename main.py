'''
Source: https://www.askpython.com/python-modules/tkinter/age-calculator
Date: 21/03/2025
'''
#import window
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

#Default Numbers
happyness = int(4)


#Funtions____________________________Commands
   #Death end if happiness is too low
def ifunhappy(happiness):
   if happiness == 1:
      messagebox.showinfo('Scylla', 'If darling really hates me that much, I will let you be in my stomach forever❤️')
      messagebox.showinfo('You died', "You chose to be in the monster's stomach forever")
      exit()

   #Changing the number for happiness to an emoji
def happinesstoface(happyness):

   if happyness == 5:
      face = '😘'
      return face
   if happyness == 4:
      face = '☺️'
      return face
   if happyness == 3:
      face = '😐'
      return face
   if happyness == 2:
      face = '☹️'
      return face
   if happyness == 1:
      face = '😂'
      return face

def update():
   lb_scylla.config(text=str(happinesstoface(happyness)))
   bg.config(file=background)


#Destroying the window
def exit():
   window.destroy()



#Funtions____________________________Starting Events

   #Starting from "Wake up" scence
def wakeup():
      # Use the global variables
   global speak, event, button1, button2, button1txt, button2txt, background
      #Changing

   messagebox.showinfo('Scylla', 'Good Morning Darling~~ Here is your shirt.')
   button1txt = "Continue"
   button2txt = "Continue"
   background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\Wakeup.png"
   update()
   btn_right.config(text = button1txt, command=grabclothes)
   btn_left.config(text = button2txt, command=grabclothes)

   #Changing scence to "Grab Clothes"
def grabclothes():
      # Use the global variables
   global speak, event, button1, button2, button1txt, button2txt, background
      # Changing
   messagebox.showinfo('Scylla', 'Get into clothes quickly.')
   button1txt = "Push her"
   button2txt = "Listen quietly"
   background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\grabclothes.png"
   update()
   btn_right.config(text = button1txt, command=push)
   btn_left.config(text = button2txt, command=downstair)

   #If button "push" was click
def push():

      # Use the global variable
   global happyness
   window.title('BEHAVE WELL!')
   messagebox.showinfo('Scylla', 'What are you trying to do?')
   messagebox.showinfo('Unhappy', 'She is now unhappy')
   happyness -= 1
   lb_scylla.config(text=str(happinesstoface(happyness)))
   messagebox.showinfo('Scylla', 'Stop playing around.')
   downstair()

   #Down Stairs
def downstair():

     # Use the global variables
   global speak, event, button1, button2, button1txt, button2txt, background
      # Changing
   messagebox.showinfo('Scylla', 'I made breakfast for you, come down stairs.')
   button1txt = "Continue"
   button2txt = "Continue"
   background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\downstair.png"
   update()
   btn_right.config(text=button1txt, command=rawmeat)
   btn_left.config(text=button2txt, command=rawmeat)

def rawmeat():

     # Use the global variables
   global speak, event, button1, button2, button1txt, button2txt, background
      # Changing
   button1txt = "Leave it"
   button2txt = "Eat"
   background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\Rawmeat.png"
   update()
   btn_right.config(text=button1txt, command=Line1)
   btn_left.config(text=button2txt, command=Line2)

#Funtions____________________________Line 1

def Line1 ():
   # Use the global variables
   global speak, event, button1, button2, button1txt, button2txt, background
   # Changing
   button1txt = "I don't eat raw."
   button2txt = "Throw meat away."
   background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\whynoteating.png"
   update()
   btn_right.config(text=button1txt, command=Intokitchen)
   btn_left.config(text=button2txt, command=throwmeat)

def throwmeat():
   # Use the global variables
   global speak, event, button1, button2, button1txt, button2txt, background
   # Changing
   button1txt = "Resist"
   button2txt = "Eat"
   background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\Forceeat.png"
   update()
   btn_right.config(text=button1txt, command=Intokitchen)
   btn_left.config(text=button2txt, command=throwmeat)
#________Line 1 - Kinfe and Kill
def Intokitchen():
   # Use the global variables
   global speak, event, button1, button2, button1txt, button2txt, background
   # Changing

   messagebox.showinfo('Scylla', 'Here is the kitchen! It can be a bit dirty because I was making breakfast.')
   button1txt = "Continue"
   button2txt = "Continue"
   background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\Intokitchen.png"
   update()
   btn_right.config(text=button1txt, command=cutmeat)
   btn_left.config(text=button2txt, command=cutmeat)

def cutmeat():
   # Use the global variables
   global speak, event, button1, button2, button1txt, button2txt, background
   # Changing
   messagebox.showinfo('Scylla', 'I will be in the lounge, tell me when you finish!')
   button1txt = "Continue"
   button2txt = "Continue"
   background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\cuttingmeat.png"
   update()
   btn_right.config(text=button1txt, command=cutmeat)
   btn_left.config(text=button2txt, command=cutmeat)

#________Line 2
def Line2():
   # Use the global variables
   global speak, event, button1, button2, button1txt, button2txt, background








#Main________________________________FORMAT
background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\StartScence.png"
#Create a window
window = tk.Tk()
window.geometry("640x840")
bg = tk.PhotoImage(file = background)
label1 = tk.Label( window, image = bg)
label1.place(x = 0, y = 100)
window.resizable(width=False,height=False)
window.title('YOUR LOVE STORY!')
speak = ""
#Labels for heading and Subheading of GUI
lb_heading = tk.Label(window, text="Me and Darling's daily life~❤️", font=("Arial", 20), fg="black")
lb_run = tk.Label(window, text="RUN", font=("Arial", 8), fg="black", bg="white")
lb_scylla = tk.Label(window, text=str(happinesstoface(happyness)), font=('Arial', 20, "bold"), fg="black")
lb_speak = tk.Label(window, text = speak, font=("Arial", 20))

button1txt ="~~~~~Start~~~~~"
button1 = wakeup
button2txt = "--------Exit--------"
button2 = exit


#Button 1
btn_left = tk.Button(window, text=button1txt, font=("Arial", 11), command= button1)

#Button 2
btn_right = tk.Button(window, text=button2txt, font=("Arial", 11), command= button2)



#Placing elements
lb_heading.place(x=145, y=30)
lb_scylla.place(x=40,y=40)
btn_left.place(x=254,y=507)
btn_right.place(x=263,y=587)














window.mainloop()
