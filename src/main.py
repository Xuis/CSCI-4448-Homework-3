# =============================================================================

# =============================================================================

# from src.tool import Tool
from storeDate import StoreDate
# from store import Store
# from catalog import Catalog
# from client import Client

NUM_SIMULATION_DAYS = 35

print ("The program runs!")


# hardwareStore = Store()
# catalog = Catalog()
# client = Client()

# hardwareStore = Store(catalog, client)

# Each day:
currSim = StoreDate()
today = currSim.simulateDay()
while (today != -1):
    print(today)
    today = currSim.simulateDay()
    # hardwareStore.open(day)
    # hardwareStore.close()
    # Shuffle CustomerList




    # If tools are available
        # Customer enters stor

    # for customer in list:
        # if customer.toolBox[] :
            # customer.rentTool
        # if customer.toolBox.tool is Due:
            # customer.returnTool




        