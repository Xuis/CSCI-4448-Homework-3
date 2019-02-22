# =============================================================================
# There are 20 tools in 5 Categories: Paining, Concrete, Plumbing, Woodwork
# Yardwork each with unique names and pricePerDay by category
# Tools are in Store.Catalog
# Tools are rented by Customers
# =============================================================================


class Tool:
    def __init__(self):
        self.name = "Unknown Tool"
        self.daysTillReturn = 0

class PaintingTool(Tool):

    def __init__(self, tool_name):
        self.name = tool_name
        self.pricePerDay = 1.0

class ConcreteTool(Tool):
    def __init__(self, tool_name):
        self.name = tool_name
        self.pricePerDay = 3.0


class PlumbingTool(Tool):
    def __init__(self, tool_name):
        self.name = tool_name
        self.pricePerDay = 2.0


class WoodworkTool(Tool):
    def __init__(self, tool_name):
        self.name = tool_name
        self.pricePerDay = 2.0

class YardworkTool(Tool):
    def __init__(self, tool_name):
        self.name = tool_name
        self.pricePerDay = 1.0