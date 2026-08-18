def dishonestCapacityCalculator():
    while True:    
        print('Enter TB or GB for the advertised unit: ')
        unit = input('>')

        #Calculate the maount that the advertised capacity lies:
        if unit == 'TB' or unit == 'tb':
            discrepancy = 1000000000000 / 1099511627776
        elif unit == 'GB' or unit =='gb':
            discrepancy = 1000000000 / 1073741824
        else:
            print('Please enter a valid answer')
            continue

        print('Enter the advertised capacity: ')
        advertised_capacity = input('>')
        advertised_capacity = float(advertised_capacity)

        #calculate the real capacity, round it to the nearest hundreths,
        #and convert it to a string so it can be concatenated:
        real_capacity = str(round(advertised_capacity * discrepancy, 2))

        print('The actual capacity is ' + real_capacity + ' ' + unit)
        break

dishonestCapacityCalculator()