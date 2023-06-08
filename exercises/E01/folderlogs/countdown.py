import os
from datetime import datetime
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

# creating a dataframe for the output
df= pd.DataFrame(events)
print(df)

# logging the output
with open(log_file, 'a') as log:
    # Redirect the print output to the log file
    print(events, file=log)

print("Structured array printed to the log file successfully.")

