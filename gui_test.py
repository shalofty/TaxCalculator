import tkinter
import tkinter.tix
from tkinter import *
from tkinter import ttk
from fed_dicts import *
from fed_utils import *
from test import *

root = Tk()
root.configure(bg='grey')
root.geometry('300x450')
root.title("Python Income Tax Calculator")
root.resizable(False, False)

frame = Frame(
    root,
    bg="white",
    width=600,
    height=25
)
frame.place(x=0, y=400)

# DROPDOWN MENU for STATE selection
# Options

stateOptions = [
    "AL",
    "AK",
    "AZ",
    "AR",
    "CA",
    "CO",
    "CT",
    "DE",
    "DC",
    "FL",
    "GA",
    "HI",
    "ID",
    "IL",
    "IN",
    "IA",
    "KS",
    "KY",
    "LA",
    "ME",
    "MD",
    "MA",
    "MI",
    "MN",
    "MS",
    "MO",
    "MT",
    "NE",
    "NV",
    "NH",
    "NJ",
    "NM",
    "NY",
    "NC",
    "ND",
    "OH",
    "OK",
    "OR",
    "PA",
    "RI",
    "SC",
    "SD",
    "TN",
    "TX",
    "UT",
    "VT",
    "VA",
    "WA",
    "WV",
    "WI",
    "WY"
]

stateClicked = StringVar()
stateClicked.set("")

stateDrop = OptionMenu(root, stateClicked, *stateOptions)
stateDrop.pack()
stateDrop.place(x=10, y=5)

# LABEL 1, WAGES -- Initialize a label to display the User Input
box1label = Label(root, text="Wages and Tips", font=("Arial", 8), width=20)
box1label.pack()
box1label.place(x=10, y=45)

# BOX 1, WAGES -- Create an Entry widget to accept User Input
box1entry = Entry(root, width=20)
box1entry.focus_set()
box1entry.pack()
box1entry.place(x=150, y=45)

# LABEL 2, FEDERAL TAX -- Initialize a label to display the User Input
box2label = Label(root, text="Federal Income Taxes", font=("Arial", 8), width=20)
box2label.pack()
box2label.place(x=10, y=75)

# BOX 2, FEDERAL TAX -- Create an Entry widget to accept User Input
box2entry = Entry(root, width=20)
box2entry.focus_set()
box2entry.pack()
box2entry.place(x=150, y=75)

# LABEL 3, SS WAGES -- Initialize a label to display the User Input
box3label = Label(root, text="Social Security Wages", font=("Arial", 8), width=20)
box3label.pack()
box3label.place(x=10, y=105)

# BOX 3, SS WAGES -- Create an Entry widget to accept User Input
box3entry = Entry(root, width=20)
box3entry.focus_set()
box3entry.pack()
box3entry.place(x=150, y=105)

# LABEL 4, SS TAX -- Initialize a label to display the User Input
box4label = Label(root, text="Social Security Taxes", font=("Arial", 8), width=20)
box4label.pack()
box4label.place(x=10, y=135)

# BOX 4, SS TAX -- Create an Entry widget to accept User Input
box4entry = Entry(root, width=20)
box4entry.focus_set()
box4entry.pack()
box4entry.place(x=150, y=135)

# LABEL 5, MEDICARE WAGES -- Initialize a label to display the User Input
box5label = Label(root, text="Medicare Wages", font=("Arial", 8), width=20)
box5label.pack()
box5label.place(x=10, y=165)

# BOX 5, MEDICARE WAGES -- Create an Entry widget to accept User Input
box5entry = Entry(root, width=20)
box5entry.focus_set()
box5entry.pack()
box5entry.place(x=150, y=165)

# LABEL 6, MEDICARE TAX -- Initialize a label to display the User Input
box6label = Label(root, text="Medicare Taxes", font=("Arial", 8), width=20)
box6label.pack()
box6label.place(x=10, y=195)

# BOX 6, MEDICARE TAX -- Create an Entry widget to accept User Input
box6entry = Entry(root, width=20)
box6entry.focus_set()
box6entry.pack()
box6entry.place(x=150, y=195)

# LABEL 7, SOCIAL SECURITY TIPS -- Initialize a label to display the User Input
box7label = Label(root, text="Social Security Tips", font=("Arial", 8), width=20)
box7label.pack()
box7label.place(x=10, y=225)

# BOX 7, SOCIAL SECURITY TIPS -- Create an Entry widget to accept User Input
box7entry = Entry(root, width=20)
box7entry.focus_set()
box7entry.pack()
box7entry.place(x=150, y=225)

# LABEL 8, ALLOCATED TIPS -- Initialize a label to display the User Input
box8label = Label(root, text="Allocated Tips", font=("Arial", 8), width=20)
box8label.pack()
box8label.place(x=10, y=255)

# BOX 8, ALLOCATED TIPS -- Create an Entry widget to accept User Input
box8entry = Entry(root, width=20)
box8entry.focus_set()
box8entry.pack()
box8entry.place(x=150, y=255)

# LABEL 9, STATE WAGES -- Initialize a label to display the User Input
box9label = Label(root, text="State Wages", font=("Arial", 8), width=20)
box9label.pack()
box9label.place(x=10, y=285)

# BOX 9, STATE WAGES -- Create an Entry widget to accept User Input
box9entry = Entry(root, width=20)
box9entry.focus_set()
box9entry.pack()
box9entry.place(x=150, y=285)

# LABEL 10, STATE TAX -- Initialize a label to display the User Input
boxXlabel = Label(root, text="State Taxes", font=("Arial", 8), width=20)
boxXlabel.pack()
boxXlabel.place(x=10, y=315)

# BOX 10, STATE TAX -- Create an Entry widget to accept User Input
boxXentry = Entry(root, width=20)
boxXentry.focus_set()
boxXentry.pack()
boxXentry.place(x=150, y=315)


# Submit Button

def submit():
    stateClicked.get()
    box1entry.get()

submit_button = tkinter.Button(root, text="Submit", command=submit)
submit_button.place(x=100, y=100)



# Run the window
root.mainloop()
