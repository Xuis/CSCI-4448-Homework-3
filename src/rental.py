"""
Since a customer can rent multiple items at a time, and must return those items at the same time,
the rental class stores this information

Must store:
1. Information on when rental occured so can return on time
2. Must contain a list of the items that were rented

1. Price
2. Customer
3. Rental Date
4. Rental Length (Days or nights)
5. List of items

Take in list of items and record rental date and must return date
"""
# =============================================================================
# 
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

