s=float(input('Введите кол-во секунд: '))
x=s//3600
y=(s%3600)//60
z=(s%3600)%60
print('Введённое вами время составляет: ',int(x),'часов, ',int(y),' минут, ',int(z),' секунд ')
