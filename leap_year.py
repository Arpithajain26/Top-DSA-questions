def leap_year(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        print("leap year")
    else:
        print("not leap year")
leap_year(1996)
leap_year(1997)