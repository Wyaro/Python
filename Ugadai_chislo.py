import random
c=random.randint(1,1001)
x=-1
print('Угадай число от 1 до 1000')
while x!=c:
    x=int(input())
    if x>c:
        print('Неизвестное число меньше того, что вы ввели!')
    elif x<c:
        print('Неизвестное число больше того, что вы ввели!')
    else:
        print('Вы отгадали число! Поздравляем с победой!')
        break
