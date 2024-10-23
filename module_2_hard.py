num_=(input('введите целое число от 3 до 20: '))
if num_.isnumeric()==True and int(num_) >= 3 and int(num_) <= 20:
    num_=int(num_)
    pass_=""
    for i in range(1, int(num_/2)+1):
        for j in range(2,num_):
            if num_%(i+j)==0 and i!=j:
                pass_+=str(i)+str(j)

    print(pass_)
else:
    print('некорректное значение, повторите ввод!')