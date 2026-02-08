# Laboratory 2 – Exploring Multithreading and Multiprocessing in Python

## Activity Summary

In this laboratory, we implemented a Grade Computing System that calculates the General Weighted Average (GWA) using both multithreading and multiprocessing in Python. We measured execution times, observed execution order behavior, and analyzed differences in concurrency and parallelism.

---

## Performance Comparison

| Method          | Execution Order Behavior | GWA Output Behavior         | Execution Time |
| --------------- | ------------------------ | --------------------------- | -------------- |
| Multithreading  | Non-deterministic order  | Printed as threads finish   | ______ sec     |
| Multiprocessing | Non-deterministic order  | Printed as processes finish | ______ sec     |

Observation:
Outputs appear in different order because threads and processes execute concurrently and are scheduled independently by the operating system.

---

## Questions and Answers

### 1. Which approach demonstrates true parallelism in Python? Explain

Multiprocessing demonstrates true parallelism because each process runs in its own Python interpreter and memory space. It bypasses the Global Interpreter Lock (GIL), allowing multiple CPU cores to execute tasks simultaneously.

---

### 2. Compare execution times between multithreading and multiprocessing

Multithreading generally has lower overhead but does not achieve true parallelism for CPU-bound tasks due to the GIL. Multiprocessing may have higher startup overhead but performs better for CPU-intensive workloads when multiple cores are available.

---

### 3. Can Python handle true parallelism using threads? Why or why not?

No. Python threads cannot achieve true parallelism for CPU-bound tasks because of the Global Interpreter Lock (GIL), which allows only one thread to execute Python bytecode at a time within a single process.

---

### 4. What happens if you input a large number of grades (e.g., 1000)? Which method is faster and why?

With a large number of grades, multithreading may experience increased context switching overhead. Multiprocessing may perform better for CPU-bound calculations because it uses multiple cores. However, creating too many processes can also increase overhead. A process pool would be more efficient for large inputs.

---

### 5. Which method is better for CPU-bound tasks and which for I/O-bound tasks?

Multiprocessing is better for CPU-bound tasks because it enables true parallel execution across multiple cores.
Multithreading is better for I/O-bound tasks because threads can run while waiting for input or output operations to complete.

---

### 6. How did your group apply creative coding or algorithmic solutions in this lab?

Our group implemented dynamic user input handling, modular function design, execution time benchmarking, and improved output formatting. We structured the program for readability and compared execution behavior systematically.
