import time
from multiprocessing import Pool, cpu_count
from typing import List

def compute_gwa_mp(student_grades: List[int]) -> float:
    """Calculate GWA for a single student."""
    return sum(student_grades) / len(student_grades)

def startMulti(students: List[List[int]]) -> None:
    """Process students using multiprocessing pool."""
    start = time.time()

    num_processes = cpu_count()

    with Pool(processes=num_processes) as pool:
        results = pool.map(compute_gwa_mp, students)

    end = time.time()
    
    print(f"Processed {len(students)} students using {num_processes} cores.")
    if results:
        print(f"Sample GWAs (first 5): {[f'{gwa:.2f}' for gwa in results[:5]]}")
    print(f"Execution Time: {end - start:.6f} seconds")