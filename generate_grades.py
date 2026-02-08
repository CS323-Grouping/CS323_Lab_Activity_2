import random
import os

def generate_grades_file(filename="grades.txt", num_students=1000, subjects_per_student=10):
    # 1. Define folder name and create it if it doesn't exist
    folder_name = "grades"
    os.makedirs(folder_name, exist_ok=True)

    # 2. Update the full file path
    filepath = os.path.join(folder_name, filename)

    total_grades = num_students * subjects_per_student
    print(f"Generating {total_grades} grades for {num_students} students ({subjects_per_student} subjects each)...")
    
    # 3. Write to the file inside the folder
    with open(filepath, "w") as f:
        for student_id in range(num_students):
            for _ in range(subjects_per_student):
                # Generate a random grade between 70 and 100
                grade = random.randint(70, 100)
                f.write(f"{grade}\n")
    
    print(f"Successfully created '{filepath}' with {total_grades} lines.")

if __name__ == "__main__":
    generate_grades_file()