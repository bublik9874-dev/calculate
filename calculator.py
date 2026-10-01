

def main():
    print("Добро пожаловать в калькулятор!")
    
    while True:
        print("\nВыберите операцию:")
        print("1. Сложение (+)")
        print("2. Вычитание (-)")
        print("3. Умножение (*)")
        print("4. Деление (/)")
        print("5. Выход")
        
        choice = input("\nВаш выбор (1-5): ")
        
        if choice == '5':
            print("До свидания!")
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("Неверный выбор!")
            continue
        
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка! Введите числа.")
            continue
        
        if choice == '1':
            result = num1 + num2
            print(f"Результат: {num1} + {num2} = {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"Результат: {num1} - {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"Результат: {num1} * {num2} = {result}")
        elif choice == '4':
            if num2 == 0:
                print("Ошибка! Деление на ноль.")
            else:
                result = num1 / num2
                print(f"Результат: {num1} / {num2} = {result}")

if __name__ == "__main__":
    main()
except KeyboardInterrupt:
    print("\nРабота калькулятора прекращена")
