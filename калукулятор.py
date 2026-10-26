print("=== Калькулятор ===")
while True:
    first = input("\nВведи перове число (или q для выхода): ")
    if first == "q":
        print("Пока!")
        break
    a = float(first)
    op = input("Введи действие (+, -, *, /):")
    b = float(input("Введи второе число :"))
    if op =="+":
        print("Результат:", a + b )
    elif op == "-":
        print("Результат:", a - b)
    elif op == "*":
        print("Результат:", a * b)
    elif op == "/":
        if b == 0:
             print("Ошибка: на ноль делить нельзя9")
        else:
             print("Результат:", a / b)
    else:
         print("Ошибка : такого действия нет")
