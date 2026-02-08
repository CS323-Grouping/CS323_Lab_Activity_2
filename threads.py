import threading
import time

import utils as utils

def compute_gwa(grades):
    gwa = sum(grades) / len(grades)
    print(f"[Thread] Calculated GWA: {gwa}")

threads = []

def startThreading(grades_list):
    start = time.time()
    for grade in grades_list:
        t = threading.Thread(target=compute_gwa, args=([grade],))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    end = time.time()

    print(f"Threads ended in {end-start}")
