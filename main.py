# # Чтение информации из файла
# print('Чтение информации из файла')
file = open("my_file.txt")
# print(file.read())
# print()
# 
# print('первые 5 символов')
# # Далее, в методе read мы можем указать некий числовой аргумент, например,
# file.seek(0)
# print(file.read(5))
# # Тогда из файла будут считаны первые 5 символов
# print()
# 
# print('построчное чтение файла')
# # readline() построчное чтение файла
# s = file.readline()
# print(s)
# s = file.readline()
# print(s)
# s = file.readline()
# print(s)
# # метод seek()
# file.seek(0)  # устанавливаем метку в начало
# s = file.readline()
# print(s)


# print('file - итерируемый объект!!!')
# for i in file:
#     s = file.readline()
#     print(s)


# print('\n', 'текущая файловая позиция')
# # текущая файловая позиция
# pos = file.tell()
# print( pos )

# print('\n', 'избавляемся от лишних строк')
# # избавляемся от лишних строк
# s = file.readline().strip()
# print(s)
# s = file.readline().strip()
# print(s)
# s = file.readline()
# print(s)
# 
# 
# 
# readlines()
# print('\n', 'readlines()')
# s = file.readlines()
# print(s)
# 
# new = []
# for i in s:
#     new.append(i.strip())
# print(new)
    
# file = open("my_file.txt")
# for i in file:
#     new.append(file.readline().strip())
# f.close()
# print(new)



# 
# 
# # менеджер контекста
# print('\n', 'менеджер контекста')
# with open("my_file.txt") as file:
#     for line in file:
#         print(line.strip())
# 
# 
# # запись в файл
# print('\n', 'запись в файл')
# with open("out.txt", "w") as f:
#     f.write("Hello World!")
# # проверим
# with open("out.txt") as f:
#     print(f.read())
# # 
# # # или так
# rec = "Привет Мир!"
# with open("out.txt", "w") as f:
#     f.write(rec)
#     
# # проверим
# with open("out.txt") as f:
#     print(f.read())
# 
# # если записать еще раз
# with open("out.txt", "w") as f:
#     f.write("Hello!")
#     
# # проверим
# with open("out.txt") as f:
#     print(f.read())
# 
# 
# # дозапись в файл
# print("\n", "дозапись в файл")
# with open("out.txt", "a") as f:
#     f.write("\n")
#     f.write("Hello Hello!")       
# 
# # проверим
# with open("out.txt") as f:
#     print(f.read())
#   
#   
# writelines
# print("\n", "writelines")
ls = ["Сижу за решеткой в темнице сырой.",
      "Вскормленный в неволе орел молодой,",
      "Мой грустный товарищ,", "махая крылом,",
      "Кровавую пищу клюет под окном"]
# 
with open("out.txt", "w") as f:
    f.writelines(ls)
# 
# # проверим
# with open("out.txt") as f:
#     print(f.read())
# 
# 
# бинарный режим
# # запись списка
# print("\n", "бинарный режим запись списка")
# import pickle
# with open("out.bin", "wb") as f:
#     pickle.dump(ls, f)
# 
# # чтение 
# with open("out.bin", "rb") as f:
#     data = pickle.load(f)
# print(data)
# # 
# # # запись словаря
# print("\n", "бинарный режим запись словаря")
# d = {"name": "Ivan", "last_name": "Egoroff", "age": 25, "status": True}
# import pickle
# with open("out.bin", "wb") as f:
#     pickle.dump(d, f)
# 
# # чтение 
# with open("out.bin", "rb") as f:
#     data = pickle.load(f)
# print(data)

# 
# 
# # os
# print("\n", "модуль os")
# import os
# print('имя ОС: ', os.name)  # имя ОС
# print('текущая директория: ', os.getcwd()) # текущая директория
# print('список файлов и директорий в текущей папке:')
# print(os.listdir(path="."))  # список файлов и директорий в текущей папке.
# print('True, если путь существует: ', os.path.exists("out.bin"))  # True, если путь существует
# print('абсолютный путь текущего каталога: ', os.getcwd())  # абсолютный путь текущего каталога
# print('абсолютный путь до каталога: ', os.path.dirname("file_8\out.bin"))  # абсолютный путь до каталога
# print('Имя файла: ', os.path.basename("file_8\out.bin"))  # Имя файла
# # 




