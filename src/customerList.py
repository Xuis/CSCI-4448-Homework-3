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

    
    
    def getCustomerList(self):
        return self.list

