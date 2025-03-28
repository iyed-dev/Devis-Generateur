import customtkinter as ctk
from tkinter import filedialog, messagebox
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
import os
from datetime import datetime

class DevisApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Générateur de Devis")
        self.geometry("750x700")
        self.configure(bg="#2e2e2e")
        
        self.nom_entreprise = "..."
        self.siret = "En cours d'immatriculation..."
        self.adresse_entreprise = "...."
        self.contact = "...."
        self.logo_path = None
        self.signature_path = None
        
        self.dossier_enregistrement = ""
        
        self.label_nom = ctk.CTkLabel(self, text="Nom du Client:", text_color="white", font=('Helvetica', 14))
        self.label_nom.pack(pady=5)
        self.entry_nom = ctk.CTkEntry(self, placeholder_text="Nom du client", font=('Helvetica', 12))
        self.entry_nom.pack(pady=5)
        
        self.label_raison_sociale = ctk.CTkLabel(self, text="Raison sociale (client professionnel):", text_color="white", font=('Helvetica', 14))
        self.label_raison_sociale.pack(pady=5)
        self.entry_raison_sociale = ctk.CTkEntry(self, placeholder_text="Raison sociale", font=('Helvetica', 12))
        self.entry_raison_sociale.pack(pady=5)
        
        self.label_adresse = ctk.CTkLabel(self, text="Adresse du Client:", text_color="white", font=('Helvetica', 14))
        self.label_adresse.pack(pady=5)
        self.entry_adresse = ctk.CTkEntry(self, placeholder_text="Adresse du client", font=('Helvetica', 12))
        self.entry_adresse.pack(pady=5)

        self.label_siren = ctk.CTkLabel(self, text="Numéro SIREN (client professionnel):", text_color="white", font=('Helvetica', 14))
        self.label_siren.pack(pady=5)
        self.entry_siren = ctk.CTkEntry(self, placeholder_text="Numéro SIREN", font=('Helvetica', 12))
        self.entry_siren.pack(pady=5)

        self.label_services = ctk.CTkLabel(self, text="Services:", text_color="white", font=('Helvetica', 14))
        self.label_services.pack(pady=5)
        
        self.services = []
        self.btn_add_service = ctk.CTkButton(self, text="Ajouter un Service", command=self.ajouter_service, font=('Helvetica', 12))
        self.btn_add_service.pack(pady=10)
        
        self.btn_logo = ctk.CTkButton(self, text="Ajouter un Logo", command=self.ajouter_logo, font=('Helvetica', 12))
        self.btn_logo.pack(pady=5)
        
        self.btn_signature = ctk.CTkButton(self, text="Ajouter une Signature", command=self.ajouter_signature, font=('Helvetica', 12))
        self.btn_signature.pack(pady=5)
        
        self.btn_dossier = ctk.CTkButton(self, text="Choisir un dossier d'enregistrement", command=self.choisir_dossier, font=('Helvetica', 12))
        self.btn_dossier.pack(pady=5)
        
        self.bouton_generer = ctk.CTkButton(self, text="Générer PDF", command=self.generer_pdf, font=('Helvetica', 14))
        self.bouton_generer.pack(pady=20)
    
    def ajouter_service(self):
        frame = ctk.CTkFrame(self)
        frame.pack(pady=5)
        entry_service = ctk.CTkEntry(frame, placeholder_text="Nom du service", font=('Helvetica', 12))
        entry_service.pack(side="left", padx=5)
        entry_quantite = ctk.CTkEntry(frame, placeholder_text="Quantité", font=('Helvetica', 12))
        entry_quantite.pack(side="left", padx=5)
        entry_prix = ctk.CTkEntry(frame, placeholder_text="Prix unitaire", font=('Helvetica', 12))
        entry_prix.pack(side="left", padx=5)
        self.services.append((entry_service, entry_quantite, entry_prix))
    
    def ajouter_logo(self):
        self.logo_path = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.jpg;*.jpeg")])
        if self.logo_path:
            messagebox.showinfo("Succès", "Logo ajouté avec succès!")
    
    def ajouter_signature(self):
        self.signature_path = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.jpg;*.jpeg")])
        if self.signature_path:
            messagebox.showinfo("Succès", "Signature ajoutée avec succès!")
    
    def choisir_dossier(self):
        self.dossier_enregistrement = filedialog.askdirectory()
        if self.dossier_enregistrement:
            messagebox.showinfo("Succès", "Dossier sélectionné avec succès!")
    
    def generer_pdf(self):
        nom_client = self.entry_nom.get()
        adresse_client = self.entry_adresse.get()
        raison_sociale = self.entry_raison_sociale.get()
        siren_client = self.entry_siren.get()
        if not self.dossier_enregistrement:
            self.dossier_enregistrement = os.getcwd()
        filename = os.path.join(self.dossier_enregistrement, f"devis_{nom_client}.pdf")
        
        doc = SimpleDocTemplate(filename, pagesize=A4)
        elements = []
        styles = getSampleStyleSheet()
        
        if self.logo_path:
            elements.append(Image(self.logo_path, width=100, height=100))
        elements.append(Paragraph(f"<b>{self.nom_entreprise}</b>", styles["Title"]))
        elements.append(Paragraph(f"SIRET: {self.siret}", styles["Normal"]))
        elements.append(Paragraph(f"Adresse: {self.adresse_entreprise}", styles["Normal"]))
        elements.append(Paragraph(f"Contact: {self.contact}", styles["Normal"]))
        elements.append(Spacer(1, 20))
        
        elements.append(Paragraph(f"<b>Devis pour: {nom_client}</b>", styles["Heading2"]))
        elements.append(Paragraph(f"Raison Sociale: {raison_sociale}", styles["Normal"]))
        elements.append(Paragraph(f"Numéro SIREN: {siren_client}", styles["Normal"]))
        elements.append(Paragraph(f"Adresse: {adresse_client}", styles["Normal"]))
        elements.append(Spacer(1, 20))
        
        data = [["Service", "Quantité", "Prix Unitaire (€)", "Total (€)"]]
        total_general = 0
        for entry_service, entry_quantite, entry_prix in self.services:
            service = entry_service.get()
            quantite = int(entry_quantite.get()) if entry_quantite.get().isdigit() else 1
            prix = float(entry_prix.get()) if entry_prix.get().replace('.', '', 1).isdigit() else 0.0
            total = quantite * prix
            total_general += total
            data.append([service, quantite, prix, total])
        
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        elements.append(table)
        elements.append(Spacer(1, 20))
        
        if total_general == 0:
            elements.append(Paragraph("<b>Offert</b>", styles["Title"]))
        else:
            elements.append(Paragraph(f"<b>Total à payer: {total_general} €</b>", styles["Title"]))
        elements.append(Paragraph("TVA non applicable, art. 293B du CGI", styles["Italic"]))
        
        elements.append(Spacer(1, 20))
        elements.append(Paragraph(f"Date d'émission: {datetime.today().strftime('%d/%m/%Y')}", styles["Normal"]))
        elements.append(Paragraph("Validité du devis: 30 jours", styles["Normal"]))
        
        if self.signature_path:
            elements.append(Image(self.signature_path, width=100, height=50))
        
        doc.build(elements)
        messagebox.showinfo("Succès", f"Devis généré: {filename}")

if __name__ == "__main__":
    app = DevisApp()
    app.mainloop()
