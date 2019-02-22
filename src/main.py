# =============================================================================

# =============================================================================

from store import Store
from tool import Tool

simulationDays = 35

print ("The program runs!")

hardware = Store()

for day in range(simulationDays):
    hardware.open()
    hardware.close()

# Each day:
#for day in range(simulationDays):
#   Shuffle CustomerList
    
#    for customer in list:
#        if customer.toolBox[] :
#       
    
#           customer.rentTool
#       if customer.toolBox.tool is Due:
#           customer.returnTool




        