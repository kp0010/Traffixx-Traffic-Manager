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

YELLOW_TIME = 5  # secs

# Dimensions and Positions for Video Players and Traffic Lights

# Vid Players

plREL_SIZE = .30

plCOL1_x = .17
plCOL2_x = .55

plROW1_y = .31
plROW2_y = .69

# TL Pos and Info

tlCOL1_x = .35
tlCOL2_x = .73

RED, YELLOW, GREEN, ALL, NONE = 1, 2, 3, 4, 0

REDon = "#f1592a"
GREENon = "#37b44c"
YELLOWon = "#fff44d"


class Dashboard(tk.Frame):
    def __init__(self, root):

        self.tlmanager = TLmanager.TLmanager()
        self.detector = detection.Detector()

        self.green_timer = tk.IntVar(root)

        super().__init__(master=root)
        self.window = root

        window_height = self.window.winfo_screenheight()
        window_width = self.window.winfo_screenwidth()

        self.config(height=window_height, width=window_width, bg=BGCOLOR)
        self.pack(expand=True, fill=tk.BOTH)

        # TL Image

        img_names = ["TlNone", "TlRed", "TlYellow", "TlGreen", "TlAll"]

        self.tl_img_paths = [TL_IMG_PATH + name + ".png" for name in img_names]

        # 0 = None
        # 1 = Red
        # 2 = Yellow
        # 3 = Green
        # 4 = All

        # Video

        VIDEOS = os.listdir(VIDEO_PATH)
        VIDEOS = [vid for vid in VIDEOS if vid[-3:] in ["mp4", "m4v"]]

        self.SELECTED_VIDEOS = random.sample(VIDEOS, k=4)

        pl_width, pl_height = 700, 390

        self.rel_positions = [(plCOL1_x, plROW1_y), (plCOL2_x, plROW1_y), (plCOL1_x, plROW2_y), (plCOL2_x, plROW2_y)]

        # Player 1

        p1pos = self.rel_positions[0]

        p1frame = tk.Frame(master=self, bg=BGCOLOR, height=pl_height, width=pl_width)
        p1frame.place(relx=p1pos[0], rely=p1pos[1], relwidth=plREL_SIZE, relheight=plREL_SIZE, anchor=tk.CENTER)

        player1 = TkinterVideo(master=p1frame, bg=BGCOLOR, height=800, width=390)
        player1.load(VIDEO_PATH + self.SELECTED_VIDEOS[0])
        # player1.set_size((pl_width, pl_height))
        tk.Misc.lift(player1)
        player1.bind("<<Ended>>", lambda _: player1.play())
        player1.pack(expand=tk.YES, fill=tk.BOTH)

        # Player 2

        p2pos = self.rel_positions[1]

        p2frame = tk.Frame(master=self, bg=BGCOLOR, height=pl_height, width=pl_width)
        p2frame.place(relx=p2pos[0], rely=p2pos[1], relwidth=plREL_SIZE, relheight=plREL_SIZE, anchor=tk.CENTER)

        player2 = TkinterVideo(master=p2frame, bg=BGCOLOR, height=800, width=390)
        player2.load(VIDEO_PATH + self.SELECTED_VIDEOS[1])
        # player2.set_size((pl_width, pl_height))
        tk.Misc.lift(player2)
        player2.bind("<<Ended>>", lambda _: player2.play())
        player2.pack(expand=tk.YES, fill=tk.BOTH)

        # Player 3

        p3pos = self.rel_positions[2]

        p3frame = tk.Frame(master=self, bg=BGCOLOR, height=pl_height, width=pl_width)
        p3frame.place(relx=p3pos[0], rely=p3pos[1], relwidth=plREL_SIZE, relheight=plREL_SIZE, anchor=tk.CENTER)

        player3 = TkinterVideo(master=p3frame, bg=BGCOLOR, height=800, width=390)
        player3.load(VIDEO_PATH + self.SELECTED_VIDEOS[2])
        # player3.set_size((pl_width, pl_height))
        tk.Misc.lift(player3)
        player3.bind("<<Ended>>", lambda _: player3.play())
        player3.pack(expand=tk.YES, fill=tk.BOTH)

        # Player 4

        p4pos = self.rel_positions[3]

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
        self.window.after(500, self.pause_all)

        self.window.update()

        # Buttons

        play_all_btn = tk.Button(text="Play All", command=self.play_all)
        play_all_btn.place(relx=0.793, rely=0.545, relheight=0.05, relwidth=0.19)

        pause_all_btn = tk.Button(text="Pause All", command=self.pause_all)
        pause_all_btn.place(relx=0.793, rely=0.6, relheight=0.05, relwidth=0.19)

        self.pause_vars = [tk.BooleanVar() for _ in range(4)]

        pause_1_chkbtn = tk.Checkbutton(root, text="Pause 1", onvalue=True, offvalue=False, height=2, width=10,
                                        variable=self.pause_vars[0])
        pause_1_chkbtn.place(relx=0.793, rely=0.655, relwidth=0.045, relheight=0.05)

        pause_2_chkbtn = tk.Checkbutton(root, text="Pause 2", onvalue=True, offvalue=False, height=2, width=10,
                                        variable=self.pause_vars[1])
        pause_2_chkbtn.place(relx=0.8415, rely=0.655, relwidth=0.045, relheight=0.05)

        pause_3_chkbtn = tk.Checkbutton(root, text="Pause 3", onvalue=True, offvalue=False, height=2, width=10,
                                        variable=self.pause_vars[2])
        pause_3_chkbtn.place(relx=0.89, rely=0.655, relwidth=0.045, relheight=0.05)

        pause_4_chkbtn = tk.Checkbutton(root, text="Pause 4", onvalue=True, offvalue=False, height=2, width=10,
                                        variable=self.pause_vars[3])
        pause_4_chkbtn.place(relx=0.9385, rely=0.655, relwidth=0.044, relheight=0.05)

        pause_selective_btn = tk.Button(text="Pause Selected", command=self.pause_selective)
        pause_selective_btn.place(relx=0.793, rely=0.765, relwidth=0.19, relheight=0.05)

        play_selective_btn = tk.Button(text="Play Selected", command=self.play_selective)
        play_selective_btn.place(relx=0.793, rely=0.71, relwidth=0.19, relheight=0.05)

        self.tl_height = int(window_height * (plREL_SIZE + 0.001))
        self.tl_width = int(self.tl_height * .345)

        # Traffic Lights
        self.tl_img_pil = []
        for tl in self.tl_img_paths:
            io = Image.open(tl)
            # Width/Height ratio for Images = 0.345

            io = io.resize(size=(self.tl_width, self.tl_height))
            img = ImageTk.PhotoImage(io)

            self.tl_img_pil.append(img)

        self.tl_width /= window_width
        self.tl_height /= window_height

        self.tl_state_to_img = {idx: img for img, idx in zip(self.tl_img_pil, range(0, 5))}

        tl_positions = [(tlCOL1_x, plROW1_y), (tlCOL2_x, plROW1_y), (tlCOL1_x, plROW2_y), (tlCOL2_x, plROW2_y)]

        self.tl_img = []
        for pos in tl_positions:
            tl_img_lbl = tk.Label(self, image=self.tl_state_to_img[ALL], bg=BGCOLOR)
            tl_img_lbl.place(relx=pos[0], rely=pos[1], anchor=tk.CENTER, relheight=self.tl_height,
                             relwidth=self.tl_width)
            self.tl_img.append(tl_img_lbl)

        self.window.after(2000, self.green_for_n)

        # UI

        def create_player_ui(x, y, idx):
            line_bottom = tk.Canvas(self, height=2, bg="white", highlightthickness=0)
            line_bottom.place(relx=x + self.tl_width / 2, rely=y + plREL_SIZE / 2, anchor=tk.CENTER,
                              relwidth=plREL_SIZE + 0.058)
            line_top = tk.Canvas(self, height=2, bg="white", highlightthickness=0)
            line_top.place(relx=x + self.tl_width / 2, rely=y - plREL_SIZE / 2, anchor=tk.CENTER,
                           relwidth=plREL_SIZE + 0.058)
            line_left = tk.Canvas(self, width=2, bg="white", highlightthickness=0)
            line_left.place(relx=x - plREL_SIZE / 2, rely=y, anchor=tk.CENTER, relheight=plREL_SIZE)
            line_right = tk.Canvas(self, width=2, bg="white", highlightthickness=0)
            line_right.place(relx=x + plREL_SIZE / 2 + self.tl_width, rely=y, anchor=tk.CENTER, relheight=plREL_SIZE)
            line_mid = tk.Canvas(self, width=2, bg="white", highlightthickness=0)
            line_mid.place(relx=x + plREL_SIZE / 2 + 0.002, rely=y, anchor=tk.CENTER, relheight=plREL_SIZE)

            input_label = tk.Label(self, text=f"CCTV 00{idx + 1}", font=("LCDDot TR", 14, "bold"), bg="white",
                                   fg=BGCOLOR)
            input_label.place(relx=x - plREL_SIZE / 2, rely=y - plREL_SIZE / 2, anchor=tk.NW)

        for idx, pos in enumerate(self.rel_positions):
            create_player_ui(*pos, idx)

        # Traffic Light Counter

        self.counter_label = tk.Label(self, text="", font=("LCDDOT TR", 18, "bold"), bg=GREENon, fg="white",
                                      textvariable=self.green_timer)
        self.counter_label.place(relx=1.5, rely=1, anchor=tk.CENTER)

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

    def update_lights(self, tl_dict):
        for tl_num, state in tl_dict.items():
            self.tl_img[tl_num]["image"] = self.tl_state_to_img[state]

    def get_duration(self):
        durations = [player.current_duration() for player in self.players]
        return durations

    def get_allocated_time(self):

        allt_times = []

        for vid, dur in zip(self.SELECTED_VIDEOS, self.get_duration()):
            self.detector.set_vid(vid)
            count_vehicles = self.detector.get_count(dur, show=0)
            allt_time = self.tlmanager.get_alloted_time(count_vehicles)

            allt_times.append(allt_time)

        sel_tl, green_time_alloted = self.tlmanager.select_tl(allt_times)

        print(sel_tl, green_time_alloted)

        return sel_tl, green_time_alloted

    def green_for_n(self, sel_tl=None, green_time_allt=None):
        self.pause_all()
        self.update_lights({0: RED, 1: RED, 2: RED, 3: RED})
        if sel_tl is None and green_time_allt is None:
            sel_tl, green_time_allt = self.get_allocated_time()

        self.players[sel_tl].play()

        pos = self.rel_positions[sel_tl]
        self.pos_counter_label(*pos)

        self.green_counter(green_time_allt)
        self.update_lights({sel_tl: GREEN})

        def yellow_after_n():
            self.update_lights({sel_tl: YELLOW})
            self.players[sel_tl].pause()

            new_tl, new_allt = self.get_allocated_time()

            self.window.after((YELLOW_TIME - 2) * 1000, self.green_for_n, new_tl, new_allt)  # YELLOW TIME IN AFTER

        self.window.after(green_time_allt * 1000, yellow_after_n)  # GREEN TIME IN AFTER

    def green_counter(self, green_time=None):
        if green_time is not None:
            self.green_timer.set(green_time)
        if self.green_timer.get() > 0:
            self.green_timer.set(self.green_timer.get() - 1)
            self.window.after(1000, self.green_counter)
        else:
            self.pos_counter_label(10000, 0)
            self.counter_label["text"] = ""

    def pos_counter_label(self, x, y):
        self.counter_label.place(relx=x + plREL_SIZE / 2 + self.tl_width / 2 + 0.001, rely=y + self.tl_height / 3,
                                 anchor=tk.CENTER)


if __name__ == "__main__":
    window = tk.Tk()

    window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}")

    window["bg"] = BGCOLOR

    window.state("zoomed")
    window.resizable(width=False, height=False)
    window.title("Traffic Lights Management")

    dash = Dashboard(window)
    window.mainloop()
