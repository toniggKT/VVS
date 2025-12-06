'''Введение данных'''
print('Введите lvl (1-5)')
lvl = int(input())
print('Введите строку')
s = str(input())

#test_1='приВет МИР'
#test_2='Ботать круто! Очень КрутО!'

'''lvl 1: реализую upper, lower, capitalize;
Принимаю строку(str),
возвращаю измененную строку'''
def lvl1(s: str) -> str:
    print('Выберите стиль боя! (upper, lower, capitalize)')
    meth = str(input())
    if meth == 'upper':
        return s.upper()
    elif meth == 'lower':
        return s.lower()
    elif meth == 'capitalize':
        return s.capitalize()
    else:
        print('Не пониимаю((')


'''lvl 2: реализую find, replace, count;
Принимаю строку(str),
возвращаю измененную строку'''
def lvl2(s: str) -> str:
    print('Выберите стиль боя! (find, replace, count)')
    meth = str(input())
    '''Принимает что искать (в нижнем регистре)
    Возвращает первое вхождение'''
    if meth == 'find':
        print('Выберите что искать (регистр не учитывается)')
        s0 = str(input()).lower()
        s1 = s.lower()
        a1 = int(s1.find(s0))
        return a1
    '''Принимает заменяемое, на что заменяется
    Возвращает измененную строку'''
    if meth == 'replace':
        print('Выберите что заменяется (регистр не учитывается) и на что')
        s1 = str(input()).lower() #заменяется
        s2 = str(input()) #замена
        s_new = s.replace(s1, s2, -1) #new str
        return s_new
    if meth == 'count':
        print('Выберите что подсчитаем в строке')
        s_poisk = str(input()).lower()
        s_lower = s.lower()
        count = s_lower.count(s_poisk)
        return count
    if (meth != 'find') and (meth != 'replace') and (meth != 'count'):
        print('Не пониимаю((')


'''lvl 3: реализую split, join;
Принимаю строку(str) или массив,
возвращаю измененную строку'''
def lvl3(s: str)->str:
  print('Выберите стиль боя! (split, join)')
  meth=str(input())
  if meth=='split':
    print('Выберите разделитель')
    s_razd = str(input())
    s_new = s.split(s_razd)
    return s_new
  if meth == 'join':
    s_new = "".join(s)
    return s_new
  if (meth != 'spit') and (meth != 'join'):
      print('Не пониимаю((')

'''lvl 4: реализую isdigit, isalpha, strip;
Принимаю строку(str),
возвращаю измененную строку'''
def lvl4(s: str)->str:
    print('Выберите стиль боя! (isdigit, isalpha, strip)')
    meth = str(input())
    if meth=='isdigit':
        return s.isdigit()
    elif meth=='isalpha':
        return s.isalpha()
    elif meth=='strip':
        return s.strip()
    else:
        print('Не пониимаю((')

'''lvl 5: реализую все методы;
Принимаю строку(str),
возвращаю измененную строку'''
def lvl5(s: str)->str:
    print('Выберите стиль боя! (любой метод!)')
    meth = str(input())
    #lvl1
    if meth == 'upper':
        s = s.upper()
        return s.upper()
    elif meth == 'lower':
        s = s.lower()
        return s.lower()
    elif meth == 'capitalize':
        s = s.capitalize()
        return s.capitalize()
    #lvl2
    elif meth == 'find':
        print('Выберите что искать (регистр не учитывается)')
        s0 = str(input()).lower()
        s1 = s.lower()
        a1 = int(s1.find(s0))
        return a1
    elif meth == 'replace':
        print('Выберите что заменяется (регистр не учитывается) и на что')
        s1 = str(input()).lower()
        s2 = str(input())
        s_new = s.replace(s1, s2, -1)
        s = s_new
        return s_new
    elif meth == 'count':
        print('Выберите что подсчитаем в строке')
        s_poisk = str(input()).lower()
        s_lower = s.lower()
        count = s_lower.count(s_poisk)
        return count
    #lvl3
    elif meth == 'split':
        print('Выберите разделитель')
        s_razd = str(input())
        s_new = s.split(s_razd)
        s = s_new
        return s_new
    elif meth == 'join':
        s_new = "".join(s)
        s = s_new
        return s_new
    #lvl4
    elif meth=='isdigit':
        s = s.isdigit()
        return s.isdigit()
    elif meth=='isalpha':
        s = s.isalpha()
        return s.isalpha()
    elif meth=='strip':
        s = s.strip()
        return s.strip()
    else:
        print('Не пониимаю((')

if lvl == 1:
    print(lvl1(s))
if lvl == 2:
    print(lvl2(s))
if lvl == 3:
    print(lvl3(s))
if lvl == 4:
    print(lvl4(s))

deside = '1'
if lvl == 5:
    while (deside == '1'):
        print('Напишите 1, если хотите продолжить/начать бой!')
        deside = str(input())
        if deside != '1':
            print('Бой окончен!')
        else:
            s = lvl5(s)
            print(s)




