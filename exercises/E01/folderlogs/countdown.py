import os
from datetime import datetime
import numpy as np
import timeit


# Assign values to the structured array directly with datetime64 data type
events = np.array([
    ('summer_break', np.datetime64('2023-06-09')),
    ('lia_start', np.datetime64('2023-09-25')),
    ('christmas', np.datetime64('2023-12-24')),
    ('bellas_birthday', np.datetime64('2023-12-07')),
    ('new_year', np.datetime64('2024-01-01')),
    ('graduation_party', np.datetime64('2024-06-09'))
], dtype=[('name', 'U20'), ('date', 'datetime64[D]')])

# Print the structured array
print(events)


countdown_py_path = os.path.abspath(__file__)
countdown_dir = os.path.dirname(countdown_py_path)
log_filepath = os.path.join(countdown_dir, "folderlogs", "countdown.log")
