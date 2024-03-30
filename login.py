from tkinter import *
from PIL import ImageTk, Image


class login:
    def __init__(self, window):
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

        self.lgn_frame = Frame(self.window, bg="#020202", width=1050, height=700)
        self.lgn_frame.place(x=250, y=80)


        # Title Text

        self.txt = "WELCOME TO SMART TRAFFIC MANAGEMENT SYSTEM"
        self.heading = Label(self.lgn_frame, text=self.txt, font=("Ariel", 25, "bold"), bg="black", fg="white")
        self.heading.place(x=70, y=100, width=900, height=30)


        # Splash Images
        
        self.side_image = Image.open("Assets/Images/LoginSplash.png")
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg="black")
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=160)

        self.sign_in_image = Image.open("Assets/Images/UserAvatar.png")
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg="black")
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=680, y=200)


        # Sign In Label

        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="black", fg="white", font=("Ariel", 17, "bold"))
        self.sign_in_label.place(x=710, y=305)


        # Username

        self.username_label = Label(self.lgn_frame, text="Username", bg="black", fg="#4f4e4d",
                                    font=("Ariel", 13, "bold"))
        self.username_label.place(x=600, y=370)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="black", fg="white",
                                    font=("Ariel", 13, "bold"), cursor="xterm #AFAFAF", insertbackground="#AFAFAF")
        self.username_entry.place(x=635, y=393)
        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=600, y=420)

        self.username_icon = Image.open("Assets/Images/UsernameIcon.png")
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg="black")
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=600, y=392)


        # Password

        self.password_label = Label(self.lgn_frame, text="Password", bg="black", fg="#4f4e4d",
                                    font=("Ariel", 13, "bold"))
        self.password_label.place(x=600, y=450)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="black", fg="white",
                                    font=("Ariel", 13, "bold"), cursor="xterm #AFAFAF", insertbackground="#AFAFAF")
        self.password_entry.place(x=635, y=473)
        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=600, y=500)

        self.password_icon = Image.open("Assets/Images/PasswordIcon.png")
        photo = ImageTk.PhotoImage(self.username_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg="black")
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=600, y=472)


        # Login Button

        self.lgn_button = Image.open("Assets/Images/LoginBtnBg.png")
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg="black", borderwidth=0)
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=600, y=510)

        self.login = Button(self.lgn_button_label, text="LOGIN", font=("Ariel", 13, "bold"), width=25, bd=0,
                            bg="#3047ff", cursor="hand2", activebackground="#3047ff", activeforeground="black",
                            fg="white")
        self.login.place(x=20, y=15)

        # Forgot Button

        self.forgot_button = Button(self.lgn_frame, text="Forgot Password ?", font=("Ariel", 13, "bold underline"),
                                    width=25, bd=0, bg="black", cursor="hand2", activebackground="black",
                                    activeforeground="green", fg="white")
        self.forgot_button.place(x=640, y=570)


        # Sign Up

        self.sign_up_label = Label(self.lgn_frame, text="No account yet?", font=("Ariel", 13, "bold",), bg="black",
                                   fg="white")
        self.sign_up_label.place(x=600, y=620)

        self.sign_up_button = Image.open("Assets/Images/SignUpNow.png")
        photo = ImageTk.PhotoImage(self.sign_up_button)
        self.sign_up_button_label = Button(self.lgn_frame, image=photo, bg="black", activebackground="black",
                                           cursor="hand2", bd=0)
        self.sign_up_button_label.image = photo
        self.sign_up_button_label.place(x=750, y=614)


        # Show Hide Password

        self.show_image = Image.open("Assets/Images/ShowIcon.png")
        self.photo1 = ImageTk.PhotoImage(self.show_image)
        self.show_button = Button(self.lgn_frame, image=self.photo1, bg="white", activebackground="white",
                                  cursor="hand2", bd=0, command=self.show)
        self.show_button.image = self.photo1
        self.hide()
        self.show_button.place(x=906, y=478)

        self.hide_image = Image.open("Assets/Images/HideIcon.png")
        self.photo = ImageTk.PhotoImage(self.hide_image)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.photo, bg="white", activebackground="white",
                                  cursor="hand2", bd=0, command=self.hide)
        self.hide_button.image = self.photo
        self.hide_button.place(x=906, y=478)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.photo1, bg="white", activebackground="white",
                                  cursor="hand2", bd=0, command=self.show)
        self.show_button.image = self.photo1
        self.show_button.place(x=906, y=478)
        self.password_entry.config(show="*")


def page():
    window = Tk(className="LoginPage")
    login(window)
    window.mainloop()


if __name__ == "__main__":
    page()
