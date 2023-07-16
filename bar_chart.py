import matplotlib.pyplot as plt
import __main__
import datetime
import mplcursors


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

    except ValueError:
        msg = 'Choose available date'
        return None, None, msg


# Stacked bar chart
def stacked_bar_chart(activities, first_date, last_date):
    try:
        df_data_time, data_activities, msg = bar_chosen_dates_and_activities(activities, first_date, last_date)
        if df_data_time is not None and data_activities is not None:
            df_data_time = df_data_time.T       # transposition

            # Change date format from YYYY-MM-DD to weekday
            days_list = []
            for _ in list(df_data_time.index):
                day = datetime.datetime.strptime(_, "%Y-%m-%d").strftime('%A')
                days_list.append(day)
            df_data_time['days'] = days_list
            df_data_time.set_index('days', inplace=True)

            # Calculation from datetime.delta time to seconds in int
            for a in data_activities:
                df_data_time[a] = df_data_time[a].dt.total_seconds()/3600

            # plot data in stack manner of bar type
            df_data_time.plot(kind='bar', stacked=True, title='')
            plt.xticks(rotation=30)
            plt.ylabel('Hours [h]')
            plt.title(first_date+' - '+last_date)

            # Create red line
            plt.axhline(8, color='red', lw=1)   # Create vertical line for 8 hours
            plt.axhline(6, color='blue', lw=1)  # Create vertical line for 6 hours

            # Create annotation to bars
            cursor = mplcursors.cursor(hover=mplcursors.HoverMode.Transient)

            @cursor.connect("add")
            def on_add(sel):
                x, y, width, height = sel.artist[sel.index].get_bbox().bounds
                sel.annotation.set(text=f"{str(datetime.timedelta(seconds=height*3600))}",
                                   position=(0, 20), anncoords="offset points")

            plt.show()

            return msg
        else:
            return msg
    except AttributeError:
        msg = "The \"To date\" is\n earlier date than \"From date\""
        return msg
