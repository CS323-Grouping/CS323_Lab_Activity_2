import threading
import time

# Function to process a chunk of students
def process_students(student_list, thread_id):
    count = 0
    for student_grades in student_list:
        gwa = sum(student_grades) / len(student_grades)
        # Optional: Print every 10th student to avoid spamming console
        # print(f"[Thread-{thread_id}] Student GWA: {gwa:.2f}")
        count += 1
    return count

def startThreading(students):
    start = time.time()
    
    # 1. Define number of workers (threads)
    num_workers = 4
    threads = []
    
    # 2. Split students among workers
    # If we have 120 students, each worker gets 30.
    chunk_size = len(students) // num_workers
    
    for i in range(num_workers):
        # Determine start and end indices for this worker
        start_index = i * chunk_size
        # Ensure the last worker gets any remaining students (if not divisible)
        end_index = len(students) if i == num_workers - 1 else (i + 1) * chunk_size
        
        subset = students[start_index:end_index]
        
        t = threading.Thread(target=process_students, args=(subset, i))
        threads.append(t)
        t.start()

    # 3. Wait for all threads to finish
    for t in threads:
        t.join()

    end = time.time()
    print(f"Processed {len(students)} students using {num_workers} threads.")
    print(f"Execution Time: {end - start:.6f} seconds")