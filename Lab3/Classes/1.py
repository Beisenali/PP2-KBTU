class StringManipulator:
    def getString(self):
        self.iss = input("Enter a string: ")
        
    def printString(self):
        print(self.iss.upper())
        
str_manip = StringManipulator()
str_manip.getString()
str_manip.printString()
