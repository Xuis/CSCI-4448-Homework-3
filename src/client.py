from customer import BusinessCustomer, CasualCustomer, RegularCustomer

class Client:
    def __init__(self):
        self.list = []
        for i in range(3):
            self.list.append(BusinessCustomer("business_{}".format(i)))
            self.list.append((CasualCustomer("casual_{}".format(i))))
            self.list.append((RegularCustomer("regular_{}".format(i))))

        self.list.append(RegularCustomer("regular_4"))