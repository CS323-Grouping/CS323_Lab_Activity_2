import random
import os

def generate_grades_file(
    filename="grades.txt",
    num_students=1000,
    subjects_per_student=10,
    min_grade=70,
    max_grade=100
):
    folder_name = "grades"
    os.makedirs(folder_name, exist_ok=True)
    filepath = os.path.join(folder_name, filename)

    total_grades = num_students * subjects_per_student

    print("=" * 50)
    print("GRADE DATA GENERATION")
    print("=" * 50)
    print(f"Students            : {num_students}")
    print(f"Subjects per student: {subjects_per_student}")
    print(f"Grade range         : {min_grade} - {max_grade}")
    print("-" * 50)

    with open(filepath, "w") as f:
        for _ in range(total_grades):
            grade = random.randint(min_grade, max_grade)
            f.write(f"{grade}\n")

    print(f"File generated successfully!")
    print(f"Total values written: {total_grades}")
    print(f"Saved at            : {filepath}")
    print("=" * 50)

if __name__ == "__main__":
    generate_grades_file()
