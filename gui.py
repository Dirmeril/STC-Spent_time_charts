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
        self.frame.pack(side='top', pady=2,)
        # self.frame_r = ctk.CTkFrame(self)
        # self.frame_r.pack(side='top', pady=2,)
        self.frame_d = ctk.CTkFrame(self)
        self.frame_d.pack(side='bottom', pady=2, fill='x')


        # Create chart buttons: pie and bar
        self.circle = ctk.CTkButton(self.frame, text="Pie chart", corner_radius=10,
                                    command=lambda: [self.checkbox_activities(), charts.pie_chart(self.to_chart, self.first_date, self.last_date)])
        self.circle.grid(row=0, column=0, pady=20, padx=20)

        self.bar = ctk.CTkButton(self.frame, text="Bar chart", corner_radius=10,
                                 command=lambda: [self.checkbox_activities(), charts.stacked_bar_chart(self.to_chart, self.first_date, self.last_date)])
        self.bar.grid(row=0, column=1, pady=20, padx=20)

        # Create option bars with dates
        self.first_date = list(__main__.activity_summary.keys())[0]
        self.last_date = list(__main__.activity_summary.keys())[-1]
        self.from_option_var = ctk.StringVar(value=self.first_date)  # set initial value
        self.from_option = ctk.CTkOptionMenu(self.frame, values=[a for a in __main__.activity_summary.keys()],
                                             command=self.chosen_first_date, variable=self.from_option_var)
        self.from_option.grid(row=0, column=2, pady=30, padx=30, sticky='s')
        self.from_option.set(self.first_date)

        self.to_option_var = ctk.StringVar(value=self.last_date)  # set initial value
        self.to_option = ctk.CTkOptionMenu(self.frame, values=[a for a in __main__.activity_summary.keys()],
                                           command=self.chosen_last_date, variable=self.to_option_var)
        self.to_option.grid(row=0, column=3, pady=30, padx=30, sticky='s')
        self.to_option.set(self.last_date)

        # Create labels for option_menu_dates
        self.label_from_option = ctk.CTkLabel(self.frame, text="From date:")
        self.label_from_option.grid(row=0, column=2, sticky='nw', padx=30)

        self.label_to_option = ctk.CTkLabel(self.frame, text="To date:")
        self.label_to_option.grid(row=0, column=3, sticky='nw', padx=30)

        # Create checkboxes for activities
        self.to_chart = []      # To function: checkbox_activities
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
                self.checkbox = ctk.CTkCheckBox(self.frame_d, text=self.sorted_activity,
                                                variable=self.activities_var[self.sorted_activity], onvalue=1,
                                                offvalue=0)
                self.checkbox.grid(row=self.counter, column=0, pady=5, padx=20, ipadx=15, sticky='ew')
            else:
                self.checkbox = ctk.CTkCheckBox(self.frame_d, text=self.sorted_activity,
                                                variable=self.activities_var[self.sorted_activity], onvalue=1,
                                                offvalue=0)
                self.checkbox.grid(row=self.counter - 1, column=1, pady=5, padx=5, ipadx=15, sticky='ew')

    # Function to choose activities
    def checkbox_activities(self):
        self.to_chart = []
        for key, value in self.activities_var.items():
            if value.get() == 1:
                self.to_chart.append(key)

    # Function to choose range dates
    def chosen_first_date(self, choice):
        self.first_date = choice

    def chosen_last_date(self, choice):
        self.last_date = choice

