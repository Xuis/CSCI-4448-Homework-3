
class Simulator:
    def __init__(self, store):
        self.store = store
        self.days = []
        
    def setNumDaysToRun(self, numDaysToRun):
        self.days = [i for i in range(numDaysToRun)]
# -------------------- New UML Methods -------------------
    def startSimulation(self, store):
        print ("The program runs!")
        for day in self.days:
            store.open(day)

        
        
        print(store.getRentals())