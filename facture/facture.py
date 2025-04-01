

# Format de la facture txt
def facture_txt(liste_produits, total_general):
    open("facture.txt", "w").write("KING'S STORE :\n")
    for produit in liste_produits:
        open("facture.txt", "w").write("Produits achetés :\n")
        open("facture.txt", "a").write(f"{produit['nom']}, \n - Quantité : {produit['quantite']}, Prix unitaire : {produit['prix_unitaire']}€, Total : {produit['total']}€\n")
    open("facture.txt", "a").write(f"Total général : {total_general} €.\n")
    print("Facture enregistrée sous format TXT.")
    
    
    
# Format de la facture Word
def facture_word(liste_produits, total_general):
    from docx import Document
    document = Document()
    document.add_heading("KING'S STORE", level=1)
    document.add_paragraph("Produits achetés :")
    for produit in liste_produits:
        document.add_paragraph(f"{produit['nom']}, \n - Quantité : {produit['quantite']}, Prix unitaire : {produit['prix_unitaire']}€, Total : {produit['total']}€")
    document.add_paragraph(f"Total général : {total_general} €.")
    document.save("facture.docx")
    print("Facture enregistrée sous format Word.")
    
    
# Format de la facture PDF
from fpdf import FPDF

from fpdf import FPDF

def facture_pdf(liste_produits, total_general):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # 🏪 Titre
    pdf.cell(200, 10, txt="KING'S STORE", ln=1, align="C")
    pdf.cell(200, 10, txt="Produits achetés", ln=1, align="C")

    # 📦 Liste des produits
    for produit in liste_produits:
        texte = f"{produit['nom']}, Quantité : {produit['quantite']}, Prix unitaire : {produit['prix_unitaire']}€, Total : {produit['total']}€"
        
        # ✅ Remplacement des caractères spéciaux
        texte = texte.encode("latin-1", "replace").decode("latin-1")  
        
        pdf.set_font("Arial", "", 12)  # Assurer la police avant chaque texte
        pdf.multi_cell(0, 10, txt=texte)  # multi_cell gère les longues lignes
    
    # 💰 Total général
    total_texte = f"Total général : {total_general} €."
    total_texte = total_texte.encode("latin-1", "replace").decode("latin-1")  # Sécuriser l'encodage
    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 10, txt=total_texte, ln=1, align="C")

    # 📄 Sauvegarde du fichier PDF
    pdf.output("facture.pdf", "F")
    print("✅ Facture enregistrée sous format PDF.")


    
    
# Format de la facture Excel
def facture_excel(liste_produits, total_general):
    import pandas as pd
    df = pd.DataFrame(liste_produits)
    df.to_excel("facture.xlsx", index=False)
    print("Facture enregistrée sous format Excel.")
