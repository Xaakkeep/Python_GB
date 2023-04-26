import task_30
import task_32

def main():
    task_input = int(input('Выберите задние 30, 32: '))
    if task_input == 30:
        task_30.task()
    elif task_input == 32:
        task_32.task()


if __name__ == "__main__":
    main()