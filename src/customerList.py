from customer import BusinessCustomer, CasualCustomer, RegularCustomer

class Client:
    def __init__(self):
        self.list = []
        for i in range(3):
            self.list.append(BusinessCustomer("business_{}".format(i)))
            self.list.append((CasualCustomer("casual_{}".format(i))))
            self.list.append((RegularCustomer("regular_{}".format(i))))

        self.list.append(RegularCustomer("regular_4"))

    def getCustomerList(self):
        return self.list

# -------------------- New UML Methods -------------------

    # go through all customers and create a queue for rentals and a queue for returns
    def wakeAllCustomers(self):
        return -1

    # All queued customers return tools
    def performReturns(self):
        return -1

    # All queued customers perform rentals
    def performRental(self):
        return -1