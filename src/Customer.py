# =============================================================================
# There are 10 customers in 3 categories each with a unique name
# Customers can rent a max of 3 tools for 7 nights
# Business customers always rent 3 tools for 7 nights
# Casual customers rent 1-2 tools for 1-2 nights
# Regular customers rent 1-3 tools for 3-5 nights
# Customers interact with Store through renting and returning of tools and 
# paying for the tools.
# =============================================================================

import numpy as np
from random import randint

class Customer:
    def __init__(self, name):
        self.__name = name
        self.__shoppingCart = []
        self.__maxNumItems = 3
        self.__currentNumItems = len(self.__shoppingCart)

    # return number of Items customer has rented
    def getNumItemsRented(self):
	    return self.__currentNumItems

    def requestRental(self, inventory, day):
        # a customer will only rent a item if enough Items are available
        # and customers can only have 3 at a time
        # returns the total payment for rental order, the Items to be rented and for how long
        numItemsDesired = self.getNumItemsDesired()
        numNights = self.getNumNightsDesired()
        Items = []
        payment_due = 0
        if len(inventory) >= numItemsDesired:
            Items = self.pickItems(inventory, day, numItemsDesired, numNights)
            payment_due = self.payStore(Items, numNights)
        return (payment_due, Items, numNights)

    def pickItems(self, inventory, day, numItemsDesired, numNights):
        # allows the customer to put together an order. Checks to make sure the
        # customer has not randomly selected the same item twice as it cannot be
        # rented twice!
        renting = []
        while len(renting) < numItemsDesired:
            renteditem = np.random.choice(inventory)
            if renteditem not in renting:
                renteditem.dayDue = day + numNights
                renting.append(renteditem)
                self.__shoppingCart.append(renteditem)
        return renting 

    def willRentItems(self):
        # probability to shop based on # of Items in shoppingCart
        if self.__currentNumItems == self.__maxNumItems:
            return 0
        else:
            factor = 3*(self.__currentNumItems + 1)
            shopping = np.random.choice([1, 0], 1, p=[.5 / factor, 1 - (.5 / factor)])
            return shopping

    def getNumNightsDesired(self):
        # how long to rent the Items for!
        if "business" in self.__name:
            return 7
        elif "casual" in self.__name:
            return randint(1,2)
        else:
            return randint(3,5)

    def getNumItemsDesired(self):
        # how many Items to rent
        if "business" in self.__name:
            return 3
        elif "casual" in self.__name:
            if len(self.__shoppingCart) ==2:
                return 1
            else:        
                return randint(1, 2)
        else:
            top = 3-self.__currentNumItems
            return randint(1, top)


    # return Items a customer has due on the specified day
    def returnItems(self, day):
        Items = []
        for item in self.__shoppingCart:
            if item.dayDue == day:
                Items.append(item)
                self.__shoppingCart.remove(item)
        return Items


    def payStore(self, Items, nights):
        # calculates the total amount owed for Items the customer would like to rent
        paymentOwed = 0
        for item in Items:
            paymentOwed += item.getCostPerDay() * nights
        return paymentOwed

    def getName(self):
        return self.__name

# Subclasses for the Superclass customer
# these classes init with the Superclass values, but use their own max/min values
class CasualCustomer(Customer):
    def __init__(self, name):
        Customer.__init__(self, name)


class BusinessCustomer(Customer):
    def __init__(self, name):
        Customer.__init__(self, name)


class RegularCustomer(Customer):
    def __init__(self, name):
        Customer.__init__(self, name)


# the customer factory returns a newly instantiated customer based on their name
class CustomerFactory:
    def create_customer(name):
        if 'business' in name:
            return BusinessCustomer(name)
        if 'regular' in name:
            return RegularCustomer(name)
        if 'casual' in name:
            return CasualCustomer(name)
