<<<<<<< HEAD
# =============================================================================

# =============================================================================

# from src.tool import Tool
from storeDate import StoreDate
# from store import Store
from catalog import Catalog
# from client import Client
=======
from src.store import Store
from src.catalog import Catalog
from src.client import Client
from src.storeDate import StoreDate
>>>>>>> ea667aebb198ec3e9d78261322b37e26baaeb79e

NUM_SIMULATION_DAYS = 35

print ("The program runs!")


<<<<<<< HEAD
# hardwareStore = Store()
catalog = Catalog()
catalog.create_catalog()
# client = Client()
=======
catalog = Catalog()
client = Client()
>>>>>>> ea667aebb198ec3e9d78261322b37e26baaeb79e

hardwareStore = Store(catalog, client)

# Each day:
currSim = StoreDate()
today = currSim.simulateDay()
while (today != -1):
    print(today)
    today = currSim.simulateDay()
    for customer in client.list:
        tools = customer.returnTool(today)
        hardwareStore.inventory.returnTool(tools)
