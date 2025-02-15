import tkinter as tk
from tkinter import *
import os, cv2
import shutil
import csv
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time
import tkinter.font as font
import pyttsx3

# project module
import show_attendance
import takeImage
import trainImage
import automaticAttedance

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Attendance System Running"

if __name__ == "__main__":
    app.run(debug=True)



# engine = pyttsx3.init()
# engine.say("Welcome!")
# engine.say("Please browse through your options..")
# engine.runAndWait()


import tkinter as tk
import pyttsx3
import os


def text_to_speech(user_text): 
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()

haarcasecade_path = "haarcascade_frontalface_default.xml"
trainimagelabel_path = "./TrainingImageLabel/Trainner.yml"
trainimage_path = "/TrainingImage"
if not os.path.exists(trainimage_path):
    os.makedirs(trainimage_path)

studentdetail_path = "./StudentDetails/studentdetails.csv"
attendance_path = "Attendance"

# Window Setup
window = tk.Tk()
window.title("Present Sir- Automated Attendance system")
window.geometry("1280x720")
window.configure(bg="#E6E6FA")  # Dark background color


# Create gradient background for window
canvas = tk.Canvas(window, width=1280, height=720)
canvas.place(x=0, y=0)


# Function to destroy screen
def del_sc1():
    sc1.destroy()

# Error message for name and enrollment number
def err_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry("400x130")
    sc1.iconbitmap("AMS.ico")
    sc1.title("Warning!!")
    sc1.configure(background="#333333")  # Dark background for error window
    sc1.resizable(0, 0)

    # Label for the error message with shadow effect
    label = tk.Label(
        sc1,
        text="Enrollment & Name required!",
        fg="#F1C40F",  # Gold color for the text
        bg="#333333",  # Dark background for consistency
        font=("Arial", 16, "bold"),
        relief="solid",
        bd=2,
        padx=10,
        pady=10
    )
    label.pack(pady=20)

    # Add shadow effect
    shadow_label = tk.Label(
        sc1,
        text="Enrollment & Name required!",
        fg="gray",
        bg="#333333",  # Matching background for consistency
        font=("Arial", 16, "bold"),
        relief="solid",
        bd=2,
        padx=10,
        pady=10
    )
    shadow_label.place(x=label.winfo_x() + 2, y=label.winfo_y() + 2)

    # OK Button with updated styling and rounded corners
    button = tk.Button(
        sc1,
        text="OK",
        command=del_sc1,
        fg="white",
        bg="#F39C12",  # Gold background for the button
        width=12,
        height=2,
        font=("Arial", 14, "bold"),
        relief="flat",
        activebackground="#F1C40F",  # Lighter gold on hover
    )
    button.pack(pady=10)
    
    # Rounded corners for button and shadow effect
    button.config(borderwidth=3, relief="raised")
    button.bind("<Enter>", lambda e: button.config(bg="#F1C40F"))  # On hover, change background
    button.bind("<Leave>", lambda e: button.config(bg="#F39C12"))  # On hover end, revert background


def testVal(inStr, acttyp):
    if acttyp == "1":  # insert
        if not inStr.isdigit():
            return False
    return True


logo = Image.open("UI_Image/0001.png")
logo = logo.resize((50, 47), Image.LANCZOS)
logo1 = ImageTk.PhotoImage(logo)
titl = tk.Label(window, bg="#1A1A1A", relief=RIDGE, bd=10, font=("Verdana", 30, "bold"))
titl.pack(fill=X)
l1 = tk.Label(window, image=logo1, bg="#1A1A1A",)
l1.place(x=470, y=10)


titl = tk.Label(
    window, text="Present Sir", bg="#1A1A1A", fg="#F1C40F", font=("Verdana", 27, "bold"),
)
titl.place(x=525, y=12)

a = tk.Label(
    window,
    text="Automated Attendence system",
    bg="#1A1A1A",  # Dark background for the main text
    fg="#F1C40F",  # Bright yellow color
    bd=10,
    font=("Verdana", 35, "bold"),
)
a.pack()


ri = Image.open("UI_Image/register.png")
r = ImageTk.PhotoImage(ri)
label1 = Label(window, image=r)
label1.image = r
label1.place(x=100, y=270)

ai = Image.open("UI_Image/attendance.png")
a = ImageTk.PhotoImage(ai)
label2 = Label(window, image=a)
label2.image = a
label2.place(x=980, y=270)

vi = Image.open("UI_Image/verifyy.png")
v = ImageTk.PhotoImage(vi)
label3 = Label(window, image=v)
label3.image = v
label3.place(x=600, y=270)


def TakeImageUI():
    ImageUI = Tk()
    ImageUI.title("Take Student Image..")
    ImageUI.geometry("780x480")
    ImageUI.configure(background="#1A1A1A")  # Dark background for the image window
    ImageUI.resizable(0, 0)
    titl = tk.Label(ImageUI, bg="#1A1A1A", relief=RIDGE, bd=10, font=("Verdana", 30, "bold"))
    titl.pack(fill=X)
    # image and title
    titl = tk.Label(
        ImageUI, text="Register Your Face", bg="#1A1A1A", fg="#F39C12", font=("Verdana", 30, "bold"),
    )
    titl.place(x=270, y=12)

    # heading
    a = tk.Label(
        ImageUI,
        text="Enter the details",
        bg="#1A1A1A",  # Dark background for the details label
        fg="#F1C40F",  # Bright yellow text color
        bd=10,
        font=("Verdana", 24, "bold"),
    )
    a.place(x=280, y=75)

    # ER no
    lbl1 = tk.Label(
        ImageUI,
        text="Enrollment No",
        width=10,
        height=2,
        bg="#1A1A1A",
        fg="#F1C40F",
        bd=5,
        relief=RIDGE,
        font=("Verdana", 14),
    )
    lbl1.place(x=120, y=130)
    txt1 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        validate="key",
        bg="#333333",  # Dark input background
        fg="#F1C40F",  # Bright text color for input
        relief=RIDGE,
        font=("Verdana", 18, "bold"),
    )
    txt1.place(x=250, y=130)
    txt1["validatecommand"] = (txt1.register(testVal), "%P", "%d")

    # name
    lbl2 = tk.Label(
        ImageUI,
        text="Name",
        width=10,
        height=2,
        bg="#1A1A1A",
        fg="#F1C40F",
        bd=5,
        relief=RIDGE,
        font=("Verdana", 14),
    )
    lbl2.place(x=120, y=200)
    txt2 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        bg="#333333",  # Dark input background
        fg="#F1C40F",  # Bright text color for input
        relief=RIDGE,
        font=("Verdana", 18, "bold"),
    )
    txt2.place(x=250, y=200)

    lbl3 = tk.Label(
        ImageUI,
        text="Notification",
        width=10,
        height=2,
        bg="#1A1A1A",
        fg="#F1C40F",
        bd=5,
        relief=RIDGE,
        font=("Verdana", 14),
    )
    lbl3.place(x=120, y=270)

    message = tk.Label(
        ImageUI,
        text="",
        width=32,
        height=2,
        bd=5,
        bg="#333333",  # Dark background for messages
        fg="#F1C40F",  # Bright text color for messages
        relief=RIDGE,
        font=("Verdana", 14, "bold"),
    )
    message.place(x=250, y=270)

    def take_image():
        l1 = txt1.get()
        l2 = txt2.get()
        takeImage.TakeImage(
            l1,
            l2,
            haarcasecade_path,
            trainimage_path,
            message,
            err_screen,
            text_to_speech,
        )
        txt1.delete(0, "end")
        txt2.delete(0, "end")

    # take Image button
    takeImg = tk.Button(
        ImageUI,
        text="Take Image",
        command=take_image,
        bd=10,
        font=("Verdana", 18, "bold"),
        bg="#333333",  # Dark background for the button
        fg="#F1C40F",  # Bright text color for the button
        height=2,
        width=12,
        relief=RIDGE,
    )
    takeImg.place(x=130, y=350)

    def train_image():
        trainImage.TrainImage(
            haarcasecade_path,
            trainimage_path,
            trainimagelabel_path,
            message,
            text_to_speech,
        )
    # Train Image function call
    trainImg = tk.Button(
         ImageUI,
        text="Train Image",
        command=train_image,
        bd=10,
        font=("Verdana", 18, "bold"),
        bg="#333333",  # Dark background for the button
        fg="yellow",  # Bright text color for the button
        height=2,
        width=12,
        relief=tk.RIDGE,
        )
    trainImg.place(x=360, y=350)

# Register a new student button
r = tk.Button(
    window,
    text="Register a new student",
    command=TakeImageUI,
    bd=10,
    font=("Verdana", 16),
    bg="black",
    fg="yellow",
    height=2,
    width=17,
    relief=tk.RIDGE,  # Added relief to match the style
)
r.place(x=100, y=520)

# Take Attendance button
def automatic_attedance():
    automaticAttedance.subjectChoose(text_to_speech)

r = tk.Button(
    window,
    text="Take Attendance",
    command=automatic_attedance,
    bd=10,
    font=("Verdana", 16),
    bg="black",
    fg="yellow",
    height=2,
    width=17,
    relief=tk.RIDGE,  # Added relief to match the style
)
r.place(x=600, y=520)

# View Attendance button
def view_attendance():
    show_attendance.subjectchoose(text_to_speech)

r = tk.Button(
    window,
    text="View Attendance",
    command=view_attendance,
    bd=10,
    font=("Verdana", 16),
    bg="black",
    fg="yellow",
    height=2,
    width=17,
    relief=tk.RIDGE,  # Added relief to match the style
)
r.place(x=1000, y=520)

# Exit button
r = tk.Button(
    window,
    text="EXIT",
    bd=10,
    command=quit,
    font=("Verdana", 16),
    bg="black",
    fg="yellow",
    height=2,
    width=17,
    relief=tk.RIDGE,  # Added relief to match the style
)
r.place(x=600, y=660)

window.mainloop()

        
        