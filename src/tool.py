# =============================================================================
# There are 20 tools in 5 Categories: Paining, Concrete, Plumbing, Woodwork
# Yardwork each with unique names and pricePerDay by category
# Tools are in Store.Catalog
# Tools are rented by Customers
# =============================================================================
from enum import Enum

class Tool:
    # Tool is the super class for all tools, it holds all base attributes and methods 
    def __init__(self, name):
        self.name = name
        self.rented = False
        self.costPerDay = 0
        self.dayRented = 0
        self.dayDue = 0

        
    def getCostPerDay(self):
        return self.costPerDay


class PaintingTool(Tool):
    def __init__(self,name):
        super().__init__(name)
        self.costPerDay = ToolCost.PAINT.value


class ConcreteTool(Tool):
    def __init__(self, name):
        super().__init__(name)
        self.costPerDay = ToolCost.CONCRETE.value


class PlumbingTool(Tool):
    def __init__(self, name):
        super().__init__(name)
        self.costPerDay = ToolCost.PLUMBING.value


class WoodWorkTool(Tool):
    def __init__(self, name):
        super().__init__(name)
        self.costPerDay = ToolCost.WOODWORK.value


class YardWorkTool(Tool):
    def __init__(self, name):
        super().__init__(name)
        self.costPerDay = ToolCost.YARDWORK.value

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

class ToolCost(Enum):
    PAINT = 2
    CONCRETE = 10
    PLUMBING = 5
    WOODWORK = 3
    YARDWORK = 4

