class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        # Using formatted strings (f-strings) for clean output
        print(f"{self.real}i + {self.img}j")

    def __add__(self,num2): #dunder function
        #It allows you to use + directly between two objects of class Complex.
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)

    def __sub__(self,num2): #dunder function
        # #It allows you to use + directly between two objects of class Complex.
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal,newImg)


num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 6)
num2.showNumber()

print("-"*8)
num3 = num1 + num2 #this will work now because of dunder function
# num3 = num1.__add__(num2) #is translated as
# num3 = num1.add(num2)
num3.showNumber()

num4 = num1 - num2
num4.showNumber()
