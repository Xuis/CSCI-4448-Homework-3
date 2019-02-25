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
            customerList.wakeAllCustomers()
            customerList.performReturns(today, hardwareStore)
            customerList.performRentals(today, hardwareStore)
            today = currSim.simulateDay()
        print(hardwareStore.getRentals())