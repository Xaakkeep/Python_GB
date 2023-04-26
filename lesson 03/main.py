import task_16
import task_18
import task_20


def main():
    task_input = int(input('Выберите задние 16, 18, 20: '))
    if task_input == 16:
        task_16.task()
    elif task_input == 18:
        task_18.task()
    elif task_input == 20:
        task_20.task()
      


if __name__ == "__main__":
    main()