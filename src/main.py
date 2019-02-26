# =============================================================================
# Instantiates necessary class objects and passes them to the Simulator 
# 
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
