# Liste pour l'historique des calculs
historique_calculs = []

# Fonction pour afficher l'historique
def afficher_historique(historique):
    for calcul in historique:
        print(calcul)

def calcul_operation(nombres, operation):
    resultat = nombres[0]
    for nombre in nombres[1:]:
        if operation == '+':
            resultat += nombre
        elif operation == '-':
            resultat -= nombre
        elif operation == '*':
            resultat *= nombre
        elif operation == '/':
            if nombre == 0:
                raise ValueError("Division par zéro impossible.")
            resultat /= nombre
    return resultat

while True:
    try:
        # Liste pour stocker les nombres
        nombres = []

        # Saisie des nombres
        print("Entrez les nombres un par un suivis de '=' pour terminer :")
        while True:
            entree = input()
            if entree == "=":
                break
            nombres.append(float(entree))

        # Vérifie si au moins un nombre a été saisi
        if len(nombres) < 1:
            raise ValueError("Au moins un nombre est requis.")

        # Saisie de l'opérateur
        operation = input("Entrez l'opération (+, -, *, /) : ")

        # Vérification de l'opérateur
        if operation not in '+-*/':
            raise ValueError("Opération invalide.")

        # Effectue le calcul
        resultat = calcul_operation(nombres, operation)

        # Affiche le résultat du calcul
        print(f"Résultat : {resultat}")

        # Construire la chaîne de calcul pour l'historique
        calcul = str(nombres[0])
        for num in nombres[1:]:
            calcul += f" {operation} {num}"
        calcul += f" = {resultat}"

        # Ajoute le calcul à l'historique
        historique_calculs.append(calcul)

        # Gestion de l'historique
        choix_historique = input("Voulez-vous voir l'historique ou l'effacer ? (voir/effacer/ne rien faire) : ")
        if choix_historique.lower() == 'voir':
            afficher_historique(historique_calculs)
        elif choix_historique.lower() == 'effacer':
            historique_calculs.clear()
            print("Historique effacé.")

        # Demande si l'utilisateur veut continuer
        continuer = input("Voulez-vous effectuer un autre calcul ? (oui/non) : ")
        if continuer.lower() == 'non':
            break

    except ValueError as erreur:
        print(f"Erreur : {erreur}. Veuillez réessayer.")