# int
a = 5
type(a)

# float
b = 5.5

# kompleks sayılar
x = 2j + 1
type(x)

# String
st = "hello ı st"
type(st)

# boolean
type(True)
type(False)

# liste
liste = ["ad", "cd", "kl"]
type(liste)

# Sözlük (dictionary) / key:value
x = {"name": "Aysenur", "Age": "18"}
type(x)

# Tuple
y = ("python", "ml", "ds")
type(y)

# set
y = {"python", "ml", "ds"}
type(y)

# Liste, tuple, set ve dictionary veri yapıları
# aynı zamanda Python Collections(Arrays)
# olarak ifade edilir.

# sayının karesinde ** kullanılır. ex. a ** 2

# Tipleri değiştirme
# int(a)
# float(b)
# str(a)

# Karakter dizileri - "" ya da '' içerisinde yazılır
# """ """ - üç tırnak içerisinde yazmak da uzun stringler için kullanılır

# Karakter dizilerinde Slice işlemi
name = "Aysenur"
name[0]  # 0. indexi getirir
name[0:2]  # 0 dan başla ikiye kadar git

# Karakter dizilerinde karakter sorgulama
# Python case sensitivedir
# "Ay" in name

# String (Karakter Dizisi) Metotları

dir(str)  # str ile kullanılabilecek metotlar

# Eğer bir fonksiyon class içerisinde tanımlanMAdıysa fonksiyondur
# len() - string uzunluğunu verir

# Eğer bir fonksiyon class içerisinde tanımlandıysa metot denir.
# upper() - Karakter dizilerini BÜYÜTÜR
# lower() - Karakter dizilerini küçültür

name = "Aysenur Deniz"
name.replace("A", "a")  # replace karakter değiştirme için kullanılır. A yerine a gelsin.
name.split()  # split defaultta boşluğa göre bölme işlemi yapar. Bu değiştirilebilir.
name.strip("e")  # kırpma işlemi yapar. e gördüğü yerde bölmelere ayırır.
name.capitalize()  # ilk harfi büyütür.

# Liste
# * Değiştirlebilir
# * Sıralıdır (Index işlemleri yapılır)
# * Kapsayıcıdır (birden fazla veri yapısını içerebilir)

notes = [1, 2, 3, [5, 8, 9], 4]
notes[3][2]  # liste içi listeye erişim - sıralı çünkü

# liste metotları
notes.append("2")  # listeye ekleme işlemi yapar
notes.pop(0)  # 0. indexi siler
notes.insert(2, 99)  # ikinci indexe 99 ekle

# Sözlükler (Dictionary)
# Değiştirilebilir
# Sırasız (3.7 sürümünden sonra sıralı)
# Kapsayıcı
# key-value

dic = {"name": "Aysenur",
       "date": ["21.5", 542]}

dic["name"]  # name in valuesu gelir
# dic.get(name) # name in valuesu gelir

dic["date"][1]  # date keyindeki listeden birinci indexi getir.

dic["name"] = "Gul"  # değiştirme yapar

dic.keys()  # bütün keylere erişme
dic.values()  # bütün valuelara erişme

# dic e tuple demetleri olarak erişme
dic.items()

# güncelleme veya yeni key-value ekler
dic.update({"name": "Aynur"})

# Demet (Tuple)
# Değiştirilemez
# Sıralıdır
# Kapsayıcıdır

# Set -  Hız gerektiren durumalarda kullanılır
# Değiştirilebilir
# Sırasız + Eşsizdir
# Kapsayıcıdır

set1 = set([1, 2, 3])
set2 = set([4, 5, 1])

#set1 de olur set2 de olmayan
set1.difference(set2)
set1 - set2 # aynı

#iki kümede de birbirinde olmayanlar
set1.symmetric_difference(set2)
set2.symmetric_difference(set1)

# iki kümenin kesişimi
set1.intersection(set2)
set2.intersection(set1)
set1 & set2 # aynı

# iki kümenin birleşimi
set1.union(set2)
set2.union(set1)

# iki kümenin kesişimi boş mu
set1.isdisjoint(set2)

# bir küme diğerinin alt kümesi mi
set1.issubset(set2)

# bir küme diğerini kapsıyor mu
set1.issuperset(set2)
