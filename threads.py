import threading
import time
from typing import List

def process_students(student_list: List[List[int]]) -> List[float]:
    """Calculate GWA for each student in the list."""
    results = []
    for student_grades in student_list:
        gwa = sum(student_grades) / len(student_grades)
        results.append(gwa)
    return results

def startThreading(students: List[List[int]]) -> None:
    """Process students using multithreading with worker pool."""
    start = time.time()

    num_workers = 4
    threads = []
    results = []
    lock = threading.Lock()

    chunk_size = len(students) // num_workers
    
    def worker(subset: List[List[int]], thread_id: int) -> None:
        """Worker thread function to process student grades."""
        gwas = process_students(subset)
        with lock:
            results.extend(gwas)
    
    for i in range(num_workers):
        start_index = i * chunk_size
        end_index = len(students) if i == num_workers - 1 else (i + 1) * chunk_size
        
        subset = students[start_index:end_index]
        
        t = threading.Thread(target=worker, args=(subset, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end = time.time()
    print(f"Processed {len(students)} students using {num_workers} threads.")
    if results:
        print(f"Sample GWAs (first 5): {[f'{gwa:.2f}' for gwa in results[:5]]}")
    print(f"Execution Time: {end - start:.6f} seconds")