import os
from typing import List

def inputGrades() -> List[int]:
    res = []
    ans = input("Do you want to use the local grades file? (y/n): ")

    if ans.lower() == "y":
        file_path = os.path.join("grades", "grades.txt")
        
        try:
            with open(file_path, "r") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        res.append(int(line))
            print(f"✅ Successfully loaded {len(res)} grades from '{file_path}'")
        except FileNotFoundError:
            print(f"❌ Error: '{file_path}' not found. Please run 'generate_grades.py' first.")
    else:
        print("\nManual input mode. Enter one grade at a time (type 'x' to finish):")
        while True:
            a = input("Enter grade: ")
            if a.lower() == "x":
                break
            if a.isdigit():
                grade = int(a)
                if 0 <= grade <= 100:
                    res.append(grade)
                else:
                    print("Invalid input. Grade must be between 0 and 100.")
            else:
                print("⚠️ Invalid input. Please enter a number between 0-100.")

        print(f"✅ Total {len(res)} grades entered manually.\n")

    return res
