# STC-Spent_time_charts
### Library
`pip install customtkinter  
pip install pandas  
pip install matplotlib  
pip install tkcalendar  
pip install mplcursors`

### About the program
A program collect data from file work_log.txt and display sum activities in all range in pie chart or acvities per day in stacked bar chart. The program allows choose activities and time range which will be display. With slider bar you can discard activity which is under from 1 to 5% in sum all activites in day (stacked bar) and in the time range (pie chart). The text file must be in the same folder as the program.
You can select only highlighted dates.
Load data from file work_log.txt which has pattern:  
'Activity; time spent on activity; date when activity started

For example:  
Projects;0:40:05.218156;2023-03-09 14:26:13.265291  
Emails;0:00:03.573324;2023-03-09 14:26:16.837471  
Meeting;0:21:06.452207;2023-03-09 14:26:23.289742   
etc.

![menu](https://github.com/Dirmeril/STC-Spent_time_charts/assets/102697092/e77b3bb7-6ec0-4f09-a3ab-266fc310a196)

![bar](https://github.com/Dirmeril/STC-Spent_time_charts/assets/102697092/82ab6348-d31e-4d02-b75a-d7f7674d684d)


