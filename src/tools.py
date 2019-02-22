# =============================================================================
# There are 20 tools in 5 Categories: Paining, Concrete, Plumbing, Woodwork
# Yardwork each with unique names and pricePerDay by category
# Tools are in Store.Catalog
# Tools are rented by Customers
# =============================================================================


class Tools:
    def __init__(self, tool_name):
        self.name = tool_name
        self.daysTillReturn = 0
        self.pricePerDay = SetToolPrice.getPrice(self.name)
        return 1

    def returnTool(self):
        return -1
        

class SetToolPrice:

    def getPrice(tool):
        if 'concrete' in tool:
            return 3.0
        if "painting" in tool:
            return 1.0
        if "plumbing" in tool:
            return 2.0
        if "woodwork" in tool:
            return 2.0
        if "yardwork" in tool:
            return 3.0

class ConcreteTool(Tool):

    def returnTool(self):
        return -1

class PaintingTool(Tool):

    def returnTool(self):
        return -1

class PlumbingTool(Tool):

    def returnTool(self):
        return -1


class WoodworkTool(Tool):

    def returnTool(self):
        return -1


class YardworkTool(Tool):

    def returnTool(self):
        return -1