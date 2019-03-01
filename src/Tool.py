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
        self._name = name
        self._costPerDay = 0
        self._dayDue = 0

        
    def getCostPerDay(self):
        return self._costPerDay

    def getName(self):
        return self._name


# below are all the tool subclasses. 
# They initialize with Tool __init__ then get their cost per day values from the ToolCost class
class PaintingTool(Tool):
    def __init__(self,name):
        super().__init__(name)
        self._costPerDay = ToolCost.PAINT.value


class ConcreteTool(Tool):
    def __init__(self, name):
        super().__init__(name)
        self._costPerDay = ToolCost.CONCRETE.value


class PlumbingTool(Tool):
    def __init__(self, name):
        super().__init__(name)
        self._costPerDay = ToolCost.PLUMBING.value


class WoodWorkTool(Tool):
    def __init__(self, name):
        super().__init__(name)
        self._costPerDay = ToolCost.WOODWORK.value


class YardWorkTool(Tool):
    def __init__(self, name):
        super().__init__(name)
        self._costPerDay = ToolCost.YARDWORK.value

class ItemFactory:
    # Tool factory is called by the catalog to instantiate tools of varying types 
    # by passing in their names. The factory uses the names to determine which type
    # of tool needs to be created.
    def create_item(name):
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
    # ToolCost encapsulates the varying costs of tools. 
    # The individual tools __init__ with a call to retieve their cost.
    PAINT = 2
    CONCRETE = 10
    PLUMBING = 5
    WOODWORK = 3
    YARDWORK = 4

