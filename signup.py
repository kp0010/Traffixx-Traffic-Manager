import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

BGCOLOR = "#" + "03" * 3

class SignUp:
    def __init__(self,window):
        self.window = window

        window_height = self.window.winfo_screenheight()
        window_width = self.window.winfo_screenwidth()

        self.window.geometry(f"{window_width}x{window_height}")

        self.window.state("zoomed")
        self.window.resizable(0, 0)
        self.window.title("Traffic Light Management")

        # Background

        self.bg_frame = Image.open("Assets/Images/Bg.png")
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill="both", expand=True)

        # Frame

        self.lgn_frame = Frame(self.window, bg=BGCOLOR, width=1050, height=700)
        self.lgn_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Title Text

        self.txt = "SIGN UP FORM"
        self.heading = Label(self.lgn_frame, text=self.txt, font=("Ariel", 25, "bold"), bg=BGCOLOR, fg="white")
        self.heading.place(x=70, y=45, width=900, height=30)

        # Traffic Police ID

        self.id_number_label = Label(self.lgn_frame, text="ID Number", bg=BGCOLOR, fg="#4f4e4d",
                                    font=("Ariel", 13, "bold"))
        self.id_number_label.place(x=400,y=110)

        self.id_number_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg=BGCOLOR, fg="white",
                                    font=("Ariel", 13, "bold"), cursor="xterm #AFAFAF", insertbackground="#AFAFAF")
        self.id_number_entry.place(x=400, y=140)
        self.id_number_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="white", highlightthickness=0)
        self.id_number_line.place(x=400, y=160)


        #Username/Full Name

        self.username_label = Label(self.lgn_frame, text="Username/Full Name", bg=BGCOLOR, fg="#4f4e4d",
                                    font=("Ariel", 13, "bold"))
        self.username_label.place(x=400,y=200)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg=BGCOLOR, fg="white",
                                    font=("Ariel", 13, "bold"), cursor="xterm #AFAFAF", insertbackground="#AFAFAF")
        self.username_entry.place(x=400, y=230)
        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="white", highlightthickness=0)
        self.username_line.place(x=400, y=250)


        #Password

        self.password_label = Label(self.lgn_frame, text="Password", bg=BGCOLOR, fg="#4f4e4d",
                                    font=("Ariel", 13, "bold"))
        self.password_label.place(x=400,y=280)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg=BGCOLOR, fg="white",
                                    font=("Ariel", 13, "bold"), cursor="xterm #AFAFAF", insertbackground="#AFAFAF")
        self.password_entry.place(x=400, y=310)
        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="white", highlightthickness=0)
        self.password_line.place(x=400, y=330)


        #Phone Number

        self.phone_number_label = Label(self.lgn_frame, text="Phone Number", bg=BGCOLOR, fg="#4f4e4d",
                                    font=("Ariel", 13, "bold"))
        self.phone_number_label.place(x=400,y=370)

        self.phone_number_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg=BGCOLOR, fg="white",
                                    font=("Ariel", 13, "bold"), cursor="xterm #AFAFAF", insertbackground="#AFAFAF")
        self.phone_number_entry.place(x=400, y=400)
        self.phone_number_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="white", highlightthickness=0)
        self.phone_number_line.place(x=400, y=420)


        #Email id

        self.email_label = Label(self.lgn_frame, text="Email ID", bg=BGCOLOR, fg="#4f4e4d",
                                    font=("Ariel", 13, "bold"))
        self.email_label.place(x=400,y=450)

        self.email_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg=BGCOLOR, fg="white",
                                    font=("Ariel", 13, "bold"), cursor="xterm #AFAFAF", insertbackground="#AFAFAF")
        self.email_entry.place(x=400, y=480)
        self.email_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="white", highlightthickness=0)
        self.email_line.place(x=400, y=500)




def page():
    window = Tk()
    SignUp(window)
    window.mainloop()


if __name__ == "__main__":
    page()