import matplotlib.pyplot as plt
import pandas as pd
import __main__
import numpy as np


# Sum data for pie chart
def chosen_dates_and_activities(activities, first_date, last_date, discard_number):
    try:
        dates = list(__main__.activity_summary.keys())
        first = dates.index(first_date)
        last = dates.index(last_date)+1

        # Swap dates and activities to DataFrame
        chosen_activities = __main__.df_activity_summary.loc[[a for a in activities], [d for d in dates[first:last]]]

        # Discard of small values
        data_sum_in_rows = chosen_activities.sum(axis=1)
        counter = -1
        activities_without_small_percent = []
        activities_small_percent = []
        for act in data_sum_in_rows:
            counter += 1
            if act * 100 / data_sum_in_rows.sum(axis=0) > discard_number:
                activities_without_small_percent.append(data_sum_in_rows.index[counter])
            else:
                activities_small_percent.append(data_sum_in_rows.index[counter])
        chosen_activities_without_small_percent = data_sum_in_rows.loc[[a for a in activities_without_small_percent]]

        # Sum all discarded times
        chosen_activities_small_percent = data_sum_in_rows.loc[[a for a in activities_small_percent]]
        chosen_activities_small_percent = chosen_activities_small_percent.sum(axis=0)
        # Add discarded values to rest
        if discard_number != 0:
            chosen_activities_without_small_percent.loc['Other'] = chosen_activities_small_percent
        msg = ''
        return chosen_activities_without_small_percent, activities_without_small_percent, msg

    except ValueError:
        msg = 'Choose available date'
        return None, None, msg


# Pie chart
def pie_chart(activities, first_date, last_date, discard_number):
    try:
        data_time, data_activities, msg = chosen_dates_and_activities(activities, first_date, last_date, discard_number)
        if data_time is not None and data_activities is not None:
            col_dates = first_date+' - '+last_date
            df_data_time = pd.DataFrame(data_time, columns=[col_dates])

            # Calculation from datetime.delta time to seconds in int
            df_data_time[col_dates] = df_data_time[col_dates].dt.total_seconds()

            def func(pct, time_from_date_time):
                absolute = np.round(pct / 100. * np.sum(time_from_date_time), 2)
                hours = int(absolute)
                mint = int((absolute - hours)*60)
                return f"{pct:.1f}% ({hours}:{mint:02d})"

            data = [x/3600 for x in df_data_time[col_dates]]
            df_data_time.plot.pie(y=col_dates, figsize=(6, 5), autopct=lambda p: func(p, data), legend=False,
                                  title=col_dates, ylabel='')
            # df_data_time.plot
            plt.show()
            return msg
        else:
            return msg

    except AttributeError:
        msg = "The \"To date\" is\n earlier date than \"From date\""
        return msg
