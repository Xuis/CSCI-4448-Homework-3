# =============================================================================
# This is for the store to record a history of rentals.
# Needs (per prompt):
# 1. Price
# 2. Customer
# 4. List of tools
# =============================================================================

class RentalRecord:
# -------------------- New UML Methods -------------------
    def __init__(self):
        self.rentalList = []
        self.unfinishedRentals = []

    def addRental(self, rentalRecord):
        self.rentalList.append(rentalRecord)
        return

    def getAllRentals(self):
        #returns a list of all the recorded rentals
        # Including finished and unfinished
        return self.rentalList

    # Not sure we need this or if this is the right place.
    #Regarding above comment, could this maybe go in Store?
    def getCurrentRentals(self):
        # returns a list of currently unfinished rentals
        # Not sure if needed.
        for rentalRecord in self.rentalList:
            if rentalRecord.complete == False:
                self.unfinishedRentals.append(rentalRecord)
                
        return self.unfinishedRentals
