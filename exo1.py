def triangle(N):
    for i in range(N + 1):
        for _ in range(i):
            print("*", end=" ")
        print("")


def pyramide(N):
    for i, j in zip(range(N, 0, -1), range(N)):
        for _ in range(j):
            print("", end=" ")
        for _ in range(i):
            print("*", end=" ")
        print("")


if __name__ == "__main__":
    n = int(input("Merci de préciser le nombre de lignes:  "))
    triangle(n)
    print("")
    pyramide(n)
