#
# This class will handle the days in the simulation 
#

class StoreDate:
    # World duration will be the duration of the simulation
	def __init__(self):
		self.todayInd = 0
        self.worldDuration = 35
    
    def __init__(self, worldDuration):
		self.todayInd = 0
        self.worldDuration = worldDuration

    def getDay(self):
        return todayInd