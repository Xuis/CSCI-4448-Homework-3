from customer import BusinessCustomer, CasualCustomer, RegularCustomer

class CustomerList:

    def getCustomerList(self):
        return self.list

# -------------------- New UML Methods -------------------
    def __init__(self):
        self.list = []
        for i in range(3):
            self.list.append(BusinessCustomer("business_{}".format(i)))
            self.list.append((CasualCustomer("casual_{}".format(i))))
            self.list.append((RegularCustomer("regular_{}".format(i))))

        self.list.append(RegularCustomer("regular_4"))

    # go through all customers and create a queue for rentals and a queue for returns
    def wakeAllCustomers(self):
        return -1

    # All queued customers return tools
    def performReturns(self, today, hardwareStore):
        for customer in self.list:
                tools = customer.returnTools(today)
                hardwareStore.getInventory().returnTool(tools)
        return -1

    # All queued customers perform rentals
    def performRentals(self, today, hardwareStore):
        for customer in self.list:
                shopping = customer.shop_today()
                if shopping:
                    payment, tools, due = customer.rentTool(hardwareStore.inventory.onhand, today)
                    hardwareStore.inventory.rentTool(tools)
                    hardwareStore.createRental(today, customer.name, tools, payment, today, due)

        return -1