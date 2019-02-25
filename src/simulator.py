from store import Store
from catalog import Catalog
from customerList import CustomerList
from storeDate import StoreDate

class Simulator:
# -------------------- New UML Methods -------------------
    def startSimulation(self):
        NUM_SIMULATION_DAYS = 35

        print ("The program runs!")

        catalog = Catalog()
        catalog.create_catalog()
        customerList = CustomerList()
        hardwareStore = Store(catalog, customerList)

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

            # for customer in client.list:
                # tools = customer.returnTool(today)
                # hardwareStore.inventory.returnTool(tools)
            today = currSim.simulateDay()
            for customer in customerList.list:
                tools = customer.returnTools()
                # hardwareStore.inventory.returnTool(tools)
            for customer in customerList.list:
                shopping = customer.shop_today()
                if shopping:
                    payment, tools, due = customer.rentTool(hardwareStore.inventory.onhand, today)
                    hardwareStore.inventory.rentTool(tools)
                    hardwareStore.createRental(today, customer.name, tools, payment, today, due)

        print(hardwareStore.rentals)