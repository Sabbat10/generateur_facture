liste_produits = []  # Liste pour stocker les produits
total_general = 0  # Variable pour le total de tous les prix

while True:
    print("1. Faire des achats\n2. Consulter le solde\n3. Quitter")
    choix = input("Entrez votre choix: ")

    if choix == "1":
        try:
            entrer_produit = input("Entrez le nom du produit: ")
            entrer_quantite = int(input("Entrez la quantité: "))
            entrer_prix = int(input("Entrez le prix du produit: "))

            if entrer_quantite <= 0:
                print("La quantité doit être supérieure à 0.")
                continue
            if entrer_prix <= 0:
                print("Le prix doit être supérieur à 0.")
                continue

            # Calcul du total pour ce produit
            total_produit = entrer_quantite * entrer_prix

            # Ajout du produit à la liste
            liste_produits.append({
                "nom": entrer_produit,
                "quantite": entrer_quantite,
                "prix_unitaire": entrer_prix,
                "total": total_produit
            })

            # Mise à jour du total général
            total_general += total_produit
            print("")
            print(f"Vous avez ajouté {entrer_quantite} de {entrer_produit} au prix de {entrer_prix} euros chacun.")
            print(f"Total pour ce produit : {total_produit} euros.")
            print("Merci pour votre achat!")
            print("")

        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

    elif choix == "2":
        print("Produits achetés :")
        for produit in liste_produits:
            print(f"- {produit['nom']}: {produit['quantite']} x {produit['prix_unitaire']}€ = {produit['total']}€")
        print(f"Total général : {total_general} €.")

    elif choix == "3":
        print("Au revoir!")
        break

    else:
        print("Choix invalide. Veuillez réessayer.")