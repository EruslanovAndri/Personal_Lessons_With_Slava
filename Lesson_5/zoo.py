# В зоопарке есть зайцы, лисы и медведи, они живут в вольер. 
# Реализуйте класс для каждого из животных. Затем создайте класс вольер. 
# Реализуйте внутри класса вольер поле, которое будет содержать список с экземплярами класса зверей. 
# Реализуйте метод добавления животных в вольер и просмотр всех животных из вольера.

# Три класса для трех животных rabbit,fox,bear
# Класс вольер 
# Функции в классе вольер 
    # def add_new_animals
    # def print_all_animals

class Aviary:
    def __init__(self):
        self.empty_list = []
    
    @staticmethod
    def add_information():
        name = input('Enter a name -> ')
        age = int(input('Enter an age -> '))
        gender = input('Enter gender -> ')
        return name, age, gender

    def add_rabbit_in_aviary(self):
        animal_info = self.add_information()
        rabbit = Rabbit(*animal_info)
        self.empty_list.append(rabbit)
        
    def add_fox_in_aviary(self):
        animal_info = self.add_information()
        fox = Fox(*animal_info)
        self.empty_list.append(fox)

    def add_bear_in_aviary(self):
        animal_info = self.add_information()
        bear = Bear(*animal_info)
        self.empty_list.append(bear)
    
    def __str__(self):
        return '\n'.join([str(animal) for animal in self.empty_list])

class Rabbit:
    def __init__(self,name: str='',age: int=0,gender: str=''):
        self.name = name
        self.age = age
        self.gender = gender 

    def __str__(self) -> str:
        return f'Name: {self.name},Age: {self.age},Gender: {self.gender}'

class Fox:
    def __init__(self,name: str='',age: int=0,gender: str=''):
        self.name = name
        self.age = age
        self.gender = gender 
    
    def __str__(self) -> str:
        return f'Name: {self.name},Age: {self.age},Gender: {self.gender}'

class Bear:
    def __init__(self,name: str='',age: int=0,gender: str=''):
        self.name = name
        self.age = age
        self.gender = gender 
    
    def __str__(self) -> str:
        return f'Name: {self.name},Age: {self.age},Gender: {self.gender}'

aviary = Aviary()
aviary.add_fox_in_aviary()
aviary.add_bear_in_aviary()
print(aviary)