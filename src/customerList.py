from customer import BusinessCustomer, CasualCustomer, RegularCustomer

class CustomerList:

    def getCustomerList(self):
        return self.list

# -------------------- New UML Methods -------------------
    # Constructor for customer
    def __init__(self):
        self.list = []
        for i in range(3):
            self.list.append(BusinessCustomer("business_{}".format(i)))
            self.list.append((CasualCustomer("casual_{}".format(i))))
            self.list.append((RegularCustomer("regular_{}".format(i))))

        self.list.append(RegularCustomer("regular_4"))

    # go through all customers and create a queue for rentals and a queue for returns
    # This method determines how the rental and return queues are organized (which customers will get to go first)
    def wakeAllCustomers(self):
        return -1

    # All queued customers return tools
    def performReturns(self, today, hardwareStore):
        for customer in self.list:
                tools = customer.returnTools(today)
                hardwareStore.getInventory().returnTool(tools)

    # All queued customers perform rentals
    #def performRentals(self, today, hardwareStore):
        #for customer in self.list:
            #(numTools, numNights) = customer.requestRental(hardwareStore.getInventory().getOnhand(), today)
            # hardwareStore.inventory.rentTool(tools)
            # hardwareStore.createRental(today, customer.name, tools, payment, today, due)