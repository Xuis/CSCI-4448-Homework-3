class Reporting:

    def print_final_inventory(inventory):
        print("Inventory on hand after day 35:")
        if len(inventory.onhand) > 0:
            for tool in inventory.onhand:
                print(tool.name," : ", tool.costPerDay)
        else: 
            print("We are currently out of tools!")

    def print_total_income(income):
        print("Income at the end of day 35: ", income)

    def print_rentals(df):
        print("Completed Rentals")
        completed = df.loc[(df['Day Due']<36)]
        print(completed)
        incomplete = df.loc[(df['Day Due'] >=36)]
        print("Incomplete Rentals")
        print(incomplete)
