import json
from enum import Enum

class TaskStatus(Enum):
    """Перечисление для статусов задачи."""
    NOT_COMPLETED = "не выполнена"
    COMPLETED = "выполнена"

class Task:
    """
    Класс для инициализации задачи с атрибутами.
    """
    def __init__(self, id, title, description, category, due_date, priority, status = TaskStatus.NOT_COMPLETED.value):
        self.id = id
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date
        self.priority = priority
        self.status = status

    def __str__(self):
        return (f"ID: {self.id}, Title: {self.title}, Category: {self.category}, "
                f"Due Date: {self.due_date}, Priority: {self.priority}, Status: {self.status}")

class TaskManager:
    """
    Класс для управления списком задач.
    """
    def __init__(self, file_path="tasks.json"):
        self.file_path = file_path
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        """
        Функция для загрузки данных из json файла.
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.tasks = [Task(**task) for task in data]
        except FileNotFoundError:
            print(f"Ошибка: файл {self.file_path} не найден.")
        except json.JSONDecodeError:
            print(f"Ошибка: файл {self.file_path} поврежден или не содержит правильные данные.")
    
    def save_tasks(self):
        """
        Функция для сохранения данных в json файл.
        """
        with open(self.file_path, "w", encoding="utf-8") as file:
            data = [task.__dict__ for task in self.tasks]
            json.dump(data, file, indent=4, ensure_ascii=False)

    def show_tasks(self, category=None):
        """
        Функция для отображения всех задач или задач с определенной категорией.
        """
        filtered_tasks = self.tasks
        if category:
            filtered_tasks = [task for task in filtered_tasks if task.category.lower() == category.lower()]
        
        if not filtered_tasks:
            print("Задач нет.")
        else:
            for task in filtered_tasks:
                print(task)

    def add_task(self, title, description, category, due_date, priority):
        """
        Функция для добавления новой задачи.
        """
        task_id = max([task.id for task in self.tasks], default=0) + 1
        new_task = Task(task_id, title, description, category, due_date, priority)
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Задача добавлена.")

    def edit_task(self, task_id, title=None, description=None, category=None, due_date=None, priority=None, status=None):
        """
        Функция для изменения задачи.
        """
        task = next((task for task in self.tasks if task.id == task_id), None)
        if task:
            if title:
                task.title = title
            if description:
                task.description = description
            if category:
                task.category = category
            if due_date:
                task.due_date = due_date
            if priority:
                task.priority = priority
            if status:
                task.status = status
            self.save_tasks()
        else:
            print("Задача с таким id не найдена.")

    def mark_as_completed(self, task_id):
        """
        Функция для отметки задачи как выполненной.
        """
        self.edit_task(task_id, status=TaskStatus.COMPLETED.value)

    def delete_task(self, task_id):
        """
        Функция для удаления задачи.
        """
        task_to_remove = next((task for task in self.tasks if task.id == task_id), None)
        if task_to_remove:
            self.tasks.remove(task_to_remove)
            self.save_tasks()
            print(f"Задача '{task_to_remove.title}' удалена.")
        else:
            print("Ошибка: задача с таким id не найдена.")

    def delete_tasks_by_category(self, category):
        """
        Функция для удаления задач с определенной категорией.
        """
        tasks_to_remove = [task for task in self.tasks if task.category.lower() == category.lower()]
        if tasks_to_remove:
            for task in tasks_to_remove:
                self.tasks.remove(task)
            self.save_tasks()
            print(f"Задачи с категорией '{category}' удалены.")
        else:
            print("Ошибка: задачи с такой категорией не найдены.")

    def find_tasks(self, query):
        """
        Функция для поиска задач по ключевому слову.
        """
        found_tasks = [task for task in self.tasks if query.lower() in task.title.lower() or query.lower() in task.description.lower()]
        if found_tasks:
            for task in found_tasks:
                print(task)
        else:
            print("Задач с такими ключевыми словами нет.")

    def find_tasks_category(self, category):
        """
        Функция для поиска задач по категории.
        """
        found_tasks = [task for task in self.tasks if category.lower() in task.category.lower()]
        if found_tasks:
            for task in found_tasks:
                print(task)
        else:
            print("Задач с такой категорией нет.")

    def find_tasks_status(self, status):
        """
        Функция для поиска задач по статусу.
        """
        found_tasks = [task for task in self.tasks if status.lower() in task.status.lower()]
        if found_tasks:
            for task in found_tasks:
                print(task)
        else:
            print("Задач с таким статусом нет.")
