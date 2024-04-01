import tkinter as tk
from tkVideoPlayer import TkinterVideo
import tkvideo.tkvideo as tkv

BGCOLOR = "#2A2A2A"


class Dashboard(tk.Frame):
    def __init__(self, window):
        super().__init__()
        self.window = window

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

        row1_y = .26
        row2_y = .74


        rel_positions = [(col1_x, row1_y), (col1_x, row2_y), (col2_x, row1_y), (col2_x, row2_y)]
        
        # Player 1

        p1pos = rel_positions[0]

        p1frame = tk.Frame(master=self, bg=BGCOLOR, height=pl_height, width=pl_width)
        p1frame.place(relx=p1pos[0], rely=p1pos[1],
                      relwidth=rel_size, relheight=rel_size, anchor=tk.CENTER)

        player1 = TkinterVideo(master=p1frame, bg=BGCOLOR, height=800, width=390)
        player1.load(r"Assets/Videos/rush.mp4")
        player1.set_size((pl_width, pl_height))
        player1.play()
        player1.pack(expand=tk.YES, fill=tk.BOTH)

        # Player 2

        p2pos = rel_positions[1]

        p2frame = tk.Frame(master=self, bg=BGCOLOR, height=pl_height, width=pl_width)
        p2frame.place(relx=p2pos[0], rely=p2pos[1],
                      relwidth=rel_size, relheight=rel_size, anchor=tk.CENTER)

        player2 = TkinterVideo(master=p2frame, bg=BGCOLOR, height=800, width=390)
        player2.load(r"Assets/Videos/rush.mp4")
        player2.set_size((pl_width, pl_height))
        player2.play()
        player2.pack(expand=tk.YES, fill=tk.BOTH)

        # Player 3

        p3pos = rel_positions[2]

        p3frame = tk.Frame(master=self, bg=BGCOLOR, height=pl_height, width=pl_width)
        p3frame.place(relx=p3pos[0], rely=p3pos[1],
                      relwidth=rel_size, relheight=rel_size, anchor=tk.CENTER)

        player3 = TkinterVideo(master=p3frame, bg=BGCOLOR, height=800, width=390)
        player3.load(r"Assets/Videos/rush.mp4")
        player3.set_size((pl_width, pl_height))
        player3.play()
        player3.pack(expand=tk.YES, fill=tk.BOTH)

        # Player 4

        p4pos = rel_positions[3]

        p4frame = tk.Frame(master=self, bg=BGCOLOR, height=pl_height, width=pl_width)
        p4frame.place(relx=p4pos[0], rely=p4pos[1],
                      relwidth=rel_size, relheight=rel_size, anchor=tk.CENTER)

        player4 = TkinterVideo(master=p4frame, bg=BGCOLOR, height=800, width=390)
        player4.load(r"Assets/Videos/rush.mp4")
        player4.set_size((pl_width, pl_height))
        player4.play()
        player4.pack(expand=tk.YES, fill=tk.BOTH)


        # def p2stop():
        #     player2.pause()
        #     def p2play():
        #         player2.play()
        #         return
        #
        #     window.after(5000, p2play)
        #
        # window.after(5000, p2stop)

        self.window.update()


if __name__ == "__main__":
    window = tk.Tk()
    dash = Dashboard(window)
    window.mainloop()
