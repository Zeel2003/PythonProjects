from math import floor

class CompoundInterestCalculator:
    def __init__(self,pAmount, interestRate, time):
        self.pAmount = pAmount
        self.interestRate = interestRate
        self.time = time

    def calculatinginterest(self):
        return self.pAmount * (1 + self.interestRate/100) ** self.time


pAmount = float(input('Please enter principal amount: $'))
interestRate = float(input('Please enter Rate of Interest: '))
time = float(input("Please enter loan time period (just number & in years): "))

calculator = CompoundInterestCalculator(pAmount,interestRate,time)

print('\nIn',floor(time),'years, you will have (compounded annually) $', round(calculator.calculatinginterest(),2))