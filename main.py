import gui
# import customtkinter as ctk
import sum_time


if __name__ == '__main__':
    my_labels, numbers, add = sum_time.sum_time()
    app = gui.App()
    app.mainloop()
