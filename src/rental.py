# =============================================================================
# Created each time a customer rents an item.
# =============================================================================
class Rental:
    def __init__(self, day, customerName, itemsRented, rentalTotal, dayDue):
        self.__customer = customerName
        self.__day = day
        self.__items = itemsRented
        self.__rentalLength = dayDue - day
        self.__dayDue = dayDue
        
        # Calculate the cost of the rental:
        self.cost = 0
        for item in self.__items:
            self.cost += item.getCostPerDay() * self.__rentalLength

    def getItems(self):
        return self.__items

    def getCustomer(self):
        return self.__customer

    def getRentalLength(self):
        return self.__rentalLength

    def getRentalDueDate(self):
        return self.__dayDue