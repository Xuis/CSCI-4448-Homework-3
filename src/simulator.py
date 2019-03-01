# =============================================================================
# Simmulates the activity of the Rental Store for 35 days. 
# Each Day:
#    Random number customers "come in"
#    Only customers who CAN rent, will come in
#    Every customer that comes in WILL rent
#    Every customer will rent Items according to their type
#    Every customer will create a Rental
#    When the Store has 0 Items, there will be zero customers
# =============================================================================
class Simulator:
    def __init__(self, store):
        self.store = store
        self.customerList = store.getCustomerList()
        self.days = []
        
    def setNumDaysToRun(self, numDaysToRun):
        self.days = [i for i in range(numDaysToRun)]

    def startSimulation(self):        
        for day in self.days:
            self.simulate_customerReturns(day)
            self.simulate_customerRentals(day)
  
    def simulate_customerReturns(self, day):
        returned_Items=[]
        for customer in self.customerList:
            Items = customer.returnItems(day)
            for item in Items:
                returned_Items.append(item)
        self.store.getInventory().returnItem(returned_Items)

    def simulate_customerRentals(self, day):
        for customer in self.customerList:
            if customer.willRentItems():
                payment, Items, numNights = customer.requestRental(self.store.getInventory().onhand, day)
                self.store.setIncome(self.store.getIncome() + payment)
                self.store.getInventory().rentItem(Items)
                if payment:
                    self.store.createRental(day, customer.name, Items, payment, numNights + day)