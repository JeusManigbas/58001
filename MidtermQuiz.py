#Distance conversion
#Centimeter = cm
#Kilometer = km
#Inches = in

class DistanceConversion:
    def distance_conversion(distance, input_conversion, output_conversion):

        if input_conversion == 'm':
            if output_conversion == 'cm':
                return distance * 100
            elif output_conversion == 'km':
                return distance / 1000
            elif output_conversion == 'in':
                return distance * 39.37
        else:
            return distance

    while True:
        print('Enter the value of the distance:')
        value = float(input())
        print('Enter the unit of the value of the distance (m):')
        input_conversion = input().upper()
        print('Enter the intended unit of the value of the distance (cm, km, ot in)')
        output_conversion = input().upper()

        result = distance_conversion(value, input_conversion, output_conversion)
        print(f'{value} {input_conversion} = {result} {output_conversion}')