import os
from typing import List

def inputGrades() -> List[int]:
    res = []
    ans = input("Use Local File (y/n): ")

    if ans.lower() == "y":
        file_path = os.path.join("grades", "grades.txt")
        
        try:
            with open(file_path, "r") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        res.append(int(line))
        except FileNotFoundError:
            print(f"Error: '{file_path}' not found. Please run generate_grades.py first.")
    else:
        print("Manual input mode...")
        while True:
            a = input("Enter Grade (0-100, x for exit): ")
            if a.lower() == "x":
                break
            if a.isdigit():
                grade = int(a)
                if 0 <= grade <= 100:
                    res.append(grade)
                else:
                    print("Invalid input. Grade must be between 0 and 100.")
            else:
                print("Invalid input. Please enter a number.")

    return res