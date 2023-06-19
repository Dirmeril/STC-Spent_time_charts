import matplotlib.pyplot as plt
import numpy as np
import __main__


# Pie Chart
def pie_chart():
    plt.rcParams.update({'figure.autolayout': True})
    y = np.array(__main__.numbers)
    plt.pie(y, labels=__main__.my_labels, autopct=lambda p: '{:.0f}%'.format(p * int(__main__.add) / 100))
    plt.show()


# Bar chart
def bar_chart():
    plt.rcParams.update({'figure.autolayout': True})
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.barh(__main__.my_labels, __main__.numbers)
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
