"""
Catalog to contain the 20 tool offerings that the store will rent
"""

from tool import ConcreteTool, PaintingTool, PlumbingTool, WoodWorkTool, YardWorkTool
from customer import BusinessCustomer, CasualCustomer, RegularCustomer

class Catalog:
    def __init__(self):

        self.onhand = []
        self.onloan = []

    def create_catalog(self):
        for i in range(4):
            self.onhand.append(ConcreteTool("concrete_{}".format(i)))
            self.onhand.append(PaintingTool("painting_{}".format(i)))
            self.onhand.append(PlumbingTool("plumbing_{}".format(i)))
            self.onhand.append(WoodWorkTool("woodwoork_{}".format(i)))
            self.onhand.append(YardWorkTool("yardwork_{}".format(i)))
        return self.onhand


    def rentTool(self, tool):
        # move tool from on hand to rented
        del self.onhand[tool]
        self.onloan.append(tool)

    def returnTool(self, tools):
        for tool in tools:
            del self.onloan[tool]
            self.onhand.append(tool)


