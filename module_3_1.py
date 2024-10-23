calls = 0
def count_calls(): #счетчик
    global calls
    calls +=1
    print('количество итераций:', calls)
def string_info(string): #регистр
    my_tuple=(len(string),string.upper(),string.lower())
    print (my_tuple)
    count_calls()
def is_contains(string,list_to_search): #поиск
    comm=False
    for i in list_to_search:
        if i.upper()==string.upper():
            comm=True
            print(comm, '- есть элемент в списке')
            break
    if comm==False:
            print(comm, '- нет элемента в списке')
    count_calls()
comm=1
while comm==1:
    if comm==1:
        str_=input('1 функция (регистры) - введите строку: ')
        string_info(str_)
        comm=int(input('продолжить с 1-й функцией - 1 -"да" ?:'))
    else:
        break
comm=1
while comm==1:
    if comm==1:
        str_=input('2 функция (поиск значения) - введите строку: ')
        spis_ = input('введите список через запятую: ')
        is_contains(str_,spis_.split(','))
        comm=int(input('продолжить со 2-й функцией - 1 "да" ?:'))
    else:
        break
print('всего итераций: ', calls)