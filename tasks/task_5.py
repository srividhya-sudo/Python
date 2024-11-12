""" 
data = [[1001, "steeve", ["brooklyn", "USA", ["captain america"]]]]
extract the captain america from the data and print it in uppercase

OUTPUT:- 
  CAPTAIN AMERICA
"""



#Task
data = [[1001, "steeve", ["brooklyn", "USA", ["captain america"]]]]
captain_america = data [0][2][2][0]
#captain_america = data [-1][-1][-1][-1]
print(captain_america.upper())
