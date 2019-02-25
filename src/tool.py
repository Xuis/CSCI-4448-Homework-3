# =============================================================================
# There are 20 tools in 5 Categories: Paining, Concrete, Plumbing, Woodwork
# Yardwork each with unique names and pricePerDay by category
# Tools are in Store.Catalog
# Tools are rented by Customers
# =============================================================================


class Tool:
    def rentTool(self):
        self.rented = True
        
    def getName(self):
        return self.name
        
    def getCostPerDay(self):
        return self.costPerDay

    def isRented(self):
        return self.rented
# -------------------- New UML Methods -------------------
    def __init__(self, name):
        self.name = name
        self.rented = False
        self.costPerDay = 0
        self.dayRented = 0
        self.dayDue = 0
        self.costPerDay = 0

    def getCurrentRenter(self):
        return -1


class PaintingTool(Tool):
     def setCostPerDay(self):
         self.costPerDay= CostPerDay.paint


class ConcreteTool(Tool):
	def setCostPerDay(self):
		self.costPerDay = CostPerDay.concrete


class PlumbingTool(Tool):
	def setCostPerDay(self):
		self.costPerDay = CostPerDay.plumbing


class WoodWorkTool(Tool):
	def setCostPerDay(self):
		self.costPerDay = CostPerDay.woodwork


class YardWorkTool(Tool):
	def setCostPerDay(self):
		self.costPerDay = CostPerDay.yardwork


class CostPerDay:
	paint = 2
	concrete = 10
	plumbing = 5
	woodwork = 3
	yardwork = 4
