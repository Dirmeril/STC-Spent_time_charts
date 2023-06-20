import customtkinter as ctk
import charts
import __main__


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('340x210')
        self.resizable(True, True)
        self.title('STC')
        self.frame = ctk.CTkFrame(self)
        self.frame.pack()

        # Create button
        self.circle = ctk.CTkButton(self.frame, text="Pie chart", command=charts.pie_chart, corner_radius=10)
        self.circle.grid(row=0, column=0, pady=20, padx=20)

        self.bar = ctk.CTkButton(self.frame, text="Bar chart", command=charts.bar_chart, corner_radius=10)
        self.bar.grid(row=1, column=0, pady=20, padx=20)

        # Create checkbox'y
        self.checkboxes = []
        self.counter: int = -1
        for activity in __main__.activity_summary.keys():
            self.counter += 1
            self.var = ctk.StringVar(value="on")
            self.checkboxes.append(self.var)
            self.checkbox = ctk.CTkCheckBox(self.frame, text=activity, variable=self.var, onvalue="on", offvalue="off", command=self.checkbox_event)
            self.checkbox.grid(row=self.counter, column=1, pady=20, padx=20)

    def checkbox_event(self):
        print("checkbox toggled, current value:", self.var.get())
