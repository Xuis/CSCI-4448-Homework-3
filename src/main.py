# =============================================================================

# =============================================================================

# from store import Store
# from src.tool import Tool
from storeDate import StoreDate

NUM_SIMULATION_DAYS = 35

print ("The program runs!")

# hardwareStore = Store()

# Each day:
for day in range(0, NUM_SIMULATION_DAYS):
    print("Day {} simulated.".format(day))
    # hardwareStore.open(day)
    # hardwareStore.close()
    # Shuffle CustomerList

    currSim = StoreDate()
    today = currSim.simulateDay()
    while (today != -1):
        print(today)
        today = currSim.simulateDay()


    # If tools are available
        # Customer enters stor

    # for customer in list:
        # if customer.toolBox[] :
            # customer.rentTool
        # if customer.toolBox.tool is Due:
            # customer.returnTool




        