import matplotlib.pyplot as plt
import pandas as pd
import __main__


# Chosen activities and dates transfer to stacked bar
def bar_chosen_dates_and_activities(activities, first_date, last_date):
    try:
        dates = list(__main__.activity_summary.keys())
        first = dates.index(first_date)
        last = dates.index(last_date)+1

        # Swap dates and activities to DataFrame
        chosen_activities = __main__.df_activity_summary.loc[[a for a in activities], [d for d in dates[first:last]]]
        list_of_activities = [a for a in activities]
        msg = ''
        return chosen_activities, list_of_activities, msg

    except ValueError as e:
        msg = 'Choose available date'
        return None, None, msg


# Stacked bar chart
def stacked_bar_chart(activities, first_date, last_date):
    try:
        df_data_time, data_activities, msg = bar_chosen_dates_and_activities(activities, first_date, last_date)
        if df_data_time is not None and data_activities is not None:
            df_data_time = df_data_time.T       # transposition

            # Calculation from datetime.delta time to seconds in int
            for a in data_activities:
                df_data_time[a] = df_data_time[a].dt.total_seconds()

            # plot data in stack manner of bar type
            df_data_time.plot(kind='bar', stacked=True, title='', figsize=(12, 4))
            plt.xticks(rotation=30)

            plt.subplots_adjust(left=0.2, bottom=0.2)
            plt.show()
            return msg
        else:
            return msg
    except AttributeError as e:
        msg = "The \"To date\" is\n earlier date than \"From date\""
        return msg

