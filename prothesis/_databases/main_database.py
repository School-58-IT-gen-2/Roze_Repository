from prothesis.model.places.event_class import Common_event
from prothesis.model.places.event_class import Set_act
from prothesis.model.places.event_class import Text_act
from prothesis.model.places.event_class import Choice_act
from prothesis.model.places.event_class import Random_choice_act
from prothesis.model.places.npc_class import NPC
from prothesis.model.places.enemy_class import Enemy
from prothesis._databases.items_database import all_weapons
from prothesis._databases.items_database import items


#БАЗА ДАННЫХ ДЛЯ НПС
Sage = NPC(name='Мудрец', texture='prothesis/_databases/photos_database/Sage.jpg', dialogue={'Привет':'День добрый', 'кто ты?':'меня зовут мудрец, хотя местные называют меня сумашедшим', 'где я?':'добро пожаловать'})
Trasher = NPC(name='Мусорник', texture='prothesis/_databases/photos_database/Sage.jpg', dialogue={'Кто ты?':'Я.. если бы я сам знал... кожаные создания зовут меня Мусорником, хотя до того, как они сотворили со мной это.. я точно был кем-то значимым.', 'Как ты относишься к людям?':'Люди.. эти создания сатаны?! Они убили во мне все, что делало меня полезным и любимым...Они считают, что все должны им прислуживать, но наконец настало наше время отмщения!.'})
Trader = NPC(name='Торговец', texture='prothesis/_databases/photos_database/Sage.jpg', products = [all_weapons['кинжал пораженный коррозией'], all_weapons['магнитный крюк'], items['бинты'], items['ингалятор']], dialogue={'Кто ты?':'Я просто старый торгаш, живущий прекрасной жизнью странника.. а у тебя, вижу, жизнь далеко не скучная, хотя.. я бы сказал сложная. Зато в организме всегда хватает железа!', 'Как вы относитесь к машинам?':'Машины... они давно стали как люди. Если Главную систему обтянут кожей, я не отличу ее от моей тещи! ха-ха... в любом случае, этот конфликт не моего маленького ума дело, мне без разницы кто ты, путник, но учти, лучше в дальнейшем на конфликты не нарываться, у многих тут нейронных связей побольше будет. Если бы они ещё умели ими пользоваться..'}  )
Trader2 = NPC(name='Торговец', texture='prothesis/_databases/photos_database/Sage.jpg', products = [all_weapons['кинжал пораженный коррозией'], all_weapons['магнитный крюк'], items['бинты'], items['ингалятор']], dialogue={'Кто ты?':'Я.. раньше был любимцем всех первых красоток - сушилка "Дайсон", а сейчас люди зачастую даже водой пользоваться бояться , какая там укладка..', 'Как ты относишься к людям?':'Люди.. я помню времена своей популярности, они покупали меня за бешенные деньги, потом совершенствовали.. Меня наделили многими свойствами, а потом забыли, в виду отсутствия надобности.. эх, вот бы снова быть самым желанным подарком на новый год...'}  )

npcs_for_stages = {1:[Trader, Trader2]}
npcs_random = {1:[Sage, Trasher]}



#БАЗА ДАННЫХ ДЛЯ ВРАГОВ
Toster = Enemy('хлебоподжариватель', 'сбои', 100, all_weapons['кулак'], 5, 'loot')
Archives = Enemy('компьютер из библиотеки', 'сбои', 50, all_weapons['кулак'], 10, 'loot')
Bandit = Enemy('бандит', 'кровотечение', 100, all_weapons['кинжал пораженный коррозией'], 15, 'loot')
Wanderer = Enemy('бродяга','кровотечение', 100, all_weapons['кинжал пораженный коррозией'], 5, 'loot')

enemies_for_stages = {1:[Toster, Archives, Bandit, Wanderer]}


#БАЗА ДАННЫХ ДЛЯ СОБЫТИЙ
Snake_event = Common_event('Запретный плод.', 'Вы встречаете механическую змею', 
                           [
                               Text_act('К вам подходит робо-змея и предлагает купить Яблоко за 25 Кредитов'),
                               Choice_act('Вы бы предпочли...', 
                                          {
                                              'Отказаться': Text_act('Безопасность важнее риска, вы уходите, змей исчезает.'),
                                              'Согласиться!': Set_act({'air':25}, 'А вы рисковый бро! За смелость змей вознаградил тебя мини-инголятором в виде яблока.')
                                          })
                           ])

Wafle_event = Common_event('Приятного аппетита.', 'Вы бродите уже так долго.. вы очень хотите кушать.. стоп. Что это?', 
                           [
                                Text_act('Вы встретили  добрую вафельницу!'),
                                Random_choice_act('Она не против накормить вас, только вот сколько это вафля уже лежит внутри..?', 
                                                  {
                                                    Set_act({'health':20}, 'Она свежая! Вы вкусно покушали и готовы продолжать путь.'):0.7,
                                                    Set_act({'health':-20}, 'Она явно старше вас.. но чувство голода сильнее. Вы съедаете её.. кажется, вам не хорошо.'):0.3
                                                    })
                            ])

events_for_stages = {1:[Snake_event, Wafle_event]}