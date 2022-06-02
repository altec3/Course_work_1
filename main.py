from utils import get_word, get_ending, morse_encode, print_statistics

TASK_COUNT = 3

# dictionary with sets of endings
ENDS = {1: ["о", "а", "о"], 2: ["ых", "ая", "ые"], 3: ["ей", "ь", "и"]}


# Intro
print(
    "Сегодня мы потренируемся расшифровывать азбуку Морзе."
    "\nВам будет показан{} {} кодов{} последовательност{}. "
    "Ваша задача определить, что за слова или фразы "
    "закодированны в данных последовательностях.".format(
        get_ending(TASK_COUNT, ENDS[1]),
        TASK_COUNT,
        get_ending(TASK_COUNT, ENDS[2]),
        get_ending(TASK_COUNT, ENDS[3]),
    ))

# The block of tasks output
if input(
       "\nЕсли передумали, введите \"exit\""
       "\nДля продолжения нажмите Enter "
       ).lower() != "exit":
    answers = []

    for task in range(TASK_COUNT):
        word = get_word()
        print(f"\nСлово {task + 1}: {morse_encode(word)}")

        user_answer = input("Ваш ответ: ").lower()
        if user_answer == word:
            print(f"Верно, {word.title()}!")
            answers.append(True)
        else:
            print(f"Неверно! Правильный ответ {word.title()}.")
            answers.append(False)

    # The block of results output
    print()
    print_statistics(answers)
