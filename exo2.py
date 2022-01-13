def triangle(N):
    for i in range(N + 1):
        for j in range(i):
            print(j + 1, end=" ")
        print("")


def triangle2(N):
    for i in range(N, 0, -1):
        for j in range(i):
            print(j + 1, end=" ")
        print("")


if __name__ == "__main__":
    while True:
        try:
            n = int(input("Merci de préciser le nombre de lignes:  "))
            if n > 0:
                break
            print("Entrez un nombre supérieur à 0!")
        except ValueError:
            print("Entrez un nombre entier!")
            continue

    triangle(n)
    print("")
    triangle2(n)
