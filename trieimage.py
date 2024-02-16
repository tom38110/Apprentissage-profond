import os
import hashlib
from PIL import Image

def get_image_hash(image_path):
    """
    Calcule le hash MD5 d'une image.
    """
    with open(image_path, 'rb') as f:
        image_hash = hashlib.md5(f.read()).hexdigest()
    return image_hash

def remove_duplicates(directory):
    """
    Supprime les images en double dans un répertoire.
    """
    image_hashes = set()
    duplicate_images = []

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            try:
                image_hash = get_image_hash(filepath)
                if image_hash in image_hashes:
                    duplicate_images.append(filepath)
                else:
                    image_hashes.add(image_hash)
            except Exception as e:
                print(f"Impossible de traiter l'image {filepath}: {e}")

    for duplicate_image in duplicate_images:
        os.remove(duplicate_image)
        print(f"Image en double supprimée : {duplicate_image}")

if __name__ == "__main__":
    directory = "Hotel_Assezat"  # Répertoire contenant les images
    remove_duplicates(directory)
