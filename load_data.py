import os
import datetime


def load():
    name = 'work_log.txt'
    get_dir = os.getcwd()
    file = os.path.join(get_dir, name)
    activity = {}
    counter: int = 0
    with open(file, 'r') as f:
        for line in f:
            counter += 1
            part = line.split(';')
            if len(part) == 3:
                if part[0] in activity:
                    time_list = [activity[part[0]], part[1]]
                    my_sum = datetime.timedelta()
                    for i in time_list:
                        (h, m, sec) = i.split(':')
                        if sec.find('.') != -1:
                            (s, ms) = sec.split('.')
                        else:
                            s = sec
                        d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                        my_sum += d
                    activity[part[0]] = str(my_sum)
                else:
                    first_time = part[1].split('.')
                    activity[part[0]] = first_time[0]
            else:
                print('Error! Line: {}: {}'.format(counter, part))
    return activity
