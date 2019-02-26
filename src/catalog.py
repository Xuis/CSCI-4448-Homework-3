"""
Catalog to contain the 20 tool offerings that the store will rent
"""

from tool import ToolFactory

class Catalog:
    def __init__(self):
        self.onhand = []
        self.create_catalog()
        self.onloan = []

    def create_catalog(self):
        for i in range(4):
            self.onhand.append(ToolFactory.create_tool("concrete_{}".format(i)))
            self.onhand.append(ToolFactory.create_tool("painting_{}".format(i)))
            self.onhand.append(ToolFactory.create_tool("plumbing_{}".format(i)))
            self.onhand.append(ToolFactory.create_tool("woodwoork_{}".format(i)))
            self.onhand.append(ToolFactory.create_tool("yardwork_{}".format(i)))
        return self.onhand

    def getToolCost(self, tool):
        return tool.getCostPerDay()

    def getToolAvail(self, tool):
        return tool.isRented()

    def getOnhand(self):
        return self.onhand
    def rentTool(self, tools):
        # move tool from on hand to rented
        for tool in tools:
            self.onhand.remove(tool)
            self.onloan.append(tool)
    def returnTool(self, tools):
        for tool in tools:
            self.onloan.remove(tool)
            self.onhand.append(tool)



