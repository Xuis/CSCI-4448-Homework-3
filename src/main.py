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
from Store import Store
from catalog import Catalog
from customerList import CustomerList
from reporting import Reporting
import pandas as pd

customerList = CustomerList()
catalog = Catalog()
store = Store(catalog, customerList)
simulation = Simulator(store)
simulation.setNumDaysToRun(35)
simulation.startSimulation()

 
    
labels = ['Customer Name', 'Item 1', 'Item 2', 'Item 3', 'Days', 'Day Due', 'Total Cost']
superRentalList = []
for rental in store.getRentalList():
    itemNames = [None, None, None]
    for index in range(len(rental.getItems())):
        for item in rental.getItems():        
            itemNames[index] = item.getName() 
    superRentalList.append([rental.getCustomer(), itemNames[0], itemNames[1], itemNames[2], rental.getRentalLength(), rental.getRentalDueDate() + 1, rental.cost])

df = pd.DataFrame(superRentalList)
df.columns = labels

Reporting.print_final_inventory(store.getInventory())
Reporting.print_total_income(store.getIncome())
Reporting.print_rentals(df)
