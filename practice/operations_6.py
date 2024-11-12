#arithmatic operations
num = 30
num += 5 # num = num + 5
num *= 5 # num = num * 5
num /= 5 # num = num / 5

# should be greater than 20 and even number
num = 4
print((num>20) and (num%2==0))
print((num>20) or (num%2==0))

# in, not in
print("code" in "codewala")
print("code" in "Codewala")
print("code" not in "Codewala")

print("=====================================")
# identity operators
a = -3
b = -3
# object pooling range (-6, +256)
print(a==b)
print(a is b)