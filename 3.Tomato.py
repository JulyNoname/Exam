#не факт, что корректно работает, не получилась ф-я all_are_ripe
class Tomato:
    states={1: 'семечка', 2: 'росток', 3: 'зеленые помидоры', 4: 'красные помидоры'}
    def __init__(self, index):
        self._index = index
        self._state = 1

    def grow(self):              #переход на след стадию созревания
        if self._state < 4:
            self._state += 1

    def is_ripe(self):            #проверка, последняя ли стадия созревания
        if self._state == 4:
            print('Созрел')
        else:
            print('Не созрел')


class TomatoBush:

    def __init__(self, number): #надо ли сюда добавлять парметр tomatoes
        self.tomatoes=[Tomato(index) for index in range(0, number+1)] #генератор списка помидорок

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        for tomato in self.tomatoes:
            if tomato.is_ripe()==True:
                print('True')
            else:
                print('False')

    def give_away_all(self): #собрали урожай, т.е список станет пустым
        self.tomatoes = []

class Gardener:

    def __init__(self, name, plant):
        self.name = name #публичный
        self._plant = plant #protected

    def work(self):
        self._plant.grow_all() #за счет работы садовника осуществляется переход на след этап созревания

    def harvest(self):
        if self._plant.all_are_ripe(): #если все плоды созрели
            self._plant.give_away_all()  #список станет пустым (собирается урожай)
        else:
            print('не созрели')  #предупреждение, что не созрели (в ином случае)

    @staticmethod
    def knowledge_base():  #справка по садоводству
        print('помидоры нужно собирать красными, если они синие - вы плохой садовник')

Gardener.knowledge_base()
pomidorka = TomatoBush(10) # 10 помидорок
objgardener = Gardener('July', pomidorka)
objgardener.work()
objgardener.harvest()
objgardener.work()
objgardener.harvest()
