def ref_demo(x):
    print("x=",x," id=",id(x))
    x=42
    print("x=",x," id=",id(x))


#ref_demo(12)


def arithmetic_mean(x, *l):
    """ The function calculates the arithmetic mean of a non-empty
        arbitrary number of numbers """
    sum = x
    for i in l:
        sum += i

    return sum / (1.0 + len(l))


def f():
    global s
    print(s)
    s="test inside"
    
    print(s)


def temperature(t):
    def celsius2fahrenheit(x):
        return 9*x/5

    result = "It's " + str(celsius2fahrenheit(t)) + " degrees"
    return result


def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper
    
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def test():
    orders = [ ["34587","Learning Python, Mark Lutz", 4, 40.95], 
	   ["98762","Programming Python, Mark Lutz", 5, 56.80], 
           ["77226","Head First Python, Paul Barry",3,32.95]]

min_order = 100
invoice_totals = list(map(lambda x: x if x[1] >= min_order else (x[0], x[1] + 10) , 
			  map(lambda x: (x[0],x[2] * x[3]), orders)))

print(invoice_totals)
    
