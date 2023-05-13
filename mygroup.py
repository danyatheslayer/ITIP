groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5],
    },
    {
        "name": "Дарья",
        "surname": "Ветрова",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4],
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5],
    },
    {
        "name": "Данил",
        "surname": "Кузнецов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [4, 4, 4],
    },
    {
        "name": "Георгий",
        "surname": "Сырников",
        "exams": ["БЖД", "ИС", "ИТИП"],
        "marks": [5, 5, 3],
    },
    {
        "name": "Артемий",
        "surname": "Лебедев",
        "exams": ["Ассемблер", "ИБ", "СИИ"],
        "marks": [4, 4, 5],
    },
]


def print_students(students):
    print(
        "Имя".ljust(15), "Фамилия".ljust(10), "Экзамены".ljust(30), "Оценки".ljust(20)
    )
    for student in students:
        print(
            student["name"].ljust(15),
            student["surname"].ljust(10),
            str(student["exams"]).ljust(30),
            str(student["marks"]).ljust(20),
        )


def sort_by_average(students, mark):
    print(
        "Имя".ljust(15), "Фамилия".ljust(10), "Экзамены".ljust(30), "Оценки".ljust(20)
    )
    for student in students:
        if ((sum(student["marks"])/ len(student["marks"])) > mark):
            print(
                student["name"].ljust(15),
                student["surname"].ljust(10),
                str(student["exams"]).ljust(30),
                str(student["marks"]).ljust(20),
            )

def main():
    try:
        user_input = float(input("Введите число: "))
        sort_by_average(groupmates, user_input)
    except ValueError:
        print("Ошибка: Вы ввели не число.")

if __name__ == '__main__':
    main()
