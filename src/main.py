# =============================================================================
# Instantiates necessary class objects and passes them to the Simulator 
# 
# =============================================================================

from simulator import Simulator
from store import Store
from catalog import Catalog
from customer import Customer


def main():
    #customerList = CustomerFactory()
    #catalog = ToolFactory()
    store = Store(catalog, customerList)
    simulation = Simulator()
    simulation.startSimulation()
