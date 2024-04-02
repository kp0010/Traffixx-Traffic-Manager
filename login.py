import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

BGCOLOR = "#" + "03" * 3


class login(tk.Frame):
    def __init__(self, window):
        super().__init__(window)
        self.window = window

        self.window.config(bg="red")

        self.pack(fill=tk.BOTH, expand=True)

        # Background

        self.bg_frame = Image.open("Assets/Images/Bg.png")
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self, image=photo, bg=BGCOLOR)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill=tk.BOTH, expand=True)

        # Frame

        self.lgn_frame = Frame(self, bg=BGCOLOR, width=1050, height=700)
        self.lgn_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Title Text

        self.txt = "WELCOME TO SMART TRAFFIC MANAGEMENT SYSTEM"
        self.heading = Label(self.lgn_frame, text=self.txt, font=("Ariel", 25, "bold"), bg=BGCOLOR, fg="white")
        self.heading.place(x=70, y=45, width=900, height=30)

        # Splash Images

        self.side_image = Image.open("Assets/Images/LoginSplash.png")
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg=BGCOLOR)
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=160)

        self.sign_in_image = Image.open("Assets/Images/UserAvatar.png")
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg=BGCOLOR)
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=680, y=200)

        # Sign In Label

        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg=BGCOLOR, fg="white", font=("Ariel", 17, "bold"))
        self.sign_in_label.place(x=710, y=305)

        # Username

        self.username_label = Label(self.lgn_frame, text="Username", bg=BGCOLOR, fg="#4f4e4d",
                                    font=("Ariel", 13, "bold"))
        self.username_label.place(x=600, y=370)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg=BGCOLOR, fg="white",
                                    font=("Ariel", 13, "bold"), cursor="xterm #AFAFAF", insertbackground="#AFAFAF")
        self.username_entry.place(x=635, y=393)
        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="white", highlightthickness=0)
        self.username_line.place(x=600, y=420)

        self.username_icon = Image.open("Assets/Images/UsernameIcon.png")
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg=BGCOLOR)
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=600, y=392)

        # Password

        self.password_label = Label(self.lgn_frame, text="Password", bg=BGCOLOR, fg="#4f4e4d",
                                    font=("Ariel", 13, "bold"))
        self.password_label.place(x=600, y=450)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg=BGCOLOR, fg="white",
                                    font=("Ariel", 13, "bold"), cursor="xterm #AFAFAF", insertbackground="#AFAFAF")
        self.password_entry.place(x=635, y=473)
        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="white", highlightthickness=0)
        self.password_line.place(x=600, y=500)

        self.password_icon = Image.open("Assets/Images/PasswordIcon.png")
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg=BGCOLOR)
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=600, y=472)

        # Login Button

        self.lgn_button = Image.open("Assets/Images/LoginBtnBg.png")
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg=BGCOLOR, borderwidth=0)
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=600, y=510)

        def login_to_dash():
            self.destroy()
            import dashboard
            dashboard.Dashboard(self.window)

        self.login = Button(self.lgn_button_label, text="LOGIN", font=("Ariel", 13, "bold"), width=25, bd=0,
                            bg="#3047ff", cursor="hand2", activebackground="#3047ff", activeforeground="lightblue",
                            fg="white", command=login_to_dash)

        self.login.place(x=20, y=15)  # will check info in database

        # Forgot Button

        self.forgot_button = Button(self.lgn_frame, text="Forgot Password ?", font=("Ariel", 13, "bold underline"),
                                    width=25, bd=0, bg=BGCOLOR, cursor="hand2", activebackground=BGCOLOR,
                                    activeforeground="lightblue", fg="white")
        self.forgot_button.place(x=625,
                                 y=570)  # will allow to change password by verifying name,id,phoneno,email of user

        # Sign Up

        self.sign_up_label = Label(self.lgn_frame, text="No account yet?", font=("Ariel", 13, "bold",), bg=BGCOLOR,
                                   fg="white")
        self.sign_up_label.place(x=600, y=620)

        self.sign_up_button = Image.open("Assets/Images/SignUp2.png")
        photo = ImageTk.PhotoImage(self.sign_up_button)
        self.sign_up_button_label = tk.Label(self.lgn_frame, image=photo, bg=BGCOLOR, borderwidth=0,
                                             activebackground=BGCOLOR, fg="white",
                                             cursor="hand2", bd=0)
        self.sign_up_button_label.image = photo
        self.sign_up_button_label.place(x=750, y=614)

        self.sign_up = Button(self.sign_up_button_label, text="SIGN UP", font=("Ariel", 10, "bold"), width=10, bd=0,
                              bg="#3abee1", cursor="hand2", activebackground="#3abee1", activeforeground="lightblue",
                              fg="white")

        self.sign_up.place(x=15, y=5)

        # Show Hide Password

        self.show_image = Image.open("Assets/Images/ShowIcon.png")
        self.photo1 = ImageTk.PhotoImage(self.show_image)
        self.show_button = Button(self.lgn_frame, image=self.photo1, bg=BGCOLOR, activebackground="white",
                                  cursor="hand2", bd=0, command=self.show)
        self.show_button.image = self.photo1
        self.hide()
        self.show_button.place(x=906, y=478)

        self.hide_image = Image.open("Assets/Images/HideIcon.png")
        self.photo = ImageTk.PhotoImage(self.hide_image)

    def show(self):
        hide_button = Button(self.lgn_frame, image=self.photo, bg="white", activebackground="white",
                                  cursor="hand2", bd=0, command=self.hide)
        hide_button.image = self.photo
        hide_button.place(x=906, y=478)
        self.password_entry.config(show='')

    def hide(self):
        show_button = Button(self.lgn_frame, image=self.photo1, bg="white", activebackground="white",
                                  cursor="hand2", bd=0, command=self.show)
        show_button.image = self.photo1
        show_button.place(x=906, y=478)
        self.password_entry.config(show="*")


def page():
    window = Tk()

    window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}")

    window["bg"] = BGCOLOR

    window.state("zoomed")
    window.resizable(width=False, height=False)
    window.title("Traffic Light Management")

    login(window)
    window.mainloop()


if __name__ == "__main__":
    page()
