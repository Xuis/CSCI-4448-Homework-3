from src.store import Store
from src.catalog import Catalog
from src.client import Client

NUM_SIMULATION_DAYS = 35

print ("The program runs!")

catalog = Catalog()
client = Client()

hardwareStore = Store(catalog, client)
# Each day:
for day in range(0, NUM_SIMULATION_DAYS):
    print("Day {} simulated.".format(day))
    hardwareStore.open(day)
    hardwareStore.close()
    # Shuffle CustomerList

    # While (isDay)

    # If tools are available
        # Customer enters stor

    # for customer in list:
        # if customer.toolBox[] :
            # customer.rentTool
        # if customer.toolBox.tool is Due:
            # customer.returnTool




        