# =============================================================================
# There are 20 tools in 5 Categories: Paining, Concrete, Plumbing, Woodwork
# Yardwork each with unique names and pricePerDay by category
# Tools are in Store.Catalog
# Tools are rented by Customers
# =============================================================================


class Tools:
    def __init__(self, tool_name):
        self.name = tool_name
        self.pricePerDay = 0.0
        
        
class PaintingTool(Tools):
    
    def __init__(self, tool_name):
        self.name = tool_name
        self.pricePerDay = 1.0
        
class ConcreteTool(Tools):
    def __init__(self, tool_name):
        self.name = tool_name
        self.pricePerDay = 3.0
        
        
class PlumbingTool(Tools):
    def __init__(self, tool_name):
        self.name = tool_name
        self.pricePerDay = 2.0
        
        
class WoodworkTool(Tools):
    def __init__(self, tool_name):
        self.name = tool_name
        self.pricePerDay = 2.0
        
class YardworkTool(Tools):
    def __init__(self, tool_name):
        self.name = tool_name
        self.pricePerDay = 1.0