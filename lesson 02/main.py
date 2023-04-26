import task_10
import task_12
import task_14


def main():
    task_input = int(input('Выберите задние 10, 12, 14: '))
    if task_input == 10:
        task_10.task()
    elif task_input == 12:
        task_12.task()
    elif task_input == 14:
        task_14.task()
      


if __name__ == "__main__":
    main()