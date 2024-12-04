# Консольное приложение "Менеджер задач"

## Описание
Консольное приложение для управления списком задач.  
Приложение позволяет добавлять, удалять, изменять, искать и отображать задачи.  
Каждая задача содержит следующие поля:  
 * id (уникальный идентификатор, генерируется автоматически)
 * title (название задачи)
 * description (описание задачи)
 * category (категория задачи)
 * due_date (срок выполнения задачи)
 * priority (приоритет задачи: низкий/средний/высокий)
 * status (статус задачи: не выполнена/выполнена)

---
## Функционал
1. Просмотр задач: 
* Просмотр всех текущих задач. 
* Просмотр задач по категориям (например, работа, личное, обучение). 
2. Добавление задачи: Добавление новой задачи с указанием названия, описания, категории, срока 
выполнения и приоритета (низкий, средний, высокий). 
3. Изменение задачи: 
* Редактирование существующей задачи. 
* Отметка задачи как выполненной. 
4. Удаление задачи: Удаление задачи по идентификатору или категории. 
5. Поиск задач: Поиск по ключевым словам, категории или статусу выполнения.  
Данные хранятся в json файле. Есть обработка ошибок.

---
## Инструкция по использованию
### Запуск приложения
1. Скачайте и установите Python.
2. Скачайте репозиторий.
3. Запустите приложение в консоли с помощью команды `python main.py`

### Использование приложения
При запуске приложения отобразится меню.  
```
---------------Меню---------------
1. Просмотр всех задач
2. Просмотр задач по категории
3. Добавить задачу
4. Изменить задачу
5. Отметить задачу как выполненную
6. Удалить задачу
7. Удалить задачи по категории
8. Поиск задач
9. Выход
-----------------------------------
Выберите действие (цифру):
```
В консоль выводятся подсказки о том, что необходимо ввести.

## Тестирование
Для того чтобы запустить тестирование введите в консоль `python -m unittest test_task_manager.py`
