import unittest
from unittest.mock import patch, MagicMock
from task import TaskManager, Task, TaskStatus
import json

class TestTaskManager(unittest.TestCase):
    
    @patch('builtins.open', new_callable=MagicMock)
    def setUp(self, mock_open):
        # Сначала создадим фиктивные задачи в JSON файле
        self.mock_data = [
            {"id": 1, "title": "Задача 1", "description": "Описание 1", "category": "Категория 1", "due_date": "2024-12-31", "priority": "низкий", "status": "не выполнена"},
            {"id": 2, "title": "Задача 2", "description": "Описание 2", "category": "Категория 2", "due_date": "2024-11-30", "priority": "средний", "status": "выполнена"}
        ]
        
        # Имитируем открытие файла
        mock_open.return_value.__enter__.return_value.read.return_value = json.dumps(self.mock_data)
        
        # Создадим экземпляр TaskManager
        self.task_manager = TaskManager(file_path="tasks_test.json")
    
    def test_load_tasks(self):
        # Проверим, что задачи загружены корректно
        self.assertEqual(len(self.task_manager.tasks), 2)
        self.assertEqual(self.task_manager.tasks[0].title, "Задача 1")
        self.assertEqual(self.task_manager.tasks[1].status, "выполнена")
    
    def test_add_task(self):
        # Добавим задачу
        self.task_manager.add_task("Задача 3", "Описание 3", "категория 3", "2025-01-01", "высокий")
        self.assertEqual(len(self.task_manager.tasks), 3)
        self.assertEqual(self.task_manager.tasks[-1].title, "Задача 3")
    
    def test_edit_task(self):
        # Изменим задачу
        self.task_manager.edit_task(1, title="Обновленная задача", description="Обновленное описание")
        self.assertEqual(self.task_manager.tasks[0].title, "Обновленная задача")
        self.assertEqual(self.task_manager.tasks[0].description, "Обновленное описание")
    
    def test_mark_as_completed(self):
        # Отметим задачу как выполненную
        self.task_manager.mark_as_completed(1)
        self.assertEqual(self.task_manager.tasks[0].status, "выполнена")
    
    def test_delete_task(self):
        # Удалим задачу
        self.task_manager.delete_task(1)
        self.assertEqual(len(self.task_manager.tasks), 1)
        self.assertEqual(self.task_manager.tasks[0].title, "Задача 2")
    
    def test_find_tasks(self):
        # Проверим поиск по ключевым словам
        self.task_manager.find_tasks("Задача 2")
    
    def test_delete_tasks_by_category(self):
        # Удалим задачи по категории
        self.task_manager.delete_tasks_by_category("категория 1")
        self.assertEqual(len(self.task_manager.tasks), 1)


if __name__ == '__main__':
    unittest.main()

