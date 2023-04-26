import task_22
import task_24

def main():
    task_input = int(input('Выберите задние 22, 24: '))
    if task_input == 22:
        task_22.task()
    elif task_input == 24:
        task_24.task()
        
if __name__ == "__main__":
    main()