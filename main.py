import multi
import threads
import utils
import time

if __name__ == "__main__":
    # 1. Load the raw data (flat list of 1200 integers)
    raw_grades = utils.inputGrades()
    
    if not raw_grades:
        print("No grades found.")
        exit()

    # 2. Group into Students (Chunks of 10)
    # Result is a list of lists: [[85, 90...], [88, 92...]]
    subjects_per_student = 10
    students = [raw_grades[i:i + subjects_per_student] 
                for i in range(0, len(raw_grades), subjects_per_student)]

    print(f"\nLoaded {len(raw_grades)} grades.")
    print(f"Identified {len(students)} students.\n")

    # 3. Run Multithreading
    print("--- Multithreading (4 Worker Threads) ---")
    threads.startThreading(students)
    
    print("\n" + "="*30 + "\n")

    # 4. Run Multiprocessing
    print("--- Multiprocessing (Pool) ---")
    multi.startMulti(students)
