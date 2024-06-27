estaciones = {'1': "calle76", '2': "calle72", '3': "flores", '4': "calle63", '5': "calle57", '6': "marly", '7': "calle45", '8': "av.39", '9': "profamilia", '10': "calle26"}

print("las posibles rutas de calle 76 a calle 26 puedes ser: ")
print("\n", estaciones['1'], estaciones['4'], estaciones['6'], estaciones['8'], estaciones['10'])
print("\n", estaciones['1'], estaciones['3'], estaciones['4'], estaciones['9'], estaciones['10'])
print("\n", estaciones['1'], estaciones['2'], estaciones['7'], estaciones['9'], estaciones['10'])
print("\n y las posibles rutas de calle 26 a calle 76 pueden ser: ")
print("\n", estaciones['10'], estaciones['7'], estaciones['4'], estaciones['3'], estaciones['1'])
print("\n", estaciones['10'], estaciones['8'], estaciones['5'], estaciones['4'], estaciones['1'])    
print("\n", estaciones['10'], estaciones['9'], estaciones['7'], estaciones['3'], estaciones['1'])