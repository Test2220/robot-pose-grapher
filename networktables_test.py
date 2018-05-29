import csv
import time
import math
from networktables import NetworkTables

# To see messages from networktables, you must setup logging
import logging
logging.basicConfig(level=logging.DEBUG)

NetworkTables.initialize()
sd = NetworkTables.getTable("SmartDashboard")

time.sleep(2)
with open('test_path.csv') as csvfile:
    time.sleep(1)
    reader = csv.DictReader(csvfile)
    for row in reader:
        x = float(row['x'])
        x = x * 12
        y = float(row['y'])
        y = y * 12.0
        angle = float(row['heading'])
        sd.putNumber('Field X', y)
        sd.putNumber('Field Y', x)
        sd.putNumber('Path Actual Heading', angle)
        print(x, y, angle)
        time.sleep(0.01)