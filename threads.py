import threading
import time

def process_students(student_list, thread_id):
    count = 0
    for student_grades in student_list:
        gwa = sum(student_grades) / len(student_grades)
        count += 1
    return count

def startThreading(students):
    start = time.time()

    num_workers = 4
    threads = []

    chunk_size = len(students) // num_workers
    
    for i in range(num_workers):
        start_index = i * chunk_size
        end_index = len(students) if i == num_workers - 1 else (i + 1) * chunk_size
        
        subset = students[start_index:end_index]
        
        t = threading.Thread(target=process_students, args=(subset, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end = time.time()
    print(f"Processed {len(students)} students using {num_workers} threads.")
    print(f"Execution Time: {end - start:.6f} seconds")