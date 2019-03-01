# =============================================================================
# prints all elements for final reporting as requested by assignment
# =============================================================================

from Catalog import Catalog

class Reporting:
    def print_final_inventory(inventory):
        # prints the ending inventory of store
        print("Inventory on hand after day 35:")
        if len(inventory.getOnhand()) > 0:
            for tool in inventory.getOnhand():
                print(tool.getName()," : ", tool.getCostPerDay())
        else: 
            print("We are currently out of tools!")

    def print_total_income(income):
        # prints the total amount made by store
        print("Income at the end of day 35: ", income)

    def print_rentals(df):
        # prints completed rentals and incomplete rentals
        completed = df.loc[(df['Day Due']<36)]
        print("Completed Rentals")
        print(completed)
        incomplete = df.loc[(df['Day Due'] >=36)]
        print("Incomplete Rentals")
        print(incomplete)
