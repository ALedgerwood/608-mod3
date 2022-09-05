# python object representing a purchase for a given amount

class Purchase(object):

    def __init__(self, amount):
        self.amount = amount

    def calculateTax(self, taxPercent):
        return self.amount * taxPercent/100
    
    def calculateTip(self, tipPercent):
        return self.amount * tipPercent/100
    
    def calculateTotal(self, taxPercent, tipPercent):
        return self.amount * (1 + taxPercent/100 + tipPercent/100)

# amount of purchase object
purchase = Purchase(100)

# tax and tip percentages
taxPercent = 7.5
tipPercent = 20

# calculate the tax and tip amounts
tax = purchase.calculateTax(taxPercent)
tip = purchase.calculateTip(tipPercent)

# display results
print('Tax', tax)
print('Tip', tip)
print('Total', purchase.calculateTotal(taxPercent, tipPercent))
