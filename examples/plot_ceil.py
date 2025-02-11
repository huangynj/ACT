"""
Simple plot of 2D data
----------------------

This is an example of how to download and
plot ceiliometer data from the SGP site
over Oklahoma.

"""

import matplotlib.pyplot as plt
import act
import os

# Place your username and token here
username = os.getenv('ARM_USERNAME')
token = os.getenv('ARM_PASSWORD')

# If the username and token are not set, use the existing sample file
if username is None or token is None or len(username) == 0 or len(token) == 0:
    ceil_ds = act.io.armfiles.read_netcdf(act.tests.sample_files.EXAMPLE_CEIL1)
else:
    # Example to show how easy it is to download ARM data if a username/token are set
    act.discovery.download_data(username, token, 'sgpceilC1.b1', '2017-01-14', '2017-01-19')
    ceil_ds = act.io.armfiles.read_netcdf('./sgpceilC1.b1/*')

ceil_ds = act.corrections.ceil.correct_ceil(ceil_ds, -9999.0)
display = act.plotting.TimeSeriesDisplay(ceil_ds, subplot_shape=(1,), figsize=(15, 5))
display.plot('backscatter', subplot_index=(0,))
plt.show()
