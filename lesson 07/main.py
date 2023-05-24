import task_34
import task_36

def main():
    task_input = int(input('Выберите задние 34, 36: '))
    if task_input == 34:
        task_34.task()
    elif task_input == 36:
        num_row = int(input("Введите количество строк: "))
        num_column = int(input("Введите количество столбцов: "))
        task_36.print_operation_table(lambda x, y: x * y, num_row, num_column)


if __name__ == "__main__":
    main()