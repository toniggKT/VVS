import random


#генерация лабиринта
n = int(random.randint(3, 10)) #столбцы, за x
m = int(random.randint(3, 8)) #строки, за y
rooms = ['пусто', 'сундук', 'монстр', 'ловушка', 'портал', 'ключ'] #0 - пусто, 1 - сундук, 2 - монстр, 3 - ловушка, 4 - портал, 5 - ключ

print(n, m)
labirint = [ [random.randint(0, 3) for j in range(n)] for i in range(m)]
labirint[0][0] = 0

#Портал и ключ
key_x = random.randint(1, n-2)
key_y = random.randint(1, m-2)
portal_x = random.randint(1, n-2)
portal_y = random.randint(1, m-2)

if (portal_x == key_x and portal_y == key_y):
    portal_x = n-1
    portal_y = m-1

labirint[key_y][key_x] = 'K'
labirint[portal_y][portal_x] = 'P'

for i in range(m):
    print(*labirint[i])

#Начальные данные: хп, инвентарь, координаты, флаги
hp = int(5)
bag = ['0']*5
ataka = 1

x = int(0)
y = int(0)

fl_monstr = 0 #2
fl_portal = 0 #P
fl_key = 0 #K
fl_bag_key = 0
fl_box = 0 #1
fl_catch = 0 #3

def action(x, y):
    m = ['Проверить инвентарь']
    if x!=0:
        m.append('влево') #
    if x!=(n-1):
        m.append('вправо') #
    if y!=0:
        m.append('вверх') #
    if y!=(m-1):
        m.append('вниз') #
    if fl_monstr==1:
        m.append('сражаться')#
    if fl_box==1:
        m.append('открыть сундук')
    if fl_key==1:
        m.append('взять ключ') #
    if fl_bag_key==1 and fl_portal==1:
        m.append('выйти наконец!') #
    if fl_bag_key==0 and fl_portal==1:
        m.append('запомню, что тут портал') #
    if fl_catch==1:
        m.append('выбраться из ловушки (-1хп)')#

    print('Доступные действия:')
    for i in range(len(m)):
        if i!=len(m)-1:
            print(m[i], end=', ')
        else:
            print(m[i])

    print('выберите действие:')
    act = int(input())
    return act
#движение
def move(x, y, act):
    if act == 'влево':
        x = x-1
    if act == 'вправо':
        x = x+1
    if act == 'вверх':
        y = y+1
    if act == 'вниз':
        y = y-1

    room = labirint[y][x]
    if room == 0:
        fl_monstr = 0  # 2
        fl_portal = 0  # P
        fl_key = 0  # K
        fl_box = 0  # 1
        fl_catch = 0  # 3
    if room == 'K':
        fl_monstr = 0  # 2
        fl_portal = 0  # P
        fl_key = 1  # K
        fl_box = 0  # 1
        fl_catch = 0  # 3
    if room == 'P':
        fl_monstr = 0  # 2
        fl_portal = 1  # P
        fl_key = 0  # K
        fl_box = 0  # 1
        fl_catch = 0  # 3
    if room == 2:
        fl_monstr = 1  # 2
        fl_portal = 0  # P
        fl_key = 0  # K
        fl_box = 0  # 1
        fl_catch = 0  # 3
    if room == 3:
        fl_monstr = 0  # 2
        fl_portal = 0  # P
        fl_key = 0  # K
        fl_box = 0  # 1
        fl_catch = 1  # 3
    if room == 1:
        fl_monstr = 0  # 2
        fl_portal = 0  # P
        fl_key = 0  # K
        fl_box = 1  # 1
        fl_catch = 0  # 3


#взять ключ
def key():
    fl_bag_key = 1
    print('Теперь ключ у вас!')
    fl_key = 0
    labirint[key_y][key_x] = 0
#выход
def escape():
    print('Подравляю! Вы победили!')
    fl_portal = -1
#ловушка
def catch(hp):
    hp = hp - 1
    if hp == 0:
        print('О нет! Вы умерли! Игра окончена')
    fl_catch = 0
#сражение с монстром
def battle(ataka, ataka_m, hp):
    if ataka>ataka_m:
        print('Поздравляю! Вы победили!')
        fl_monstr = 0
    else:
        print('Вы проиграли! Теперь вы можете только бежать!')
        fl_monstr = 0
        hp = hp - 1
        if hp == 0:
            print('О нет! Вы умерли! Игра окончена')
#проверка инвентаря
def bagg(bag):
    for i in range(len(bag)):
        if i != (len(bag) - 1):
            if bag[i] == '0':
                print('Пусто', end=', ')
            if bag[i] == '1':
                print('Aмулет здоровья', end=', ')
            if bag[i] == '2':
                print('Aмулет силы', end=', ')
        else:
            if bag[i] == '0':
                print('Пусто')
            if bag[i] == '1':
                print('Aмулет здоровья')
            if bag[i] == '2':
                print('Aмулет силы')
    print('Отсортировать? (0 - нет, 1 - да)')
    ch = int(input())
    if ch == 1:
        bag.sort()
        for i in range(len(bag)):
            if i != (len(bag) - 1):
                if bag[i] == '0':
                    print('Пусто', end=', ')
                if bag[i] == '1':
                    print('Aмулет здоровья', end=', ')
                if bag[i] == '2':
                    print('Aмулет силы', end=', ')
            else:
                if bag[i] == '0':
                    print('Пусто')
                if bag[i] == '1':
                    print('Aмулет здоровья')
                if bag[i] == '2':
                    print('Aмулет силы')
#сундук
def box(bag, ataka, hp):
    a = random.randint(1, 2)
    if a == 1:
        print('В сундуке лежит амулет здоровья (+1 к хп при наличии в инвентаре)')
    else:
        print('В сундуке лежит амулет силы (+1 к атаке при наличии в инвентаре)')
    if bag.count('0')==0:
        print('О нет, ваш инвентарь полон! Вы можете что-нибудь выбросить и '
              'взять вместо этого предмет (0 - не выбрасывать, 1 - выбросить амулет здоровья, 2 - амулет силы)')
        v = int(input())
        if v == 0:
            print('Сундук неожиданно исчез!')
        elif v == 1:
            ind = bag.index('1')
            bag[ind] = '0'
            if a==1:
                hp+=1
            else:
                ataka+=1
            bag[ind] = str(a)
        else:
            ind = bag.index('2')
            bag[ind] = '0'
            if a==1:
                hp+=1
            else:
                ataka+=1
            bag[ind] = str(a)
        fl_box = 0


print('Приветствуем игрока! Начнем игру!')

actt = action(x, y)
if actt == 'влево' or actt == 'вправо' or  actt == 'вверх' or  actt == 'вниз':
    move(x, y, actt)
if actt == 'Проверить инвентарь':
    bagg(bag)
if actt == 'сражаться':
    print('Вы встретили монстра! Сражайтесь!')
    battle(ataka, y, hp)
if actt == 'открыть сундук':
    box(bag, ataka, hp)
if actt == 'взять ключ':
    key()
if acct == 'выйти наконец!':
    escape()
if acct == 'запомню, что тут портал':
    print('Тут портал....Не могу войти')
if acct == 'выбраться из ловушки (-1хп)':
    catch(hp)

