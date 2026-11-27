# Installation : pip install gTTS
from gtts import gTTS

phrase = "Bonjour,Définissez brièvement le principe de la synthèse vocale (TTS) et identifiez au moins trois bibliothèques Python couramment utilisées (par exemple : une solution hors-ligne, une solution en ligne et une solution basée sur les voix neuronales)."

# Créer l'objet TTS avec la langue française (envoie le texte à Google)
tts = gTTS(text=phrase, lang='fr', slow=False)

# Sauvegarder le résultat en fichier MP3
tts.save("sortie_gtts.mp3")
print("Fichier audio créé : sortie_gtts.mp3")