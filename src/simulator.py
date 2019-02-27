# =============================================================================
# Simmulates the activity of the Rental Store for 35 days. 
# Each Day:
#    Random number customers "come in"
#    Only customers who CAN rent, will come in
#    Every customer that comes in WILL rent
#    Every customer will rent tools according to their type
#    Every customer will create a Rental
#    When the Store has 0 tools, there will be zero customers
# =============================================================================
class Simulator:
    def __init__(self, store):
        self.store = store
        self.customerList = store.customerList
        self.days = []
        
    def setNumDaysToRun(self, numDaysToRun):
        self.days = [i for i in range(numDaysToRun)]

    def startSimulation(self):
        
        for day in self.days:
            self.customerFunctions(day)
            
            
            
    def customerFunctions(self, day):
        self.simulate_customerReturns(day)
        self.simulate_customerRentals(day)

    def simulate_customerReturns(self, day):
        returned_tools=[]
        for customer in self.customerList:
            tools = customer.returnTools(day)
            for tool in tools:
                returned_tools.append(tool)
        self.store.inventory.returnTool(returned_tools)

    def simulate_customerRentals(self, day):
        for customer in self.customerList:
            if customer.willRentTools():
                payment, tools, numNights = customer.requestRental(self.store.inventory.onhand, day)
                self.store.income += payment
                self.store.inventory.rentTool(tools)
                self.store.createRental(day, customer.name, tools, payment, numNights + day)

    def print_daily(self, day):
        print("DAY:", day)    
        #print("ON HAND:")    
        #print(self.store.inventory.onhand)
        #print("ON LOAN:")
        #print(self.store.inventory.onloan)
        print(self.store.income)
