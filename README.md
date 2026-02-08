# Laboratory 2 – Exploring Multithreading and Multiprocessing in Python

## Activity Summary

In this laboratory, we implemented a Grade Computing System that calculates the General Weighted Average (GWA) using both multithreading and multiprocessing in Python. To handle large datasets efficiently, we implemented a **"Chunking Strategy"** (grouping grades by student) and used **Worker Pools** to manage system resources. We measured execution times, observed execution order behavior, and analyzed differences in concurrency and parallelism.

---

## Performance Comparison

| Method          | Execution Order Behavior | GWA Output Behavior         | Execution Time      |
| --------------- | ------------------------ | --------------------------- | ------------------- |
| Multithreading  | Non-deterministic order  | Printed as threads finish   | **0.2057 sec**      |
| Multiprocessing | Non-deterministic order  | Printed as processes finish | **0.6459 sec**      |

**Observation:**
In our experiment with 1,000,000 students, **Multithreading was approximately 3x faster** than Multiprocessing. Even though Multiprocessing utilizes multiple cores, the mathematical calculation (averaging 10 numbers) was too "lightweight." The high overhead of creating processes and serializing data (Inter-Process Communication) outweighed the benefits of parallel execution.

---

## Questions and Answers

### 1. Which approach demonstrates true parallelism in Python? Explain

**Multiprocessing** demonstrates true parallelism. Each process runs in its own Python interpreter with its own independent memory space. This bypasses the Global Interpreter Lock (GIL), allowing the program to utilize multiple CPU cores simultaneously to execute tasks at the exact same time.

---

### 2. Compare execution times between multithreading and multiprocessing

Based on our results, **Multithreading was significantly faster (0.20s)** compared to **Multiprocessing (0.64s)**.

* **Multithreading:** Had lower overhead because threads share the same memory space. Even though they ran concurrently (not truly parallel due to the GIL), the fast context switching was efficient for this specific task.
* **Multiprocessing:** Was slower because the time required to spawn processes and copy data between them exceeded the time it took to actually perform the simple GWA calculation.

---

### 3. Can Python handle true parallelism using threads? Why or why not?

**No.** Python threads cannot achieve true parallelism for CPU-bound tasks because of the **Global Interpreter Lock (GIL)**. The GIL is a mutex that allows only one thread to hold control of the Python interpreter at any one time, forcing threads to execute sequentially (time-sliced) rather than simultaneously.

---

### 4. What happens if you input a large number of grades (e.g., 1000 or 1,000,000)? Which method is faster and why?

When processing a massive dataset (1,000,000 students), **Multithreading remained faster**.

* **Reason:** The "task payload" (calculating the average of 10 integers) is extremely small. The system overhead for Multiprocessing (pickling data, starting processes) is fixed and relatively high. Unless the calculation per student is complex (e.g., heavy matrix math), the overhead of Multiprocessing will always make it slower than the lightweight threads for simple arithmetic.

---

### 5. Which method is better for CPU-bound tasks and which for I/O-bound tasks?

* **Multiprocessing** is better for **Heavy CPU-bound tasks** (e.g., video processing, complex mathematical modeling) where the calculation time is long enough to justify the startup cost.
* **Multithreading** is better for **I/O-bound tasks** (e.g., file operations, network requests) or **Lightweight CPU tasks** (like our GWA calc) where low overhead is critical.

---

### 6. How did your group apply creative coding or algorithmic solutions in this lab?

We optimized the performance by implementing a **Chunking and Pooling Strategy**:

1. **Data Transformation:** Instead of processing raw numbers, we grouped grades into "Student" chunks (lists of 10 subjects) in `main.py`.
2. **Worker Pools:** In `multi.py` and `threads.py`, we replaced the inefficient "one-process-per-item" approach with a fixed **Pool of Workers** (mapped to CPU cores). This prevented system crashing and allowed us to scale to 10 million grades effortlessly.
3. **Grade Generation:** We also added a custom function that generates a set amount of grades randomly. And a custom function to read the grades from a file or have a manual input of grades.
