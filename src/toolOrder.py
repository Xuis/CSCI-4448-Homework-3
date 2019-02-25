import numpy as np

class ToolOrder:

    def getOrder(type):
        if type == 'business':
            return 3, 7
        if type == 'casual':
            return random.randint(1, 2), random.randint(1, 2)
        if type == 'regular':
            return random.randint(1, 3), random.randint(3, 5)