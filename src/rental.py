"""
Since a customer can rent multiple tools at a time, and must return those tools at the same time,
the rental class stores this information

Must store:
1. Information on when rental occured so can return on time
2. Must contain a list of the tools that were rented

1. Price
2. Customer
3. Rental Date
4. Rental Length (Days or nights)
5. List of tools

Take in list of tools and record rental date and must return date
"""

class Rental:
# -------------------- New UML Methods -------------------
    def __init__(self, customer, date, tools, daysRented):
        self.customer = customer
        self.date = date #TODO Get the current Date automatically
        self.tools = tools
        self.days = daysRented

        # Calculate the cost of the rental:
        self.cost = 0
        for tool in tools:
            self.cost += tool.getCostPerDay() * self.days

    def getDueDate(self):
        return self.date + self.days

    def reportString(self):
        # Retuns a "report" of the rental in a string formself.
        # for use in print() statements
        toolsString = ""
        for tool in self.tools:  # formats all the tool names into a string.
            toolsString += (tool.getName()  + " ")
            toolsString = toolsString.rstrip()
        string = self.customer.name + " rented [" + toolsString + "] for " + self.days + " days which totaled to $" +  self.cost
        return string
