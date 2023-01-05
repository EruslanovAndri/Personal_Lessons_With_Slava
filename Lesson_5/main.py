# name: str - имя пользователя
# surname: str - фамилия пользователя
# number: int - номер телефона пользователя

# change name - изменить имя
# change surename - изменит фамилию
# change number - изменить номер
# see_info - вывести информацию (магический метод)

class PhonePerson:
    def __init__(self, name: str='', surname: str='', number: int=0):
        self.name = name
        self.surname = surname
        self.number = number


    def change_name(self, new_name):
        if not isinstance(new_name,str):
            raise ValueError('New name is not str')
        self.name = new_name

    def change_surname(self,new_surname):
        if not isinstance(new_surname,str):
            raise ValueError('New surname os not str')
        self.surname = new_surname

    def change_numbers(self, new_number):
        if not isinstance(new_number,int):
            raise ValueError('New number is not int')
        if len(str(new_number)) != 11:
            raise ValueError('Length of the new number is not correct')
        self.number = new_number
            
    def __str__(self) -> str:
        return f'Name: {self.name}, Surname: {self.surname}, Telephone: {self.number}'
        



first = PhonePerson('Andrey','Eruslanov',89263133828)
print(first.name,first.surname)
first.change_name(new_name='Ivan')
print(first.name)
print(first.name,first.surname)
first.change_surname(new_surname='Ivanov')
print(first.surname)
first.change_numbers(new_number=99999999999)
print(first.number)
first.__str__()
print(first)
