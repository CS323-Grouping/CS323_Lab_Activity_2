import multi, threads

import utils as utils


if __name__ == "__main__":
    grades = utils.inputGrades()

    print("--Threads--")
    threads.startThreading(grades)

    grades = utils.inputGrades()

    print("--multi process--")
    multi.startMulti(grades)




