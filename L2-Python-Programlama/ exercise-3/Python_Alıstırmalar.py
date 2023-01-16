# Görev 1: Verilen değerlerin veri yapılarını inceleyiniz

x = 8
type(x)
# <class 'int'>

y = 3.2
type(y)
# <class 'float'>

z = 8j + 18
type(z)
# <class 'complex'>

a = "Hello World"
type(a)
# <class 'str'>

b = True
type(b)
# <class 'bool'>

c = 23 < 22
type(c)
# <class 'bool'>

l = [1, 2, 3, 4]
type(l)
# <class 'list'>

d = {
    "Name": "John",
    "Age": "27",
    "Address": "Downtown"
}
type(d)
# <class 'dict'>

t = ("Machine Learning", "Data Science")
type(t)
# <class 'tuple'>

s = {"Python", "Machine Learning", "Data Science"}
type(s)
# <class 'set'>


# --------------------------------------------------------
# Görev 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz,
# kelime kelime ayırınız.

text = "The goal is to turn data ito information, and information into insight"

text_split = text.upper().split(" ")

# --------------------------------------------------------
# Görev 3: Verilen listeye aşağıdaki adımları uygulayınız.

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# Adım 1: Verilen listenin eleman sayısına bakınız.

len(lst)

# Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.

lst[0], lst[10]

# Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.

data = list()

for i in range(0, 4):
    data.append(lst[i])

# Adım 4: Sekizinci indeksteki elemanı siliniz.

lst.pop(8)

# Adım 5: Yeni bir eleman ekleyiniz.

lst.append("M")

# Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.

lst.insert(8, "N")

# -------------------------------------------------------
# Görev 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.

dict = {
    'Cristian': ["America", 18],
    'Daisy': ["England", 12],
    'Antonio': ["Spain", 22],
    'Dante': ["Italy", 25]
}

# Adım 1: Key değerlerine erişiniz.

dict.keys()

# Adım 2: Value'lara erişiniz.

dict.values()

# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.

dict['Daisy'] = ["England", 13]

# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.

dict['Ahmet'] = ["Turkey", 24]

# Adım 5: Antonio'yu dictionary'den siliniz.

dict.pop('Antonio')

# ----------------------------------------------------
# Görev 5: Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri
# return eden fonksiyon yazınız

l = [2, 13, 18, 93, 22]
even, odd = list(), list()
even_list, odd_list = list(), list()


def func(d):
    for i in range(0, len(d)):
        if d[i] % 2 == 0:
            even.append(d[i])
        else:
            odd.append(d[i])
    return even, odd


even_list, odd_list = func(l)

# -----------------------------------------------
# Görev 6: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük
# harfe çeviriniz ve başına NUM ekleyiniz.

import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns

["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]
# df[col].dtype != "O" -> tipi Object değilse


# Görev 7: List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan
# değişkenlerin isimlerinin sonuna "FLAG" yazınız

[col.upper() if "no" in col else col.upper() + "_FLAG" for col in df.columns]

# Görev 8: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan
# değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz

og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]

