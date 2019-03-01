# =============================================================================
# Customer list holds a list of customers. Clever eh?
# at instantiation the class calls CustomerFactory to fill a list of customers 
# all customers have unique names, and are of 1 of 3 types.
# =============================================================================
from Customer import CustomerFactory

class CustomerList:

    def __init__(self):
        self.__list = self.create_list()

    def create_list(self):
        temp = []
        for i in range(3):
            temp.append(CustomerFactory.create_customer("business_{}".format(i)))
            temp.append(CustomerFactory.create_customer("casual_{}".format(i)))
            temp.append(CustomerFactory.create_customer("regular_{}".format(i)))

        temp.append(CustomerFactory.create_customer("regular_3"))
        return temp
   
    def getCustomerList(self):
        return self.__list

