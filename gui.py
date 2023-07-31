from tkcalendar import Calendar
import customtkinter as ctk
import bar_chart
import pie_chart
import __main__
from tkinter import ttk
from datetime import datetime


# noinspection PyTypeChecker
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry()
        self.resizable(False, False)
        self.title('STC')
        # Create frame on top
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=2, side='top')
        # Create frame on left-down
        self.frame_3 = ctk.CTkFrame(self)
        self.frame_3.pack(side='left', fill='both')
        # Create frame on right-down
        self.frame_4 = ctk.CTkFrame(self)
        self.frame_4.pack(side='left', fill='both', expand=True)
        # macOS (correct display colors)
        self.style = ttk.Style(self.frame)
        self.style.theme_use('clam')

        self.sorted_activity = None
        self.first_date_to_button = None
        self.last_date_to_button = None
        self.text = None

        # Create inside first frame in 'frame on top' for buttons
        self.frame_buttons = ctk.CTkFrame(self.frame)
        self.frame_buttons.grid(row=0, column=0, pady=5, padx=20, sticky='nsew')

        # Create buttons pie and bar
        self.circle = ctk.CTkButton(self.frame_buttons, text="Pie chart", corner_radius=10,
                                    command=lambda: [self.checkbox_activities(), self.chosen_date(), self.pie_chart()])
        self.circle.pack(pady=20, padx=20, side='top')

        self.bar = ctk.CTkButton(self.frame_buttons, text="Bar chart", corner_radius=10,
                                 command=lambda: [self.checkbox_activities(), self.chosen_date(), self.bar_chart()])
        self.bar.pack(pady=20, padx=20, side='top')

        # Create Message Box
        self.label_message = ctk.CTkLabel(self.frame_buttons, text='The largest range\nselected by default')
        self.label_message.pack(side='top')

        # Create inside second frame in 'frame on top' for SliderBar
        self.frame_slider = ctk.CTkFrame(self.frame)
        self.frame_slider.grid(row=0, column=1, pady=5, sticky='nsew')

        # Create SliderBar
        self.slider = ctk.CTkSlider(self.frame_slider, from_=0, to=5, orientation='vertical', number_of_steps=5,
                                    command=self.slider_number)
        self.slider.pack(side='top', padx=15)
        self.slider.bind("<MouseWheel>", self.mouse_wheel)  # add function to MouseWheel

        # Default settings for label and SliderBar value
        self.slider.set(1)
        self.discard_number = 1

        # Create Label for SliderBar
        self.label_slider = ctk.CTkLabel(self.frame_slider, text=int(self.slider.get()))
        self.label_slider.pack(side='bottom')

        # Create labels for option_menu_dates/calendars
        self.label_from_option = ctk.CTkLabel(self.frame, text="From date:")
        self.label_from_option.grid(row=0, column=2, sticky='nw', padx=30, )

        self.label_to_option = ctk.CTkLabel(self.frame, text="To date:")
        self.label_to_option.grid(row=0, column=3, sticky='nw', padx=30)

        # Create calendar_start
        self.first_date = list(__main__.activity_summary.keys())[0]
        self.cal_start = Calendar(self.frame, background='DodgerBlue4', selectmode='day',
                                  borderwidth=2, year=int(self.first_date.split('-')[0]),
                                  month=int(self.first_date.split('-')[1]), day=int(self.first_date.split('-')[2]))
        # foreground='black' color for letters and numbers
        self.cal_start.grid(row=0, column=2, pady=22, padx=30, sticky='s')

        # Create calender_end
        self.last_date = list(__main__.activity_summary.keys())[-1]
        self.cal_end = Calendar(self.frame, background='DodgerBlue4', selectmode='day',
                                borderwidth=2, year=int(self.last_date.split('-')[0]),
                                month=int(self.last_date.split('-')[1]), day=int(self.last_date.split('-')[2]))
        self.cal_end.grid(row=0, column=3, pady=22, padx=30, sticky='s')

        # Mark available dates
        for date in list(__main__.activity_summary.keys()):
            self.cal_start.calevent_create(datetime.strptime(date, "%Y-%m-%d"), "Highlighted Date", "event")
            self.cal_end.calevent_create(datetime.strptime(date, "%Y-%m-%d"), "Highlighted Date", "event")
        self.cal_start.tag_config("event", background='forest green')
        self.cal_end.tag_config("event", background='forest green')

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
            if self.counter % 3 == 0:
                self.checkbox = ctk.CTkCheckBox(self.frame_3, text=self.sorted_activity,
                                                variable=self.activities_var[self.sorted_activity], onvalue=1,
                                                offvalue=0)
                self.checkbox.grid(row=self.counter, column=0, pady=5, padx=20, ipadx=15, sticky='ew')
            elif self.counter % 3 == 2:
                self.checkbox = ctk.CTkCheckBox(self.frame_3, text=self.sorted_activity,
                                                variable=self.activities_var[self.sorted_activity], onvalue=1,
                                                offvalue=0)
                self.checkbox.grid(row=self.counter - 2, column=2, pady=5, padx=5, ipadx=15, sticky='ew')
            else:
                self.checkbox = ctk.CTkCheckBox(self.frame_3, text=self.sorted_activity,
                                                variable=self.activities_var[self.sorted_activity], onvalue=1,
                                                offvalue=0)
                self.checkbox.grid(row=self.counter - 1, column=1, pady=5, padx=5, ipadx=15, sticky='ew')

        # Create text-pool for error in load data
        self.textbox = ctk.CTkTextbox(self.frame_4, corner_radius=0)
        self.textbox.pack(padx=1, fill='both', expand=True)
        self.textbox.insert('insert', "Lines which haven't been load in data:\n")
        for _ in __main__.error_list:
            self.textbox.insert("insert", str(_))
        # self.textbox.insert("insert", [str(_) for _ in __main__.error_list])

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
        self.text = pie_chart.pie_chart(self.to_chart, self.first_date_to_button, self.last_date_to_button,
                                        self.discard_number)
        self.label_message.configure(text=self.text)

    def bar_chart(self):
        self.text = bar_chart.stacked_bar_chart(self.to_chart, self.first_date_to_button, self.last_date_to_button,
                                                self.discard_number)
        self.label_message.configure(text=self.text)

    def slider_number(self, value):
        self.discard_number = int(value)
        self.label_slider.configure(text=int(value))

    def mouse_wheel(self, event):
        # Mouse wheel scrolling support
        delta = -1 if event.delta < 0 else 1
        new_value = self.slider.get() + delta

        # Limiting the value of the slider to the range of 0-100
        new_value = int(max(0, min(5, new_value)))

        # Set a new slider value
        self.slider.set(new_value)
        self.slider_number(new_value)
