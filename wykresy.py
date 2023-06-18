# import os
# import datetime
# import matplotlib.pyplot as plt
# import numpy as np
#
# name = 'work_log.txt'
# get_dir = os.getcwd()
# file = os.path.join(get_dir, name)
# activity = {}
#
# with open(file,'r') as f:
#     for line in f:
#         part = line.split(';')
#         if len(part) == 3:
#             print("aktywność: %s, czas spędzony: %s, data: %s" % (part[0], part[1], part[2]))
#             if part[0] in activity:
#                 timeList = [activity[part[0]],part[1]]
#                 mysum = datetime.timedelta()
#                 for i in timeList:
#                     (h, m, sec) = i.split(':')
#                     if sec.find('.') != -1:
#                         (s, ms) = sec.split('.')
#                     else:
#                         s = sec
#                     d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
#                     mysum += d
#                 activity[part[0]] = str(mysum)
#             else:
#                 czas = part[1].split('.')
#                 activity[part[0]] = czas[0]
#         else:
#             print('Nieprawidłowy format')
#
# print(activity.items())
#
# ### Wyliczenie alltime
# allTime = datetime.timedelta()
# for i in activity.values():
#     (h, m, sec) = i.split(':')
#     d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(sec))
#     allTime += d
# print(type(allTime))
# print(allTime.seconds,'moje sekundy')
# print(allTime.days,'moje dni')
# allTime_in_sec = allTime.seconds + allTime.days*24*3600
#
# ### procentowe wyliczenie czasu
# percentage = {}
# print(activity.keys())
# for a in activity.keys():
#     (h, m, sec) = activity[a].split(':')
#     d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
#     per = 100*d.seconds/allTime_in_sec
#     percentage[a] = per
# ### sprawdzanie sumy
# add = 0
# for p in percentage.values():
#     add += p
#
# ###Sortowanie
# print(sorted(percentage.items(), key=lambda x: x[1]))
# posortowane = {}
# posortowane.update(sorted(percentage.items(), key=lambda x: x[1]))
#
# while True:
#     ###Ładowanie danych do wykresu
#     mylabels = list(posortowane.keys())
#     numbers = list(posortowane.values())
#     # for pi in posortowane.keys():
#     #     mylabels.append(pi)
#     #     numbers.append(percentage[pi])
#
#     a = input('''Wybierz wykres:
#               1 - Kołowy
#               2 - Słupkowy
#               0 - Zakończ program
#               ''')
#     if a == '1':
#         ### Rysowanie wykresu kołowego
#         plt.rcParams.update({'figure.autolayout': True})
#         y = np.array(numbers)
#         plt.pie(y, labels=mylabels, autopct=lambda p: '{:.0f}%'.format(p * int(add) / 100))
#         plt.show()
#     elif a == '2':
#         ###Rysowanie wykresu słupkowego
#         plt.rcParams.update({'figure.autolayout': True})
#         fig, ax = plt.subplots(figsize=(10, 5))
#         ax.barh(mylabels, numbers)
#         ax.invert_yaxis()
#         # Add annotation to bars
#         for i in ax.patches:
#             plt.text(i.get_width() + 0.2, i.get_y() + 0.5,
#                      str(round((i.get_width()), 2)),
#                      fontsize=9, fontweight='bold',
#                      color='black')
#         # Remove x, y Ticks
#         ax.xaxis.set_ticks_position('none')
#         ax.yaxis.set_ticks_position('none')
#         # Remove axes splines
#         for s in ['top', 'left', 'right']:
#             ax.spines[s].set_visible(False)
#         # Add x, y gridlines
#         ax.grid(color='grey', linewidth=0.5, alpha=0.7, linestyle ='-.')
#         plt.show()
#     elif a == '0':
#         break
#     else:
#         print('Wprowadziłeś nieprawidłowy numer')
#
