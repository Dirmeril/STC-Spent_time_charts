import matplotlib.pyplot as plt
import pandas as pd
import __main__
import gui


# Sum data for pie chart
def chosen_dates_and_activities(activities, first_date, last_date):
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
        for act in data_sum_in_rows:
            counter += 1
            if act * 100 / data_sum_in_rows.sum(axis=0) >= 1:
                activities_without_small_percent.append(data_sum_in_rows.index[counter])
        chosen_activities_without_small_percent = data_sum_in_rows.loc[[a for a in activities_without_small_percent]]
        msg = ''
        return chosen_activities_without_small_percent, activities_without_small_percent, msg

    except ValueError as e:
        msg = 'Choose available date'
        return None, None, msg




# Pie chart
def pie_chart(activities, first_date, last_date):
    try:
        data_time, data_activities, msg = chosen_dates_and_activities(activities, first_date, last_date)
        if data_time is not None and data_activities is not None:
            col_dates = first_date+' - '+last_date
            df_data_time = pd.DataFrame(data_time, columns=[col_dates])

            # Calculation from datetime.delta time to seconds in int
            df_data_time[col_dates] = df_data_time[col_dates].dt.total_seconds()
            df_data_time.plot.pie(y=col_dates, figsize=(6, 5), autopct=lambda p: f'{p:.0f}%', legend=False, title=col_dates, ylabel='')
            # df_data_time.plot
            plt.show()
            return msg
        else:
            return msg

    except AttributeError as e:
        msg = "The \"To date\" is\n earlier date than \"From date\""
        return msg