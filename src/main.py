from store import Store
from tool import Tool

simulationDays = 35

print ("The program runs!")

hardware = Store()

for day in range(simulationDays):
    hardware.open()
    hardware.close()
