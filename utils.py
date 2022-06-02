import random

dictionary = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
    }


def get_ending(number: int, kit: list) -> str:
    """Returns a correct ending for word

    :param number: number to match the word with
    :param kit: set of endings
    :return: correct ending from the set
    """
    if (not isinstance(number, int) or
            not isinstance(kit, list) or
            len(kit) != 3):
        return ""
    if 10 < number % 100 < 15:
        return kit[0]
    temp = number % 10
    if temp == 1:
        return kit[1]
    elif 1 < temp < 5:
        return kit[2]
    else:
        return kit[0]


def morse_encode(word: str) -> str:
    """Encodes word in Morse code

    :param word: word for encode
    :return: word in Morse code
    """

    encoded_word = []
    for letter in word:
        if letter in dictionary:
            encoded_word.append(dictionary[letter])
        else:
            encoded_word.append("unknown")
    return " ".join(encoded_word)


def get_word() -> str:
    """Returns a random word"""

    words = [
             "multiply", "nothing", "course", "stay", "wheel",
             "full", "force", "blue", "object", "decide",
             "surface", "deep", "moon", "island", "foot",
             "system", "busy", "test", "record", "boat", "sos"
             ]
    return random.choice(words)


def print_statistics(answers: list) -> None:
    """Prints statistic of completed tasks

    :param answers: list with results of completed tasks.
    This list must be in the format [True, False, ...]
    """

    print(f"Всего задачек: {len(answers)}")
    print(f"Отвечено верно: {answers.count(True)}")
    print(f"Отвечено неверно: {answers.count(False)}")
