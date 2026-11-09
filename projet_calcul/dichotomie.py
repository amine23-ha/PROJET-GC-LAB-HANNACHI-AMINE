"""Recherche d'une racine par dichotomie."""

def f(x):
    return x * x - 2

def dichotomie(a, b, precision):
    if f(a) * f(b) > 0:
        print("L'intervalle ne convient pas.")
        return None

    compteur = 0
    while b - a > precision:
        milieu = (a + b) / 2
        if f(a) * f(milieu) <= 0:
            b = milieu
        else:
            a = milieu
        compteur = compteur + 1

    resultat = (a + b) / 2
    print("Racine approchée :", resultat)
    print("Nombre d'itérations :", compteur)
    print("Vérification f(x) :", f(resultat))
    return resultat

if __name__ == "__main__":
    dichotomie(1, 2, 0.000001)
