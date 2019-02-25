# =============================================================================
# There are 20 tools in 5 Categories: Paining, Concrete, Plumbing, Woodwork
# Yardwork each with unique names and pricePerDay by category
# Tools are in Store.Catalog
# Tools are rented by Customers
# =============================================================================


class Tool:
    CPD_PAINT = 2
    CPD_CONCRETE = 10
    CPD_PLUMBING = 5
    CPD_WOODWORK = 3
    CPD_YARDWORK = 4

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

    def getCurrentRenter(self):
        return -1

    def getDayRented(self):
        return self.dayRented

    def getcostPerDay(self):
        return self.costPerDay



class PaintingTool(Tool):
    def __init__(self, name):
        self.name = name
        self.rented = False
        self.costPerDay = self.CPD_PAINT
        self.dayRented = 0
        self.dayDue = 0
        
class ConcreteTool(Tool):
    def __init__(self, name):
        self.name = name
        self.rented = False
        self.costPerDay = self.CPD_CONCRETE
        self.dayRented = 0
        self.dayDue = 0


class PlumbingTool(Tool):
    def __init__(self, name):
        self.name = name
        self.rented = False
        self.costPerDay = self.CPD_PLUMBING
        self.dayRented = 0
        self.dayDue = 0


class WoodWorkTool(Tool):
    def __init__(self, name):
        self.name = name
        self.rented = False
        self.costPerDay = self.CPD_WOODWORK
        self.dayRented = 0
        self.dayDue = 0


class YardWorkTool(Tool):
    def __init__(self, name):
        self.name = name
        self.rented = False
        self.costPerDay = self.CPD_YARDWORK
        self.dayRented = 0
        self.dayDue = 0
