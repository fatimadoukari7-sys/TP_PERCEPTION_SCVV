import pyttsx3

phrase = "Bonjour,Définissez brièvement le principe de la synthèse vocale (TTS) et identifiez au moins trois bibliothèques Python couramment utilisées (par exemple : une solution hors-ligne, une solution en ligne et une solution basée sur les voix neuronales)."


# Initialiser le moteur de synthèse
moteur = pyttsx3.init()

# Régler la vitesse de parole (mots par minute)
moteur.setProperty('rate', 150)

# Chercher une voix française parmi les voix installées
for voix in moteur.getProperty('voices'):
    if 'fr' in voix.id.lower() or 'french' in voix.name.lower():
        moteur.setProperty('voice', voix.id)
        break

# Lecture directe
moteur.say(phrase)
moteur.runAndWait()

# Enregistrement dans un fichier audio
moteur.save_to_file(phrase, "sortie_pyttsx3.wav")
moteur.runAndWait()