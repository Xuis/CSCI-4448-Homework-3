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

class Customer:
    def __init__(self, name):
        self.name = name
        self.toolbox = []
        self.maxNumTools = 3
        self.minNumTools = 0
        self.minNights = 0
        self.maxNights = 7
        self.currentNumTools = len(self.toolbox)

    # return number of tools customer has rented
    def getNumToolsRented(self):
	    return self.currentNumTools

    def requestRental(self, inventory, day):
        # a customer will only rent a tool if enough tools are available
        # and customers can only have 3 at a time
        # returns the total payment for rental order, the tools to be rented and for how long
        numToolsDesired = self.getNumToolsDesired()
        numNights = self.getNumNightsDesired()
        tools = []
        payment_due = 0
        if len(inventory) >= numToolsDesired:
            tools = self.pickTools(inventory, day, numToolsDesired, numNights)
            payment_due = self.payStore(tools, numNights)
        return (payment_due, tools, numNights)

    def pickTools(self, inventory, day, numToolsDesired, numNights):
        # allows the customer to put together an order. Checks to make sure the
        # customer has not randomly selected the same tool twice as it cannot be
        # rented twice!
        renting = []
        while len(renting) < numToolsDesired:
            rentedTool = np.random.choice(inventory)
            if rentedTool not in renting:
                renting.append(rentedTool)
                rentedTool.dayRented = day
                rentedTool.dayDue = day + numNights
                self.toolbox.append(rentedTool)
        return renting

    def willRentTools(self):
        # probability to shop based on # of tools in toolbox
        if self.currentNumTools == self.maxNumTools:
            return 0
        else:
            factor = 3*(self.currentNumTools + 1)
            shopping = np.random.choice([1, 0], 1, p=[.5 / factor, 1 - (.5 / factor)])
            return shopping

    def getNumNightsDesired(self):
        # how long to rent the tools for!
        numNightsDesired = np.random.choice(list(range(self.minNights, self.maxNights + 1)))
        return numNightsDesired

    def getNumToolsDesired(self):
        # how many tools to rent
        numToolsDesired = np.random.choice(range(self.minNumTools, self.maxNumTools - self.currentNumTools))
        return numToolsDesired


    # return tools a customer has due on the specified day
    def returnTools(self, day):
        tools = []
        for tool in self.toolbox:
            if tool.dayDue == day:
                tools.append(tool)
                self.toolbox.remove(tool)
        return tools


    def payStore(self, tools, nights):
        # calculates the total amount owed for tools the customer would like to rent
        paymentOwed = 0
        for tool in tools:
            paymentOwed += tool.costPerDay * nights
        return paymentOwed

# Subclasses for the Superclass customer
# these classes init with the Superclass values, but use their own max/min values
class CasualCustomer(Customer):
    def __init__(self, name):
        Customer.__init__(self, name)
        self.maxNights = 2
        self.minNights = 1
        self.maxNumTools = 2


class BusinessCustomer(Customer):
    def __init__(self, name):
        Customer.__init__(self, name)
        self.maxNights = 5
        self.minNights = 5

    def getNumToolsDesired(self):
        return 3


class RegularCustomer(Customer):
    def __init__(self, name):
        Customer.__init__(self, name)
        self.maxNights = 5
        self.minNights = 3
        self.maxNumTools = 3
        self.minNumTools = 1


# the customer factory returns a newly instantiated customer based on their name
class CustomerFactory:
    def create_customer(name):
        if 'business' in name:
            return BusinessCustomer(name)
        if 'regular' in name:
            return RegularCustomer(name)
        if 'casual' in name:
            return CasualCustomer(name)
