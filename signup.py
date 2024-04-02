import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

import login

BGCOLOR = "#" + "03" * 3


class SignUp(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root, bg=BGCOLOR)

        self.window = root

        self.pack(expand=True, fill=tk.BOTH)

        # Background

        self.bg_frame = Image.open("Assets/Images/Bg.png")
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill="both", expand=True)

        # Frame

        self.sign_up_frame = Frame(self, bg=BGCOLOR, width=1050, height=700)
        self.sign_up_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Title Text

        self.txt = "REGISTER"
        self.heading = Label(self.sign_up_frame, text=self.txt, font=("Ariel", 25, "bold"), bg=BGCOLOR, fg="white")
        self.heading.place(relx=.5, rely=.1, width=900, height=30, anchor=tk.CENTER)

        # Traffic Police ID

        self.id_number_label = Label(self.sign_up_frame, text="ID Number", bg=BGCOLOR, fg="#4f4e4d",
                                     font=("Ariel", 13, "bold"))
        self.id_number_label.place(x=200, y=130)

        self.id_number_entry = Entry(self.sign_up_frame, highlightthickness=0, relief=FLAT, bg=BGCOLOR, fg="white",
                                     font=("Ariel", 13, "bold"), cursor="xterm #AFAFAF", insertbackground="#AFAFAF")
        self.id_number_entry.place(x=235, y=153)
        self.id_number_line = Canvas(self.sign_up_frame, width=300, height=2.0, bg="white", highlightthickness=0)
        self.id_number_line.place(x=200, y=180)

        self.id_icon = Image.open("Assets/Icons/id_icon.png")
        photo = ImageTk.PhotoImage(self.id_icon)
        self.id_icon_label = Label(self.sign_up_frame, image=photo, bg=BGCOLOR)
        self.id_icon_label.image = photo
        self.id_icon_label.place(x=200, y=157)

        # Username/Full Name

        self.username_label = Label(self.sign_up_frame, text="Full Name", bg=BGCOLOR, fg="#4f4e4d",
                                    font=("Ariel", 13, "bold"))
        self.username_label.place(x=200, y=210)

        self.username_entry = Entry(self.sign_up_frame, highlightthickness=0, relief=FLAT, bg=BGCOLOR, fg="white",
                                    font=("Ariel", 13, "bold"), cursor="xterm #AFAFAF", insertbackground="#AFAFAF")
        self.username_entry.place(x=235, y=233)
        self.username_line = Canvas(self.sign_up_frame, width=300, height=2.0, bg="white", highlightthickness=0)
        self.username_line.place(x=200, y=260)

        self.username_icon = Image.open("Assets/Icons/UsernameIcon.png")
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.sign_up_frame, image=photo, bg=BGCOLOR)
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=200, y=232)

        # Password

        self.password_label = Label(self.sign_up_frame, text="Password", bg=BGCOLOR, fg="#4f4e4d",
                                    font=("Ariel", 13, "bold"))
        self.password_label.place(x=200, y=290)

        self.password_entry = Entry(self.sign_up_frame, highlightthickness=0, relief=FLAT, bg=BGCOLOR, fg="white",
                                    font=("Ariel", 13, "bold"), cursor="xterm #AFAFAF", insertbackground="#AFAFAF")
        self.password_entry.place(x=235, y=313)
        self.password_line = Canvas(self.sign_up_frame, width=300, height=2.0, bg="white", highlightthickness=0)
        self.password_line.place(x=200, y=340)

        self.password_icon = Image.open("Assets/Icons/PasswordIcon.png")
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.sign_up_frame, image=photo, bg=BGCOLOR)
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=200, y=312)

        # Phone Number

        def validate_phoneno(inp):
            if len(str(inp)) > 10:
                return False

            elif inp.isdigit() or inp == "":
                return True

            return False

        validator = self.window.register(validate_phoneno)

        self.phone_number_label = Label(self.sign_up_frame, text="Phone Number", bg=BGCOLOR, fg="#4f4e4d",
                                        font=("Ariel", 13, "bold"))
        self.phone_number_label.place(x=200, y=370)

        self.phone_number_entry = Entry(self.sign_up_frame, highlightthickness=0, relief=FLAT, bg=BGCOLOR, fg="white",
                                        font=("Ariel", 13, "bold"), cursor="xterm #AFAFAF", insertbackground="#AFAFAF",
                                        validate="key", validatecommand=(validator, "%P"))
        self.phone_number_entry.place(x=235, y=393)
        self.phone_number_line = Canvas(self.sign_up_frame, width=300, height=2.0, bg="white", highlightthickness=0)
        self.phone_number_line.place(x=200, y=420)

        self.phone_icon = Image.open("Assets/Icons/phone_icon.png")
        photo = ImageTk.PhotoImage(self.phone_icon)
        self.phone_icon_label = Label(self.sign_up_frame, image=photo, bg=BGCOLOR)
        self.phone_icon_label.image = photo
        self.phone_icon_label.place(x=200, y=392)

        # Email id

        self.email_label = Label(self.sign_up_frame, text="Email ID", bg=BGCOLOR, fg="#4f4e4d",
                                 font=("Ariel", 13, "bold"))
        self.email_label.place(x=200, y=450)

        self.email_entry = Entry(self.sign_up_frame, highlightthickness=0, relief=FLAT, bg=BGCOLOR, fg="white",
                                 font=("Ariel", 13, "bold"), cursor="xterm #AFAFAF", insertbackground="#AFAFAF")
        self.email_entry.place(x=235, y=473)
        self.email_line = Canvas(self.sign_up_frame, width=300, height=2.0, bg="white", highlightthickness=0)
        self.email_line.place(x=200, y=500)

        self.mail_icon = Image.open("Assets/Icons/mail_icon.png")
        photo = ImageTk.PhotoImage(self.mail_icon)
        self.mail_icon_label = Label(self.sign_up_frame, image=photo, bg=BGCOLOR)
        self.mail_icon_label.image = photo
        self.mail_icon_label.place(x=200, y=472)

        # Submit Button

        self.submit_button = Image.open("Assets/Images/SubmitBtnBg1.png")
        photo = ImageTk.PhotoImage(self.submit_button)
        self.submit_button_label = Label(self.sign_up_frame, image=photo, bg=BGCOLOR, borderwidth=0)
        self.submit_button_label.image = photo
        self.submit_button_label.place(x=220, y=530)

        self.submit = Button(self.submit_button_label, text="SUBMIT", font=("Ariel", 13, "bold"), width=20, bd=0,
                             bg="#3047ff", cursor="hand2", activebackground="#3047ff", activeforeground="lightblue",
                             fg="white")

        self.submit.place(x=18, y=10)  # info will be inserted in database

        # Signin

        self.log_in_label = Label(self.sign_up_frame, text="Already have an account?", font=("Ariel", 13, "bold",),
                                  bg=BGCOLOR,
                                  fg="white")
        self.log_in_label.place(x=200, y=600)

        self.log_in_button = Image.open("Assets/Images/SignUp2.png")
        photo = ImageTk.PhotoImage(self.log_in_button)
        self.log_in_button_label = tk.Label(self.sign_up_frame, image=photo, bg=BGCOLOR, borderwidth=0,
                                            activebackground=BGCOLOR,
                                            cursor="hand2", bd=0)
        self.log_in_button_label.image = photo
        self.log_in_button_label.place(x=410, y=595)

        def signup_to_login():
            self.destroy()
            login.Login(self.window)

        self.log_in = Button(self.log_in_button_label, text="LOG IN", font=("Ariel", 10, "bold"), width=10, bd=0,
                             bg="#3abee1", cursor="hand2", activebackground="#3abee1", activeforeground="lightblue",
                             fg="white", command=signup_to_login)

        self.log_in.place(x=15, y=5)


if __name__ == "__main__":
    window = Tk()

    window_height = window.winfo_screenheight()
    window_width = window.winfo_screenwidth()

    window.geometry(f"{window_width}x{window_height}")

    window.state("zoomed")
    window.resizable(0, 0)
    window.title("Traffic Light Management")

    SignUp(window)

    window.mainloop()
