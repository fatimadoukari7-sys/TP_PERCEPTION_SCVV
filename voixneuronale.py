# Installation : pip install coqui-tts
from TTS.api import TTS

phrase = "Bonjour,Définissez brièvement le principe de la synthèse vocale (TTS) et identifiez au moins trois bibliothèques Python couramment utilisées (par exemple : une solution hors-ligne, une solution en ligne et une solution basée sur les voix neuronales)."


# Charger un modèle neuronal français (téléchargé automatiquement la 1re fois)
tts = TTS("tts_models/fr/css10/vits")

# Générer le fichier audio
tts.tts_to_file(text=phrase, file_path="sortie_coqui.wav")
print("Fichier audio créé : sortie_coqui.wav")