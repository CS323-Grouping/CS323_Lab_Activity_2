import multi
import threads
import utils
import time

if __name__ == "__main__":
    raw_grades = utils.inputGrades()
    
    if not raw_grades:
        print("No grades found.")
        exit()

    subjects_per_student = 10
    students = [raw_grades[i:i + subjects_per_student] 
                for i in range(0, len(raw_grades), subjects_per_student)]

    print(f"\nLoaded {len(raw_grades)} grades.")
    print(f"Identified {len(students)} students.\n")

    print("--- Multithreading (4 Worker Threads) ---")
    threads.startThreading(students)
    
    print("\n" + "="*30 + "\n")

    print("--- Multiprocessing (Pool) ---")
    multi.startMulti(students)
