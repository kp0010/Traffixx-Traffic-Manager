from tkinter import *
from PIL import ImageTk, Image


class login:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1920x1080')
        self.window.state('zoomed')
        self.window.resizable(0, 0)

        self.bg_frame = Image.open('images\\background3.jpg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')

        self.lgn_frame = Frame(self.window, bg='black', width=1050, height=700)
        self.lgn_frame.place(x=250, y=80)

        self.txt = 'WELCOME TO SMART TRAFFIC MANAGEMENT SYSTEM'
        self.heading = Label(self.lgn_frame, text=self.txt, font=('Arail', 25, 'bold'), bg='black', fg='white')
        self.heading.place(x=70, y=100, width=900, height=30)

        self.side_image = Image.open('images\\vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='black')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=160)

        self.sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='black')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=680, y=200)

        self.sign_in_label = Label(self.lgn_frame, text='Sign In', bg='black', fg='white', font=('Arail', 17, 'bold'))
        self.sign_in_label.place(x=710, y=305)

        self.username_label = Label(self.lgn_frame, text='Username', bg='black', fg='#4f4e4d',
                                    font=('Arail', 13, 'bold'))
        self.username_label.place(x=600, y=370)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='black', fg='white',
                                    font=('Arail', 13, 'bold'))
        self.username_entry.place(x=635, y=396)
        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.username_line.place(x=600, y=420)

        self.username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='black')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=600, y=392)

        self.password_label = Label(self.lgn_frame, text='Password', bg='black', fg='#4f4e4d',
                                    font=('Arail', 13, 'bold'))
        self.password_label.place(x=600, y=450)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='black', fg='white',
                                    font=('Arail', 13, 'bold'))
        self.password_entry.place(x=635, y=476)
        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.password_line.place(x=600, y=500)

        self.password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='black')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=600, y=472)

        self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='black')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=600, y=510)

        self.login = Button(self.lgn_button_label, text='LOGIN', font=('Arial', 13, 'bold'), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', activeforeground='red',
                            fg='white')
        self.login.place(x=20, y=15)

        self.forgot_button = Button(self.lgn_frame, text='Forgot Password ?', font=('Arial', 13, 'bold underline'),
                                    width=25, bd=0, bg='black', cursor='hand2', activebackground='black',
                                    activeforeground='green', fg='white')
        self.forgot_button.place(x=640, y=570)

        self.sign_up_label = Label(self.lgn_frame, text='No account yet?', font=('Arial', 13, 'bold',), bg='black',
                                   fg='white')
        self.sign_up_label.place(x=600, y=620)

        self.sign_up_button = Image.open('images\\register.png')
        photo = ImageTk.PhotoImage(self.sign_up_button)
        self.sign_up_button_label = Button(self.lgn_frame, image=photo, bg='black', activebackground='black',
                                           cursor='hand2', bd=0)
        self.sign_up_button_label.image = photo
        self.sign_up_button_label.place(x=750, y=614)

        self.show_image = Image.open('images\\show.png')
        self.photo1 = ImageTk.PhotoImage(self.show_image)
        self.show_button = Button(self.lgn_frame, image=self.photo1, bg='white', activebackground='white',
                                  cursor='hand2', bd=0, command=self.show)
        self.show_button.image = self.photo1
        self.show_button.place(x=906, y=478)

        self.hide_image = Image.open('images\\hide.png')
        self.photo = ImageTk.PhotoImage(self.hide_image)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.photo, bg='white', activebackground='white',
                                  cursor='hand2', bd=0, command=self.hide)
        self.hide_button.image = self.photo
        self.hide_button.place(x=906, y=478)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.photo1, bg='white', activebackground='white',
                                  cursor='hand2', bd=0, command=self.show)
        self.show_button.image = self.photo1
        self.show_button.place(x=906, y=478)
        self.password_entry.config(show='*')


def page():
    window = Tk(className='LoginPage')
    login(window)
    window.mainloop()


if __name__ == "__main__":
    page()
