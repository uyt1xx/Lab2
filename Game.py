import random

def guess_the_number():
    number_to_guess = random.randint(1, 10)
    attempts = 3

    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 10. У вас есть 3 попытки, чтобы угадать его.")

    for attempt in range(1, attempts + 1):
        try:
            user_guess = int(input(f"Попытка {attempt}: Введите ваше число: "))

            if user_guess == number_to_guess:
                print(f"Поздравляю! Вы угадали число {number_to_guess} с {attempt}-й попытки!")
                return
            elif user_guess < number_to_guess:
                print("Загаданное число больше.")
            else:
                print("Загаданное число меньше.")
        except ValueError:
            print("Пожалуйста, введите корректное число.")

    print(f"Вы исчерпали все попытки. Загаданное число было: {number_to_guess}. Удачи в следующий раз!")

if __name__ == "__main__":
    guess_the_number()
