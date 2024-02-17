import pyautogui

try:
    while True:
        # Obtenir les coordonnées de la position de la souris
        x, y = pyautogui.position()
        
        # Afficher les coordonnées en temps réel
        print(f"Position de la souris : x = {x}, y = {y}", end='\r', flush=True)
except KeyboardInterrupt:
    print("\nTerminé.")
