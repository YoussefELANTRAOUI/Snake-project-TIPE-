from snakeql import SnakeQAgent
import os

# Créer le dossier pickle s'il n'existe pas
if not os.path.exists('pickle'):
    os.makedirs('pickle')

print("Démarrage de l'entraînement...")
agent = SnakeQAgent()

# L'entraînement va prendre un moment (10 000 épisodes par défaut)
# Il affichera la progression tous les 25 épisodes
agent.train()

print("Entraînement terminé !")