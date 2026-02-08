import os

def inputGrades() -> list[int]:
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
            a = input("Enter Grade (x for exit): ")
            if a.lower() == "x":
                break
            if a.isdigit():
                res.append(int(a))
            else:
                print("Invalid input.")

    return res