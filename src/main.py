# =============================================================================
# Instantiates necessary class objects and passes them to the Simulator 
# FINAL REPORT CONTENTS:
# * Number of tools left in Store inventory after 35 days
# * Amount of money made by store after 35 complete days
# * A list of all completed Rentals that includes:
#     * which tools rented by which customers
#     * How many days those tools were rented
#     * How much that total rental cost
# * A list of all outstanding rentals with the same information
# =============================================================================

from simulator import Simulator
from store import Store
from catalog import Catalog
from customerList import CustomerList

customerList = CustomerList()
catalog = Catalog()
store = Store(catalog, customerList)
simulation = Simulator(store)
simulation.setNumDaysToRun(35)
simulation.startSimulation()
