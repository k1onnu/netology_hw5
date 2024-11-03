from datetime import datetime

def main():
    formats = {
        "The Moscow Times": "%A, %B %d, %Y",
        "The Guardian": "%A, %d.%m.%y",
        "Daily News": "%A, %d %B %Y"
    }

    print("Введите дату в формате:\n"
          "1. The Moscow Times — 'Wednesday, October 2, 2002'\n"
          "2. The Guardian — 'Friday, 11.10.13'\n"
          "3. Daily News — 'Thursday, 18 August 1977'\n"
          "Для выхода введите 'exit'.\n")

    while True:
        user = input("Введите дату:")
        if user.lower() == 'exit':
            break

        converted_date = None
        for name, fmt in formats.items():
            try:
                converted_date = datetime.strptime(user, fmt)
                print(f"{name}: {converted_date}")
                break
            except ValueError:
                continue

        if converted_date is None:
            print("Неверный формат даты.")

if __name__ == "__main__":
    main()