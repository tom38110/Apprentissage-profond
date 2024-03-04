import os

def rename_images(folder_path):
    # Vérifier si le chemin fourni est un dossier
    if not os.path.isdir(folder_path):
        print("Le chemin spécifié n'est pas un dossier valide.")
        return
    
    # Obtenir la liste des fichiers dans le dossier
    files = os.listdir(folder_path)
    
    # Filtrer les fichiers pour ne garder que les images
    image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    
    # Parcourir toutes les images et les renommer
    for i, image_file in enumerate(image_files):
        # Obtenir le chemin complet de l'image à renommer
        old_path = os.path.join(folder_path, image_file)
        
        # Créer le nouveau nom de fichier
        new_name = os.path.join(folder_path, f"image_{i}.{image_file.split('.')[-1]}")
        
        # Renommer l'image
        os.rename(old_path, new_name)
        
        print(f"L'image {image_file} a été renommée en {os.path.basename(new_name)}.")

# Utilisation de la fonction
folder_path = "./Validation/Gare_Matabiau"  # Chemin actuel
rename_images(folder_path)

