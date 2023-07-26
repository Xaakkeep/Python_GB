import csv

def read_phones():
    print(f'\nКонтакты:\n')
    with open('phonebook.csv', 'r', newline='',encoding='utf-8') as csvfile:
        base_read = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for i in base_read:
            print(', '.join(i))
    main()        
def add_phones():
    print(f'Добвление контакта:\n')
    with open('phonebook.csv', 'a', encoding='utf-8') as w_file:
        # names = ["Фамилия", "Имя", "Телефон", "Описание"]
        # files_add = csv.DictWriter(w_file, delimiter=',', lineterminator='\r', fieldnames=names)
        
        files_add = csv.writer(w_file, delimiter=',', lineterminator='\r')
                
        surname, name, tel = input("Введите контакт через пробел(Фамилия Имя Телефон): \n").split()
        description = input("Добавьте описание контакта: ")
        # files_add.writeheader()
        # files_add.writerow({"Фамилия": surname, "Имя" : name, "Телефон" : tel, "Описание" : description})
        files_add.writerow([surname, name, tel, description])
        

def del_phones():
    pass
       
def fine_phones():
    pass            
            
def main():            
    print(f'Телефоный справочник:\n'
        f'1. Чтение всего справочника\n'
        f'2. Добавить\n'
        f'3. Поиск\n'
        f'4. Удалить\n'
        f'5. Выход')

    user_input = int(input("Ввод: "))
    if user_input == 1:
        read_phones()
    elif user_input == 2:
        add_phones()
    elif user_input == 3:
        fine_phones()
    elif user_input == 4:
        del_phones()
    else:
        pass

if __name__ == "__main__":
    main()