## Daniel Ham
## Write a function


def leap_year(year):
    leap = False
    
    if year >= 1900 and year <= 10**5:
        if year % 400  == 0:
            leap = True
        elif year % 100 == 0:
            leap = False
        elif year % 4 == 0:
            leap = True
        else:
            leap = False
    return leap



## Main
print(leap_year(int(input())))
