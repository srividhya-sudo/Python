"""employee_db = [
        (1234, 'John', 'Physics', 23000),
        (1235, 'Nick', 'Maths', 13000),
        (1236, 'Samantha', 'Maths', 40000), 
        (1237, 'Amanda', 'Chemistry', 25000), 
        (1238, 'Vicky', 'Maths', 10000), 
    ]
print least salaried employee
print highest salaried employee
print Maths employees
sorting based on employees salaries
Print employees whose name starts with A
Print employees whose salary is in range of 20000 to 30000 (inclusive).
print even id Employees
----------MORE TASKS---------
count number of maths employees
count number of vowels in each employee name
reverse the characters in subjects and print only subjects
print the (name in lowercase, subject in uppercase)
Generate user id for each user by concatenating name and id (eg:- Nick_1235)"""




employee_db = [
    (1234, 'Akki', 'Physics', 23000),
    (1235, 'Srividhya', 'Maths', 13000),
    (1236, 'Nikhil', 'Maths', 40000),
    (1237, 'Gayathri', 'Chemistry', 25000),
    (1238, 'Anil', 'Maths', 10000),
]

# 1. Print least salaried employee
least_salaried = min(employee_db, key=lambda x: x[3])
print(f"Least salaried employee: Name={least_salaried[1]},Salary={least_salaried[3]}")

# 2. Print highest salaried employee
highest_salaried = max(employee_db, key=lambda x: x[3])
print(f"Highest salaried employee: Name={highest_salaried[1]},Salary={highest_salaried[3]}")

# 3. Print Maths employees
maths_employees = [emp for emp in employee_db if emp[2] == 'Maths']
print("Maths employees:")
for emp in maths_employees:
    print(f"Name={emp[1]},Subject={emp[2]},")

# 4. Sorting based on employee salaries
sorted_employees = sorted(employee_db, key=lambda x: x[3])
print("Employees sorted by salary:")
for emp in sorted_employees:
    print(f"ID={emp[0]}, Name={emp[1]}, Subject={emp[2]}, Salary={emp[3]}")

# 5. Print employees whose name starts with 'A'
a_employees = [emp for emp in employee_db if emp[1].startswith('A')]
print("Employees whose name starts with 'A':")
for emp in a_employees:
    print(f"Name={emp[1]}")

# 6. Print employees whose salary is in the range of 20000 to 30000 (inclusive)
salary_range_employees = [emp for emp in employee_db if 20000 <= emp[3] <= 30000]
print("Employees with salary in range of 20000 to 30000:")
for emp in salary_range_employees:
    print(f"Name={emp[1]},Salary={emp[3]}")

# 7. Print even ID Employees
even_id_employees = [emp for emp in employee_db if emp[0] % 2 == 0]
print("Even ID employees:")
for emp in even_id_employees:
    print(f"ID={emp[0]}, Name={emp[1]}, Subject={emp[2]}, Salary={emp[3]}")

# 8. Count number of Maths employees
maths_count = len(maths_employees)
print(f"Number of Maths employees: {maths_count}")

# 9. Count number of vowels in each employee name
vowel_counts = {emp[1]: sum(1 for char in emp[1].lower() if char in 'aeiou') for emp in employee_db}
print("Vowel counts in each employee name:")
for name, count in vowel_counts.items():
    print(f"{name}: {count}")

# 10. Reverse the characters in subjects and print only subjects
reversed_subjects = [emp[2][::-1] for emp in employee_db]
print("Reversed subjects:")
for subject in reversed_subjects:
    print(subject)

# 11. Print (name in lowercase, subject in uppercase)
print("Name in lowercase, subject in uppercase:")
for emp in employee_db:
    print(f"Name={emp[1].lower()}, Subject={emp[2].upper()}")

# 12. Generate user ID for each user
user_ids = [f"{emp[1]}_{emp[0]}" for emp in employee_db]
print("Generated user IDs:")
for user_id in user_ids:
    print(user_id)
