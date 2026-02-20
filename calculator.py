import tkinter as tk

root = tk.Tk()
root.title("Калькулятор")
root.geometry("380x450")
root.configure(bg="#414141")

# Поля ввода
entry1 = tk.Entry(root, font=("Helvetica", 16))
entry1.pack(pady=10)

entry2 = tk.Entry(root, font=("Helvetica", 16))
entry2.pack(pady=10)

# Окно результата
result_label = tk.Label(root, text="Результат появится здесь",
                        font=("Helvetica", 16), bg="white", fg="black")
result_label.pack(pady=20)

def format_result(value):
    if value.is_integer():
        return int(value)
    else:
        return value

# Функция суммы
def summa():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        result = a + b
        result_label.config(text=f"Сумма: {format_result(result)}")
    except ValueError:
        result_label.config(text="Ошибка: введите числа!")

# Функция разности
def raznost():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        result = a - b
        result_label.config(text=f"Разность: {format_result(result)}")
    except ValueError:
        result_label.config(text="Ошибка: введите числа!")

# Функция произведения
def proizvedenie():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        result = a * b
        result_label.config(text=f"Произведение: {format_result(result)}")
    except ValueError:
        result_label.config(text="Ошибка: введите числа!")

# Функция деления
def delenie():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        if b == 0:
            result_label.config(text="Ошибка: деление на ноль!")
        else:
            result = a / b
            result_label.config(text=f"Частное: {format_result(result)}")
    except ValueError:
        result_label.config(text="Ошибка: введите числа!")

# Кнопки
btn_sum = tk.Button(root, text="Сумма", command=summa,
                    font=("Helvetica", 14), bg="#FF7A22", fg="white")
btn_sum.pack(pady=5)

btn_sub = tk.Button(root, text="Разность", command=raznost,
                    font=("Helvetica", 14), bg="#FF7A22", fg="white")
btn_sub.pack(pady=5)

btn_mul = tk.Button(root, text="Произведение", command=proizvedenie,
                    font=("Helvetica", 14), bg="#FF7A22", fg="white")
btn_mul.pack(pady=5)

btn_div = tk.Button(root, text="Деление", command=delenie,
                    font=("Helvetica", 14), bg="#FF7A22", fg="white")
btn_div.pack(pady=5)

# Запуск приложения
root.mainloop()