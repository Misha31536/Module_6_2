class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__engine_power = int(__engine_power)
        self.__color = str(__color)

    def get_model(self):
        return (f' Модель:  {self.__model}')

    def get_horsepower(self):
        return (f'Мощность: {self.__engine_power}')


    def get_color(self):
        return (f'Цвет:  {self.__color}')

    def print_info (self):
        get_model = self.get_model()
        print(get_model)
        get_horsepower = self.get_horsepower()
        print(get_horsepower)
        get_color = self.get_color()
        print(get_color)
        print(f'Владелец {self.owner}')

    def set_color(self, new_color):
        if new_color.casefold() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')



class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()
