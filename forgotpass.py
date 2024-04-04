import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image

BGCOLOR = "#" + "03" * 3

class ForgotPass(tk.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.window = root
        self.pack(fill=tk.BOTH, expand=True)

        #Background

        self.bg_frame = Image.open("Assets/Images/Bg.png")
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self, image=photo, bg=BGCOLOR)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill=tk.BOTH, expand=True)

        # Frame

        self.fg_pass_frame = Frame(self, bg=BGCOLOR, width=800, height=700)
        self.fg_pass_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Title Text

        self.txt = "FORGOT PASSWORD ?"
        self.heading = Label(self.fg_pass_frame, text=self.txt, font=("Ariel", 25, "bold"), bg=BGCOLOR, fg="white")
        self.heading.place(x=0, y=85, width=800, height=30)

        # Text

        self.txt = ("Provide your account details for which for which you want to reset your password")
        self.heading = Label(self.fg_pass_frame, text=self.txt, font=("Ariel", 8), bg=BGCOLOR, fg="white")
        self.heading.place(x=0, y=120, width=800, height=30)

        # UserID

        self.id_number_label = Label(self.fg_pass_frame, text="ID Number", bg=BGCOLOR, fg="#4f4e4d",
                                     font=("Ariel", 13, "bold"))
        self.id_number_label.place(x=250, y=210)

        self.id_number_entry = Entry(self.fg_pass_frame, highlightthickness=0, relief=FLAT, bg=BGCOLOR, fg="white",
                                     font=("Ariel", 13, "bold"), cursor="xterm #AFAFAF", insertbackground="#AFAFAF")
        self.id_number_entry.place(x=285, y=233)
        self.id_number_line = Canvas(self.fg_pass_frame, width=300, height=2.0, bg="white", highlightthickness=0)
        self.id_number_line.place(x=250, y=260)

        self.id_icon = Image.open("Assets/Icons/id_icon.png")
        photo = ImageTk.PhotoImage(self.id_icon)
        self.id_icon_label = Label(self.fg_pass_frame, image=photo, bg=BGCOLOR)
        self.id_icon_label.image = photo
        self.id_icon_label.place(x=250, y=237)

        # Username/Full Name

        self.username_label = Label(self.fg_pass_frame, text="Full Name", bg=BGCOLOR, fg="#4f4e4d",
                                    font=("Ariel", 13, "bold"))
        self.username_label.place(x=250, y=290)

        self.username_entry = Entry(self.fg_pass_frame, highlightthickness=0, relief=FLAT, bg=BGCOLOR, fg="white",
                                    font=("Ariel", 13, "bold"), cursor="xterm #AFAFAF", insertbackground="#AFAFAF")
        self.username_entry.place(x=285, y=313)
        self.username_line = Canvas(self.fg_pass_frame, width=300, height=2.0, bg="white", highlightthickness=0)
        self.username_line.place(x=250, y=340)

        self.username_icon = Image.open("Assets/Icons/UsernameIcon.png")
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.fg_pass_frame, image=photo, bg=BGCOLOR)
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=250, y=312)
        
        # Phone number
        
        def validate_phoneno(inp):
            if len(str(inp)) > 10:
                return False

            elif inp.isdigit() or inp == "":
                return True

            return False

        validator = self.window.register(validate_phoneno)

        self.phone_number_label = Label(self.fg_pass_frame, text="Phone Number", bg=BGCOLOR, fg="#4f4e4d",
                                        font=("Ariel", 13, "bold"))
        self.phone_number_label.place(x=250, y=370)

        self.phone_number_entry = Entry(self.fg_pass_frame, highlightthickness=0, relief=FLAT, bg=BGCOLOR, fg="white",
                                        font=("Ariel", 13, "bold"), cursor="xterm #AFAFAF", insertbackground="#AFAFAF",
                                        validate="key", validatecommand=(validator, "%P"))
        self.phone_number_entry.place(x=285, y=393)
        self.phone_number_line = Canvas(self.fg_pass_frame, width=300, height=2.0, bg="white", highlightthickness=0)
        self.phone_number_line.place(x=250, y=420)

        self.phone_icon = Image.open("Assets/Icons/phone_icon.png")
        photo = ImageTk.PhotoImage(self.phone_icon)
        self.phone_icon_label = Label(self.fg_pass_frame, image=photo, bg=BGCOLOR)
        self.phone_icon_label.image = photo
        self.phone_icon_label.place(x=250, y=392)

        # Email id

        self.email_label = Label(self.fg_pass_frame, text="Email ID", bg=BGCOLOR, fg="#4f4e4d",
                                 font=("Ariel", 13, "bold"))
        self.email_label.place(x=250, y=450)

        self.email_entry = Entry(self.fg_pass_frame, highlightthickness=0, relief=FLAT, bg=BGCOLOR, fg="white",
                                 font=("Ariel", 13, "bold"), cursor="xterm #AFAFAF", insertbackground="#AFAFAF")
        self.email_entry.place(x=285, y=473)
        self.email_line = Canvas(self.fg_pass_frame, width=300, height=2.0, bg="white", highlightthickness=0)
        self.email_line.place(x=250, y=500)

        self.mail_icon = Image.open("Assets/Icons/mail_icon1.png")
        photo = ImageTk.PhotoImage(self.mail_icon)
        self.mail_icon_label = Label(self.fg_pass_frame, image=photo, bg=BGCOLOR)
        self.mail_icon_label.image = photo
        self.mail_icon_label.place(x=250, y=472)

        # Submit

        self.submit_button = Image.open("Assets/Images/submit1.png")
        photo = ImageTk.PhotoImage(self.submit_button)
        self.submit_button_label = Label(self.fg_pass_frame, image=photo, bg=BGCOLOR, borderwidth=0)
        self.submit_button_label.image = photo
        self.submit_button_label.place(x=260, y=550)

        self.submit = Button(self.submit_button_label, text="SUBMIT", font=("Ariel", 13, "bold"), width=20, bd=0,
                             bg="#5271ff", cursor="hand2", activebackground="#5271ff", activeforeground="lightblue",
                             fg="white")   # command to new frame remaining

        self.submit.place(x=24, y=10)

        # Remaining to print the text that the info entered is valid or invalid in the database after
        # clicking submit button


if __name__ == "__main__":
    window = Tk()

    window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}")
    window["bg"] = BGCOLOR

    window.state("zoomed")
    window.resizable(width=False, height=False)
    window.title("TrafficLights Management")

    ForgotPass(window)
    window.mainloop()