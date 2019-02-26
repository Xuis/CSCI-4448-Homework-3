# =============================================================================
# Instantiates necessary class objects and passes them to the Simulator 
# 
# =============================================================================

from simulator import Simulator
from store import Store
from catalog import Catalog
from customerList import CustomerList

customerList = CustomerList()

def main():
    customerList = CustomerFactory()
    #catalog = ToolFactory()
    store = Store(catalog, customerList)
    simulation = Simulator()
    simulation.setNumDaysToRun(35)
    simulation.startSimulation()
