#
# This class will handle the days in the simulation 
#

class StoreDate:
    # World duration will be the duration of the simulation
    def __init__(self):
        self.todayInd = 1
        self.worldDuration = 35

# -------------------- New UML Methods -------------------

    def getDay(self):
        return todayInd

    def simulateDay(self):
        currDay = self.todayInd
        if currDay > self.worldDuration:
            return -1
        self.todayInd += 1
        return currDay