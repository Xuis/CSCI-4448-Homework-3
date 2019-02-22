from src.store import Store
from src.tool import Tool

NUM_SIMULATION_DAYS = 35

print ("The program runs!")

hardware = Store()

for day in range(0, NUM_SIMULATION_DAYS):
    print("Day {} simulated.".format(day))
    hardware.open()
    hardware.close()
