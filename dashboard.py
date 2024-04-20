import os
import random
import tkinter as tk
from tkVideoPlayer import TkinterVideo
from PIL import ImageTk, Image, ImageOps

import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

import database
import detection
import TLmanager

import warnings

warnings.filterwarnings("ignore")

SEC_UNIT = 100

BGCOLOR = "#" + "10" * 3

VIDEO_PATH = "Assets/Videos/"
TL_IMG_PATH = "Assets/Images/TrafficLights/"

YELLOW_TIME = 5  # secs

# Dimensions and Positions for Video Players and Traffic Lights

# Vid Players

plREL_SIZE = .30

plCOL1_x = .16
plCOL2_x = .54

plROW1_y = .31
plROW2_y = .69

# TL Pos and Info

tlCOL1_x = .34
tlCOL2_x = .72

RED, YELLOW, GREEN, ALL, NONE = 1, 2, 3, 4, 0

REDon = "#f1592a"
GREENon = "#37b44c"
YELLOWon = "#fff44d"


class Dashboard(tk.Frame):
    def __init__(self, root):

        self.tlmanager = TLmanager.TLmanager()
        self.detector = detection.Detector()
        self.db = database.Database()

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

        self.tl_height_abs = int(window_height * (plREL_SIZE + 0.001))
        self.tl_width_abs = int(self.tl_height_abs * .345)

        # Graphs

        self.graph_1_2 = tk.Label(bg=BGCOLOR)
        self.graph_1_2.place(relx=0.88, rely=plROW1_y, anchor=tk.CENTER,
                             relwidth=self.tl_height_abs / window_width * 1.37,
                             relheight=self.tl_height_abs / window_height + .002)

        self.graph_3_4 = tk.Label(bg=BGCOLOR)
        self.graph_3_4.place(relx=0.88, rely=plROW2_y, anchor=tk.CENTER,
                             relwidth=self.tl_height_abs / window_width * 1.37,
                             relheight=self.tl_height_abs / window_height + .002)

        # Traffic Lights

        self.tl_img_pil = []
        for tl in self.tl_img_paths:
            io = Image.open(tl)
            # Width/Height ratio for Images = 0.345

            io = io.resize(size=(self.tl_width_abs, self.tl_height_abs))
            img = ImageTk.PhotoImage(io)

            self.tl_img_pil.append(img)

        self.tl_width = self.tl_width_abs / window_width
        self.tl_height = self.tl_height_abs / window_height

        self.tl_state_to_img = {idx: img for img, idx in zip(self.tl_img_pil, range(0, 5))}

        tl_positions = [(tlCOL1_x, plROW1_y), (tlCOL2_x, plROW1_y), (tlCOL1_x, plROW2_y), (tlCOL2_x, plROW2_y)]

        self.tl_img = []
        for pos in tl_positions:
            tl_img_lbl = tk.Label(self, image=self.tl_state_to_img[ALL], bg=BGCOLOR)
            tl_img_lbl.place(relx=pos[0], rely=pos[1], anchor=tk.CENTER, relheight=self.tl_height,
                             relwidth=self.tl_width)
            self.tl_img.append(tl_img_lbl)

        self.allt_times = []  # Store Allotment Times
        self.count_label_list = []  # Store Labels displaying Count
        self.alloted_label_list = []  # Store Labels displaying Alloted Time

        self.window.after(1000, self.green_for_n)

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

            count_label = tk.Label(self, text=f"Vehicle Count: Calculating", font=("Ariel", 11, "normal"), bg=BGCOLOR,
                                   fg="white")
            count_label.place(relx=x - plREL_SIZE / 2 - 0.001, rely=y + plREL_SIZE / 2 + 0.017, anchor=tk.W)
            self.count_label_list.append(count_label)

            alloted_label = tk.Label(self, text=f"Alloted Time: Calculating", font=("Ariel", 11, "normal"), bg=BGCOLOR,
                                     fg="white")
            alloted_label.place(relx=x - plREL_SIZE / 2 - 0.001, rely=y + plREL_SIZE / 2 + 0.045,
                                anchor=tk.W)
            self.alloted_label_list.append(alloted_label)

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

    def update_lights(self, tl_dict):
        for tl_num, state in tl_dict.items():
            self.tl_img[tl_num]["image"] = self.tl_state_to_img[state]

    def get_duration(self):
        durations = [player.current_duration() for player in self.players]
        return durations

    def get_allocated_time(self):
        count_vehicles_list = []
        self.allt_times = []  # Clear Prev Alloted Times

        for vid, dur in zip(self.SELECTED_VIDEOS, self.get_duration()):
            self.detector.set_vid(vid)
            count_vehicles = self.detector.get_count(dur, show=0)
            count_vehicles_list.append(count_vehicles)

            allt_time = self.tlmanager.get_alloted_time(count_vehicles)
            self.allt_times.append(allt_time)

        sel_tl, green_time_alloted = self.tlmanager.select_tl(self.allt_times)

        self.graph_update()
        self.db.insert_current_cycle_info(self.allt_times)
        self.vehicle_count_display(count_vehicles_list)
        self.allotted_time_display(self.allt_times)

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

        self.window.after(green_time_allt * SEC_UNIT, yellow_after_n)  # GREEN TIME IN AFTER

    def green_counter(self, green_time=None):
        if green_time is not None:
            self.green_timer.set(green_time)
        if self.green_timer.get() > 0:
            self.green_timer.set(self.green_timer.get() - 1)
            self.window.after(SEC_UNIT, self.green_counter)
        else:
            self.pos_counter_label(10000, 0)
            self.counter_label["text"] = ""

    def pos_counter_label(self, x, y):
        self.counter_label.place(relx=x + plREL_SIZE / 2 + self.tl_width / 2 + 0.001, rely=y + self.tl_height / 3,
                                 anchor=tk.CENTER)

    def vehicle_count_display(self, count_vehicles_list):
        for count, label in zip(count_vehicles_list, self.count_label_list):
            count_vehicles_list_formatted = [
                f"{cls_count} {cls_name.title()}(es)" if cls_name[-1] == "s" else f"{cls_count} {cls_name.title()}(s)"
                for cls_name, cls_count in count.items() if cls_count > 0]

            count_str = "Vehicle Count: " + (", ".join(count_vehicles_list_formatted) or "Lane Empty")

            label["text"] = count_str

    def allotted_time_display(self, alloted_time_list):
        for time, label in zip(alloted_time_list, self.alloted_label_list):
            time_str = f"Allotted Time: {time} secs"
            label["text"] = time_str

    def graph_update(self):
        import numpy as np

        plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
        sns.set(style="darkgrid")

        sns.set(rc={'axes.facecolor': '#f3f3f3', 'figure.facecolor': '#f3f3f3'})
        graph_1_2, graph_3_4 = self.db.current_instance_info()

        g_1_2 = sns.lineplot(graph_1_2, x="cycle_num", y="time_alloted", hue="lane_num", linewidth=3,
                             palette=["#ff595e", "#6a4c93"])

        handle, lables = g_1_2.get_legend_handles_labels()
        g_1_2.legend(handle[:2], ["Lane 1", "Lane 2"])
        g_1_2.set(xlabel=None, ylabel=None)

        plt.savefig("Assets/Graphs/graph_1_2.jpg")

        img = Image.open("Assets/Graphs/graph_1_2.jpg").resize(
            (int(self.tl_height_abs * 1.6), int(self.tl_height_abs * 1.05)))

        img = ImageOps.invert(img)
        img = ImageTk.PhotoImage(img)

        self.graph_1_2["image"] = img
        self.graph_1_2.image = img

        plt.cla()

        plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
        sns.set(style="darkgrid")

        g_3_4 = sns.lineplot(graph_3_4, x="cycle_num", y="time_alloted", linewidth=3,
                             palette=["#104b51", "#03989e"], hue="lane_num")

        handle, lables = g_3_4.get_legend_handles_labels()
        g_3_4.legend(handle[:2], ["Lane 3", "Lane 4"])
        g_3_4.set(xlabel=None, ylabel=None)

        plt.savefig("Assets/Graphs/graph_3_4.jpg")

        img = Image.open("Assets/Graphs/graph_3_4.jpg").resize(
            (int(self.tl_height_abs * 1.6), int(self.tl_height_abs * 1.05)))
        img = ImageOps.invert(img)
        img = ImageTk.PhotoImage(img)

        self.graph_3_4["image"] = img
        self.graph_3_4.image = img

        plt.cla()


if __name__ == "__main__":
    window = tk.Tk()

    window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}")

    window["bg"] = BGCOLOR

    window.state("zoomed")
    window.resizable(width=False, height=False)
    window.title("Traffic Lights Management")

    dash = Dashboard(window)

    window.mainloop()
