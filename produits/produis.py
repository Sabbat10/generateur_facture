liste_produits = []  # Liste pour stocker les produits
total_general = 0  # Variable pour le total de tous les prix


# entrer_produit = input("Entrez le nom du produit: ")
# entrer_quantite = int(input("Entrez la quantité: "))
# entrer_prix = int(input("Entrez le prix du produit: "))

def ajout_produit(produits, nom_produit, quantite_produit, prix_produit, total_produit):
    
     produits.append({
          "nom": nom_produit,
          "quantite": quantite_produit,
          "prix_unitaire": prix_produit,
          "total": total_produit
    })
     
     return produits