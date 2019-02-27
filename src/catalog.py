# =============================================================================
# Catalog to contain the 20 tool offerings that the store will offer
# =============================================================================

from tool import ToolFactory

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
            self.onhand.append(ToolFactory.create_tool("concrete_{}".format(i)))
            self.onhand.append(ToolFactory.create_tool("painting_{}".format(i)))
            self.onhand.append(ToolFactory.create_tool("plumbing_{}".format(i)))
            self.onhand.append(ToolFactory.create_tool("woodwoork_{}".format(i)))
            self.onhand.append(ToolFactory.create_tool("yardwork_{}".format(i)))

    def rentTool(self, tools):
        # move tool from on hand to on loan
        for tool in tools:
            self.onhand.remove(tool)
            self.onloan.append(tool)

    def returnTool(self, tools):
        # move tool from on loan to on hand
        for tool in tools:
            self.onloan.remove(tool)
            self.onhand.append(tool)

