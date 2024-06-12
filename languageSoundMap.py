def generate_language_sound_map(languages, colors):
    return {language: {color: f'./sounds/{language}/{color}.mp3' for color in colors} for language in languages}

languages = ['English', 'Spanish', 'Cantonese']
colors = ['red', 'yellow', 'blue', 'green', 'orange']

languageSoundMap = generate_language_sound_map(languages, colors)