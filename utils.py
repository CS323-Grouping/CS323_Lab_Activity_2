def inputGrades() -> list[int]:
    res = []
    while True:
        a = input("Enter Input (x for exit) : ")

        if a == "x":
            break
        res.append(int(a))

    return res
