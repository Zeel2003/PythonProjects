input_format = input('How do you want to enter your salary,\n1) Hourly\n2) Weekly\n3) Monthly\n4) Yearly\n')

usr_working_hrs = float(input('Enter number of hours you work per week: '))

usr_overtime = float(input('Enter number of overtime hours you did this week(if not any, enter 0): '))

if input_format == "Hourly":
    usr_hr_salary = float(input('Enter your base salary per Hour: '))
    calculate1 = usr_hr_salary * usr_working_hrs
    print('Your salary for',usr_working_hrs,'is $',calculate1)
elif input_format == "Weekly":
    usr_wk_salary = float(input('Enter your base salary per Week: '))
    calculate2 = usr_wk_salary * usr_working_hrs
    print('Your salary for',usr_working_hrs,'is $',calculate2)
elif input_format == "Monthly":
    usr_mon_salary = float(input('Enter your base salary per Month: '))
    calculate3 = usr_mon_salary * usr_working_hrs
    print('Your salary for',usr_working_hrs,'is $',calculate3)
elif input_format == "Yearly":
    usr_yr_salary = float(input('Enter your base salary per Year: '))
    calculate4 = usr_yr_salary * usr_working_hrs
    print('Your salary for',usr_working_hrs,'is $',calculate4)

if usr_overtime > 0:
    OT_rate = input("What is your overtime pay rate percentage(don't include percentage sign): ")
    print('Your overtime pay is',usr_hr_salary * OT_rate * usr_overtime)

