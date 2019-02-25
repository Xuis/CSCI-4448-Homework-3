# =============================================================================
# Store "has-a" Catalog
# Store "has-a" Customer 
# Store tracks Rentals (invoices) and Inventory
# =============================================================================


class Store:
    def __init__(self, catalog, client):
        self.customerList = client.list
        self.inventory = catalog
        self.month = [i for i in range(35)]
        self.rentals = {}



    def createRental(self, day, customerName, toolsRented, rentalTotal, dayRented, dayDue):
        self.rentals[day] = {"Customer Name": customerName,
                             "Tools": toolsRented,
                             "Payment": rentalTotal,
                             "Day Rented": dayRented,
                             "Due Date": dayDue}
