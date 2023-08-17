class SimpleInterestCalculator:
    def __init__(self,pAmount,interestRate,time):
        self.pAmount = pAmount
        self.interestRate = interestRate
        self.time = time

    def calculate_simple_interest(self):
        return (self.pAmount * self.interestRate * self.time) / 100
    

# Given values

# calculator = SimpleInterestCalculator(1000,4.1,10)
# interest = calculator.calculate_simple_interest()
# print('Your investment of 1000 for 10 years for 2.5 percentage interest will give you total return of',
#       interest + 1000)



pAmount = float(input('Please enter principle amount: '))
interestRate = float(input('Please enter interest rate: '))
time = float(input('Please enter time period in years: '))

calculator = SimpleInterestCalculator(pAmount, interestRate,time)
interest = calculator.calculate_simple_interest()
print('Your investment of',pAmount,'for',time,'years, with',interestRate,
      'interest rate will give you total return of',interest + pAmount,'after',time,'years.')

