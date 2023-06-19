import datetime
import load_data


def sum_time():
    # time calculation
    activity = load_data.load()
    all_time = datetime.timedelta()
    for i in activity.values():
        (h, m, sec) = i.split(':')
        d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(sec))
        all_time += d
    all_time_in_sec = all_time.seconds + all_time.days*24*3600

    # percentage time calculation
    percentage = {}
    for a in activity.keys():
        (h, m, sec) = activity[a].split(':')
        d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(sec))
        per = 100*d.seconds/all_time_in_sec
        percentage[a] = per
    # check the sum
    total_time = 0
    for p in percentage.values():
        total_time += p

    # sort data time
    sort_time = {}
    sort_time.update(sorted(percentage.items(), key=lambda x: x[1]))

    # Load data into the chart
    my_labels = list(sort_time.keys())
    numbers = list(sort_time.values())

    return my_labels, numbers, total_time
