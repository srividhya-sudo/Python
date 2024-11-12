# non-return function & parameterized function
#def welcome(name, bank):
    #print(f"Hello {name}, Happy {bank} Banking")

#welcome("Nick", "Sbi")
#welcome("Rick", "Hdfc")
#welcome("Akash", "Canara")
#welcome("Anil", "ICICI")

# return function & parameterized function
 #def welcome(name, bank):
    #return f"Hello {name}, Happy {bank} Banking"

#print(welcome("Diya", "BOB"))
#print(welcome("Mouni", "Hdfc"))
#print(welcome("Suu", "CANARA"))
#print(welcome("Varsha", "Indian"))

"""#non-parametrized function & return function
 def oneToFive():
    for i in range(1, 6):
    print(i)
  return "done"

print(oneToFive())


# non-parametrized function & non-return function
def oneToFive():
  for i in range(1, 6):
    print(i)

oneToFive() """

# *args
def numbers(a, *args):
    print(f"Numbers are {a}, {args}")

print(numbers(10, 20, 30, 40))
numbers(30, 40)

# **kwargs(variable keyword arguments)



def details(**kwargs):
    print(kwargs)

details(age=15, name="gayathri", brother="vidhya")



def details(a, **kwargs):
    print(kwargs)

details(100, age=15, name="tom", brother="jerry") 



def details(a, *args, **kwargs):
    print(a, args, kwargs)

details(100, 200, 300, 400, city="newyork", age=15, name="lilliput", brother="doramon") 
