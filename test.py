

def input_surname():
    return input('Введите фамилия контакта: ').title()


def input_name():
    return input('Введите имя контакта: ').title()


def input_patronymic():
    return input('Введите отчество: ').title()

def input_phone():
    return input('Введите телефон контакта: ')

def input_address():
    return input('Введите адресс контакта: ').title()

def read_phonebook(file = 'phonebook.txt'):
    with open(file, 'r', encoding='utf-8') as file:
        contacts_str = file.read()
        return contacts_str.rstrip().split('\n\n')
    
def write_phonebook(contact_list):
    with open('phonebook.txt', 'w', encoding='utf-8') as file:
        file.write(str.join('\n\n', contact_list) + '\n\n')

def copy_data():
    file = input('Введите имя файла: ')
    idx = int(input('выберите индекс контакта: '))
    contact_list = read_phonebook()
    while ( idx > len(contact_list) - 1 ):
        print('некорректный ввод! Индекс должен быть меньше ' + len(contact_list))
        idx = input('выберите индекс контакта: ')

    contact = contact_list[idx]

    with open(file, 'a', encoding='utf-8' ) as file:
        file.write(contact + '\n\n')

def make_contact(surname, name, patronymic, phone, address):
    return f'{surname} {name} {patronymic}: {phone}\n{address}'

def edit_contact():
    idx = int(input('выберите индекс контакт: '))
    contact_list = read_phonebook()
    while ( idx > len(contact_list) - 1):
        print('некорректный ввод! Индекс должен быть меньше' + len(contact_list))
        idx = input('выберите индекс контакта: ')

        contact = contact_list[idx]
        print('Изменить данные контакта: ')
        print(contact)

    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()

    contact_list[idx] = make_contact(surname, name, patronymic, phone, address)
    write_phonebook(contact_list)

def delete_contact():
    idx = int(input('выберите индекс контакта: '))
    contact_list = read_phonebook()
    while ( idx > len(contact_list) - 1):
        print('некорректный ввод! Индекс должен быть меньше' + len(contact_list))
        idx = input('выберите индекс контакта: ')

        contact = contact_list[idx]
        print('Вы хотите удалить этот контакт? ')
        print(contact)
        var = input('если "Да" введите 1: ')
        if var == '1':
            contact_list.pop(idx)
            write_phonebook(contact_list)




def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f'{surname} {name} {patronymic}: {phone}\n{address}\n\n'

def add_contact():
    contact_str = create_contact()
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(contact_str)

    
def print_contacts():
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_str = file.read()
        contacts_list = contacts_str.rstrip().split('\n\n')
        for n, contact in enumerate(contacts_list, 1):

          print(n, contact)
    
        
def search_contact():
    print(
        'Возможные вариаты  поиска:\n'
        '1. По фамилии\n'
        '2. По Имени\n'  
        '3. По отчеству\n'
        '4. По телефону\n'
        '5. По адресу(городу)\n'
        )
    var = input('выберите вариан поиска: ')
    while var not in ('1', '2', '3', '4', '5'):
            print('некорректный ввод!')
            var = input('выберите вариан поиска: ') 
            i_var = int(var)


    search = input('Введите данные для поиска: ').title()
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
         contacts_str = file.read()
         #print(contacts_str) 
         contacts_list = contacts_str.rstrip().split('\n\n')
         #print(list_contacts)

    for str_contact in contacts_list:
     lst_contact = str_contact.replace(':', '').split()
     if search in lst_contact[i_var]:
         #lst_contact = str_contact.split()

         print(str_contact)


    def interface():
       with open("phonebook.txt", "a", encoding='utf-8'):
        pass

    var = 0
    while var != '6':
        print(
        'Возможные вариаты:\n'
        '1. Добавить контакт\n'
        '2. Вывести на экран\n'  
        '3. Поиск контакта\n'
        '4. Редактирование контакта\n'
        '5. Удаление контакта\n'
        '6. Копирование данных\n'
        '7. Выход'
        )
        print()

        var = input('выберите вариан действия: ')
        while var not in ('1', '2', '3', '4', '5', '6', '7'):
            print('некорректный ввод!')
            var = input('выберите вариан действия: ')    
    print()
    match var:
        case '1':
            add_contact()
        case '2':
            print_contacts()
        case '3':
            search_contact()
        case '4':
            edit_contact()
        case '5':
            delete_contact()
        case '6':
            copy_data
        case '7':
                        
            print('До свидания')
    print()

if __name__ == '__main__':
   
   interface()







