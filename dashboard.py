import os
import random
import tkinter as tk
from tkVideoPlayer import TkinterVideo
from PIL import ImageTk, Image

import detection
import TLmanager

BGCOLOR = "#" + "10" * 3

VIDEO_PATH = "Assets/Videos/"
TL_IMG_PATH = "Assets/Images/TrafficLights/"

YELLOW_TIME = 5 #secs

# Dimensions and Positions for Video Players and Traffic Lights

# Vid Players

plREL_SIZE = .30

plCOL1_x = .17
plCOL2_x = .55

plROW1_y = .31
plROW2_y = .69

tlCOL1_x = .35
tlCOL2_x = .73

RED, YELLOW, GREEN, ALL, NONE = 1, 2, 3, 4, 0


class Dashboard(tk.Frame):
    def __init__(self, root):

        self.tlmanager = TLmanager.TLmanager()
        self.detector = detection.Detector()

        super().__init__(master=root)
        self.window = root

        window_height = self.window.winfo_screenheight()
        window_width = self.window.winfo_screenwidth()

        self.config(height=window_height, width=window_width, bg=BGCOLOR)
        self.pack(expand=True, fill=tk.BOTH)

        # TL Image

        self.tl_states = [RED, RED, RED, RED]
        img_names = ["TlNone", "TlRed", "TlYellow", "TlGreen", "TlAll"]

        self.tl_img_paths = [TL_IMG_PATH + name + ".png" for name in img_names]

        # 0 = None
        # 1 = Red
        # 2 = Yellow
        # 3 = Green
        # 4 = All

        # Video

        VIDEOS = os.listdir(VIDEO_PATH)
        VIDEOS = [vid for vid in VIDEOS if vid[-3:] in ["mp4", "m4a"]]

        self.SELECTED_VIDEOS = random.sample(VIDEOS, k=4)

        pl_width, pl_height = 700, 390

        rel_positions = [(plCOL1_x, plROW1_y), (plCOL2_x, plROW1_y), (plCOL1_x, plROW2_y), (plCOL2_x, plROW2_y)]

        # Player 1

        p1pos = rel_positions[0]

        p1frame = tk.Frame(master=self, bg=BGCOLOR, height=pl_height, width=pl_width)
        p1frame.place(relx=p1pos[0], rely=p1pos[1], relwidth=plREL_SIZE, relheight=plREL_SIZE, anchor=tk.CENTER)

        player1 = TkinterVideo(master=p1frame, bg=BGCOLOR, height=800, width=390)
        player1.load(VIDEO_PATH + self.SELECTED_VIDEOS[0])
        # player1.set_size((pl_width, pl_height))
        tk.Misc.lift(player1)
        player1.bind("<<Ended>>", lambda _: player1.play())
        player1.pack(expand=tk.YES, fill=tk.BOTH)

        # Player 2

        p2pos = rel_positions[1]

        p2frame = tk.Frame(master=self, bg=BGCOLOR, height=pl_height, width=pl_width)
        p2frame.place(relx=p2pos[0], rely=p2pos[1], relwidth=plREL_SIZE, relheight=plREL_SIZE, anchor=tk.CENTER)

        player2 = TkinterVideo(master=p2frame, bg=BGCOLOR, height=800, width=390)
        player2.load(VIDEO_PATH + self.SELECTED_VIDEOS[1])
        # player2.set_size((pl_width, pl_height))
        tk.Misc.lift(player2)
        player2.bind("<<Ended>>", lambda _: player2.play())
        player2.pack(expand=tk.YES, fill=tk.BOTH)

        # Player 3

        p3pos = rel_positions[2]

        p3frame = tk.Frame(master=self, bg=BGCOLOR, height=pl_height, width=pl_width)
        p3frame.place(relx=p3pos[0], rely=p3pos[1], relwidth=plREL_SIZE, relheight=plREL_SIZE, anchor=tk.CENTER)

        player3 = TkinterVideo(master=p3frame, bg=BGCOLOR, height=800, width=390)
        player3.load(VIDEO_PATH + self.SELECTED_VIDEOS[2])
        # player3.set_size((pl_width, pl_height))
        tk.Misc.lift(player3)
        player3.bind("<<Ended>>", lambda _: player3.play())
        player3.pack(expand=tk.YES, fill=tk.BOTH)

        # Player 4

        p4pos = rel_positions[3]

        p4frame = tk.Frame(master=self, bg=BGCOLOR, height=pl_height, width=pl_width)
        p4frame.place(relx=p4pos[0], rely=p4pos[1], relwidth=plREL_SIZE, relheight=plREL_SIZE, anchor=tk.CENTER)

        player4 = TkinterVideo(master=p4frame, bg=BGCOLOR, height=800, width=390)
        player4.load(VIDEO_PATH + self.SELECTED_VIDEOS[3])
        # player4.set_size((pl_width, pl_height))
        tk.Misc.lift(player4)
        player4.bind("<<Ended>>", lambda _: player4.play())
        player4.pack(expand=tk.YES, fill=tk.BOTH)

        self.players = [player1, player2, player3, player4]

        self.play_all()

        self.window.update()

        # Buttons

        play_all_btn = tk.Button(text="Play All", command=self.play_all)
        play_all_btn.place(relx=0.793, rely=0.595, relheight=0.05, relwidth=0.19)

        pause_all_btn = tk.Button(text="Pause All", command=self.pause_all)
        pause_all_btn.place(relx=0.793, rely=0.65, relheight=0.05, relwidth=0.19)

        self.pause_vars = [tk.BooleanVar() for _ in range(4)]

        pause_1_chkbtn = tk.Checkbutton(root, text="Pause 1", onvalue=True, offvalue=False, height=2, width=10,
                                        variable=self.pause_vars[0])
        pause_1_chkbtn.place(relx=0.793, rely=0.705, relwidth=0.045, relheight=0.05)

        pause_2_chkbtn = tk.Checkbutton(root, text="Pause 2", onvalue=True, offvalue=False, height=2, width=10,
                                        variable=self.pause_vars[1])
        pause_2_chkbtn.place(relx=0.8415, rely=0.705, relwidth=0.045, relheight=0.05)

        pause_3_chkbtn = tk.Checkbutton(root, text="Pause 3", onvalue=True, offvalue=False, height=2, width=10,
                                        variable=self.pause_vars[2])
        pause_3_chkbtn.place(relx=0.89, rely=0.705, relwidth=0.045, relheight=0.05)

        pause_4_chkbtn = tk.Checkbutton(root, text="Pause 4", onvalue=True, offvalue=False, height=2, width=10,
                                        variable=self.pause_vars[3])
        pause_4_chkbtn.place(relx=0.9385, rely=0.705, relwidth=0.044, relheight=0.05)

        pause_selective_btn = tk.Button(text="Pause Selected", command=self.pause_selective)
        pause_selective_btn.place(relx=0.793, rely=0.815, relwidth=0.19, relheight=0.05)

        play_selective_btn = tk.Button(text="Play Selected", command=self.play_selective)
        play_selective_btn.place(relx=0.793, rely=0.76, relwidth=0.19, relheight=0.05)

        tl_height = int(window_height * (plREL_SIZE + 0.001))
        tl_width = int(tl_height * .345)

        # Traffic Lights
        self.tl_img_pil = []
        for tl in self.tl_img_paths:
            io = Image.open(tl)
            # Width/Height ratio for Images = 0.345

            io = io.resize(size=(tl_width, tl_height))
            img = ImageTk.PhotoImage(io)

            self.tl_img_pil.append(img)

        tl_width /= window_width
        tl_height /= window_height

        self.tl_state_to_img = {idx: img for img, idx in zip(self.tl_img_pil, range(0, 5))}

        tl_positions = [(tlCOL1_x, plROW1_y), (tlCOL2_x, plROW1_y), (tlCOL1_x, plROW2_y), (tlCOL2_x, plROW2_y)]

        self.tl_img = []
        for state, pos in zip(self.tl_states, tl_positions):
            tl_img_lbl = tk.Label(self, image=self.tl_state_to_img[state], bg=BGCOLOR)
            tl_img_lbl.place(relx=pos[0], rely=pos[1], anchor=tk.CENTER, relheight=tl_height, relwidth=tl_width)
            self.tl_img.append(tl_img_lbl)

        window.after(1000, self.get_allocated_time)

    # Commands

    def play_all(self):
        for element in self.players:
            element.play()

    def pause_all(self):
        for element in self.players:
            element.pause()

    def play_selective(self):
        for var, player in zip(self.pause_vars, self.players):
            if var.get():
                player.play()

    def pause_selective(self):
        for var, player in zip(self.pause_vars, self.players):
            if var.get():
                player.pause()

    def update_lights(self, t1=None, t2=None, t3=None, t4=None):
        for idx, tl in enumerate([t1, t2, t3, t4]):
            if tl is None:
                continue
            else:
                self.tl_states[idx] = tl
                self.tl_img[idx]["image"] = self.tl_state_to_img[tl]

    def get_duration(self):
        durations = [player.current_duration() for player in self.players]
        return durations

    def get_allocated_time(self):
        self.pause_all()
        self.update_lights(t1=RED, t2=RED, t3=RED, t4=RED)

        allt_times = []

        for vid, dur in zip(self.SELECTED_VIDEOS, self.get_duration()):
            self.detector.set_vid(vid)
            count_vehicles = self.detector.get_count(dur, show=0)
            allt_time = self.tlmanager.get_alloted_time(count_vehicles)

            allt_times.append(allt_time)

        sel_tl, green_time_alloted = self.tlmanager.select_tl(allt_times)
        print(sel_tl, green_time_alloted)
        self.green_for_n(sel_tl, green_time_alloted)



    def green_for_n(self, sel_tl, green_time_allt):
        print("GREEN")
        self.players[sel_tl].play()
        self.tl_img[sel_tl]["image"] = self.tl_state_to_img[GREEN]

        def yellow_after_n():
            self.players[sel_tl].pause()
            print("EYELLOW")
            self.tl_states[sel_tl] = YELLOW

            self.tl_img[sel_tl]["image"] = self.tl_state_to_img[YELLOW]

            window.after(YELLOW_TIME * 1000, self.get_allocated_time)

        window.after(green_time_allt * 1000, yellow_after_n)




if __name__ == "__main__":
    window = tk.Tk()

    window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}")

    window["bg"] = BGCOLOR

    window.state("zoomed")
    window.resizable(width=False, height=False)
    window.title("Traffic Lights Management")

    dash = Dashboard(window)
    window.mainloop()
