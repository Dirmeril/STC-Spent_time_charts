from tkcalendar import Calendar, DateEntry
import customtkinter as ctk
import bar_chart
import pie_chart
import __main__

from datetime import datetime


# noinspection PyTypeChecker
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry()
        self.resizable(False, False)
        self.title('STC')
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=2)
        self.frame_d = ctk.CTkFrame(self)
        self.frame_d.pack(side='left', fill='x', expand=True)
        self.frame_another = ctk.CTkFrame(self)
        self.frame_another.pack(side='left', fill='both', expand=True)

        # Create frame for chart buttons pie and bar and that buttons
        self.frame_buttons = ctk.CTkFrame(self.frame)
        self.frame_buttons.grid(row=0, column=0, pady=5, padx=20, sticky='nsew')
        self.circle = ctk.CTkButton(self.frame_buttons, text="Pie chart", corner_radius=10,
                                    command=lambda: [self.checkbox_activities(), self.chosen_date(), self.pie_chart()])
        self.circle.pack(pady=20, padx=20, side='top')

        self.bar = ctk.CTkButton(self.frame_buttons, text="Bar chart", corner_radius=10,
                                 command=lambda: [self.checkbox_activities(), self.chosen_date(), self.bar_chart()])
        self.bar.pack(pady=20, padx=20, side='top')

        self.label_message = ctk.CTkLabel(self.frame_buttons, text='datyyy')
        self.label_message.pack(side='top')

        # Create labels for option_menu_dates/calendars
        self.label_from_option = ctk.CTkLabel(self.frame, text="From date:")
        self.label_from_option.grid(row=0, column=2, sticky='nw', padx=30, )

        self.label_to_option = ctk.CTkLabel(self.frame, text="To date:")
        self.label_to_option.grid(row=0, column=3, sticky='nw', padx=30)

        # Create calendar_start
        self.first_date = list(__main__.activity_summary.keys())[0]
        self.cal_start = Calendar(self.frame, background='#0C60B0', selectmode='day',
                                  foreground='white', borderwidth=2, year=int(self.first_date.split('-')[0]),
                                  month=int(self.first_date.split('-')[1]), day=int(self.first_date.split('-')[2]))
        self.cal_start.grid(row=0, column=2, pady=22, padx=30, sticky='s')

        # Create calender_end
        self.last_date = list(__main__.activity_summary.keys())[-1]
        self.cal_end = Calendar(self.frame, background='#0C60B0', selectmode='day',
                                foreground='white', borderwidth=2, year=int(self.last_date.split('-')[0]),
                                month=int(self.last_date.split('-')[1]), day=int(self.last_date.split('-')[2]))
        self.cal_end.grid(row=0, column=3, pady=22, padx=30, sticky='s')

        # Mark available dates
        for date in list(__main__.activity_summary.keys()):
            self.cal_start.calevent_create(datetime.strptime(date, "%Y-%m-%d"), "Highlighted Date", "event")
            self.cal_end.calevent_create(datetime.strptime(date, "%Y-%m-%d"), "Highlighted Date", "event")
        self.cal_start.tag_config("event", background='#46B04B')
        self.cal_end.tag_config("event", background='#46B04B')

        # Create checkbox_activities
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
    def chosen_date(self):
        self.first_date_to_button = str(self.cal_start.selection_get())
        self.last_date_to_button = str(self.cal_end.selection_get())

    def pie_chart(self):
        self.text = pie_chart.pie_chart(self.to_chart, self.first_date_to_button, self.last_date_to_button)
        self.label_message.configure(text=self.text)

    def bar_chart(self):
        self.text = bar_chart.stacked_bar_chart(self.to_chart, self.first_date_to_button, self.last_date_to_button)
        self.label_message.configure(text=self.text)

