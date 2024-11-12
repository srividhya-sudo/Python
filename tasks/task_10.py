"""
convert the following functions into anonymous functions

def homepage(name, bank):
    return f"Hey {name}, Happy {bank} Banking"

def isNegative(num):
    return num<0

def multiply(n1, n2, n3=1):
    return n1*n2*n3

def check(num):
    return num > 0 and num != 4
"""    
    
homepage = lambda name,bank: f"Hey {name}, Happy {bank} Banking"
isNegative = lambda num: num < 0
multiply = lambda n1,n2,n3=1: n1*n2*n3
check = lambda num: num > 0 and num != 4
