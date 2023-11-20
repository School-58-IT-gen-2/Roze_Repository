from creatures_database import sage
from creatures_database import events_for_stages
from creatures_database import enemies_for_stages
import random as rand

class Stage():

    def __init__(self, stage_num, stage_prologue):
        self.stage_num = stage_num #номер стадии
        self.stage_prologue = stage_prologue
        self.enemies_count = 5 #кол-во врагов на стадии
        self.events_count = 3 #кол-во событий на стадии
        self.km = 0
        
        print(f'60km [НАЧАЛО] - "{self.stage_prologue}"')  #начальное сообщение

        self.seed = ['void'] * 60  #генерация карты (сначала заполняем все 60 мест пустыми местами)
        for i in range(1, self.enemies_count + 1):
            self.seed[i * rand.randint(1, 60//self.enemies_count - 1)] = 'enemy' #равномерно, рандомно добавляем позиции с врагами
        for i in range(1, self.events_count + 1):
            self.seed[i * rand.randint(1, 60//self.events_count - 1)] = 'event' #равномерно, рандомно добавляем позиции с событиями
        self.__cycle()

    def __cycle(self):
        choice = input('\nвыбор действия>>> ')
        if choice == '': # enter - идти
            self.step()

    def step(self):
        self.km += 1
        eval(f'self.{self.seed[self.km]}()') #происходит то, что на текущей позиции в сиде
        self.__cycle()

    def void(self):
        print(f'{60 - self.km}km [ПУСТО] - "кажется здесь пусто"')
    
    def enemy(self):
        print(f'{60 - self.km}km [НАПАДЕНИЕ] - "кажется здесь враг"')
        enemy = rand.choice(enemies_for_stages[self.stage_num])
        enemy.meeting()
    
    def event(self):
        print(f'{60 - self.km}km [СОБЫТИЕ] - ', end='')
        #event = events_for_stages[self.stage_num][0]
        #event.execute()
        
    def npc(self):
        sage.meeting()
