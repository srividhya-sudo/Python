# # tuple (), ordered, immutable
# arr = ("code",1, 1, 2, 3)
# print(arr.count(1))
# print(arr)

arr = ("code",1, 1, 2, 3)
#print(arr.count(3))
print(arr)

data = [(1, "Junnu", "USA"), (2, "Junnu", "USA")]
Junnu_crt = 0
for bio in range(len(data)):
    if data[bio][1] == "Junnu":
        Junnu_crt += 1
print(Junnu_crt)
data = [(1, "Junnu", "USA"), (2, "Iraa", "USA")]
for user in range(len(data)):
    print(data[user][0]) # (1, 'Junnu', 'USA')
data = [
    (1, "Junnu", "USA", 100000), 
    (2, "Iraa", "USA", 50000),
    (12, "Honey", "uk", 200),
    (10, "bob", "up", 4000)
	]
data.sort(key=lambda x:x[2], reverse=True)
for user in range(len(data)):
    print(*data[user])
arr = [1, 2, 3, 4]
# arr[1] = 10
arr[0:2] = [10]
print(arr)