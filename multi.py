import time
from multiprocessing import Pool, cpu_count

def compute_gwa_mp(student_grades):
    return sum(student_grades) / len(student_grades)

def startMulti(students):
    start = time.time()

    num_processes = cpu_count()

    with Pool(processes=num_processes) as pool:
        results = pool.map(compute_gwa_mp, students)


    end = time.time()
    
    print(f"Processed {len(students)} students using {num_processes} cores.")
    print(f"Execution Time: {end - start:.6f} seconds")