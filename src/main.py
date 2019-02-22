from store import Store
from src.tools import Tools

simulationDays = 35

print ("The program runs!")

hardware = Store()

for day in range(simulationDays):
    hardware.open()
    hardware.close()
