import random

def generate_grades_file(filename="grades.txt", num_students=1000000, subjects_per_student=10):
    """
    Generates a file with grades.
    Total grades = num_students * subjects_per_student
    Structure: One grade per line.
    """
    total_grades = num_students * subjects_per_student
    print(f"Generating {total_grades} grades for {num_students} students ({subjects_per_student} subjects each)...")
    
    with open(filename, "w") as f:
        for student_id in range(num_students):
            for _ in range(subjects_per_student):
                # Generate a random grade between 70 and 100
                grade = random.randint(70, 100)
                f.write(f"{grade}\n")
    
    print(f"Successfully created '{filename}' with {total_grades} lines.")

if __name__ == "__main__":
    generate_grades_file()