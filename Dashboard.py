import tkinter as tk

class Dashboard(tk.Frame):
    def __init__(self, window):
        self.window = window

        window_height = self.window.winfo_screenheight()
        window_width = self.window.winfo_screenwidth()

        self.window.geometry(f"{window_width}x{window_height}")

        self.window.state("zoomed")
        self.window.resizable(0, 0)
        self.window.title("Traffic Light Management")


        # Background

        self.bg_panel = tk.Canvas(self.window, bg="#2A2A2A",
                                  height=window_height, width=window_width)

        self.bg_panel.pack()




if __name__ == "__main__":
    window = tk.Tk()
    dash = Dashboard(window)
    window.mainloop()


