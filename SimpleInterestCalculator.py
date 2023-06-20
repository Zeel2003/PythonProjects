# Create a Python class called SimpleInterestCalculator. The class should have a constructor 
# that takes the principal amount, interest rate, and time period as parameters. Implement a method 
# called calculate_simple_interest that calculates and returns the simple interest.

class SimpleInterestCalculator:
    def __init__(self,pAmount,interestRate,time):
        self.pAmount = pAmount
        self.interestRate = interestRate
        self.time = time

    def calculate_simple_interest(self):
        return (self.pAmount * self.interestRate * self.time) / 100
    

# Given values

# calculator = SimpleInterestCalculator(1000,2.5,10)
# interest = calculator.calculate_simple_interest()
# print(interest)

# user input

pAmount = float(input('Please enter principle amount: '))
interestRate = float(input('Please enter interest rate: '))
time = float(input('Please enter time period: '))

calculator = SimpleInterestCalculator(pAmount, interestRate,time)
interest = calculator.calculate_simple_interest()
print(interest)
