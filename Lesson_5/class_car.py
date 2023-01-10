# brand - str 
# model - str
# color - str
# from prettytable import PrettyTable

# class AllCars():
#     def __init__(self, brand: str,model: str,color: str) -> None:
#         self.brand = brand
#         self.model = model
#         self.color = color

#     def add_car_to_data_base(self):
#         with open('all_cars.txt','a',encoding='UTF-8') as data:
#             self.brand = input('Barnd -> ')
#             self.model = input('Model -> ')
#             self.color = input('Color -> ')
#             data.write(self.brand +'\n')
#             data.write(self.model + '\n')
#             data.write(self.color + '\n\n')
#             return data

#     def split_data(self):
#         with open('all_cars.txt','r',encoding='UTF-8') as data:
#             car_list = []
#             for num,line in enumerate(data,start=1):
#                 if not num%3:





        #    s = data.read()
        #    print(s.split())
        #    for i in range(len(s)):
        #     ','.join(s[i])
        #    return s

    # def __str__(self) -> str:
    #     return f'Brand: {self.brand},Model: {self.model},Color: {self.color}'
        



# car_data = AllCars('','','')
# print(car_data)
# # car_data.add_car_to_data_base()
# car_data.split_data()
# # print(car_data.split_data())


class Car:
    def init(self, name: str='', model: str='', color: str=''):
        self.name = name
        self.model = model
        self.color = color
    
    
    def __str__(self):
        return f'{self.name}, {self.model}, {self.color}'

class AllCar:
    def init(self):
        self.car_list = []
    
    def parse_file(self, file_path):
        with open(file_path, 'r') as file_info:
            car = []
            for line in file_info:
                if line != '\n':
                    car.append(line.strip())
                if len(car) == 3:
                    self.add_car(car[0], car[1], car[2])
                    car = []

    def add_car(self, name, model, color):
        self.car_list.append(Car(name, model, color))
    
    
    def str(self):
        result_str = ''
        for car in self.car_list:
            result_str += f"\n{str(car)}"
        return result_str
        
car_manager = AllCar()
car_manager.parse_file('data.txt')
print(car_manager)


