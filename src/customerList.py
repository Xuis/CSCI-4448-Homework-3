from customer import CustomerFactory

class CustomerList:

    # Constructor for customer
    def __init__(self):
        self.list = self.create_list()

    def create_list(self):
        temp = []
        for i in range(3):
            temp.append(CustomerFactory.create_customer("business_{}".format(i)))
            temp.append(CustomerFactory.create_customer("casual_{}".format(i)))
            temp.append(CustomerFactory.create_customer("regular_{}".format(i)))

        temp.append(CustomerFactory.create_customer("regular_3"))
        return temp

    # go through all customers and create a queue for rentals and a queue for returns
    # This method determines how the rental and return queues are organized (which customers will get to go first)
    def wakeAllCustomers(self):
        return -1
    
    def getCustomerList(self):
        return self.list


    # All queued customers return tools
    def performReturns(self, today, hardwareStore):
        for customer in self.list:
                tools = customer.returnTools(today)
                hardwareStore.getInventory().returnTool(tools)

    # All queued customers perform rentals
    def performRentals(self, today, hardwareStore):
        for customer in self.list:
            (numTools, numNights) = customer.requestRental(hardwareStore.getInventory().getOnhand(), today)
            hardwareStore.inventory.rentTool(tools)
            hardwareStore.createRental(today, customer.name, tools, payment, today, due)
