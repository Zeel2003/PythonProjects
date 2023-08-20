usr_height = float(input('Enter your height: '))
usr_weight = float(input('Enter your weight (lbs): '))
    
feet_inch = usr_height * 12

BMI = usr_weight /(feet_inch **2)

if BMI <= 18.5:
    print('Youe are underweight')
elif BMI >= 18.6 and BMI <= 24.9:
    print('You have healthy weight')
elif BMI >= 25 and BMI <= 29.9:
    print('You have overweight')
elif BMI >= 30:
    print('You are obese')