# =============================================================================

# =============================================================================

from src.store import Store
from src.tool import Tool

NUM_SIMULATION_DAYS = 35

print ("The program runs!")

hardwareStore = Store()

# Each day:
for day in range(0, NUM_SIMULATION_DAYS):
    print("Day {} simulated.".format(day))
    hardwareStore.open()
    hardwareStore.close()
    # Shuffle CustomerList
    
    # for customer in list:
        # if customer.toolBox[] :
            # customer.rentTool
        # if customer.toolBox.tool is Due:
            # customer.returnTool




        