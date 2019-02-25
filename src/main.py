# =============================================================================

# =============================================================================

# from src.tool import Tool
from store import Store
from catalog import Catalog
from client import Client
from storeDate import StoreDate

NUM_SIMULATION_DAYS = 35

print ("The program runs!")

catalog = Catalog()
catalog.create_catalog()
client = Client()

hardwareStore = Store(catalog, client)

# Each day:
currSim = StoreDate()
today = currSim.simulateDay()
while (today != -1):
    print(today)
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

    today = currSim.simulateDay()
    # for customer in client.list:
        # tools = customer.returnTool(today)
        # hardwareStore.inventory.returnTool(tools)
