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
        self.heading1 = Label(self.fg_pass_frame, text=self.txt, font=("Ariel", 8), bg=BGCOLOR, fg="white")
        self.heading1.place(x=0, y=120, width=800, height=30)

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
                             fg="white",command=self.switch_frame)   # command to new frame remaining

        self.submit.place(x=24, y=10)

        # Remaining to print the text that the info entered is valid or invalid in the database after
        # clicking submit button

    def switch_frame(self):
        self.destroy()
        NewPass(self.window)


class NewPass(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.window = root
        self.pack(fill=tk.BOTH, expand=True)

        # Background

        self.bg_frame = Image.open("Assets/Images/Bg.png")
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self, image=photo, bg=BGCOLOR)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill=tk.BOTH, expand=True)

        # Frame

        self.new_pass_frame = Frame(self, bg=BGCOLOR, width=700, height=600)
        self.new_pass_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Title Text

        self.txt = "NEW CREDENTIALS"
        self.heading2 = Label(self.new_pass_frame, text=self.txt, font=("Ariel", 25, "bold"), bg=BGCOLOR, fg="white")
        self.heading2.place(x=0, y=85, width=700, height=30)

        # Text

        self.txt = ("Your identity has been verified!")
        self.heading3 = Label(self.new_pass_frame, text=self.txt, font=("Ariel", 10), bg=BGCOLOR, fg="white")
        self.heading3.place(x=0, y=120, width=700, height=30)

        # Text

        self.txt = ("Set your new password")
        self.heading3 = Label(self.new_pass_frame, text=self.txt, font=("Ariel", 10), bg=BGCOLOR, fg="white")
        self.heading3.place(x=0, y=150, width=700, height=30)

        # New Password

        self.new_pass_label = Label(self.new_pass_frame, text="New Password", bg=BGCOLOR, fg="#4f4e4d",
                                     font=("Ariel", 13, "bold"))
        self.new_pass_label.place(x=200, y=230)

        self.new_pass_entry = Entry(self.new_pass_frame, highlightthickness=0, relief=FLAT, bg=BGCOLOR, fg="white",
                                     font=("Ariel", 13, "bold"), cursor="xterm #AFAFAF", insertbackground="#AFAFAF")
        self.new_pass_entry.place(x=235, y=253)
        self.new_pass_line = Canvas(self.new_pass_frame, width=300, height=2.0, bg="white", highlightthickness=0)
        self.new_pass_line.place(x=200, y=280)

        self.new_pass_icon = Image.open("Assets/Icons/PasswordIcon.png")
        photo = ImageTk.PhotoImage(self.new_pass_icon)
        self.new_pass_icon_label = Label(self.new_pass_frame, image=photo, bg=BGCOLOR)
        self.new_pass_icon_label.image = photo
        self.new_pass_icon_label.place(x=200, y=253)

        # Show Hide Button for New Password

        self.show_image1 = Image.open("Assets/Icons/ShowIcon.png")
        self.photo1 = ImageTk.PhotoImage(self.show_image1)
        self.show_button1 = Button(self.new_pass_frame, image=self.photo1, bg=BGCOLOR, activebackground="white",
                                  cursor="hand2", bd=0, command=self.show)
        self.show_button1.image = self.photo1
        self.hide()
        self.show_button1.place(x=505, y=255)

        self.hide_image1 = Image.open("Assets/Icons/HideIcon.png")
        self.photo2 = ImageTk.PhotoImage(self.hide_image1)

        # Confirm Password

        self.con_pass_label = Label(self.new_pass_frame, text="Confirm Password", bg=BGCOLOR, fg="#4f4e4d",
                                    font=("Ariel", 13, "bold"))
        self.con_pass_label.place(x=200, y=310)

        self.con_pass_entry = Entry(self.new_pass_frame, highlightthickness=0, relief=FLAT, bg=BGCOLOR, fg="white",
                                    font=("Ariel", 13, "bold"), cursor="xterm #AFAFAF", insertbackground="#AFAFAF")
        self.con_pass_entry.place(x=235, y=333)
        self.con_pass_line = Canvas(self.new_pass_frame, width=300, height=2.0, bg="white", highlightthickness=0)
        self.con_pass_line.place(x=200, y=360)

        self.con_pass_icon = Image.open("Assets/Icons/PasswordIcon.png")
        photo = ImageTk.PhotoImage(self.new_pass_icon)
        self.con_pass_icon_label = Label(self.new_pass_frame, image=photo, bg=BGCOLOR)
        self.con_pass_icon_label.image = photo
        self.con_pass_icon_label.place(x=200, y=333)

        # Update Password Button

        self.update_button = Image.open("Assets/Images/submit1.png")
        photo = ImageTk.PhotoImage(self.update_button)
        self.update_button_label = Label(self.new_pass_frame, image=photo, bg=BGCOLOR, borderwidth=0)
        self.update_button_label.image = photo
        self.update_button_label.place(x=210, y=450)

        self.update = Button(self.update_button_label, text="UPDATE", font=("Ariel", 13, "bold"), width=20, bd=0,
                             bg="#5271ff", cursor="hand2", activebackground="#5271ff", activeforeground="lightblue",
                             fg="white")  # command to update new password in database REMAINING

        self.update.place(x=24, y=10)

    def show(self):
        hide_button = Button(self.new_pass_frame, image=self.photo2, bg="white", activebackground="white", cursor="hand2",
                             bd=0, command=self.hide)
        hide_button.image = self.photo2
        hide_button.place(x=505, y=255)
        self.new_pass_entry.config(show='')

    def hide(self):
        show_button = Button(self.new_pass_frame, image=self.photo1, bg="white", activebackground="white", cursor="hand2",
                             bd=0, command=self.show)
        show_button.image = self.photo1
        show_button.place(x=505, y=255)
        self.new_pass_entry.config(show="*")


if __name__ == "__main__":
    window = Tk()

    window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}")
    window["bg"] = BGCOLOR

    window.state("zoomed")
    window.resizable(width=False, height=False)
    window.title("TrafficLights Management")

    ForgotPass(window)
    window.mainloop()