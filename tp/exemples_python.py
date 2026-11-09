"""Exemples simples pour commencer les TP de calcul numérique."""

def somme(a, b):
    return a + b

def moyenne(nombres):
    total = 0
    for nombre in nombres:
        total = total + nombre
    return total / len(nombres)

def valeur_polynome(x):
    # P(x) = x² - 4
    return x * x - 4

def determinant_2x2(a, b, c, d):
    return a * d - b * c

def distance_points(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

if __name__ == "__main__":
    print("Somme :", somme(3, 5))
    print("Moyenne :", moyenne([10, 12, 14]))
    print("P(3) :", valeur_polynome(3))
    print("Déterminant :", determinant_2x2(1, 2, 3, 4))
    print("Distance :", distance_points(0, 0, 3, 4))
