x = lambda a,: a*a
print(x(3))

y = lambda a, b: a + b
print(y(4, 7))


#lambda inside function

def lam_fun(n):
    return lambda a: a*n

print(lam_fun(4))