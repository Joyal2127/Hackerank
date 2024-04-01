def is_leap(year):
    leap = False
    
    if 1900 <= year <= 100000:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    leap = True20
                else:
                    leap = False
            else:
                leap = True
        else:
            leap = False
    else:
        print("not in range")
    
    return leap

year = int(input())
print(is_leap(year))