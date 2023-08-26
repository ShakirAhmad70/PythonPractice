class Calc:
    def __init__(self, a=0 ,b=0):
        self.a = a
        self.b = b
    
    def takeTwoInputs(self):
        try:
            self.a = float(input("Enter first number: "))
            self.b = float(input("Enter Second number: "))
        except ValueError:
            print("⚠️ You have entered a wrong input, please provide valid input..!!")
            self.takeTwoInputs()

    def takeSingleInput(self):
        try:
            self.a = float(input("Enter the number: "))
        except ValueError:
            print("⚠️ You have entered a wrong input, please provide valid input..!!")\
        
    def add(self):
        self.takeTwoInputs()
        print("Sum is:", self.a + self.b)
        input("Press Enter key to continue..")
        
    def sub(self):
        self.takeTwoInputs()
        print("Subtraction is:", self.a - self.b)
        input("Press Enter key to continue..")
        
    def diff(self):
        self.takeTwoInputs()
        diff = (self.a - self.b) if (self.a >= self.b) else (self.b - self.a)
        print("Difference is:",diff)
        input("Press Enter key to continue..")

    def mul(self):
        self.takeTwoInputs()
        print("Multiplication is:",self.a * self.b)
        input("Press Enter key to continue..")
    
    def div(self):
        self.takeTwoInputs()
        try:
            div = self.a / self.b
        except ZeroDivisionError:
            print("Infinite ( \u221E )")
        else:
            print("Division is:",div)
            input("Press Enter key to continue..")
        
    def square(self):
        self.takeSingleInput()
        print("Square is:",self.a * self.a)
        input("Press Enter key to continue..")
    
    def squareRoot(self):
        self.takeSingleInput()
        if self.a < 0:
            raise ValueError("⚠️ Can't calculate square root of a negative number..!!")

        guess = self.a
        e = 1e-6 #more small value will give more accuracy
        while abs(guess * guess - self.a) > e:
            guess = (guess + self.a / guess) / 2
            
        print(f"Square root is:{guess:.2f}")
        input("Press Enter key to continue..")
        
    def cube(self):
        self.takeSingleInput()
        print("Cube is:", self.a * self.a * self.a)
        input("Press Enter key to continue..")
    
    def cubeRoot(self):
        self.takeSingleInput()
        low = 0
        high = self.a
        mid = 0
        cr = 0
        while low <= high:
            mid = (low + high) // 2
            if mid * mid * mid <= self.a and (mid + 1) * (mid + 1) * (mid + 1) > self.a:
                cr = mid
                break
            elif mid * mid * mid > self.a:
                high = mid - 1
            else:
                low = mid + 1
        cr = mid
        print("Cube root is:",cr)
        input("Press Enter key to continue..")
        
    def power(self):
        self.takeTwoInputs()
        print(f"{self.a} power {self.b} is:",self.a ** self.b)
        input("Press Enter key to continue..")

        
        
        
if __name__ == "__main__":
    while True:
        print("\n","#"*30)
        print("1. Addition")
        print("2. Subtraction")
        print("3. Difference")
        print("4. Multiplication")
        print("5. Division")
        print("6. Square")
        print("7. SquareRoot")
        print("8. Cube")
        print("9. CubeRoot")
        print("10. a Power b")
        print("11. Exit Program")
        
        try:
            option = int(input("Select the option: "))
            if 0 > option > 10:
                raise IndexError
        except (ValueError, IndexError):
            print("⚠️ You have entered a wrong input, please provide valid input..!!")

        c = Calc()
        if option == 1:
            c.add()
        elif option == 2:
            c.sub()
        elif option == 3:
            c.diff()
        elif option == 4:
            c.mul()
        elif option == 5:
            c.div()
        elif option == 6:
            c.square()
        elif option == 7:
            c.squareRoot()
        elif option == 8:
            c.cube()
        elif option == 9:
            c.cubeRoot()
        elif option == 10:
            c.power()
        elif option == 11:
            import time, sys
            print("Exiting program",end="")
            for i in range(5):
                print(".",end="")
                time.sleep(0.4)
            sys.exit(0)
        else:
            print("⚠️ You have entered a wrong input, please provide valid input..!!")