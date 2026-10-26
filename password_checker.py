import secrets
import string
def generate_password(length=16):
    """Генерирует случайный надёжный пароль."""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(alphabet) for _ in range(length))
def check_strength(password):
    """Оценивает пароль от 0 до 5 и даёт советы."""
    score = 0
    tips = []
    if len(password) >= 12:
        score += 1
    else:
        tips.append("Сделай длину от 12 символов")
    if any(c.islower() for c in password):
        score += 1
    else:
            tips.append("Добавь строчные буквы (a-z)")
    if any(c.isupper() for c in password):
        score += 1
    else:
        tips.append("Добавь заглавные буквы (A-Z)")
    if any (c.isdigit() for c in password):
        score += 1
    else:
        tips.append("Добавь цифры (0-9)")
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        tips.append("Добавь спецсимволы (!@#$...)")
    return score,tips
def main():
    while True:
        print("\n=== Password Toolkit ===")
        print("1 - Сгенерировать пароль")
        print("2 - Проверить пароль")
        print("3 - Выход")
        choice = input("Выбери действие: ")
        if choice == "1":
            length = input("Длина пароля (Enter = 16: ")
            length = int(length) if length.isdigit() else 16
            print("Твой пароль:", generate_password(length))
        elif choice =="2":
            password = input("Введи пароль: ")
            score, tips = check_strength(password)
            levels = ["Очень слабый", "Слабый", "Слабый", "Средний", "Хороший", "Отличный" ]
            print(f"Оценка: {score}/5 -{levels[score]}")
            for tip in tips:
                print(".", tip)
        elif choice == "3":
            print("Пока!")
            break
        else:
            print("Неверный выбор")
if __name__ == "__main__":
    main()