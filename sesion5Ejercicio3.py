def añoBisiesto(año):
    if año % 4==0 or año % 100==0 or año%400==0:
        print('El año',año,'es bisiesto')
        return
    print('El año',año,'no es bisiesto')

añoBisiesto(1976)
añoBisiesto(2020)
añoBisiesto(2004)
añoBisiesto(1983)
añoBisiesto(1976)
añoBisiesto(1966)
añoBisiesto(1962)
añoBisiesto(1986)
añoBisiesto(1985)
añoBisiesto(2007)
añoBisiesto(1978)
