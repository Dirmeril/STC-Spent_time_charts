import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import __main__
import datetime


def chosen_dates_and_activities(activities, first_date, last_date):
    dates = list(__main__.activity_summary.keys())
    first = dates.index(first_date)
    last = dates.index(last_date)+1
    chosen_activities = __main__.df_activity_summary.loc[[a for a in activities], [d for d in dates[first:last]]]
    # Discard of small values
    data_sum_in_rows = chosen_activities.sum(axis=1)
    counter = -1
    activities_without_small_percent = []
    for act in data_sum_in_rows:
        counter += 1
        if act * 100 / data_sum_in_rows.sum(axis=0) >= 3:
            activities_without_small_percent.append(data_sum_in_rows.index[counter])
    chosen_activities_without_small_percent = data_sum_in_rows.loc[[a for a in activities_without_small_percent]]

    return chosen_activities_without_small_percent, activities_without_small_percent

#Pie chart
def pie_chart(activities, first_date, last_date):
    data_time, data_activities = chosen_dates_and_activities(activities, first_date, last_date)
    plt.rcParams.update({'figure.autolayout': True})
    data_to_chart = np.array(data_time)
    plt.pie(data_to_chart, labels=data_activities, autopct=lambda p: f'{p:.0f}%')
    plt.show()


# Bar chart
def bar_chart(activities, first_date, last_date):
    data_time, data_activities = chosen_dates_and_activities(activities, first_date, last_date)
    data_to_chart = np.array(data_time)
    plt.rcParams.update({'figure.autolayout': True})
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.barh(data_activities, data_to_chart)
    ax.invert_yaxis()
    # Add annotation to bars
    for i in ax.patches:
        plt.text(i.get_width() + 0.2, i.get_y() + 0.5,
                 str(round((i.get_width()), 2)),
                 fontsize=9, fontweight='bold',
                 color='black')
    # Remove x, y Ticks
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    # Remove axes splines
    for s in ['top', 'left', 'right']:
        ax.spines[s].set_visible(False)
    # Add x, y gridlines
    ax.grid(color='grey', linewidth=0.5, alpha=0.7, linestyle='-.')
    plt.show()
