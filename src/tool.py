# =============================================================================
# There are 20 tools in 5 Categories: Paining, Concrete, Plumbing, Woodwork
# Yardwork each with unique names and pricePerDay by category
# Tools are in Store.Catalog
# Tools are rented by Customers
# =============================================================================


class Tool:

    def __init__(self, name):
        self.CPD_PAINT = 2
        self.CPD_CONCRETE = 10
        self.CPD_PLUMBING = 5
        self.CPD_WOODWORK = 3
        self.CPD_YARDWORK = 4
        self.name = name
        self.rented = False
        self.costPerDay = 0
        self.dayRented = 0
        self.dayDue = 0

    def getDayRented(self):
        return self.dayRented

    def getcostPerDay(self):
        return self.costPerDay

    def rentTool(self):
        self.rented = True

    def setRented(self, isRented):
        self.rented = isRented
        
    def getName(self):
        return self.name
        
    def getCostPerDay(self):
        return self.costPerDay

    def isRented(self):
        return self.rented



class PaintingTool(Tool):
    def __init__(self,name):
        super().__init__(name)
        self.costPerDay = self.CPD_PAINT


class ConcreteTool(Tool):
    def __init__(self, name):
        super().__init__(name)
        self.costPerDay = self.CPD_CONCRETE


class PlumbingTool(Tool):
    def __init__(self, name):
        super().__init__(name)
        self.costPerDay = self.CPD_PLUMBING


class WoodWorkTool(Tool):
    def __init__(self, name):
        super().__init__(name)
        self.costPerDay = self.CPD_WOODWORK


class YardWorkTool(Tool):
    def __init__(self, name):
        super().__init__(name)
        self.costPerDay = self.CPD_YARDWORK

class ToolFactory:
    def create_tool(name):
        if 'paint' in name:
            return PaintingTool(name)
        elif 'concrete' in name:
            return ConcreteTool(name)
        elif 'plumbing' in name:
            return PlumbingTool(name)
        elif 'wood' in name:
            return WoodWorkTool(name)
        else:
            return YardWorkTool(name)




