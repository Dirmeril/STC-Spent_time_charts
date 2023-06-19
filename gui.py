import customtkinter as ctk
import charts


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('200x150')
        self.resizable(False, False)
        self.title('STC')
        self.frame = ctk.CTkFrame(self)
        self.frame.pack()

        # Create button
        self.circle = ctk.CTkButton(self.frame, text="Pie chart", command=charts.pie_chart, corner_radius=10)
        self.circle.grid(row=1, column=0, pady=20, padx=20)

        self.bar = ctk.CTkButton(self.frame, text="Bar chart", command=charts.bar_chart, corner_radius=10)
        self.bar.grid(row=2, column=0, pady=20, padx=20)
