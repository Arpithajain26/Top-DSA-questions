def even_or_odd(num):
    if num & 1==1:
        return "odd"
    else:
        return "even"
print(even_or_odd(2))
print(even_or_odd(57))