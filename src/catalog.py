"""
Catalog to contain the 20 tool offerings that the store will rent
"""

from tool import ConcreteTool, PaintingTool, PlumbingTool, WoodWorkTool, YardWorkTool

class Catalog:
    def create_catalog(self):
        for i in range(4):
            self.onhand.append(ConcreteTool("concrete_{}".format(i)))
            self.onhand.append(PaintingTool("painting_{}".format(i)))
            self.onhand.append(PlumbingTool("plumbing_{}".format(i)))
            self.onhand.append(WoodWorkTool("woodwoork_{}".format(i)))
            self.onhand.append(YardWorkTool("yardwork_{}".format(i)))
        return self.onhand


    def rentTool(self, tools):
        # move tool from on hand to rented
        for tool in tools:
            for i in range(len(self.onhand)-1):
                if tool.name == self.onhand[i].name:
                    self.onhand.pop(i)
                    break
            self.onloan.append(tool)

    def returnTool(self, tools):
        for tool in tools:
            for i in range(len(self.onloan)-1):
                if tool.name == self.onloan[i].name:
                    self.onloan.pop(i)
                    break
            self.onhand.append(tool)


# -------------------- New UML Methods -------------------
    def __init__(self):
        self.onhand = []
        self.create_catalog()
        self.onloan = []

    def getToolCost(self):
        return -1

    def getToolAvail(self):
        return -1