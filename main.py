import random

print("NUMBER CONVERSION GAME")
print("(You can use underscores between the digits to make it more readable for you, especially binary digits)\n")
hint = "Level choices: Newbie, Easy, Medium, Hard, Expert"
print(hint)
LEVELS = {"newbie": (1, 9), "easy": (10, 99), "medium": (100, 999), "hard": (1000, 9999), "expert": (10000, 99999)}
NUMBER_BASES = {'b': "Binary", 'o': "Octal", 'd': "Decimal", 'x': "Hexadecimal"}


def input_level():
    level = input("Level: ").lower()
    if level not in LEVELS.keys():
        print(hint)
        return input_level()
    return level


level = input_level()
level_data = LEVELS[level]

QUESTION_AMOUNT = 5
score = 0
for i in range(QUESTION_AMOUNT):
    question_base = random.choice(list(NUMBER_BASES.keys()))
    answer_base = random.choice([i for i in list(NUMBER_BASES.keys()) if i != question_base])
    print("\nQuestion " + str(i + 1) + "/" + str(QUESTION_AMOUNT))
    print(NUMBER_BASES[question_base] + " => " + NUMBER_BASES[answer_base])
    question_random = random.randint(level_data[0], level_data[1])
    true_answer = format(question_random, answer_base)
    answer = input(format(question_random, question_base) + " => ").lower().replace('_', '')
    if (answer == true_answer):
        score += 1
        print("Correct answer!")
    else:
        print("Oops, the correct answer is", true_answer)

print("\nCongratulations, you have finished the " + level + " level with " + str(
    score * (100 / QUESTION_AMOUNT)) + "% score.")
