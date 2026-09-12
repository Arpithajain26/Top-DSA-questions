def fibonaaci_series(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibonaaci_series(num-1)+fibonaaci_series(num-2)
    
