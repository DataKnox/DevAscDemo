#!/usr/bin/env python3

students = [
    'Alex Lebedev - Future DevNetOps'
]

def announce_students(students):
    for student in students:
        print(f"\n{student}\n")

def main():
    print("Hello, World!")
    print("Welcome to DevAsc")
    print("=" * 20)
    announce_students(students)

if __name__ == "__main__":
    main()
