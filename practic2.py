x = float(input("enter coordinate x: ")) #Задаём координату х с классом flaot
y = float(input("enter coordinate y: ")) #Задаём координату у с классом flaot

if x > 0 and y > 0:
    print("First type")
elif x < 0 and y > 0:
    print("Second type")
elif x < 0 and y < 0:
    print("Third type")
elif x > 0 and y < 0:
    print("Fourth type")
else:
    print("x or y or both of them are 0, its not any of the types") #Вывести это в терминал если хотя бы 1 переменная равна нулю