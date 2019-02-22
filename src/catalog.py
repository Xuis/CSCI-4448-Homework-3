"""
Catalog to contain the 20 tool offerings that the store will rent
"""
class Catalog:
    def __init__(self):
        '''
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
        '''


    def rentTool(self, tool):
        # move tool from on hand to rented
        return -1

    def returnTool(self, tool):
        # move tool from rented to on hand
        return -1
