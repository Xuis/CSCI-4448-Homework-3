# =============================================================================
# Store "has-a" Catalog
# Store "has-a" Customer 
# Store tracks Rentals (invoices) and Inventory
# =============================================================================

from tool import Tool, ConcreteTool, PaintingTool, PlumbingTool, WoodworkTool, YardworkTool
from customer import Customer

class Store:
    def __init__(self):
        self.name = "Tools 'r' Us"
        self.Ledger = []
        self.Income = 0.00
        self.catalog = Catalog()
        self.customers = {'business': [Customer("business_{}".format(i)) for i in range(4)],
                          'regular': [Customer("regular_{}".format(i)) for i in range(3)],
                          'casual': [Customer("casual_{}".format(i))for i in range(3)]}

    def open(self):
        # go through customers, see if they are renting
        return -1

    def close(self):
        return -1


class Catalog:
    def __init__(self):
        self.onhand = {'concrete': [Tool("concrete_{}".format(i)) for i in range(4)],
                       'painting': [Tool("painting_{}".format(i)) for i in range(4)],
                       'plumbing': [Tool("plumbing_{}".format(i)) for i in range(4)],
                       'woodwork': [Tool("woodwoork_{}".format(i)) for i in range(4)],
                       'yardwork': [Tool("yardwork_{}".format(i)) for i in range(4)]
                   }
        self.onloan = {"concrete": [],
                       "painting": [],
                       "plumbing": [],
                       "woodwork": [],
                       "yardword": []
                   }
        return None

    def rentTool(self, tool):
        # move tool from on hand to rented
        return -1

    def returnTool(self, tool):
        # move tool from rented to on hand
        return -1
