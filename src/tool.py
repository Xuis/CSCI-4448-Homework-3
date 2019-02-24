# =============================================================================
# There are 20 tools in 5 Categories: Paining, Concrete, Plumbing, Woodwork
# Yardwork each with unique names and pricePerDay by category
# Tools are in Store.Catalog
# Tools are rented by Customers
# =============================================================================


class Tool:
    def __init__(self, name):
        self.name = name
        self.rented = False
        self.costPerDay = 0
        self.dayRented = 0
        self.dayDue = 0        
        
    def rentTool(self):
        return self.rented = True;
        
    def getName(self):
        return self.name;
        
    def getCostPerDay(self):
        return self.costPerDay;
        
    def setCostPerDay(self, newCost):
        self.costPerDay = newCost;
        
    def isRented(self):
        return self.rented;

class PaintingTool(Tool):
	def __init__(self, name)
		Tool.__init__(self, name)
		self.rented = False
		self.costPerDay = 2
		
			
class ConcreteTool(Tool):
	def __init__(self, name):
		Tool.__init__(self, name)
		self.rented = False
		self.costPerDay = 10
		
class PlumbingTool(Tool):
	def __init__(self, name):
		Tool.__init__(self, name)
		self.rented = False
		self.costPerDay = 5

class WoodWorkTool(Tool):
	def __init__(self, name):
		Tool.__init__(self, name)
		self.rented = False
		self.costPerDay = 3
		
class YardWorkTool(Tool):
	def __init__(self, name):
		Tool.__init__(self, name)
		self.rented = False
		self.costPerDay = 4
		