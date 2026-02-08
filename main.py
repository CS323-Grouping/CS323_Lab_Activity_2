import threading
from multiprocessing import Process


def inputGrades() -> list[int]:
    res = []
    while True:
        a = input("Enter Input (x for exit) : ")

        if a == "x":
            break
        res.append(int(a))

    return res


def compute_gwa(grades):
    gwa = sum(grades) / len(grades)
    print(f"[Thread] Calculated GWA: {gwa}")

grades_list = inputGrades()

threads = []

for grade in grades_list:
    t = threading.Thread(target=compute_gwa, args=([grade],))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

def compute_gwa_mp(grades):
    gwa = sum(grades) / len(grades)
    print(f"[Process] Calculated GWA: {gwa}")

grades_list = inputGrades()

processes = []
for grade in grades_list:
    p = Process(target=compute_gwa_mp, args=([grade],))
    processes.append(p)
    p.start()

for p in processes:
    p.join()


