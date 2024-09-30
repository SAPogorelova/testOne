
# Приложение представляет собой простой менеджер задач с возможностью добавления, удаления и отметки задач как выполненных.
# Даты для задач задаются в формате "ДД-ММ-ГГГГ" и проверяются на корректность.
# Все данные о задачах хранятся в списке `tasks`, что позволяет управлять ими легко и удобно


import tkinter as tk # библиотека для создания графических интерфейсов.
from tkinter import messagebox # модуль для отображения предупреждений и других диалоговых окон.
from datetime import datetime # модуль для работы с датами и временем.


# Функция для добавления новой задачи
def add_task():
    task_name = task_entry.get() # `task_entry.get()`: получает текст, введенный в поле ввода для названия задачи
    start_date = start_date_entry.get() #получает текст из поля ввода для даты начала
    due_date = due_date_entry.get() #получает текст из поля ввода для срока выполнения

    # Проверка, что введено хотя бы название задачи
    if task_name:
        task_str = task_name #Проверяется, что название задачи не пустое. Если оно задано, то создается строка `task_str`

        # Попытка преобразования дат в правильный формат, если они введены
        if start_date:
            try:
                start_date_obj = datetime.strptime(start_date, "%d-%m-%Y")
                task_str += f" (Начало: {start_date})"
            except ValueError:
                messagebox.showwarning("Ошибка", "Введите дату начала в формате ДД-ММ-ГГГГ")
                return #попытка преобразовать строку, введенную в поле даты начала, в объект `datetime`. Если формат неправильный, отображается предупреждение.
                        #Аналогично обрабатывается и срок выполнения задачи

        if due_date:
            try:
                due_date_obj = datetime.strptime(due_date, "%d-%m-%Y")
                task_str += f", Срок: {due_date}"

                # Проверка, что дата выполнения не раньше даты начала
                if start_date and due_date_obj < start_date_obj:
                    messagebox.showwarning("Ошибка", "Дата выполнения задачи не может быть раньше даты начала")
                    return
            except ValueError:
                messagebox.showwarning("Ошибка", "Введите дату выполнения в формате ДД-ММ-ГГГГ")
                return
        # добавление задачи в список и словарь. Задача добавляется в виджет списка и также сохраняется в список `tasks` в виде словаря с информацией о задаче и ее статусе выполнения
        tasks_listbox.insert(tk.END, task_str)
        tasks.append({"name": task_name, "start_date": start_date, "due_date": due_date, "done": False})

        # Очистка полей после завершения ввода задачи
        task_entry.delete(0, tk.END)
        start_date_entry.delete(0, tk.END)
        due_date_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Ошибка", "Введите название задачи")


# Функция для удаления выбранной задачи. если ничего не будет выбрано для удаления, то выведется предупреждение.
def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
        tasks.pop(selected_task_index)
    except IndexError:
        messagebox.showwarning("Ошибка", "Выберите задачу для удаления")


# Функция для отметки задачи как выполненной
def mark_done():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task = tasks[selected_task_index]
        task['done'] = True

        # Обновляем задачу с отметкой о выполнении
        task_str = f"{task['name']} ✔"
        if task['start_date']:
            task_str += f" (Начало: {task['start_date']})"
        if task['due_date']:
            task_str += f", Срок: {task['due_date']}"

        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(selected_task_index, task_str)
    except IndexError:
        messagebox.showwarning("Ошибка", "Выберите задачу для отметки")


# Создаем окно приложения. Создается основное окно приложения и задается его заголовок
root = tk.Tk()
root.title("Менеджер задач")

# Задаем возможность изменения размеров окна
root.rowconfigure(3, weight=1)
root.columnconfigure(0, weight=1)

# Список для хранения задач
tasks = []

# Cоздание виджетов. Различные элементы управления (метки, поля ввода, кнопки) размещаются в главном окне с помощью метода `grid()` для управления их расположением.

# Поле ввода для новой задачи
tk.Label(root, text="Название задачи:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
task_entry = tk.Entry(root, width=50)
task_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

# Поля для ввода дат (необязательные)
tk.Label(root, text="Дата начала (ДД-ММ-ГГГГ):").grid(row=1, column=0, sticky="w", padx=10, pady=5)
start_date_entry = tk.Entry(root, width=20)
start_date_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

tk.Label(root, text="Срок выполнения (ДД-ММ-ГГГГ):").grid(row=2, column=0, sticky="w", padx=10, pady=5)
due_date_entry = tk.Entry(root, width=20)
due_date_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Кнопки управления
button_frame = tk.Frame(root)  # в целом, команда создает новый контейнер (рамку) для кнопок управления в графическом интерфейсе. это виджет, который используется для организованного размещения других виджетов. Он служит контейнером для группировки элементов интерфейса, таких как кнопки, метки и поля ввода
button_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
# row=4`**: Указывает, что рамка будет расположена в пятой строке (индексация начинается с 0).
# - **`column=0`**: Указывает, что рамка будет расположена в первом столбце (индексация также с 0).
# - **`columnspan=2`**: Указывает, что рамка будет занимать два столбца. Это позволяет сделать рамку шире и разместить элементы управления в нескольких столбцах.
# - **`padx=10`**: Устанавливает отступ (паддинг) по горизонтали (слева и справа) в 10 пикселей, что создает пространство вокруг рамки, чтобы она не прижималась плотно к границам окна.
# - **`pady=10`**: Устанавливает отступ (паддинг) по вертикали (сверху и снизу) в 10 пикселей, создавая аналогичное пространство в вертикальном направлении.
# - **`sticky="ew"`**: Этот параметр задает, как рамка будет растягиваться в пределах ячейки сетки. `ew` означает, что рамка будет растягиваться на весь доступный горизонтальный размер (восток-запад)


button_frame.columnconfigure([0, 1, 2], weight=1)
# настраивает поведение столбцов в сетке внутри контейнера `button_frame`, в данном случае, она задает веса для первых трех столбцов (столбцы с индексами 0, 1 и 2) для равномерного растягивания столбцов при растягивании размеров основного окна.

# создание кнопок управления задачами
add_button = tk.Button(button_frame, text="Добавить задачу", command=add_task)
add_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

delete_button = tk.Button(button_frame, text="Удалить задачу", command=delete_task)
delete_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

done_button = tk.Button(button_frame, text="Отметить как выполненную", command=mark_done)
done_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

# Список задач
tasks_listbox = tk.Listbox(root)
tasks_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

root.rowconfigure(3, weight=1)

# Запуск главного цикла
root.mainloop()