"""Take a sentence and separate the vowels and consonants.
Do not convert the sentence into lower.
If the sentence contains 0 in it, consider it as invalid,
    you dont have to separate vowels & consonants

Sample Input1:
  This Is codewala
Sample Output1:
  [vowels] --- iIoeaa
  [consonants] --- Thsscdwl

Sample Input2:
  This Is DSA
Sample Output2:
  [vowels] --- iIA
  [consonants] --- ThssDS

Sample Input3:
  I Could Do This All day
Sample Output3:
  [vowels] --- IouoiAa
  [consonants] --- CldDThslldy

CONSTRAINTS:
  should not take special characters and numbers
  sentence can have spaces
  output should not contain spaces
"""



def separate_vowels_consonants(sentence):
    vowels = "AEIOUaeiou"
    consonants = ""
    vowel_string = ""
    
    if '0' in sentence or not sentence.replace(' ', '').isalpha():
        return "Invalid input"
    
    for char in sentence:
        if char.isalpha():  
            if char in vowels:
                vowel_string += char
            else:
                consonants += char

    print(f"[vowels] --- {vowel_string}")
    print(f"[consonants] --- {consonants}")

separate_vowels_consonants("This Is codewala")
separate_vowels_consonants("This Is DSA")
separate_vowels_consonants("I Could Do This All day")







             
        
        
        
        
    
