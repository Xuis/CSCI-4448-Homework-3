# =============================================================================
# Created each time a customer rents an item.
# =============================================================================
class Rental:
    def __init__(self, day, customerName, itemsRented, rentalTotal, dayDue):
        self.customer = customerName
        self.day = day
        self.items = itemsRented
        self.rentalLength = dayDue - day
        self.dayDue = dayDue
        
        # Calculate the cost of the rental:
        self.cost = 0
        for item in self.items:
            self.cost += item.getCostPerDay() * self.rentalLength

