# Devis-Generateur
Générateur de devis légal, en Python.
Générateur de Devis en PDF avec Tkinter et ReportLab

Cette application permet de générer des devis en PDF de manière simple et personnalisée. Développée en Python, l'interface graphique utilise la bibliothèque Tkinter (et customtkinter pour une interface plus moderne et personnalisée) pour faciliter l'interaction avec l'utilisateur. Le générateur de devis permet d'ajouter des services, de spécifier leur quantité et prix, et de personnaliser le devis avec un logo et une signature.

Les fonctionnalités incluent :

Ajout des informations du client : L'utilisateur peut saisir les informations relatives au client telles que le nom, l'adresse, la raison sociale et le numéro SIREN.

Services personnalisés : Il est possible d'ajouter autant de services que nécessaire avec leur nom, quantité et prix unitaire. Le total est calculé automatiquement.

Ajout d'un logo et d'une signature : L'application permet d'ajouter un logo et une signature sous forme d'image pour personnaliser le devis.

Génération de devis en PDF : Le devis est généré au format PDF avec une mise en page professionnelle, en utilisant ReportLab, une bibliothèque puissante pour la création de documents PDF. Le PDF contient une table récapitulant les services, leurs quantités, leurs prix unitaires et leur total, ainsi que le total général.

Personnalisation des informations de l'entreprise : Les informations de l'entreprise (nom, SIRET, adresse et contact) sont automatiquement ajoutées au devis.

Enregistrement dans un dossier choisi : L'utilisateur peut choisir un dossier spécifique pour enregistrer le fichier PDF généré.

Librairies utilisées :

Tkinter : Utilisé pour créer l'interface graphique de l'application. customtkinter est une extension de Tkinter permettant de créer des interfaces modernes avec des éléments visuels plus attrayants.

ReportLab : Une bibliothèque puissante permettant de générer des documents PDF en Python. Elle est utilisée pour créer la mise en page du devis, ajouter des images et générer des tables.

filedialog : Permet à l'utilisateur de choisir un dossier ou un fichier depuis son système de fichiers.

messagebox : Affiche des boîtes de dialogue pour informer l'utilisateur du succès de ses actions (ajout de logo, sélection de dossier, génération de PDF, etc.).

Cette application est idéale pour les petites entreprises ou les freelances qui souhaitent générer des devis professionnels rapidement, avec un minimum d'effort.
