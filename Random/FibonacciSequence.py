

def fib(n):
    if n < 0:
        print("Incorrect Input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    else:
        return fib(n - 1) + fib(n - 2)

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

if __name__ == "__main__":

    # print(fib(200))
    print(recur_fibo(3))
    # for x in range(20):
    #     print(fib(x))
        