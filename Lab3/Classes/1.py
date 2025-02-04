class StringManipulator:
    def getString(self):
        self.input_string = input("Enter a string: ")
        
    def printString(self):
        print(self.input_string.upper())
        
str_manip = StringManipulator()
str_manip.getString()
str_manip.printString()
