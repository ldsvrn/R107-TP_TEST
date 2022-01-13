def produit_scalair():
    vecteurs = []
    for i in range(2):
        try:
            vecteurs.append(input(f"Merci de saisir les composantes du vecteur V{i+1}: ").split(','))
            for j in range(len(vecteurs[i])):
                vecteurs[i][j] = int(vecteurs[i][j])

            if len(vecteurs[i]) == 1: # Lance une erreur si len = 1 pour executer le "except"
                raise Exception("len 1")
        except:
            print("Un des deux vecteurs est composé d'un seul élément ou bien un autre séparateur a été utilisé!")
            return -1

    if len(vecteurs[0]) != len(vecteurs[1]):
        print("Les deux vecteurs ne sont pas de même taille!")
        return -2

    scalaire = 0
    for v1, v2 in zip(vecteurs[0], vecteurs[1]):
        scalaire += v1 * v2

    return scalaire


print(f"Le produit scalaire est {produit_scalair()}")