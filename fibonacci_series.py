def fibonacci_series(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibonacci_series(num-1)+fibonacci_series(num-2)
def fibonacci(num):
    for i in range(num):
        print(fibonacci_series(i),end=" ")
fibonacci(2)