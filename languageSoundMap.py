def generate_language_sound_map(languages, colors):
    return {language: {color: f'./audio/{language}/color/{color}.mp3' for color in colors} for language in languages}

def generate_language_sound_map_14_buttons(languages):
    return {
    language: {
        'level_1': {
            1: f'./audio/{language}/number/one.mp3',
            2: f'./audio/{language}/number/two.mp3',
            3: f'./audio/{language}/number/three.mp3',
            4: f'./audio/{language}/number/four.mp3',
            5: f'./audio/{language}/number/five.mp3',
            6: f'./audio/{language}/number/six.mp3',
            7: f'./audio/{language}/number/seven.mp3',
            8: f'./audio/{language}/number/eight.mp3',
            9: f'./audio/{language}/number/nine.mp3',
            10: f'./audio/{language}/number/ten.mp3',
            11: f'./audio/{language}/songs/twinkle.mp3',
            12: f'./audio/{language}/heart/iLoveYou.mp3',
            13: f'./audio/{language}/introduction/hiMyNameIsEli.mp3',
            14: f'./audio/{language}/level/levelOne.mp3',
        },
        'level_2': {
            1: f'./audio/{language}/color/blue.mp3',
            2: f'./audio/{language}/color/purple.mp3',
            3: f'./audio/{language}/color/red.mp3',
            4: f'./audio/{language}/color/pink.mp3',
            5: f'./audio/{language}/color/white.mp3',
            6: f'./audio/{language}/color/green.mp3',
            7: f'./audio/{language}/color/yellow.mp3',
            8: f'./audio/{language}/color/orange.mp3',
            9: f'./audio/{language}/color/brown.mp3',
            10: f'./audio/{language}/color/black.mp3',
            11: f'./audio/{language}/songs/rowyourboat.mp3',
            12: f'./audio/{language}/heart/hugme.mp3',
            13: f'./audio/{language}/introduction/iAmAnElephant.mp3',
            14: f'./audio/{language}/level/levelTwo.mp3',
        }
    } for language in languages
}


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
    'Cantonese',
    # 'Indonesian',
]
colors = ['blue', 'purple', 'red', 'pink', 'white', 'green', 'yellow', 'orange', 'brown', 'black']

# colors = ['red', 'yellow', 'blue', 'green', 'orange', 'black', 'white', 'gray', 'brown', 'pink', 'purple']
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
introductions = ['hiMyNameIsEli', 'iAmAnElepahnt']
levels = ['levelOne', 'levelTwo']

languageSoundMap = generate_language_sound_map(languages, colors)
languageSoundMapButtons14 = generate_language_sound_map_14_buttons(languages)