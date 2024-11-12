""" 
Recursion Tasks:
  create a function that can generate 20 to 5 in reverse order
  create a function that will asks for user input 5 times and print after each input
"""

def reverse_numbers(num=20):
    if num >= 5:
        print(num)
        reverse_numbers(num - 1)
reverse_numbers()  # It will print numbers from 20 to 5 in reverse order
def ask_for_input(count=1):
    if count <= 5:
        user_input = input(f"Enter input {count}: ")
        print(f"Input {count}: {user_input}")
        ask_for_input(count + 1)
ask_for_input()  # This will prompt the user for input 5 times and print after each
