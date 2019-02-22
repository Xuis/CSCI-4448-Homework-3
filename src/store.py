# =============================================================================
# Store "has-a" Catalog
# Store "has-a" Customer 
# Store tracks Rentals (invoices) and Inventory
# =============================================================================
from src.tools import ConcreteTool, PaintingTool, PlumbingTool, WoodworkTool, YardworkTool

class Store:
    def __init__(self):
        self.name = "Tools 'r' Us"
        self.Ledger = []
        self.Income = 0.00
        self.catalog = Catalog()


class Catalog:
    def __init__(self):
        self.onhand = {'concrete': [ConcreteTool("concrete_{}".format(i)) for i in range(4)],
                       'painting': [PaintingTool("painting_{}".format(i)) for i in range(4)],
                       'plumbing': [PlumbingTool("plumbing_{}".format(i)) for i in range(4)],
                       'woodwork': [WoodworkTool("woodwoork_{}".format(i)) for i in range(4)],
                       'yardwork': [YardworkTool("yardwork_{}".format(i)) for i in range(4)]
                   }
        self.onloan = {"concrete": [],
                       "painting": [],
                       "plumbing": [],
                       "woodwork": [],
                       "yardword": []}

    def rentTool(self, tool):
        # move tool from on hand to rented

    def returnTool(self, tool):
        # move tool from rented to on hand
