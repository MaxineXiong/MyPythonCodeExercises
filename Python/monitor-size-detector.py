# Write a script that detects and prints out your monitor resolution.
from screeninfo import get_monitors

for monitor in get_monitors():
    print('Width: ' + str(monitor.width) + ', Height: ' + str(monitor.height))
