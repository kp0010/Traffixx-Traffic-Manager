import os
import tkinter as tk
from tkVideoPlayer import TkinterVideo

BGCOLOR = "#" + "10" * 3

VIDEO_PATH = "Assets/Videos/"

# Dimensions and Positions for Video Players

REL_SIZE = .35

COL1_x = .21
COL2_x = .60

ROW1_y = .27
ROW2_y = .73


class Dashboard(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root)
        self.window = root

        window_height = self.window.winfo_screenheight()
        window_width = self.window.winfo_screenwidth()
        self.config(height=window_height, width=window_width, bg=BGCOLOR)
        self.pack(expand=True, fill=tk.BOTH)

        # Video

        VIDEOS = os.listdir(VIDEO_PATH)
        VIDEOS = [VIDEO_PATH + vid for vid in VIDEOS]


        pl_width, pl_height = 700, 390


        rel_positions = [(COL1_x, ROW1_y), (COL2_x, ROW1_y), (COL1_x, ROW2_y), (COL2_x, ROW2_y)]

        # Player 1

        p1pos = rel_positions[0]

        p1frame = tk.Frame(master=self, bg=BGCOLOR, height=pl_height, width=pl_width)
        p1frame.place(relx=p1pos[0], rely=p1pos[1], relwidth=REL_SIZE, relheight=REL_SIZE, anchor=tk.CENTER)

        player1 = TkinterVideo(master=p1frame, bg=BGCOLOR, height=800, width=390)
        player1.load(VIDEOS[0])
        player1.set_size((pl_width, pl_height))
        tk.Misc.lift(player1)
        player1.play()

        def loop1(_):
            player1.play()

        player1.bind("<<Ended>>", loop1)
        player1.pack(expand=tk.YES, fill=tk.BOTH)

        # Player 2

        p2pos = rel_positions[1]

        p2frame = tk.Frame(master=self, bg=BGCOLOR, height=pl_height, width=pl_width)
        p2frame.place(relx=p2pos[0], rely=p2pos[1], relwidth=REL_SIZE, relheight=REL_SIZE, anchor=tk.CENTER)

        player2 = TkinterVideo(master=p2frame, bg=BGCOLOR, height=800, width=390)
        player2.load(VIDEOS[1])
        player2.set_size((pl_width, pl_height))
        tk.Misc.lift(player2)
        player2.play()
        player2.pack(expand=tk.YES, fill=tk.BOTH)

        # Player 3

        p3pos = rel_positions[2]

        p3frame = tk.Frame(master=self, bg=BGCOLOR, height=pl_height, width=pl_width)
        p3frame.place(relx=p3pos[0], rely=p3pos[1], relwidth=REL_SIZE, relheight=REL_SIZE, anchor=tk.CENTER)

        player3 = TkinterVideo(master=p3frame, bg=BGCOLOR, height=800, width=390)
        player3.load(VIDEOS[3])
        player3.set_size((pl_width, pl_height))
        tk.Misc.lift(player3)
        player3.play()
        player3.pack(expand=tk.YES, fill=tk.BOTH)

        # Player 4

        p4pos = rel_positions[3]

        p4frame = tk.Frame(master=self, bg=BGCOLOR, height=pl_height, width=pl_width)
        p4frame.place(relx=p4pos[0], rely=p4pos[1], relwidth=REL_SIZE, relheight=REL_SIZE, anchor=tk.CENTER)

        player4 = TkinterVideo(master=p4frame, bg=BGCOLOR, height=800, width=390)
        player4.load(VIDEOS[2])
        player4.set_size((pl_width, pl_height))
        tk.Misc.lift(player4)
        player4.play()
        player4.pack(expand=tk.YES, fill=tk.BOTH)

        self.window.update()

        players = [player1, player2, player3, player4]
        # Buttons

        def play_all():
            for element in players:
                element.play()

        play_all_btn = tk.Button(text="Play All", command=play_all)
        play_all_btn.place(relx=0.793, rely=0.095, relheight=0.05, relwidth=0.19)

        def pause_all():
            for element in players:
                element.pause()

        pause_all_btn = tk.Button(text="Pause All", command=pause_all)
        pause_all_btn.place(relx=0.793, rely=0.15, relheight=0.05, relwidth=0.19)

        play_all()

        pause_vars = [tk.BooleanVar() for _ in range(4)]

        pause_1_chkbtn = tk.Checkbutton(root, text="Pause 1", onvalue=True, offvalue=False, height=2, width=10,
                                        variable=pause_vars[0])
        pause_1_chkbtn.place(relx=0.793, rely=0.205, relwidth=0.045, relheight=0.05)

        pause_2_chkbtn = tk.Checkbutton(root, text="Pause 2", onvalue=True, offvalue=False, height=2, width=10,
                                        variable=pause_vars[1])
        pause_2_chkbtn.place(relx=0.8415, rely=0.205, relwidth=0.045, relheight=0.05)

        pause_3_chkbtn = tk.Checkbutton(root, text="Pause 3", onvalue=True, offvalue=False, height=2, width=10,
                                        variable=pause_vars[2])
        pause_3_chkbtn.place(relx=0.89, rely=0.205, relwidth=0.045, relheight=0.05)

        pause_4_chkbtn = tk.Checkbutton(root, text="Pause 4", onvalue=True, offvalue=False, height=2, width=10,
                                        variable=pause_vars[3])
        pause_4_chkbtn.place(relx=0.9385, rely=0.205, relwidth=0.044, relheight=0.05)


        def pause_selective():
            for var, player in zip(pause_vars, players):
                if var.get():
                    player.pause()


        pause_selective_btn = tk.Button(text="Pause Selected", command=pause_selective)
        pause_selective_btn.place(relx=0.793, rely=0.315, relwidth=0.19, relheight=0.05)

        def play_selective():
            for var, player in zip(pause_vars, players):
                if var.get():
                    player.play()

        play_selective_btn = tk.Button(text="Play Selected", command=play_selective)
        play_selective_btn.place(relx=0.793, rely=0.26, relwidth=0.19, relheight=0.05)


if __name__ == "__main__":
    window = tk.Tk()

    window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}")

    window["bg"] = BGCOLOR

    window.state("zoomed")
    window.resizable(width=False, height=False)
    window.title("Traffic Light Management")

    dash = Dashboard(window)
    window.mainloop()
