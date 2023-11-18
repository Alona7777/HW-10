from collections import UserDict


class Field:   
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError('The phone number should be digits only and have 10 symbols')
        self.value = value


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
  
    def add_phone(self, value: str):
        phone = Phone(value)
        self.phones.append(phone)

    def remove_phone(self, phone: str):
        for item in self.phones:
            if item.value == phone:
                self.phones.remove(item)
   
    def edit_phone(self, old_phone: str, new_phone: str):   
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return phone
        raise ValueError(f'Phone: {old_phone} not found!')
            
    def find_phone(self, phone: str):
        for item in self.phones:
            if item.value == phone:
                return item
        return None
        
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record         
        
    def find(self, name: str):
        if name in self.data:
            return self.data[name]  
        return None
    
    def delete(self, name: str):
        if name in self.data:
            return self.data.pop(name)

    



if __name__ == '__main__':
    book = AddressBook()

        # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

        # Додавання запису John до адресної книги
    book.add_record(john_record)

        # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

        # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

        # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

        # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

        # Видалення запису Jane
    book.delete("Jane")
    print(book)