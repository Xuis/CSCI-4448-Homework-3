# =============================================================================
# Catalog to contain the 20 tool offerings that the store will offer
# =============================================================================

from tool import ItemFactory

class Catalog:
    # Catalog is the effective inventory for the store. I keeps track of all tools
    # and is called to move tools from on hand to on loan or vice versa
    def __init__(self):
        self.onhand = []
        self.create_catalog()
        self.onloan = []

    def create_catalog(self):
        # called at instantiation of the catalog to fill inventory with 20 tools 
        # of varying types
        for i in range(4):
            self.onhand.append(ItemFactory.create_item("concrete_{}".format(i)))
            self.onhand.append(ItemFactory.create_item("painting_{}".format(i)))
            self.onhand.append(ItemFactory.create_item("plumbing_{}".format(i)))
            self.onhand.append(ItemFactory.create_item("woodwoork_{}".format(i)))
            self.onhand.append(ItemFactory.create_item("yardwork_{}".format(i)))

    def rentItem(self, items):
        # move tool from on hand to on loan
        for item in items:
            self.onhand.remove(item)
            self.onloan.append(item)

    def returnItem(self, items):
        # move tool from on loan to on hand
        for item in items:
            self.onloan.remove(item)
            self.onhand.append(item)

