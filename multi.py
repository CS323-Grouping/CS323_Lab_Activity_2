import time
from multiprocessing import Pool, cpu_count

def compute_gwa_mp(student_grades):
    """Calculates GWA for a single student."""
    return sum(student_grades) / len(student_grades)

def startMulti(students):
    start = time.time()
    
    # Use all available CPU cores
    num_processes = cpu_count()
    
    # Create a Pool of worker processes
    with Pool(processes=num_processes) as pool:
        # map() sends the list of students to the workers automatically
        # It returns a list of results (GWAs) in order
        results = pool.map(compute_gwa_mp, students)

    # Optional: Verify results
    # print(f"First 5 GWAs: {results[:5]}")

    end = time.time()
    
    print(f"Processed {len(students)} students using {num_processes} cores.")
    print(f"Execution Time: {end - start:.6f} seconds")