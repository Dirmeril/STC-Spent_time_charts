import datetime
import load_data
import __main__

def sum():
    ### Wyliczenie alltime
    activity = __main__.activity
    allTime = datetime.timedelta()
    for i in activity.values():
        (h, m, sec) = i.split(':')
        d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(sec))
        allTime += d
    # print(type(allTime))
    # print(allTime.seconds,'moje sekundy')
    # print(allTime.days,'moje dni')
    allTime_in_sec = allTime.seconds + allTime.days*24*3600

    ### procentowe wyliczenie czasu
    percentage = {}
    # print(activity.keys())
    for a in activity.keys():
        (h, m, sec) = activity[a].split(':')
        d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(sec))
        per = 100*d.seconds/allTime_in_sec
        percentage[a] = per
    ### sprawdzanie sumy
    add = 0
    for p in percentage.values():
        add += p

    ###Sortowanie
    # print(sorted(percentage.items(), key=lambda x: x[1]))
    posortowane = {}
    posortowane.update(sorted(percentage.items(), key=lambda x: x[1]))

    ###Ładowanie danych do wykresu
    mylabels = list(posortowane.keys())
    numbers = list(posortowane.values())

    return mylabels, numbers, add