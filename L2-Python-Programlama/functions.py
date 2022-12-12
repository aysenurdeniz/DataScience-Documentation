# Fonsiyonlar
# print fonksiyonu - ?Python(help(print)) ile fonksiyon ile ilgili bilgileri alır.
# Parametre fonksiyon tanımlaması sırasında ifade edlen değişkenlerdir. fonk(a)
# Argüman bu fonksiyonlar çağrıldığında bu parametrelere karşılık gelen değerlerdir.
# Argümanlar - fonksiyonun alt görevleri olarak da bilinir


# Fonsiyon tanımlama
def calculate(x):
    print(x * 2)


calculate(5)


# İki argumanlı bir fonksiyon tanımlama
def summer(arg1, arg2):
    print(arg1 + arg2)


summer(7, 8)
summer(arg1=1, arg2=8)


# Docstring - Ayarlardan docstring ayarlamaları ile docstring yazma tipi seçilebilir
def summer(arg1, arg2):
    # docstring üç bölüm içerir:
    # fonksiyonu açıklama, argümanların tipi, return tipi,
    # açıklama vs de eklenebilir

    """ This is docstring. Sum of two numbers
    Args
    :param arg1: int, float
    :param arg2: int, float
    :return: int, float
    """

    print(arg1 + arg2)


# Fonksiyonların statement/body bölümleri
# girilen değerleri bir liste içinde saklayacak fonksiyon

list_store = []


def add_element(a, b):
    # body/statement start
    c = a * b
    list_store.append(c)
    print(list_store)
    # body/statement finish


add_element(2, 3)


# Ön tanımlı Argümanlar/Parametreler (Defaults)
# a ve b  ön tanımlı , bir değer gönderilmediğinde hatanın ortadan kalkmasını sağlar
def divide(a=0, b=1):
    print(a / b)


# dont repeat yourself
# varm, moisture, charge
def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)


# Return: Fonksiyon çıktılarını girdi olarak kullanmak
def calculate(varm, moisture, charge):
    return (varm + moisture) / charge


# Fonksiyon içerisinden foksiyon çağırmak
def all_call(varm, moisture, charge):
    a = calculate(varm, moisture, charge)
    return a


# Global & Local Variables

# Koşullar (Conditions)

# True - False
1 == 1
1 == 2

# if - else
if 1 == 1:
    print("yes")

if 1 == 2:  # çıktı vermez çünkü true değil ve içeri girmedi
    print("no")


def num_check(number):
    if number > 10:
        print("high than 10")
    elif number < 10:
        print("less than 10")
    else:
        print("equal")


num_check(4)
num_check(10)

####################### for loop

students = ["Aysenur", "Ahmet", "Senanur", "Mark"]

for student in students:
    print(student)

for student in students:
    print(student.upper())

salaries = [1000, 200, 4566, 3000]


# for salary in salaries:
#     print(int(salary * 0.5 + salary))


# don't repeat yourself
def new_salary(salary, rate):
    return int(salary * rate / 100 + salary)


for salary in salaries:
    if salary >= 3000:
        print(new_salary(salary, 10))
    else:
        print(new_salary(salary, 20))

# UYGULAMA - MÜLAKAT SORUSU
# Amaç: Aşağıdaki şekilde string değiştiren fonksiyonu yazınız

# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

text = "hi my name is john and i am learning python"

for i in range(len(text)):  # range(0, 5) de aynı - 5 sınır text boyutu olmalı
    print(i)


def alternating(string):
    new_string = ""
    # girilen string'in index'lerinde gez
    for string_index in range(len(string)):
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        else:
            new_string += string[string_index].lower()
    print(new_string)


alternating(text)

# Break & While & Continue

for salary in salaries:
    if salary == 200:
        break  # bitir - işlemi kes
        # continue - devam et, pas geç (200 u bas geçti)
    print(salary)

number = 1
while number < 5:
    print(number)
    number += 1

# Enumerate: Otomatik Counter/Indexer ile for loop

for index, student in enumerate(students):  # enumerate (students, 1) - 1. indexten başla
    print(index, student)


# UYGULAMA - MÜLAKAT SORUSU

# divide_students fonksiyonu yazınız
# Çift indexte yer alan öğrencileri bir listeye alınız.
# Tek indexte yer alan öğrencileri başka bir listeye alınız.
# Fakat bu iki liste tek bir listede return olsun.
# Tek liste içerisinde iki farklı liste olacak!

def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups


divide_students(students)


# alternating fonksiyonunun enumerate ile yazılması
def alternating_with_enumerate(string):
    new_string = ""
    for index, student in enumerate(string):
        if index % 2 == 0:
            new_string += student.upper()
        else:
            new_string += student.lower()
    print(new_string)


alternating_with_enumerate(text)

# Zip
name = ["Aysenur", "Ahmet", "Kader", "Sultan"]
age = [24, 23, 45, 21]
sala = [12000, 20000, 30000, 40000]
list(zip(name, age, sala))


# [('Aysenur', 24, 12000),
#  ('Ahmet', 23, 20000),
#  ('Kader', 45, 30000),
#  ('Sultan', 21, 40000)]

# lambda, map, filter, reduce

def summer(a, b):
    return a + b


# yerine lambda (kullan at amacı ile kullanılır) kullanılabilir

new_sum = lambda a, b: a + b
new_sum(4, 5)

# map
salaries = [2000, 1000, 4000, 7000]


def new_sala(x):
    return x * 20 / 100 + x


list(map(new_sala, salaries))
# new_sala kullan at olarak oluşturulabilir - lambda
list(map(lambda x: x * 20 / 100 + x, salaries))


# Filter

list_store2 = [1, 2, 2, 4, 5, 7, 8, 8, 9]
# ikiye bölümünden kalan sıfır mı?
list(filter(lambda x: x % 2 == 0), list_store2)


# reduce - ardarda toplama ex.
from functools import reduce
reduce(lambda a, b: a + b, list_store2)


###############################################

def ders_control (ders, contr):
    if ders == "Matematik":
        print("Mat sınavı açıklandı")
        if contr > 65:
            print("Sınavı geçtiniz")
        else:
            print("Sınavdan kaldınız")
    else:
        print("Mat sınavı açıklanmadı")


ders_control("Matematik", 70)

#############################################
A = [10, 11, 45, 23, 4, 56]
B = []

def move_toB (liste1, liste2):
    for i in liste1:
        liste2.append(i)
    liste1 =  []
    return liste1, liste2

print(move_toB(A, B))

#################################

def recurFak(x):
    val = 1
    for i in range(x):
        val = val * (i + 1)
    return val

recurFak(5)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
def count_control(liste):
    nex_list = []
    for i in fruits:
        if len(i) < 5:
            nex_list.append(i)
    print(nex_list)
    
count_control(fruits)
