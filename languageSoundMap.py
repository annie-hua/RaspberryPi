def generate_language_sound_map(languages, colors):
    return {language: {color: f'./audio/{language}/color/{color}.mp3' for color in colors} for language in languages}

languages = [
    'English',
    'Spanish',
    'Chinese',
    'Filipino', #Tagalog
    'Vietnamese',
    'Arabic',
    'Korean',
    'Hindi',
    'Russian',
    'German',
    'Portuguese',
    'Italian',
    'Urdu',
    'Telugu',
    'Persian',
    'Gujarati',
    'Hungarian',
    'Cantonese'
]
colors = ['red', 'yellow', 'blue', 'green', 'orange', 'black', 'white', 'gray', 'brown', 'pink', 'purple']

languageSoundMap = generate_language_sound_map(languages, colors)