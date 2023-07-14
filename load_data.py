import os
import datetime
import pandas as pd


def load():
    name = 'work_log.txt'
    get_dir = os.getcwd()
    file = os.path.join(get_dir, name)
    activity_summary = {}
    counter: int = 0        # To the mark lines
    with open(file, 'r') as f:
        for line in f:
            counter += 1
            parts = line.strip().split(';')
            if len(parts) == 3:
                activity_name = parts[0]
                time_str = parts[1]
                date_str = parts[2].split()[0]

                time_parts = time_str.split(':')
                hours = int(time_parts[0])
                minutes = int(time_parts[1])
                seconds = int(float(time_parts[2].split('.')[0]))

                time_delta = datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)

                if date_str not in activity_summary:
                    activity_summary[date_str] = {}

                if activity_name in activity_summary[date_str]:
                    activity_summary[date_str][activity_name] += time_delta
                else:
                    activity_summary[date_str][activity_name] = time_delta
            else:
                print('Error! Line: {}: {}'.format(counter, line))

    # Changing time format in activity_summary
    for date, activities in activity_summary.items():
        for activity, time_delta in activities.items():
            activity_summary[date][activity] = str(time_delta)
    sorting = sorted(activity_summary.items(), key=lambda x: x[0])
    activity_summary = dict(sorting)

    return activity_summary
