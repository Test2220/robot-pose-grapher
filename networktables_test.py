import csv
import time
from networktables import NetworkTables

# To see messages from networktables, you must setup logging
import logging
logging.basicConfig(level=logging.DEBUG)

NetworkTables.initialize()
sd = NetworkTables.getTable("SmartDashboard")

time.sleep(2)
with open('path.csv') as csvfile:
    time.sleep(1)
    reader = csv.DictReader(csvfile)
    for row in reader:
        x = float(row['x'])
        x = x * 12
        y = float(row['y'])
        y = y * 12.0
        sd.putNumber('Field X', y)
        sd.putNumber('Field Y', x)
        print(x, y)
        time.sleep(0.01)