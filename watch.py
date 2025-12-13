from visualsnake import VisualSnake

# Remplacez 10000 par le numéro de l'épisode que vous voulez voir
# (Le code sauvegarde aux épisodes 0, 10, ... 500, 1000, 1500, etc.)
episode_to_watch = 10000

game = VisualSnake()
print(f"Lancement de la démo pour l'épisode {episode_to_watch}...")
game.run_game(episode_to_watch)