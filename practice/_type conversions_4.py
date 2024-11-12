val=300
#print(type(val))

#int--->strS
val=30
val=str(30)
#print(val,type(val))

#int--->float
val=30
val=float(30)
#print(val,type(val))

#int--->bool
val=30
val=bool(30)
#print(val,type(val))

#str--->int
val="30"
val=int(30)
#print(val,type(val))

#str--->float
val="30"
val=float(30)
#print(val,type(val))

#srt--->bool
val="43"
val=bool(43)
#print(val,type(val))

#float--->int
val="98.999"
val=int(98.999)
#print(val,type(val))

#float--->str
val=30.79
val=str(30)
#print(val,type(val))

#float--->bool
val=30.79
val=bool(30.79)
#print(val,type(val))

#bool--->
val="0"
val=bool("0")
#print(val,type(val))

#float--->str
val=" "
val=bool(val)
#print(val,type(val))

value = "temp"
value = bool(value)
#print(value, type(value))



#composite type conversions

#list--->tuple
arr = [1, 2, 3, 3]
arr_tuple = tuple(arr)
#print(arr_tuple, type(arr_tuple))

#list--->set
arr_set = set(arr)
#print(arr_set, type(arr_set))

temp = [("name","Nikhil sir"), ["course", "python"]]
arr_dict = dict(temp)
#print(arr_dict, type(arr_dict))


crt=30
val=crt

#print(val)