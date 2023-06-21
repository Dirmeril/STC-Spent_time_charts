import customtkinter as ctk
import charts
import __main__


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry()
        self.resizable(False, False)
        self.title('STC')
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(side='top', pady=2, fill='x')
        self.frame_d = ctk.CTkFrame(self)
        self.frame_d.pack(side='top', pady=2, fill='x')

        # Create chart buttons
        self.circle = ctk.CTkButton(self.frame, text="Pie chart", command=self.checkbox_activities, corner_radius=10)
        self.circle.grid(row=0, column=0, pady=20, padx=20)

        self.bar = ctk.CTkButton(self.frame, text="Bar chart", command=charts.bar_chart and self.checkbox_event, corner_radius=10)
        self.bar.grid(row=0, column=1, pady=20, padx=20)

        # Create option bars
        self.from_option = ctk.CTkOptionMenu(self.frame, values=[a for a in __main__.activity_summary.keys()], command=None)
        self.from_option.grid(row=0, column=2, pady=20, padx=20)

        self.to_option = ctk.CTkOptionMenu(self.frame, values=[a for a in __main__.activity_summary.keys()], command=None)
        self.to_option.grid(row=0, column=3, pady=20, padx=20)

        # Create checkboxes for activities
        self.list_of_activities = []
        self.counter: int = -1
        for date in __main__.activity_summary.keys():
            for activity in __main__.activity_summary[date].keys():
                self.list_of_activities.append(activity)
        self.sorted_activities = sorted(set(self.list_of_activities))
        self.activities_var = {activity_var: ctk.IntVar(value=1) for activity_var in self.sorted_activities}
        for self.sorted_activity in self.sorted_activities:
            self.counter += 1
            # Split activities on two columns
            if self.counter % 2 == 0:
                self.checkbox = ctk.CTkCheckBox(self.frame_d, text=self.sorted_activity, variable=self.activities_var[self.sorted_activity], onvalue=1, offvalue=0)
                self.checkbox.grid(row=self.counter, column=0, pady=5, padx=20, ipadx=15, sticky='ew')
            else:
                self.checkbox = ctk.CTkCheckBox(self.frame_d, text=self.sorted_activity, variable=self.activities_var[self.sorted_activity], onvalue=1, offvalue=0)
                self.checkbox.grid(row=self.counter-1, column=1, pady=5, padx=5, ipadx=15, sticky='ew')

    def checkbox_event(self):
        for box in self.checkboxes:
            text = box.get()
            print("checkbox toggled, current value:", box, text)
        for activity in __main__.activity_summary.keys():
            print(activity)

    def checkbox_activities(self):
        to_chart = []
        for key, value in self.activities_var.items():
            if value.get() == 1:
                to_chart.append(key)
        print(to_chart)
