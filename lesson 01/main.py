import task_02
import task_04
import task_06
import task_08

def main():
    task_input = int(input('Выберите задние 2, 4, 6, 8: '))
    if task_input == 2:
        task_02.task()
    elif task_input == 4:
        task_04.task()
    elif task_input == 6:
        task_06.task()
    elif task_input == 8:
        task_08.task()        


if __name__ in "__main__":
    main()