
class Simulator:
    def __init__(self, store):
        self.store = store
        self.customerList = store.customerList
        self.days = []
        
    def setNumDaysToRun(self, numDaysToRun):
        self.days = [i for i in range(numDaysToRun)]

    def startSimulation(self):
        print ("The program runs!")
        for day in self.days:
            for tool in self.store.inventory.onhand:
                print(tool)
            self.customerFunctions(day)
            self.print_daily(day)
            
            
    def customerFunctions(self, day):
        self.customerReturns(day)
        self.customerRentals(day)

    def customerReturns(self, day):
        returned_tools=[]
        for customer in self.customerList:
            tools = customer.returnTools(day)
            for tool in tools:
                returned_tools.append(tool)
        self.store.inventory.returnTool(returned_tools)

    def customerRentals(self, day):
        for customer in self.customerList:
            payment, tools = customer.requestRental(self.store.inventory.onhand, day)
            self.store.income += payment
            self.store.inventory.rentTool(tools)

    def print_daily(self, day):
        print("DAY:", day)    
        #print("ON HAND:")    
        #print(self.store.inventory.onhand)
        #print("ON LOAN:")
        #print(self.store.inventory.onloan)
        print(self.store.income)
