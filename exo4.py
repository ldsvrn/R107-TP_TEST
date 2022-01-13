def tabl_multi():
    n = input("Quelle table de multiplication cherchez vous?: ")

    # Pas le meilleur code, mais permet d'adapter l'affichage si nombre décimal
    try:
        n = int(n)
    except ValueError:
        try:
            n = float(n)
        except ValueError:
            return []

    table = []
    for i in range(10):
        table.append(round((i + 1) * n, 2))  # arrondi
    return table


def affich_table(L):
    print(f"Voici la table de multiplication de {L[0]}:")
    for i, item in enumerate(L):
        print(f"{L[0]} * {i + 1} = {item}")


affich_table(tabl_multi())
