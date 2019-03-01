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

from Simulator import Simulator
from Store import Store
from Catalog import Catalog
from CustomerList import CustomerList
from Reporting import Reporting
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
    rentals = rental.getItems()
    for index in range(len(rental.getItems())):        
        itemNames[index] = rentals[index].getName() 
    superRentalList.append([rental.getCustomer(), itemNames[0], itemNames[1], itemNames[2], rental.getLength(), rental.getDueDate() + 1, rental.getCost()])

df = pd.DataFrame(superRentalList)
df.columns = labels

Reporting.print_final_inventory(store.getInventory())
Reporting.print_total_income(store.getIncome())
Reporting.print_rentals(df)
