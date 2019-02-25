from store import Store
from catalog import Catalog
from client import Client
from storeDate import StoreDate


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
    for customer in client.list:
        shopping = customer.shop_today()
        if shopping:
            payment, tools, due = customer.rentTool(hardwareStore.inventory.onhand, today)
            hardwareStore.inventory.rentTool(tools)
            hardwareStore.createRental(today, customer.name, tools, payment, today, due)

print(hardwareStore.rentals)
