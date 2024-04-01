import os
import tkinter as tk
from tkVideoPlayer import TkinterVideo

BGCOLOR = "#2A2A2A"

VIDEO_PATH = "Assets/Videos/"
VIDEOS = os.listdir(VIDEO_PATH)
VIDEOS = [VIDEO_PATH + vid for vid in VIDEOS]


class Dashboard(tk.Frame):
    def __init__(self, root):
        super().__init__()
        self.window = root

        window_height = self.window.winfo_screenheight()
        window_width = self.window.winfo_screenwidth()
        self.config(height=window_height, width=window_width, bg=BGCOLOR)
        self.pack()

        self.window.geometry(f"{window_width}x{window_height}")

        self.window["bg"] = BGCOLOR

        self.window.state("zoomed")
        self.window.resizable(0, 0)
        self.window.title("Traffic Light Management")

        # Video

        pl_width, pl_height = 700, 390
        rel_size = .35

        col1_x = .21
        col2_x = .60

        row1_y = .27
        row2_y = .73


        rel_positions = [(col1_x, row1_y), (col1_x, row2_y), (col2_x, row1_y), (col2_x, row2_y)]
        
        # Player 1

        p1pos = rel_positions[0]

        p1frame = tk.Frame(master=self, bg=BGCOLOR, height=pl_height, width=pl_width)
        p1frame.place(relx=p1pos[0], rely=p1pos[1],
                      relwidth=rel_size, relheight=rel_size, anchor=tk.CENTER)

        player1 = TkinterVideo(master=p1frame, bg=BGCOLOR, height=800, width=390)
        player1.load(VIDEOS[0])
        player1.set_size((pl_width, pl_height))
        player1.play()

        def loop1(e):
            player1.play()

        player1.bind("<<Ended>>", loop1)
        player1.pack(expand=tk.YES, fill=tk.BOTH)

        # Player 2

        p2pos = rel_positions[1]

        p2frame = tk.Frame(master=self, bg=BGCOLOR, height=pl_height, width=pl_width)
        p2frame.place(relx=p2pos[0], rely=p2pos[1],
                      relwidth=rel_size, relheight=rel_size, anchor=tk.CENTER)

        player2 = TkinterVideo(master=p2frame, bg=BGCOLOR, height=800, width=390)
        player2.load(VIDEOS[1])
        player2.set_size((pl_width, pl_height))
        player2.play()
        player2.pack(expand=tk.YES, fill=tk.BOTH)

        # Player 3

        p3pos = rel_positions[2]

        p3frame = tk.Frame(master=self, bg=BGCOLOR, height=pl_height, width=pl_width)
        p3frame.place(relx=p3pos[0], rely=p3pos[1],
                      relwidth=rel_size, relheight=rel_size, anchor=tk.CENTER)

        player3 = TkinterVideo(master=p3frame, bg=BGCOLOR, height=800, width=390)
        player3.load(VIDEOS[3])
        player3.set_size((pl_width, pl_height))
        player3.play()
        player3.pack(expand=tk.YES, fill=tk.BOTH)

        # Player 4

        p4pos = rel_positions[3]

        p4frame = tk.Frame(master=self, bg=BGCOLOR, height=pl_height, width=pl_width)
        p4frame.place(relx=p4pos[0], rely=p4pos[1],
                      relwidth=rel_size, relheight=rel_size, anchor=tk.CENTER)

        player4 = TkinterVideo(master=p4frame, bg=BGCOLOR, height=800, width=390)
        player4.load(VIDEOS[2])
        player4.set_size((pl_width, pl_height))
        player4.play()
        player4.pack(expand=tk.YES, fill=tk.BOTH)

        self.window.update()

        players = [player1, player2, player3, player4]

        # Buttons

        def play_all():
            for element in players:
                element.play()

        play_all_btn = tk.Button(text="Play All", command=play_all)
        play_all_btn.place(x=1222, y=80, relheight=0.05, relwidth=0.19)

        def pause_all():
            for element in players:
                element.pause()

        pause_all_btn = tk.Button(text="Pause All", command=pause_all)
        pause_all_btn.place(x=1222, y=152, relheight=0.05, relwidth=0.19)

        self.window.after(200, pause_all)


if __name__ == "__main__":
    window = tk.Tk()
    dash = Dashboard(window)
    window.mainloop()
