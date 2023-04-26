import task_26
import task_28

def main():
    task_input = int(input('Выберите задние 26, 28: '))
    if task_input == 26:
        task_26.task()
    elif task_input == 28:
        task_28.task()


if __name__ == "__main__":
    main()