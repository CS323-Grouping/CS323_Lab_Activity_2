import time
from multiprocessing import Process


def compute_gwa_mp(grades):
    gwa = sum(grades) / len(grades)
    print(f"[Process] Calculated GWA: {gwa}")


processes = []

def startMulti(grades_list):

    start = time.time()
    for grade in grades_list:
        p = Process(target=compute_gwa_mp, args=([grade],))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end = time.time()

    print(f"Multiprocess ended in {end-start}")