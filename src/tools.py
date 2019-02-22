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

    def returnTool(self):
        

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
