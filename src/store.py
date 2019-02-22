# =============================================================================
# Store "has-a" Catalog
# Store "has-a" Customer 
# Store tracks Rentals (invoices) and Inventory
# =============================================================================

# from src.tool import Tool, ConcreteTool, PaintingTool, PlumbingTool, WoodworkTool, YardworkTool
# from src.customer import Customer
# from src.catalog import Catalog
class Store:
    def __init__(self):
        '''
        self.name = "Tools 'r' Us"
        self.Ledger = []
        self.Income = 0.00
        self.catalog = Catalog()
        self.customers = {'business': [Customer("business_{}".format(i)) for i in range(4)],
                          'regular': [Customer("regular_{}".format(i)) for i in range(3)],
                          'casual': [Customer("casual_{}".format(i))for i in range(3)]}
        '''

    def open(self):
        # go through customers, see if they are renting
        return -1

    def close(self):
        return -1