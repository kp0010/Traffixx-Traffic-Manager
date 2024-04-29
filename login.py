import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

import database

BGCOLOR = "#" + "03" * 3


class Login(tk.Frame):
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

        self.lgn_frame = Frame(self, bg=BGCOLOR, width=1050, height=700)
        self.lgn_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Title Text

        self.txt = "WELCOME TO TRAFFIXX"
        self.heading = Label(self.lgn_frame, text=self.txt, font=("Ariel", 25, "bold"), bg=BGCOLOR, fg="white")
        self.heading.place(x=70, y=45, width=900, height=30)

        # Splash Images

        self.side_image = Image.open("Assets/Images/LoginSplash.png")
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg=BGCOLOR)
        self.side_image_label.image = photo
        self.side_image_label.place(x=45, y=150)

        # self.sign_in_image = Image.open("Assets/Images/UserAvatar.png")
        # photo = ImageTk.PhotoImage(self.sign_in_image)
        # self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg=BGCOLOR)
        # self.sign_in_image_label.image = photo
        # self.sign_in_image_label.place(x=680, y=140)

        self.logo_image = Image.open("Assets/Images/FinalLogo3.png")
        photo = ImageTk.PhotoImage(self.logo_image)
        self.logo_image_label = Label(self.lgn_frame, image=photo, bg=BGCOLOR)
        self.logo_image_label.image = photo
        self.logo_image_label.place(x=665, y=130)

        # Sign In Label

        self.sign_in_label = Label(self.lgn_frame, text="LOG IN", bg=BGCOLOR, fg="white", font=("Ariel", 18, "bold"))
        self.sign_in_label.place(x=700, y=290)

        # UserID

        self.userid_label = Label(self.lgn_frame, text="UserID", bg=BGCOLOR, fg="#4f4e4d", font=("Ariel", 13, "bold"))
        self.userid_label.place(x=600, y=340)

        self.userid_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg=BGCOLOR, fg="white",
                                  font=("Ariel", 13, "bold"), cursor="xterm #AFAFAF", insertbackground="#AFAFAF")
        self.userid_entry.place(x=635, y=363)
        self.userid_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="white", highlightthickness=0)
        self.userid_line.place(x=600, y=390)

        self.userid_icon = Image.open("Assets/Icons/UsernameIcon.png")
        photo = ImageTk.PhotoImage(self.userid_icon)
        self.userid_icon_label = Label(self.lgn_frame, image=photo, bg=BGCOLOR)
        self.userid_icon_label.image = photo
        self.userid_icon_label.place(x=600, y=362)

        # Password

        self.password_label = Label(self.lgn_frame, text="Password", bg=BGCOLOR, fg="#4f4e4d",
                                    font=("Ariel", 13, "bold"))
        self.password_label.place(x=600, y=420)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg=BGCOLOR, fg="white",
                                    font=("Ariel", 13, "bold"), cursor="xterm #AFAFAF", insertbackground="#AFAFAF")
        self.password_entry.place(x=635, y=443)
        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="white", highlightthickness=0)
        self.password_line.place(x=600, y=470)

        self.password_icon = Image.open("Assets/Icons/PasswordIcon.png")
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg=BGCOLOR)
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=600, y=442)

        # Login Button

        self.lgn_button = Image.open("Assets/Images/LoginBtnBg1.png")
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg=BGCOLOR, borderwidth=0)
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=625, y=495)

        # Fn to go to Dashboard after loggin in

        def login_to_dash(user):
            self.destroy()
            import dashboard
            dashboard.Dashboard(self.window, userid=user.id, username=user.name)

        def check_user_cred():
            userid = self.userid_entry.get()
            password = self.password_entry.get()

            db = database.Database()

            req_user = db.check_user_cred(userid=userid, password=password)

            if req_user is None:
                # show_error()
                self.error["text"] = "Invalid ID"

            elif not req_user:
                self.error["text"] = "Password Incorrect"
            else:
                self.error["fg"] = "green"
                self.error["text"] = "Logged In Successfully"

                self.window.after(100, login_to_dash, req_user)


        self.error = Label(self.lgn_frame, text="", font=("Ariel", 13, "normal"), bg=BGCOLOR, fg="red")
        self.error.place(x=750, y=560, anchor=tk.CENTER)

        self.login = Button(self.lgn_button_label, text="LOGIN", font=("Ariel", 13, "bold"), width=20, bd=0,
                            bg="#5271ff", cursor="hand2", activebackground="#5271ff", activeforeground="lightblue",
                            fg="white", command=check_user_cred)

        self.login.place(x=20, y=10)  # will check info in database

        # Forgot Button

        def login_to_forgotpass():
            self.destroy()
            import forgotpass
            forgotpass.ForgotPass(self.window)

        self.forgot_button = Button(self.lgn_frame, text="Forgot Password ?", font=("Ariel", 13, "bold underline"),
                                    width=25, bd=0, bg=BGCOLOR, cursor="hand2", activebackground=BGCOLOR,
                                    activeforeground="lightblue", fg="white", command=login_to_forgotpass)
        self.forgot_button.place(x=625, y=600)

        # Sign Up

        def login_to_signup():
            self.destroy()
            import signup
            signup.SignUp(self.window)

        self.sign_up_label = Label(self.lgn_frame, text="No account yet?", font=("Ariel", 13, "bold",), bg=BGCOLOR,
                                   fg="white")
        self.sign_up_label.place(x=600, y=650)

        self.sign_up_button = Image.open("Assets/Images/SignUp2.png")
        photo = ImageTk.PhotoImage(self.sign_up_button)
        self.sign_up_button_label = tk.Label(self.lgn_frame, image=photo, bg=BGCOLOR, borderwidth=0,
                                             activebackground=BGCOLOR, fg="white", cursor="hand2", bd=0)
        self.sign_up_button_label.image = photo
        self.sign_up_button_label.place(x=780, y=644)

        self.sign_up = Button(self.sign_up_button_label, text="SIGN UP", font=("Ariel", 10, "bold"), width=10, bd=0,
                              bg="#3abee1", cursor="hand2", activebackground="#3abee1", activeforeground="lightblue",
                              fg="white", command=login_to_signup)

        self.sign_up.place(x=17, y=4)

        # Show Hide Password

        self.show_image = Image.open("Assets/Icons/ShowIcon.png")
        self.photo1 = ImageTk.PhotoImage(self.show_image)
        self.show_button = Button(self.lgn_frame, image=self.photo1, bg=BGCOLOR, activebackground="white",
                                  cursor="hand2", bd=0, command=self.show)
        self.show_button.image = self.photo1
        self.hide()
        self.show_button.place(x=906, y=448)

        self.hide_image = Image.open("Assets/Icons/HideIcon.png")
        self.photo = ImageTk.PhotoImage(self.hide_image)

    def show(self):
        hide_button = Button(self.lgn_frame, image=self.photo, bg="white", activebackground="white", cursor="hand2",
                             bd=0, command=self.hide)
        hide_button.image = self.photo
        hide_button.place(x=906, y=448)
        self.password_entry.config(show='')

    def hide(self):
        show_button = Button(self.lgn_frame, image=self.photo1, bg="white", activebackground="white", cursor="hand2",
                             bd=0, command=self.show)
        show_button.image = self.photo1
        show_button.place(x=906, y=448)
        self.password_entry.config(show="*")


if __name__ == "__main__":
    window = Tk()

    icon = tk.PhotoImage(file="Assets/Images/FinalLogo3.png")
    window.wm_iconphoto(False, icon)

    window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}")

    window["bg"] = BGCOLOR

    window.state("zoomed")
    window.resizable(width=False, height=False)
    window.title("Traffixx")

    Login(window)
    window.mainloop()
