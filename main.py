import sys
from datetime import date
from task import TaskManager

# Константы для приоритетов и статусов
PRIORITIES = ["низкий", "средний", "высокий"]
STATUSES = ["не выполнена", "выполнена"]

def get_input_with_validation(value, valid_options=None, allow_empty=False, validate_func=None):
    """
    Функция для ввода с валидацией.
    
    value: Значение ввода.
    valid_options: Список допустимых вариантов.
    allow_empty: Если True, разрешить пустой ввод.
    validate_func: Функция для дополнительной валидации.
    """
    while True:
        user_input = input(value).strip()
        if not user_input and allow_empty:
            break
        if not user_input and not allow_empty:
            print("Ошибка: пустая строка, введите значение.")
            continue
        if valid_options and user_input not in valid_options:
            print(f"Ошибка: введено недопустимое значение. Доступные варианты: {', '.join(valid_options)}")
            continue
        if validate_func and not validate_func(user_input):
            print("Ошибка: введено недопустимое значение.")
            continue
        return user_input

def validate_date(date_str):
    """Валидатор для даты."""
    try:
        date.fromisoformat(date_str)
        return True
    except ValueError:
        return False

def main():
    task_manager = TaskManager()

    while True:
        print("\n---------------Меню---------------")
        print("1. Просмотр всех задач")
        print("2. Просмотр задач по категории")
        print("3. Добавить задачу")
        print("4. Изменить задачу")
        print("5. Отметить задачу как выполненную")
        print("6. Удалить задачу")
        print("7. Удалить задачи по категории")
        print("8. Поиск задач")
        print("9. Выход")
        print("-----------------------------------")

        choice = input("Выберите действие (цифру): ")

        if choice == '1':
            task_manager.show_tasks()

        elif choice == '2':
            category = input("Введите категорию: ")
            task_manager.show_tasks(category=category)

        elif choice == '3':
            title = get_input_with_validation("Введите название задачи: ")
            description = get_input_with_validation("Введите описание задачи: ")
            category = get_input_with_validation("Введите категорию задачи: ")
            due_date = get_input_with_validation("Введите срок выполнения (yyyy-mm-dd): ", validate_func=validate_date)
            priority = get_input_with_validation("Введите приоритет (низкий, средний, высокий): ", valid_options=PRIORITIES)
            task_manager.add_task(title, description, category, due_date, priority)

        elif choice == '4':
            try:
                task_id = int(input("Введите ID задачи для изменения: "))
                title = input("Введите новое название (или оставьте пустым): ")
                description = input("Введите новое описание (или оставьте пустым): ")
                category = input("Введите новую категорию (или оставьте пустым): ")
                due_date = get_input_with_validation("Введите новый срок выполнения (или оставьте пустым): ", validate_func=validate_date, allow_empty=True)
                priority = get_input_with_validation("Введите новый приоритет (низкий/средний/высокий или оставьте пустым): ", valid_options=PRIORITIES, allow_empty=True)
                status = get_input_with_validation("Введите новый статус (выполнена/не выполнена или оставьте пустым): ", valid_options=STATUSES, allow_empty=True)
                task_manager.edit_task(task_id, title, description, category, due_date, priority, status)
            except ValueError:
                print("Ошибка: неверный формат id")

        elif choice == '5':
            try:
                task_id = int(input("Введите ID задачи для отметки как выполненной: "))
                task_manager.mark_as_completed(task_id)
            except ValueError:
                print("Ошибка: неверный формат id")

        elif choice == '6':
            try:
                task_id = int(input("Введите ID задачи для удаления: "))
                task_manager.delete_task(task_id)
            except ValueError:
                print("Ошибка: неверный формат id")

        elif choice == '7':
            category = input("Введите категорию для удаления задач: ")
            task_manager.delete_tasks_by_category(category)

        elif choice == '8':
            print("Варианты поиска:")
            print("8.1. Поиск по ключевым словам")
            print("8.2. Поиск по категории")
            print("8.3. Поиск по статусу")
            find = input("Выберите вариант поиска: ")
            if find == '8.1':
                query = input("Введите запрос для поиска: ")
                task_manager.find_tasks(query)
            elif find == '8.2':
                category = input("Введите категорию для поиска: ")
                task_manager.find_tasks_category(category)
            elif find == '8.3':
                status = input("Введите статус для поиска: ")
                task_manager.find_tasks_status(status)
            else:
                print("Неверный выбор. Пожалуйста, выберите действие из меню.")

        elif choice == '9':
            sys.exit()

        else:
            print("Неверный выбор. Пожалуйста, выберите действие из меню.")

if __name__ == "__main__":
    main()
