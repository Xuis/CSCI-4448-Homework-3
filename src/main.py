from src.store import Store
from src.catalog import Catalog
from src.client import Client
from src.storeDate import StoreDate

NUM_SIMULATION_DAYS = 35

print ("The program runs!")


catalog = Catalog()
client = Client()

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
