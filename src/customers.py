# =============================================================================
# There are 10 customers in 3 categories each with a unique name
# Customers can rent a max of 3 tools for 7 nights
# Business customers always rent 3 tools for 7 nights
# Casual customers rent 1-2 tools for 1-2 nights
# Regular customers rent 1-3 tools for 3-5 nights
# Customers interact with Store through renting and returning of tools and 
# paying for the tools.
# =============================================================================


class Customers:
    def __init__(self, _name, _numToolsDesired):
        self.name = name
        self.numToolsDesired = numToolsDesired
        self.tools = []
        self.maxTools = 3
        self.maxNights = 7
    
    #self.tools[] should be list of Tool objects that have attributes
    #tool.returnDate and tool.name etc or something
    def rentTool(self, Store.Catalog, Store.Inventory):
        
        #takes in catalog, randomly picks from catalog.list
        #randomly chooses numDays
        
        return self.tools[]
    
    def returnTool(self, self.tools[]):
        
        return self.tools[]
    
    def payStore(self.tools[]):
        
        #send numNights * pricePerTool for tool in list
        #to Store.Income?
    
class CasualCustomer(Customer):
    
        def __init__(self, _name, _numToolsDesired):
        self.name = name
        self.numToolsDesired = numToolsDesired
        self.tools = []       
        self.maxTools = 2
        self.maxNights = 2
        
        
class BusinessCustomer(Customer):
    
    def __init__(self, name, numToolsDesired):
        self._name = name
        self._numToolsDesired = numToolsDesired
        self._tools = []
        
    
        
        
class RegularCustomer(Customer):
    def __init__(self, name, numToolsDesired):
        self._name = name
        self._numToolsDesired = numToolsDesired
        self._tools = []
        self.maxTools = 3
        self.maxNights = 5