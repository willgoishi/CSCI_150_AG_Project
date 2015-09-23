#Inventory Class
class Inventory:
    def __init__(self, name):
        self.name = name


        # Set default values
        self.price         = None
        self.quantity      = None
        self.purchaseDate  = None
        self.purchaseDay   = None
        self.purchaseMonth = None
        self.purchaseYear  = None
        self.firstUse      = None
        self.lastUse       = None
        self.itemType      = None

    def itemQuantity(self, totalQuantity):
        self.totalQuantity = totalQuantity + self.quantity

    #Print functions
    def printName(self):
        print ("This item is %s.") % (self.name)

    def printPriceAndQuantity(self):
        print ("%s costs $%d for %d pounds.") % (self.name, self.price, self.quantity)

    def printQuantity(self):
        print ("%s's quantity is %d pounds.") % (self.name, self.totalQuantity)

    def printPurcahseDate(self):
        print ("The purchase date for %s was %s") % (self.name, self.purchaseDate)

    def printFirstUse(self):
        print ("%s's was first used on %s") % (self.name, self.firstUSe)

    def printLastUse(self):
        print ("%s's was last used on %s") % (self.name, self.lastUse)


