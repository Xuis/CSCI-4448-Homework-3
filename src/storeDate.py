#
# This class will handle the days in the simulation 
#

class StoreDate:
    # World duration will be the duration of the simulation
# -------------------- New UML Methods -------------------
    def __init__(self):
        self.todayInd = 1
        self.worldDuration = 35

    # Return the current day index
    def getDay(self):
        return todayInd

    # simulate one day (increment day)
    # ?? Should we actually perform the day simulation here?
    def simulateDay(self):
        currDay = self.todayInd
        if currDay > self.worldDuration:
            return -1
        self.todayInd += 1
        return currDay