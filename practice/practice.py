"""#1 EVEN OR ODD
num=int(input("enter number:"))
if num % 2 == 0:
    print("EVEN")
else:
    print("ODD")
    
#2
line_of_text="Hello Welcome To python class"  
search_word="python"
if search_word is line_of_text:
    print("TRUE")
else:
    print("FALSE")  
    
    
#3
word="srividya"
vowels="aeiou"
print()

def contains_vowels(word):
    vowels = "aeiouAEIOU"
    for letter in word:
        if letter in vowels:
            return True
    return False

# Ask the user for a word
user_word = input("Please enter a word: ")

# Check for vowels and print the result
#if contains_vowels(user_word):
    #print(f"The word '{user_word}' contains vowels.")
#else:
    #print(f"The word '{user_word}' does not contain any vowels.")
    
    
#4
def check_vowel_or_consonant(char):
    vowels = "aeiouAEIOU"  # List of vowels (both lowercase and uppercase)
    
    if char.isalpha() and len(char) == 1:  # Check if the input is a single alphabet
        if char in vowels:
            return "vowel"
        else:
            return "consonant"
    else:
        return "Invalid input. Please enter a single alphabet."

# Ask the user for an alphabet
user_input = input("Please enter a single alphabet: ")

# Check and print the result
result = check_vowel_or_consonant(user_input)
print(f"The letter '{user_input}' is a {result}.")


#5


#while loop
#name="Nick"
#name = "srividhya"
#nick = 0
#while nick < len(name):
    #print(name[nick], nick)
    #nick += 1
    
    n=10
    i=1
    while i<=n:
        #print(i)
        i+=1
        
    n=1
    i=10
    while i>=n:
        #print(i)
        i-=1
        
a = 'anil'
temp = 10
while temp >= 1:
    #print(temp, a)
    temp -= 1

n = 5
while n <= 10:
     #print(n)
     n += 1
     
n = 10
while n >= 5:
    #print(n)
    n -= 1
    
start = 20
end = 30

while start <= end:
    #print(start)
    start += 1
    
start = 49
end = 39
while start >= end:
    #print(start)
    start -= 1
    
name = 'srividhya'
temp = 44
while temp < 49:
    #print(name)
    temp += 1
    
name = 'umbrella'
temp = 49
while temp >= 44:
    #print(name)
    temp -= 1
    
start = 49
end = 44
name = 'anil'
while start > end:
    #print(name)
    start -= 1
    
for i in range(start, end, -1):
    #print(i, name)
    
#i = 1
#while i <= 2:
    name, age = input().split()[:2]
    #print('name is ',name, 'age is', age)
    #print()
    i+=1"""
    
    
    
