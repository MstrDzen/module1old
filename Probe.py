print("Hello world!")
my_string = "Hello"
print(my_string)
my_number = 3
print(my_number)
print('my_string =', my_string, "|", 'my_mumber =', my_number)
my_string2 = 'Приветствую'
print('Приветствую' [0])
print('Приветствую' [-1])
print('Приветствую' [2:5])
print(len('Приветствую'))
another_string = 'Категорически '
new_string = another_string + my_string2
print(new_string)
num1 = 5
num2 = 3
sum = num1 + num2
print(sum)
result = sum + num1 * num2
print(result)

name = 'Андрей'
print('Name: ',name)
age = 39
print('Age: ',age)
age = age + 8
print('New age: ',age)
is_student = True
print('Is Student: ',is_student)

my_string = 'Домашняя работа'
print(my_string)
print('Длина строки: ',len(my_string))
print(my_string.upper())
print(my_string.lower())
print(my_string.replace(' ', ''))
print(my_string.lower()[0])
print(my_string.upper()[-1])

my_tuple = (3, 4, 'tut', 'tam')
immutable_var = my_tuple
print('Immutable_var:', immutable_var)
my_list = [5, 6, 'tut', 'tam']
mutable_list = my_list
mutable_list.append(152)
print('Mutable_list:', mutable_list)

my_list = ['апельсин','яблоко','банан','киви', 'слива', 'лимон']
print('List:', my_list)
print('Первый:', my_list[0])
print('Последний:', my_list[-1])
print("Промежуточный между 3 и 5:", my_list[3:4])
print("Промежуточный с 3 до 5:", my_list[2:4])
my_list[2] = 'груша'
print('Изменённый:', my_list)

my_dict = {'orange': 'апельсин', 'apple': 'яблоко', 'banana': 'банан', 'kiwi': 'киви', 'plum': 'слива', 'lemon': 'лимон'}
print('Словарь', my_dict)
print('Перевод:', my_dict['orange'])
my_dict.setdefault('pear', 'груша')
print('Дополненный словарь:', my_dict)

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort() # Сортировка по алфавиту
gr1 = sum(grades[0]) / len(grades[0]) # Решил ввести дополнительные переменные, так проще отслеживать, меньше ошибок.
gr2 = sum(grades[1]) / len(grades[1])
gr3 = sum(grades[2]) / len(grades[2])
gr4 = sum(grades[3]) / len(grades[3])
gr5 = sum(grades[4]) / len(grades[4])
dict_students = {students[0]: gr1, students[1]: gr2, students[2]: gr3, students[3]: gr4, students[4]: gr5}
print('Средний балл: ', dict_students)
