def inputGrades() -> list[int]:
    res = []
    ans = input("Use Local File (y/n): ")

    if ans.lower() == "y":
        with open ("grades.txt", "r") as file:
            for i in file:
                res.append(int(i.strip()))
    else:
        while True:
            a = input("Enter Input (x for exit) : ")

            if a == "x":
                break
            res.append(int(a))

    return res
