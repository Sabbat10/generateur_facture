from produits.produis import liste_produits, total_general, ajout_produit


while True:
   
    print("== Bienvenue au KING'S STORE ==")
    print("1. Faire des achats\n2. Voir les achats dans mon panier\n3. Quitter")
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
            
            # Utilisation de la fonction ajout_produit
            liste_produits = ajout_produit(liste_produits, entrer_produit, entrer_quantite, entrer_prix, total_produit)
            print(liste_produits)

            # Mise à jour du total général
            total_general += total_produit
            print("")
            
            # Affichage du produit ajouté
            print("Les produits ont été ajoutés avec succès.")
            print(f" Nom du produit: {entrer_produit}\n Quantité: {entrer_quantite}\n Prix unitaire: {entrer_prix}€\n Total: {total_produit}€")
            print("")
            
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

    elif choix == "2":
        print("")
        print("Produits achetés :")
        def afficher_produits(liste_produits):
            for produit in liste_produits:
                print(f"{produit['nom']}, \n - Quantité : {produit['quantite']}, Prix unitaire : {produit['prix_unitaire']}€, Total : {produit['total']}€")
            print(f"Total général : {total_general} €.")
            
        afficher_produits(liste_produits)
        print("")
        print("Merci de votre achat!")

    elif choix == "3":
        print("Au revoir!")
        break

    else:
        print("Choix invalide. Veuillez réessayer.")