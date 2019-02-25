"""
Catalog to contain the 20 tool offerings that the store will rent
"""

from src.tool import ConcreteTool, PaintingTool, PlumbingTool, WoodWorkTool, YardWorkTool
from src.customer import BusinessCustomer, CasualCustomer, RegularCustomer

class Catalog:
    def __init__(self):

        self.onhand = self.create_catalog
        self.onloan = []


        for i in range(4):
            self.onhand.append(ConcreteTool("concrete_{}".format(i)))
            self.onhand.append(PaintingTool("painting_{}".format(i)))
            self.onhand.append(PlumbingTool("plumbing_{}".format(i)))
            self.onhand.append(WoodWorkTool("woodwoork_{}".format(i)))
            self.onhand.append(YardWorkTool("yardwork_{}".format(i)))


    def rentTool(self, tool):
        # move tool from on hand to rented
        del self.onhand[tool]
        self.onloan.append(tool)

    def returnTool(self, tool):
        del self.onloan[tool]
        self.onhand.append(tool)


 ''' Client list will contain all store client information '''
class Client:
    def __init__(self):
        self.list = []
        for i in range(3):
            self.list.append(BusinessCustomer("business_{}".format(i)))
            self.list.append((CasualCustomer("casual_{}".format(i))))
            self.list.append((RegularCustomer("regular_{}".format(i))))

        self.list.append(RegularCustomer("regular_4"))
