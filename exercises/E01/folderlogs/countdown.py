import os
from datetime import datetime # Måste jag lägga till denna i dockerfilen?
import numpy as np
import timeit
import pandas as pd

# pathing
script_path = os.path.abspath(__file__)
source_file = script_path
log_file = os.path.join(os.path.dirname(script_path), 'countdown.log')

# assigning values 
events = np.array([
    ('summer_break', np.datetime64('2023-06-09T15:00')),
    ('lia_start', np.datetime64('2023-09-25T08:00')),
    ('christmas', np.datetime64('2023-12-24')),
    ('bellas_birthday', np.datetime64('2023-12-07')),
    ('new_year', np.datetime64('2024-01-01')),
    ('graduation_party', np.datetime64('2024-06-09T16:30'))
], dtype=[('Event', 'U20'), ('Date', 'datetime64[s]')])


# Get the current datetime
current_datetime = np.datetime64(datetime.now())

# Prepare the countdown log string
countdown_log = "-" * 50 + "\n"
countdown_log += f"Countdown from {current_datetime}\n"
countdown_log += "-" * 50 + "\n\n"

for event in events:
    event_name = event['Event']
    event_date = event['Date']
    time_left = event_date - current_datetime
    days_left = time_left.astype('timedelta64[D]')
    hours_left = (time_left.astype('timedelta64[h]') % np.timedelta64(1, 'D')).astype(int)
    minutes_left = (time_left.astype('timedelta64[m]') % np.timedelta64(1, 'h')).astype(int)

    countdown_log += f"Countdown to {event_name}: {days_left} days, {hours_left} hours, {minutes_left} minutes\n"

# Print the countdown log
# print(countdown_log)

# Write the countdown log to the file
with open(log_file, 'w') as file:
    file.write(countdown_log)



# # -- original
# # Calculate time differences in seconds
# time_diffs = events['Date'] - current_datetime
# time_left = pd.to_timedelta(time_diffs, unit='s').floor('s').astype(str)

# df = pd.DataFrame({'Event': events['Event'], 'Date': events['Date'], 'Time left': time_left})

# print(df)

# #------

# # logging the output
# with open(log_file, 'a') as log:
#     # Redirect the print output to the log file
#     print(events, file=log)

# print("Structured array printed to the log file successfully.")

