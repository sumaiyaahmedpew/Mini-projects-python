import numpy as np
from functools import reduce
import time

def calculate_grade(avg):
    """Simple grade calculator"""
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "Fail"

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_reduce(n):
    return reduce(lambda a, b: a * b, range(1, n + 1), 1)


def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

students = {}

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks (comma separated): ")
    marks_list = list(map(int, marks.split(",")))
    
    students[roll] = {
        "name": name,
        "marks": np.array(marks_list)
    }
    print(f"Student {name} added successfully!")

def view_student():
    roll = input("Enter roll number: ")
    if roll not in students:
        print("Student not found!")
        return
    
    data = students[roll]
    marks = data["marks"]
    avg = np.mean(marks)
    grade = calculate_grade(avg)
    
    print("\nReport Card")
    print("Name:", data["name"])
    print("Roll:", roll)
    print("Marks:", marks)
    print("Average:", avg)
    print("Highest:", np.max(marks))
    print("Lowest:", np.min(marks))
    print("Grade:", grade)

def class_statistics():
    if not students:
        print("No students in the system yet!")
        return
    
    all_marks = [info["marks"] for info in students.values()]
    all_marks = np.array(all_marks)
    
    print("\nClass Statistics")
    print("Average per subject:", np.mean(all_marks, axis=0))
    
    pass_count = 0
    fail_count = 0
    for info in students.values():
        if np.all(info["marks"] >= 40):
            pass_count += 1
        else:
            fail_count += 1
    
    print("Passed:", pass_count)
    print("Failed:", fail_count)

def utilities():
    print("\n1. Fibonacci Generator")
    print("2. Factorial Comparison")
    choice = input("Choose: ")
    
    if choice == "1":
        n = int(input("Enter N: "))
        fib_seq = []
        for i in range(n):
            fib_seq.append(fibonacci_recursive(i))
        print("Fibonacci sequence:", fib_seq)
    
    elif choice == "2":
        n = int(input("Enter N: "))
        
        start = time.time()
        r1 = factorial_recursive(n)
        t1 = time.time() - start
        
        start = time.time()
        r2 = factorial_reduce(n)
        t2 = time.time() - start
        
        print(f"Recursive Factorial({n}) = {r1}, Time = {t1:.6f}s")
        print(f"Reduce Factorial({n}) = {r2}, Time = {t2:.6f}s")

def main():
    while True:
        print("\n===== Student Performance Dashboard =====")
        print("1. Add Student")
        print("2. View Student Report")
        print("3. Class Statistics")
        print("4. Utilities")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_student()
        elif choice == "3":
            class_statistics()
        elif choice == "4":
            utilities()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()
