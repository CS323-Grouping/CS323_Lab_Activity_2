import random
import os

def generate_grades_file(filename="grades.txt", num_students=1000, subjects_per_student=10):
    folder_name = "grades"
    os.makedirs(folder_name, exist_ok=True)

    filepath = os.path.join(folder_name, filename)

    total_grades = num_students * subjects_per_student
    print(f"Generating {total_grades} grades for {num_students} students ({subjects_per_student} subjects each)...")

    with open(filepath, "w") as f:
        for student_id in range(num_students):
            for _ in range(subjects_per_student):
                grade = random.randint(70, 100)
                f.write(f"{grade}\n")
    
    print(f"Successfully created '{filepath}' with {total_grades} lines.")

if __name__ == "__main__":
    generate_grades_file()