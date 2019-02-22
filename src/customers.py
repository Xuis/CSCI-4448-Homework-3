# =============================================================================
# There are 10 customers in 3 categories each with a unique name
# Customers can rent a max of 3 tools for 7 nights
# Business customers always rent 3 tools for 7 nights
# Casual customers rent 1-2 tools for 1-2 nights
# Regular customers rent 1-3 tools for 3-5 nights
# Customers interact with Store through renting and returning of tools and 
# paying for the tools.
# =============================================================================
import random

class Customer:
    def __init__(self, _name):
        self.name = _name
        self.toolbox = []
        self.type = None

    def get_tool_order(self):
        return ToolOrder.getOrder(self.type)

    #self.toolbox[] should be list of Tool objects that have attributes
    #tool.returnDate and tool.name etc or something
    def rentTool(self, store_catalog, store_inventory):
        #takes in catalog, randomly picks from catalog.list
        #randomly chooses numDays
        tools, days = self.get_tool_order()

    def payStore(self):
        
        #send numNights * pricePerTool for tool in list
        #to Store.Income?

    def updateToolBox(self):
        for tool in self.toolbox:
            tool.days -= 1
            if tool.days == 0:
                self.returnTool(tool)

    def returnTool(self):
        # return tool


class CasualCustomer(Customer):
    def __init__(self, _name):
        self.name = _name
        self.toolbox = []
        self.type = 'casual'
        
class BusinessCustomer(Customer):
    def __init__(self, _name):
        self.name = _name
        self.toolbox = []
        self.type = 'business'
    def inventoryCheck(self):
        # check to see if store inventory >=3 before ordering

class RegularCustomer(Customer):
    def __init__(self, _name):
        self.name = _name
        self.toolbox = []
        self.type = 'regular'

class ToolOrder:

    def getOrder(type):
        if type == 'business':
            return 3, 7
        if type == 'casual':
            return random.randint(1,2), random.randint(1,2)
        if type == 'regular':
            return random.randint(1,3), random.randint(3,5)