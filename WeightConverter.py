is_converting = input('What do you want to convert to (kg/gm/oz)? \n')


class Convertor:

    if is_converting == 'kg':
        weight1 = float(input('Please enter weight in pounds(lbs): '))
        kg = weight1 / 2.204
        print('Weight in Kilograms (kgs) is',round(kg,2))

    if is_converting == 'gm':
        weight2 = float(input('Please enter weight in pounds(lbs): '))
        gm = weight2 * 453.6
        print('Weight in Gram (gm) is',round(gm,2))

    if is_converting == 'oz':
        weight3 = float(input('Please enter weight in pounds(lbs): '))
        oz = weight3 * 16
        print('Weight in Ounce (oz) is',round(oz,2))

