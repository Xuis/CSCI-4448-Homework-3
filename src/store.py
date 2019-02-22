# =============================================================================
# Store "has-a" Catalog
# Store "has-a" Customer 
# Store tracks Rentals (invoices) and Inventory
# =============================================================================
from src.tools import Tools
from src.customers import Customer

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
    def close(self):


class Catalog:
    def __init__(self):
        self.onhand = {'concrete': [Tools("concrete_{}".format(i)) for i in range(4)],
                       'painting': [Tools("painting_{}".format(i)) for i in range(4)],
                       'plumbing': [Tools("plumbing_{}".format(i)) for i in range(4)],
                       'woodwork': [Tools("woodwoork_{}".format(i)) for i in range(4)],
                       'yardwork': [Tools("yardwork_{}".format(i)) for i in range(4)]
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
