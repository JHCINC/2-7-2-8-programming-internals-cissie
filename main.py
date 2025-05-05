'''
Source: https://www.askpython.com/python-modules/tkinter/age-calculator
Date: 21/03/2025
'''
# import window
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Main________________________________FORMAT
background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\StartScence.png"
# Create a window
window = tk.Tk()
window.geometry("640x940")
bg = tk.PhotoImage(file=background)
background = tk.Label(window, image=bg)
background.place(x=0, y=100)
window.resizable(width=False, height=False)
window.title('YOUR LOVE STORY!')
event = ""
heading_text = "Me and Darling's daily life~❤️"
age_window_open = False
# Default Numbers
#Happiness of Scylla
happiness = int(4)
#If the main character hold a knife, start with 0 and it will change to 1 if the character choose hide knife in cook event
knife = int(0)
#If the main character have done cooking, start with 0 and it will change to 1 if the character have done cook event
cook_event = int(0)

# Funtions____________________________Commands
# Death end if happiness is too low
def ifunhappy(happiness):
    if happiness == 1:
        messagebox.showinfo('Scylla', 'If darling really hates me that much, I will let you be in my stomach forever❤️')
        messagebox.showinfo('You died', "You chose to be in the monster's stomach forever")
        death()

# Changing the number for happiness to an emoji
def happinesstoface(happiness):
    face_dict = {
        5: '😘',  # Heart kiss
        4: '☺️',  # Smiling face
        3: '😐',  # Neutral face
        2: '☹️',  # Sad face
        1: '😂'   # Laughing/crying face
    }
    return face_dict.get(happiness, '❓')  # Default to ❓ if happiness not found
# Funtion update so it can make each event shorter
def update():
    lb_scylla.config(text=str(happinesstoface(happiness)))
    bg.config(file=background)
    lb_event.config(text=event)


#check the player's age and warn them about the content
def warning():
    global age_window_open

    # Check if the age window is already open
    if age_window_open:
        return  # Do nothing if it's already open

    # Mark the age window as open
    age_window_open = True

    # Create a new top-level window for age input
    age_window = tk.Toplevel(window)
    age_window.title("Age Check")
    age_window.geometry("300x150")

    # Define a function to handle when the window is closed manually
    def on_close():
        global age_window_open
        # Reset flag to allow future windows
        age_window_open = False
        # Properly destroy the window
        age_window.destroy()

    # Override the default close button behavior to use on_close
    age_window.protocol("WM_DELETE_WINDOW", on_close)

    # Create a label prompting for the user's age
    tk.Label(age_window, text="Please enter your age:").pack(pady=10)

    # Entry widget for the user to input age
    age_entry = tk.Entry(age_window)
    age_entry.pack()

    # Submit button that triggers validation when clicked
    submit_btn = tk.Button(
        age_window,
        text="Enter",
        font=("Arial", 13),
        # Pass entry and window to validation
        command=lambda: validation(age_entry, age_window)
    )
    submit_btn.pack(pady=10)

def validation(age_entry, age_window):
    # Get the age input from the entry widget
    age_text = age_entry.get()

    # Check if the input is empty
    if not age_text:
        messagebox.showinfo('Result', 'Please enter your age')
        return

    try:
        # Try to convert the input into an integer
        age = int(age_text)

        # If age is 16 or above, allow access to the game
        if age >= 16:
            messagebox.showinfo('Result', 'As you are over the age of 16, you can proceed.\nThis game contains violent, cannibalism and bloody content.\n You are playing at your own risk')
            age_window.destroy()  # Close the age check window
            wakeup()  # Start the game

        # If age is under 16, deny access
        else:
            messagebox.showinfo('Result', 'You are underage and cannot play this game.')
            age_window.destroy()  # Close the age check window
            window.destroy()  # Close the main game window
    except ValueError:
        # Handle cases where input is not a number
        messagebox.showinfo('Result', 'Please enter numbers only')

def ending_button_position():
    heading_text = "The End"
    lb_heading.config(text=heading_text)
    button1txt = "~~~Restart~~~"
    button2txt = "--------Exit--------"
    btn_restart.place(x=5800, y=20)
    btn_left.place(x=254, y=507)
    btn_right.place(x=254, y=587)
    btn_right.config(text=button1txt, command=wakeup)
    btn_left.config(text=button2txt, command=exit)

# Destroying the window
def exit():
    window.destroy()


# Funtions____________________________Endings
# Death end
def death():
    # Use the global variables
    global speak, button1, button2, button1txt, button2txt, background, event, heading_text
    # Changing
    messagebox.showinfo('Death', 'You died.')
    event = "Now you're nothing but some flesh."
    background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Done\Death.png"
    ending_button_position()
    update()

#Human Meat Obsessed Ending
def HumanMeatObsessed():
    # Use the global variables
    global speak, event, button1, button2, button1txt, button2txt, background, heading_text
    # Changing
    messagebox.showinfo('Scylla', 'Morning Darling! Here is breakfast.')
    event = "You eat the meat more and more, and you find out that you can't live without \n" \
            "them anymore. Even after the women telling you what those are, you still \n" \
            "enjoy eating them."
    background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\HumanMeatObsessed.png"
    ending_button_position()
    update()

#Killde Monster Ending
def killend():
    # Use the global variables
    global speak, event, button1, button2, button1txt, button2txt, background, happiness, heading_text
    # Changing
    messagebox.showinfo("Kill End", "You killed the monster and run away.")
    event = "You killed the monster, now you're free and you can live a happy life?"
    background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\Run.png"
    ending_button_position()
    update()

#Love ending
def Loveend():
    # Use the global variables
    global speak, event, button1, button2, button1txt, button2txt, background, happiness, heading_text
    # Changing
    messagebox.showinfo("Love End?", "You live with Scylla happily ever after?")
    event = "Maybe you'll survive tomorrow, maybe?"
    background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Done\Love_maybe.png"
    ending_button_position()
    update()

#Monster's cooker ending
def Monsterscooker():
    # Use the global variables
    global speak, event, button1, button2, button1txt, button2txt, background, happiness, heading_text
    # Changing
    messagebox.showinfo("Kill End", "You killed the monster and run away.")
    event = "You obey to the monster and choose to cook for her from now on."
    background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\Monsterscooker.png"
    ending_button_position()
    update()

#Back Home, preparation of Sister missing ending
def backhome():
    # Use the global variables
    global speak, event, button1, button2, button1txt, button2txt, background, happiness, heading_text
    # Changing
    messagebox.showinfo("Back Home", "She lets you go, you weren't sure where to go, but you still run home")
    button1txt = "Continue"
    button2txt = "Continue"
    event = "You find a village and your memories start to come back, you find your way\n" \
            " outside a house thinking that it is your home and worrying that your mum \n" \
            "and sister could waiting for you."
    background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\Runhome.png"
    update()
    btn_right.config(text=button1txt, command=Sistermissing)
    btn_left.config(text=button2txt, command=Sistermissing)

#Sister missing ending
def Sistermissing():
    # Use the global variables
    global speak, event, button1, button2, button1txt, button2txt, background, happiness, heading_text
    # Changing
    messagebox.showinfo("Sister Missing Ending", "You ran away, but only you are homed safely.")
    event = "Your mum cried and hugged you, welcoming you home, but then she tell you\n" \
            " that your sister have also gone missing since you were. She was wearing\n" \
            " pink clothes with purple pant."
    background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\Sistermissing.png"
    btn_restart.place(x=5800, y=20)
    ending_button_position()
    update()

#Stay Forever ending
def Stayforever():
    # Use the global variables
    global speak, event, button1, button2, button1txt, button2txt, background, happiness, heading_text
    # Changing
    messagebox.showinfo("Stay Forever Ending", "You chose to stay forever.")
    event = "You stay, you stay, you stay, but how long can you stay?"
    background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Done\Love.png"
    ending_button_position()
    update()


#Funtions____________________________Starting Events

# Starting from "Wake up" scence
def wakeup():
    # Use the global variables
    global speak, event, button1, button2, button1txt, button2txt, background, happiness, knife, cook_event, Monster
    # Changing

    messagebox.showinfo('Scylla', 'Good Morning Darling~~ Here is your shirt.')
    button1txt = "Continue"
    button2txt = "Continue"
    event = "You wake up as you fall onto the floor from a bed that's 10 times\n the" \
            " size of you. In front of you is a pretty women right you've never meet."
    background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\Wakeup.png"
#Reset the placing of the buttons
    btn_restart.place(x=580, y=20)
    btn_left.place(x=0, y=507)
    btn_right.place(x=0, y=567)
#Reset the numbers
    happiness = int(4)
    knife = int(0)
    cook_event = int(0)
    Monster = "alive"
    update()
    btn_right.config(text=button1txt, command=grabclothes)
    btn_left.config(text=button2txt, command=grabclothes)



#Grabbing the clothes
def grabclothes():
    # Use the global variables
    global speak, event, button1, button2, button1txt, button2txt, background
    # Changing
    messagebox.showinfo('Scylla', 'Get into clothes quickly.')
    button1txt = "Push her"
    button2txt = "Wear it"
    event = "You grab your clothes from her."
    background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\grabclothes.png"
    update()
    btn_right.config(text=button1txt, command=push)
    btn_left.config(text=button2txt, command=downstair)


#Pushing Scylla
def push():
    # Use the global variable
    global happiness
    window.title('BEHAVE WELL!')
    messagebox.showinfo('Scylla', 'What are you trying to do?')
    messagebox.showinfo('Unhappy', 'She is now unhappy')
    happiness -= 1
    lb_scylla.config(text=str(happinesstoface(happiness)))
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
    event = "You wore your clothes while the pretty women sat on the bed\n" \
            "watches you."
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
    event = "A plate of raw meat is place on the stone table in the middle of the living\n" \
            "room, it's unlike any kind of meat you seen in the supermarket before but \n" \
            "very fresh."
    background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\Rawmeat.png"
    update()
    btn_right.config(text=button1txt, command=Line1)
    btn_left.config(text=button2txt, command=Line2)


# Funtions____________________________Line 1

def Line1():
    # Use the global variables
    global speak, event, button1, button2, button1txt, button2txt, background
    # Changing
    button1txt = "I don't eat raw."
    button2txt = "Throw meat away."
    event = "You don't want to put the plate of raw meat anywhere near your mouth.\nthe" \
            " women in front of you look like she really wants you to eat it."
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
    event = "The women suddenly change into a monster with nine snakes as her lower body.\nShe" \
            " grab the meats from the table and stuff them into your month."
    background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\Forceeat.png"
    update()
    btn_right.config(text=button1txt, command=death)
    btn_left.config(text=button2txt, command=Doyouhateme)


def Doyouhateme():
    # Use the global variables
    global speak, event, button1, button2, button1txt, button2txt, background
    # Changing
    button1txt = "Yes"
    button2txt = "No, I love you"
    event = "She change back into a women looking at you with a sad face. \n" \
            "Even though she could've killed you, she now tell you that she may let \n" \
            "you go if you tell her the truth."
    background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\whynoteating.png"
    update()
    if happiness >= 4:
        btn_right.config(text=button1txt, command=backhome)
    else:
        btn_right.config(text=button1txt, command=death)
    btn_left.config(text=button2txt, command=Stayforever)


# ________Line 1 - Kinfe and Kill
def Intokitchen():
    # Use the global variables
    global speak, event, button1, button2, button1txt, button2txt, background
    # Changing
    window.title('B? Ca@R#Fu//!')
    messagebox.showinfo('Scylla', 'Here is the kitchen! It can be a bit dirty because I was making breakfast.')
    button1txt = "Continue"
    button2txt = "Continue"
    event = "She show you where the kitchen is, and you can see that there was something\n" \
            " going on inside there to cause those mess."
    background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\Intokitchen.png"
    update()
    btn_right.config(text=button1txt, command=cutmeat)
    btn_left.config(text=button2txt, command=cutmeat)


def cutmeat():
    # Use the global variables
    global speak, event, button1, button2, button1txt, button2txt, background
    # Changing
    button1txt = "Hide Knife"
    button2txt = "Continue Cooking"
    event = "You cut the meat up into smaller pieces to cook, while the women is\n" \
            " sitting in the living room, waiting for you. AS you see the knife in\n" \
            "your hand, you have a idea."
    background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\cuttingmeat.png"
    update()
    btn_right.config(text=button1txt, command=knife1)
    btn_left.config(text=button2txt, command=finishcook)


def knife1():
    # Use the global variables
    global speak, event, button1, button2, button1txt, button2txt, background, knife
    # Changing
    knife += 1
    button1txt = "Search for others"
    button2txt = "No"
    event = "You hide the knife inside your pant while the women is not watching."
    background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\knife+1.png"
    update()
    btn_right.config(text=button1txt, command=salt)
    btn_left.config(text=button2txt, command=finishcook)


def salt():
   # Use the global variables
   global speak, event, button1, button2, button1txt, button2txt, background, knife
   # Changing
   knife += 1
   button1txt = "take it"
   button2txt = "No"
   event = "You find some salt sitting on the table."
   background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\Findsalt.png"
   update()
   btn_right.config(text=button1txt, command=whatareyoudoing)
   btn_left.config(text=button2txt, command=finishcook)

def whatareyoudoing():
    # Use the global variable
    global happiness
    window.title('Careful!')
    messagebox.showinfo('Scylla', 'What are doing?')
    messagebox.showinfo('Unhappy', 'She is now unhappy')
    happiness -= 1
    lb_scylla.config(text=str(happinesstoface(happiness)))
    messagebox.showinfo('Scylla', 'Stop playing around, just cook the meat.')
    finishcook()

def finishcook():
    # Use the global variables
    global speak, event, button1, button2, button1txt, button2txt, background, cook_event
    # Changing
    button1txt = "Eat"
    button2txt = "Give it to Scylla"
    cook_event += 1
    event = "You finished cooking, making a nice and juicy steak. You took it out of\n" \
            " the kitchen and placed it on the table."
    background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\meatcooked.png"
    update()
    btn_right.config(text=button1txt, command=Choosenextmeal)
    btn_left.config(text=button2txt, command=Doyoulikeme)


# ________Line 1 Like?
def Doyoulikeme():
    # Use the global variables
    global speak, event, button1, button2, button1txt, button2txt, background, happiness
    messagebox.showinfo('Scylla', 'Thank you darling! It tastes very good!.')
    messagebox.showinfo('Scylla', 'I am just checking... You love me right?.')
    # Changing
    button1txt = "Yes, I love you"
    button2txt = "No, I hate you"
    event = "She look at you quietly, waiting for an answer."
    happiness += 1
    background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\meatcooked.png"
    update()
    btn_right.config(text=button1txt, command=Loveend)
    btn_left.config(text=button2txt, command=Knifetrue)


# ________Line 2
def Line2():
    # Use the global variables
    global speak, event, button1, button2, button1txt, button2txt, background
    # Changing
    messagebox.showinfo('Scylla', 'How does it taste')
    button1txt = "Yummy"
    button2txt = "No reply"
    event = "You stuff all the meat into your month as fast as possible \n" \
            "to prevent tasting it. Now you hands and face are\n" \
            "cover in blood, the women in front of you still acts perfectly normal."
    background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\Taste.png"
    update()
    btn_right.config(text=button1txt, command=Choosenextmeal)
    btn_left.config(text=button2txt, command=Nextday)


# ________obey first, knife next
def Nextday():
    # Use the global variables
    global speak, event, button1, button2, button1txt, button2txt, background, happiness
    # Changing
    messagebox.showinfo('Scylla', 'Morning Darling! Here is breakfast.')
    button1txt = "Eat"
    button2txt = "Ask questions"
    window.title('B? Ca@R#Fu//!')
    happiness += 1
    event = "After eating the raw meat, you felt sick and disgust and obey to the woman\n" \
            " and did anything she told you to do. You felt so tried that you slept in the\n" \
            " house without think much. She is very happy at the moment."
    background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\Rawmeat.png"
    update()
    btn_right.config(text=button1txt, command=Nextday2)
    btn_left.config(text=button2txt, command=Ask)
    lb_scylla.config(text=str(happinesstoface(happiness)))


def Ask():
    # Use the global variables
    global speak, event, button1, button2, button1txt, button2txt, background, happiness
    # Changing
    messagebox.showinfo('Scylla', 'What do you want to know?')
    button1txt = "Who are you?"
    button2txt = "Why am I here?"
    window.title('B? Ca@R#Fu//!')
    event = "Scylla sits and smile at you."
    background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\Rawmeat.png"
    update()
    btn_right.config(text=button1txt, command=Love)
    btn_left.config(text=button2txt, command=Love)


def Nextday2():
    # Use the global variables
    global speak, event, button1, button2, button1txt, button2txt, background, happiness
    # Changing
    messagebox.showinfo('Scylla', 'Morning Darling! Here is breakfast.')
    button1txt = "Eat"
    button2txt = "Eat"
    window.title('&t*] :t!')
    event = "After eating the raw meat, you felt sick and repeat everything\n" \
            " you did the day before yesterday. Now the plate of raw meat is\n" \
            " place in front of you again, you will..."
    background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\Rawmeat.png"
    update()
    btn_right.config(text=button1txt, command=HumanMeatObsessed)
    btn_left.config(text=button2txt, command=HumanMeatObsessed)


def Love():
    # Use the global variables
    global speak, event, button1, button2, button1txt, button2txt, background, happiness
    # Changing
    messagebox.showinfo('Scylla',
                        'It is because I am your wife, we have married a long time ago. This is our love house!')
    button1txt = "Decide to do something else"
    button2txt = "Decide to stay here"
    window.title('N0 *0#!')
    event = "She start telling you every detail of your life with her, how you \n" \
            "meet each other and how much she loves you. However, you cannot \n" \
            "pick up or relate to anything she says."
    background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\Rawmeat.png"
    update()
    btn_right.config(text=button1txt, command=Line1)
    btn_left.config(text=button2txt, command=Stayforever)


# ________Cook, eat, yummy
def Choosenextmeal():
    # Use the global variables
    global speak, event, button1, button2, button1txt, button2txt, background, happiness
    # Changing
    messagebox.showinfo('Scylla', 'I am glad you like it! Come here! I can show you my food storage!')
    button1txt = "Choose one"
    button2txt = "NO human"
    window.title('B? Ca@R#Fu//!')
    happiness += 1
    event = "She is very happy at the moment. So she decided to take you to the \n" \
            "basement, in there, there are three humans. Two of them dead and one \n" \
            "alive. One girl that is like 2 years younger than you is missing \n " \
            "her arms and heart. One boy that is so broken you can't tell his age.\n" \
            " The only one alive is a boy that's covered in blood with dull eyes\n" \
            " that is full of emptiness."
    background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\Choosenextmeal.png"
    btn_restart.place(x=5800, y=20)
    btn_left.place(x=0, y=507)
    btn_right.place(x=0, y=587)
    update()
    btn_right.config(text=button1txt, command=HumanMeatObsessed)
    btn_left.config(text=button2txt, command=Justateone)
    lb_scylla.config(text=str(happinesstoface(happiness)))


def Justateone():
    # Use the global variables
    global speak, event, button1, button2, button1txt, button2txt, background, happiness
    # Changing
    messagebox.showinfo('Scylla',
                        'You just ate one though? Look at the one on the left, that was her.')
    window.title('&t*] :t!')
    event = "She start telling you every detail of your life with her, how you \n" \
            "meet each other and how much she loves you. However, you cannot \n" \
            "pick up or relate to anything she says."
    background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\justateone.png"
    update()
    if cook_event == 1:
        button1txt = "Cook it"
        button2txt = "No"
        btn_right.config(text=button1txt, command=Monsterscooker)
        btn_left.config(text=button2txt, command=Knifetrue)
    elif knife == 1:
        return Knifetrue
    else:
        button1txt = "Choose one"
        button2txt = "Fight"
        btn_right.config(text=button1txt, command=HumanMeatObsessed)
        btn_left.config(text=button2txt, command=death)


def Knifetrue():
    # Use the global variables
    global speak, event, button1, button2, button1txt, button2txt, background, happiness, Monster
    #Happiness changing
    happiness -= 1
    #Check Happiness
    ifunhappy(happiness)
    # Changing
    if knife == 1:
        button1txt = "Kill her"
        button2txt = "No"
        window.title('&t*] :t!')
        event = "You take the knife out from your clothes, and now you decide to..."
        background = "G:\My Drive\W12KT\L2DGP\Internal\Versions\Event backgrounds\Piskel\Killendornot.png"
        update()
        btn_right.config(text=button1txt, command=killend)
        btn_left.config(text=button2txt, command=death)
    elif happiness > 2:
        return backhome()
    else:
        return death()



# Labels for heading and Subheading of GUI
lb_heading = tk.Label(window, text= heading_text , font=("Arial", 20), fg="black")
lb_run = tk.Label(window, text="RUN", font=("Arial", 8), fg="black", bg="white")
lb_scylla = tk.Label(window, text=str(happinesstoface(happiness)), font=('Arial', 20, "bold"), fg="black")
lb_event = tk.Label(window, text=event, font=('Arial', 13, "bold"), fg="black")

# button text
button1txt = "~~~~~Start~~~~~"
button1 = warning
button2txt = "--------Exit--------"
button2 = exit
restarttxt = "restart"

# Button 1
btn_left = tk.Button(window, text=button1txt, font=("Arial", 11), command=button1)

# Button 2
btn_right = tk.Button(window, text=button2txt, font=("Arial", 11), command=button2)

btn_restart = tk.Button(window, text=restarttxt, font=("Arial", 11), command=wakeup)

# Placing elements
lb_heading.place(x=145, y=30)
lb_scylla.place(x=40, y=40)
lb_event.place(x=0, y=760)
btn_left.place(x=254, y=507)
btn_right.place(x=263, y=587)
btn_restart.place(x=1000, y=20)

window.mainloop()
