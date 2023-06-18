import gui
import customtkinter as ctk
import load_data
import sum_time


if __name__ == '__main__':
    activity: dict = load_data.load()
    my_labels, numbers, add = sum_time.sum()
    app = gui.App()
    app.mainloop()
