def assurance(age, annee, nbr_accident, anciennete):
    permis = 2022 - annee

    if age < 16 or nbr_accident < 0 or anciennete < 0 or permis < 0 or permis < anciennete:
        return "Anomalie"

    if anciennete >= 1:
        tarifs = ("Bleu", "Vert", "Orange", "Rouge")
    else:
        tarifs = ("Vert", "Orange", "Rouge")

    if age < 25:
        if permis < 2:
            if nbr_accident == 0:
                return tarifs[2]
            else:
                return "Refus"
        else:
            if nbr_accident == 0:
                return tarifs[1]
            elif nbr_accident == 1:
                return tarifs[2]
            else:
                return "Refus"
    else:
        if permis < 2:
            if nbr_accident == 0:
                return tarifs[1]
            elif nbr_accident == 1:
                return tarifs[2]
            else:
                return "Refus"
        else:
            if nbr_accident == 0:
                return tarifs[0]
            elif nbr_accident == 1:
                return tarifs[1]
            elif nbr_accident == 2:
                return tarifs[2]
            else:
                return "Refus"


print(assurance(26, 2020, 0, 1))
